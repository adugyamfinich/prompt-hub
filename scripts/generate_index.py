#!/usr/bin/env python3
"""
PromptHub Index Generator

Automatically generates an INDEX.md file with all prompts organized by category.

Usage:
    python scripts/generate_index.py
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass
from datetime import datetime


@dataclass
class PromptMetadata:
    """Stores metadata extracted from a prompt file"""
    title: str
    filepath: Path
    category: str
    difficulty: str
    models: str
    tags: List[str]
    description: str
    author: str
    date_added: str


class IndexGenerator:
    """Generates index of all prompts"""
    
    def __init__(self, prompts_dir: Path = None):
        self.prompts_dir = prompts_dir or Path("prompts")
        self.prompts: List[PromptMetadata] = []
    
    def extract_metadata(self, filepath: Path) -> PromptMetadata:
        """Extract metadata from a prompt file"""
        content = filepath.read_text(encoding='utf-8')
        
        # Extract title (first h1)
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else filepath.stem
        
        # Extract metadata fields
        def extract_field(field_name: str, default: str = "Unknown") -> str:
            pattern = rf'\*\*{field_name}\*\*:\s*(.+)'
            match = re.search(pattern, content)
            if match:
                value = match.group(1).strip()
                # Remove brackets and extra formatting
                value = re.sub(r'[\[\]]', '', value)
                return value
            return default
        
        category = extract_field("Category")
        difficulty = extract_field("Difficulty")
        models = extract_field("Model Compatibility", "All Models")
        author = extract_field("Author", "@unknown")
        date_added = extract_field("Date Added", "Unknown")
        
        # Extract tags
        tags_match = re.search(r'\*\*Tags\*\*:\s*(.+)', content)
        tags = []
        if tags_match:
            tags_text = tags_match.group(1)
            tags = re.findall(r'`#(\w+)`', tags_text)
        
        # Extract description
        desc_match = re.search(r'## Description\s+(.+?)(?=##)', content, re.DOTALL)
        description = "No description available."
        if desc_match:
            description = desc_match.group(1).strip()
            # Take first sentence or first 150 chars
            description = description.split('.')[0] + '.'
            if len(description) > 150:
                description = description[:147] + "..."
        
        return PromptMetadata(
            title=title,
            filepath=filepath,
            category=category,
            difficulty=difficulty,
            models=models,
            tags=tags,
            description=description,
            author=author,
            date_added=date_added
        )
    
    def collect_prompts(self):
        """Collect all prompts from the prompts directory"""
        self.prompts = []
        
        for filepath in self.prompts_dir.rglob("*.md"):
            # Skip README and other documentation
            if filepath.name.upper() in ["README.MD", "INDEX.MD"]:
                continue
            
            try:
                metadata = self.extract_metadata(filepath)
                self.prompts.append(metadata)
            except Exception as e:
                print(f"Warning: Failed to process {filepath}: {e}")
        
        # Sort by title
        self.prompts.sort(key=lambda p: p.title.lower())
    
    def generate_category_section(self, category: str) -> str:
        """Generate markdown section for a category"""
        category_prompts = [p for p in self.prompts if category in p.category]
        
        if not category_prompts:
            return ""
        
        # Sort by difficulty, then title
        difficulty_order = {"Beginner": 1, "Intermediate": 2, "Advanced": 3}
        category_prompts.sort(key=lambda p: (
            difficulty_order.get(p.difficulty, 999),
            p.title.lower()
        ))
        
        lines = [f"### {category}\n"]
        
        # Create table
        lines.append("| Prompt | Difficulty | Models | Description |")
        lines.append("|--------|-----------|---------|-------------|")
        
        for prompt in category_prompts:
            # Create relative link
            # If filepath is already relative, use it; otherwise make it relative
            if prompt.filepath.is_absolute():
                try:
                    rel_path = prompt.filepath.relative_to(Path.cwd())
                except ValueError:
                    # If we can't make it relative, just use the filename
                    rel_path = prompt.filepath
            else:
                rel_path = prompt.filepath
            link = f"[{prompt.title}]({rel_path})"
            
            # Format difficulty with emoji
            difficulty_emoji = {
                "Beginner": "🟢",
                "Intermediate": "🟡",
                "Advanced": "🔴"
            }
            difficulty = f"{difficulty_emoji.get(prompt.difficulty, '⚪')} {prompt.difficulty}"
            
            # Truncate description if too long
            desc = prompt.description
            if len(desc) > 100:
                desc = desc[:97] + "..."
            
            lines.append(f"| {link} | {difficulty} | {prompt.models} | {desc} |")
        
        lines.append("")  # Empty line after table
        return "\n".join(lines)
    
    def generate_tags_section(self) -> str:
        """Generate tag cloud section"""
        # Count tag occurrences
        tag_counts: Dict[str, int] = {}
        for prompt in self.prompts:
            for tag in prompt.tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
        
        if not tag_counts:
            return ""
        
        # Sort by count, then alphabetically
        sorted_tags = sorted(tag_counts.items(), key=lambda x: (-x[1], x[0].lower()))
        
        lines = ["## 🏷️ Browse by Tag\n"]
        
        # Create tag links (using GitHub search)
        tag_links = []
        for tag, count in sorted_tags[:30]:  # Limit to top 30 tags
            tag_links.append(f"`#{tag}` ({count})")
        
        # Format in columns
        lines.append(" · ".join(tag_links))
        lines.append("")
        
        return "\n".join(lines)
    
    def generate_statistics(self) -> str:
        """Generate statistics section"""
        total = len(self.prompts)
        
        # Count by category
        categories = {}
        for prompt in self.prompts:
            categories[prompt.category] = categories.get(prompt.category, 0) + 1
        
        # Count by difficulty
        difficulties = {}
        for prompt in self.prompts:
            difficulties[prompt.difficulty] = difficulties.get(prompt.difficulty, 0) + 1
        
        lines = ["## 📊 Repository Statistics\n"]
        lines.append(f"**Total Prompts:** {total}")
        lines.append("")
        
        lines.append("**By Category:**")
        for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
            percentage = (count / total * 100) if total > 0 else 0
            lines.append(f"- {cat}: {count} ({percentage:.1f}%)")
        
        lines.append("")
        lines.append("**By Difficulty:**")
        for diff, count in sorted(difficulties.items(), key=lambda x: -x[1]):
            percentage = (count / total * 100) if total > 0 else 0
            emoji = {"Beginner": "🟢", "Intermediate": "🟡", "Advanced": "🔴"}.get(diff, "⚪")
            lines.append(f"- {emoji} {diff}: {count} ({percentage:.1f}%)")
        
        lines.append("")
        return "\n".join(lines)
    
    def generate_recent_section(self, limit: int = 10) -> str:
        """Generate recently added prompts section"""
        # Sort by date (most recent first)
        dated_prompts = [p for p in self.prompts if p.date_added != "Unknown"]
        dated_prompts.sort(key=lambda p: p.date_added, reverse=True)
        
        if not dated_prompts:
            return ""
        
        lines = [f"## 🆕 Recently Added\n"]
        
        for prompt in dated_prompts[:limit]:
            # Create relative link
            # If filepath is already relative, use it; otherwise make it relative
            if prompt.filepath.is_absolute():
                try:
                    rel_path = prompt.filepath.relative_to(Path.cwd())
                except ValueError:
                    rel_path = prompt.filepath
            else:
                rel_path = prompt.filepath
            link = f"[{prompt.title}]({rel_path})"
            lines.append(f"- {link} - {prompt.date_added}")
        
        lines.append("")
        return "\n".join(lines)
    
    def generate_index(self) -> str:
        """Generate complete index markdown"""
        self.collect_prompts()
        
        lines = [
            "# PromptHub Index",
            "",
            f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*",
            "",
            "Complete catalog of all prompts in the repository.",
            "",
            "## 🔍 Quick Navigation",
            "",
            "- [Browse by Category](#-browse-by-category)",
            "- [Browse by Tag](#️-browse-by-tag)",
            "- [Recently Added](#-recently-added)",
            "- [Statistics](#-repository-statistics)",
            "",
            "---",
            ""
        ]
        
        # Add statistics
        lines.append(self.generate_statistics())
        
        # Add recent section
        lines.append(self.generate_recent_section())
        
        # Add categories
        lines.append("## 📁 Browse by Category\n")
        
        categories = [
            "Coding",
            "Writing", 
            "Analysis",
            "Creative",
            "Education",
            "Research"
        ]
        
        for category in categories:
            section = self.generate_category_section(category)
            if section:
                lines.append(section)
        
        # Add tags section
        lines.append(self.generate_tags_section())
        
        # Add footer
        lines.extend([
            "---",
            "",
            "## 🤝 Contributing",
            "",
            "Don't see what you're looking for? [Submit a new prompt](CONTRIBUTING.md)!",
            "",
            "**[Back to Main README](README.md)**"
        ])
        
        return "\n".join(lines)
    
    def write_index(self, output_path: Path = None):
        """Generate and write index to file"""
        output_path = output_path or Path("INDEX.md")
        
        index_content = self.generate_index()
        output_path.write_text(index_content, encoding='utf-8')
        
        print(f"✓ Generated index with {len(self.prompts)} prompts")
        print(f"✓ Written to: {output_path}")


def main():
    """Main entry point"""
    generator = IndexGenerator()
    generator.write_index()


if __name__ == "__main__":
    main()
