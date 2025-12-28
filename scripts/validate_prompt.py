#!/usr/bin/env python3
"""
PromptHub Prompt Validation Script

Validates that prompt files follow the required format and standards.

Usage:
    python scripts/validate_prompt.py path/to/prompt.md
    python scripts/validate_prompt.py prompts/by-category/coding/  # validate all in directory
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class ValidationResult:
    """Stores validation results"""
    is_valid: bool
    errors: List[str]
    warnings: List[str]
    filepath: str


class PromptValidator:
    """Validates prompt files against PromptHub standards"""
    
    REQUIRED_SECTIONS = [
        "# ",  # Title
        "## Metadata",
        "## Description",
        "## Use Case",
        "## The Prompt",
        "## Variables to Customize",
        "## Example Input/Output",
        "## Performance Notes",
        "## Related Prompts",
        "## Version History"
    ]
    
    REQUIRED_METADATA = [
        "**Category**:",
        "**Difficulty**:",
        "**Model Compatibility**:",
        "**Tags**:",
        "**Author**:",
        "**Date Added**:",
        "**Version**:"
    ]
    
    VALID_CATEGORIES = [
        "Coding", "Writing", "Analysis", 
        "Creative", "Education", "Research"
    ]
    
    VALID_DIFFICULTIES = ["Beginner", "Intermediate", "Advanced"]
    
    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self.content = ""
        self.errors = []
        self.warnings = []
        
    def validate(self) -> ValidationResult:
        """Run all validation checks"""
        if not self._load_file():
            return ValidationResult(False, self.errors, self.warnings, str(self.filepath))
            
        self._check_filename()
        self._check_required_sections()
        self._check_metadata()
        self._check_content_quality()
        self._check_examples()
        
        is_valid = len(self.errors) == 0
        
        return ValidationResult(
            is_valid=is_valid,
            errors=self.errors,
            warnings=self.warnings,
            filepath=str(self.filepath)
        )
    
    def _load_file(self) -> bool:
        """Load the prompt file"""
        if not self.filepath.exists():
            self.errors.append(f"File not found: {self.filepath}")
            return False
            
        if self.filepath.suffix != ".md":
            self.errors.append(f"File must be a .md file, got: {self.filepath.suffix}")
            return False
            
        try:
            self.content = self.filepath.read_text(encoding='utf-8')
            return True
        except Exception as e:
            self.errors.append(f"Failed to read file: {e}")
            return False
    
    def _check_filename(self):
        """Validate filename follows kebab-case convention"""
        filename = self.filepath.stem
        
        # Check for kebab-case
        if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', filename):
            self.errors.append(
                f"Filename must be in kebab-case (lowercase with hyphens): {filename}"
            )
        
        # Check length
        if len(filename) > 50:
            self.warnings.append(f"Filename is quite long ({len(filename)} chars). Consider shortening.")
    
    def _check_required_sections(self):
        """Check that all required sections are present"""
        for section in self.REQUIRED_SECTIONS:
            if section not in self.content:
                self.errors.append(f"Missing required section: {section}")
    
    def _check_metadata(self):
        """Validate metadata section"""
        # Check required fields
        for field in self.REQUIRED_METADATA:
            if field not in self.content:
                self.errors.append(f"Missing required metadata field: {field}")
        
        # Extract and validate category
        category_match = re.search(r'\*\*Category\*\*:\s*(.+)', self.content)
        if category_match:
            category = category_match.group(1).strip()
            # Remove brackets if present
            category = re.sub(r'[\[\]]', '', category)
            
            # Check if it's one of the valid categories
            valid_found = any(cat in category for cat in self.VALID_CATEGORIES)
            if not valid_found:
                self.errors.append(
                    f"Invalid category: {category}. Must be one of: {', '.join(self.VALID_CATEGORIES)}"
                )
        
        # Extract and validate difficulty
        difficulty_match = re.search(r'\*\*Difficulty\*\*:\s*(.+)', self.content)
        if difficulty_match:
            difficulty = difficulty_match.group(1).strip()
            difficulty = re.sub(r'[\[\]]', '', difficulty)
            
            valid_found = any(diff in difficulty for diff in self.VALID_DIFFICULTIES)
            if not valid_found:
                self.errors.append(
                    f"Invalid difficulty: {difficulty}. Must be one of: {', '.join(self.VALID_DIFFICULTIES)}"
                )
        
        # Check version format
        version_match = re.search(r'\*\*Version\*\*:\s*(.+)', self.content)
        if version_match:
            version = version_match.group(1).strip()
            if not re.match(r'^\d+\.\d+$', version):
                self.warnings.append(f"Version format should be X.Y (e.g., 1.0): {version}")
        
        # Check date format
        date_match = re.search(r'\*\*Date Added\*\*:\s*(.+)', self.content)
        if date_match:
            date = date_match.group(1).strip()
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
                self.errors.append(f"Date must be in YYYY-MM-DD format: {date}")
    
    def _check_content_quality(self):
        """Check content quality indicators"""
        # Check description length
        desc_match = re.search(r'## Description\s+(.+?)(?=##)', self.content, re.DOTALL)
        if desc_match:
            description = desc_match.group(1).strip()
            if len(description) < 50:
                self.warnings.append("Description seems too short (less than 50 characters)")
            if len(description) > 500:
                self.warnings.append("Description seems quite long (over 500 characters). Consider being more concise.")
        
        # Check for placeholder text
        placeholders = [
            "[Your text here]",
            "[TODO]",
            "[PLACEHOLDER]",
            "[Enter",
            "[Provide"
        ]
        for placeholder in placeholders:
            if placeholder in self.content:
                self.errors.append(f"Found placeholder text that needs to be filled: {placeholder}")
        
        # Check for prompt content
        prompt_section = re.search(r'## The Prompt\s+```(.+?)```', self.content, re.DOTALL)
        if not prompt_section:
            self.errors.append("The Prompt section must contain the prompt in a code block (```)")
        else:
            prompt_text = prompt_section.group(1).strip()
            if len(prompt_text) < 50:
                self.warnings.append("The prompt seems very short. Is it complete?")
        
        # Check for variables documentation
        if "{" in self.content and "}" in self.content:
            # Has variables, should have documentation
            if "## Variables to Customize" not in self.content:
                self.warnings.append("Prompt contains variables but 'Variables to Customize' section might be empty")
    
    def _check_examples(self):
        """Validate examples section"""
        example_section = re.search(r'## Example Input/Output(.+?)(?=##)', self.content, re.DOTALL)
        
        if not example_section:
            self.warnings.append("Could not find Example Input/Output section content")
            return
        
        example_content = example_section.group(1)
        
        # Check for input and output
        if "**Input:**" not in example_content and "**Customized Prompt:**" not in example_content:
            self.warnings.append("Examples should show input or customized prompt")
        
        if "**Output:**" not in example_content:
            self.warnings.append("Examples should show output")
        
        # Check for code blocks in examples
        code_blocks = re.findall(r'```', example_content)
        if len(code_blocks) < 2:
            self.warnings.append("Examples should use code blocks (```) for better formatting")


def validate_directory(directory: Path) -> List[ValidationResult]:
    """Validate all .md files in a directory"""
    results = []
    
    for filepath in directory.rglob("*.md"):
        # Skip README and other documentation files
        if filepath.name.upper() in ["README.MD", "CONTRIBUTING.MD", "LICENSE.MD"]:
            continue
        
        validator = PromptValidator(filepath)
        result = validator.validate()
        results.append(result)
    
    return results


def print_results(results: List[ValidationResult]):
    """Print validation results in a readable format"""
    total = len(results)
    valid = sum(1 for r in results if r.is_valid)
    
    print(f"\n{'='*70}")
    print(f"VALIDATION RESULTS: {valid}/{total} files passed")
    print(f"{'='*70}\n")
    
    for result in results:
        status = "✓ PASS" if result.is_valid else "✗ FAIL"
        color = "\033[92m" if result.is_valid else "\033[91m"
        reset = "\033[0m"
        
        print(f"{color}{status}{reset} {result.filepath}")
        
        if result.errors:
            print(f"  Errors ({len(result.errors)}):")
            for error in result.errors:
                print(f"    ✗ {error}")
        
        if result.warnings:
            print(f"  Warnings ({len(result.warnings)}):")
            for warning in result.warnings:
                print(f"    ⚠ {warning}")
        
        print()
    
    if valid == total:
        print("🎉 All prompts are valid!\n")
        return 0
    else:
        print(f"❌ {total - valid} prompt(s) need attention.\n")
        return 1


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python validate_prompt.py <path/to/prompt.md or directory>")
        sys.exit(1)
    
    path = Path(sys.argv[1])
    
    if not path.exists():
        print(f"Error: Path does not exist: {path}")
        sys.exit(1)
    
    if path.is_file():
        validator = PromptValidator(path)
        result = validator.validate()
        results = [result]
    elif path.is_dir():
        results = validate_directory(path)
    else:
        print(f"Error: Path must be a file or directory: {path}")
        sys.exit(1)
    
    exit_code = print_results(results)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
