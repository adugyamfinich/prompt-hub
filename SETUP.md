# PromptHub Setup Guide

Step-by-step instructions to set up your PromptHub repository.

## 📋 Prerequisites

- Git installed
- GitHub account
- Python 3.8+ (for validation scripts)
- Text editor or IDE

## 🚀 Quick Setup (5 minutes)

### 1. Create Repository on GitHub

```bash
# Option A: Using GitHub CLI
gh repo create prompt-hub --public --clone

# Option B: Via GitHub website
# 1. Go to github.com/new
# 2. Name: prompt-hub (or your preferred name)
# 3. Public repository
# 4. Initialize with README: NO (we have our own)
# 5. Create repository
```

### 2. Upload Project Files

```bash
# Navigate to your project directory
cd prompt-hub

# Copy all starter files from PromptHub package

# Initialize git
git init
git add .
git commit -m "Initial commit: PromptHub setup"

# Connect to GitHub
git remote add origin https://github.com/adugyamfinich/prompt-hub.git
git branch -M main
git push -u origin main
```

### 3. Enable GitHub Actions

GitHub Actions should work automatically once you push. Verify:

1. Go to your repository on GitHub
2. Click "Actions" tab
3. You should see workflows ready to run

### 4. Configure Repository Settings

#### Enable Issues and Discussions
1. Go to Settings → General
2. Check "Issues"
3. Check "Discussions"

#### Set up Labels

Go to Issues → Labels and create:
- `prompt-submission` (green)
- `needs-review` (yellow)
- `bug` (red)
- `enhancement` (blue)
- `documentation` (light blue)
- `category:coding` (purple)
- `category:writing` (purple)
- `category:analysis` (purple)
- `category:creative` (purple)
- `category:education` (purple)
- `category:research` (purple)

#### Enable GitHub Pages (Optional)

For documentation website:
1. Settings → Pages
2. Source: Deploy from branch
3. Branch: main, folder: /docs
4. Save

## 🔧 Customization

### Update Repository Information

Replace placeholders in these files:

**README.md:**
```markdown
- Update Twitter link (or remove)
- Add your actual GitHub username
- Customize featured prompts section
```

**CONTRIBUTING.md:**
```markdown
- Replace [INSERT CONTACT EMAIL] with your email
- Update Discord/Slack links if you have them
```

**CODE_OF_CONDUCT.md:**
```markdown
- Replace [INSERT CONTACT EMAIL] with enforcement contact
```

**All link references:**
```bash
# Find and replace
adugyamfinich → your-github-username
your-email@example.com → your@email.com
```

### Customize Project Name

If you chose a different name:

```bash
# Update in all files
find . -type f -name "*.md" -exec sed -i 's/PromptHub/YourName/g' {} +
find . -type f -name "*.md" -exec sed -i 's/prompt-hub/your-name/g' {} +
```

## 📝 Adding Your First Prompt

### Quick Method (via Issue)

1. Go to Issues → New Issue
2. Select "Prompt Submission" template
3. Fill out the form
4. Submit
5. Maintainer (you!) will create the PR

### Standard Method (via Pull Request)

```bash
# 1. Create new branch
git checkout -b add-my-first-prompt

# 2. Copy template
cp templates/prompt-template.md prompts/by-category/coding/my-prompt.md

# 3. Fill in the template
# Edit prompts/by-category/coding/my-prompt.md

# 4. Validate
python scripts/validate_prompt.py prompts/by-category/coding/my-prompt.md

# 5. Commit and push
git add .
git commit -m "Add: My First Prompt"
git push origin add-my-first-prompt

# 6. Create PR on GitHub
gh pr create --title "Add: My First Prompt" --body "My first prompt submission!"
```

## 🧪 Testing Setup

### Validate Scripts Work

```bash
# Test validation script
python scripts/validate_prompt.py prompts/by-category/coding/python-code-debugger-pro.md

# Expected output: ✓ PASS
```

### Generate Initial Index

```bash
# Create index
python scripts/generate_index.py

# Check output
cat INDEX.md
```

### Test GitHub Actions Locally (Optional)

Install act:
```bash
# macOS
brew install act

# Linux
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# Run workflow locally
act -l  # List workflows
act push  # Simulate push event
```

## 🌐 Optional: Deploy Documentation Site

### Using GitHub Pages

Already configured if you followed setup above. Documentation will be at:
```
https://adugyamfinich.github.io/prompt-hub/
```

### Using MkDocs (Advanced)

```bash
# Install MkDocs
pip install mkdocs mkdocs-material

# Create mkdocs.yml
cat > mkdocs.yml << EOF
site_name: PromptHub
theme:
  name: material
  palette:
    primary: indigo
nav:
  - Home: README.md
  - Contributing: CONTRIBUTING.md
  - Guides:
      - Quick Start: docs/quick-start.md
      - Best Practices: docs/best-practices.md
      - Taxonomy: docs/taxonomy.md
      - Evaluation: docs/evaluation-guide.md
EOF

# Build site
mkdocs build

# Preview locally
mkdocs serve
# Visit http://127.0.0.1:8000
```

## 🤝 Community Setup

### Set Up Discussions

1. Enable Discussions (Settings → General)
2. Create categories:
   - 💡 Ideas
   - 🙏 Q&A
   - 📣 Announcements
   - 🎉 Show and Tell

### Create Issue Templates

Already included in `.github/ISSUE_TEMPLATE/`:
- `prompt-submission.md`
- `bug-report.md`

### Add Contribution Recognition

Install all-contributors:
```bash
npx all-contributors-cli init
npx all-contributors-cli add YOUR-NAME code,doc
```

## 📊 Analytics (Optional)

### Enable GitHub Insights

Built-in at: `https://github.com/adugyamfinich/prompt-hub/insights`

### Track Star History

Use: https://star-history.com/

Embed in README:
```markdown
[![Star History](https://api.star-history.com/svg?repos=adugyamfinich/prompt-hub&type=Date)](https://star-history.com/#adugyamfinich/prompt-hub)
```

## 🔒 Security

### Enable Security Features

1. Settings → Security & analysis
2. Enable:
   - Dependency graph
   - Dependabot alerts
   - Dependabot security updates

### Add SECURITY.md

```markdown
# Security Policy

## Reporting a Vulnerability

Email: security@yourproject.com

We take security seriously and will respond within 48 hours.
```

## 📈 Growth Strategies

### 1. Seed with Quality Content

Add 10-20 high-quality prompts before promoting:
- Cover main categories
- Include various difficulty levels
- Provide excellent examples

### 2. Promote

- Share on Reddit (r/ChatGPT, r/ClaudeAI, r/MachineLearning)
- Post on Twitter/X with relevant hashtags
- Submit to Awesome Lists (awesome-chatgpt-prompts, etc.)
- Share in Discord communities
- Write blog post announcing launch

### 3. Engage Community

- Respond quickly to issues
- Thank contributors
- Feature community prompts
- Regular updates/newsletters

### 4. Maintain Quality

- Review all submissions
- Update outdated prompts
- Remove deprecated content
- Keep documentation current

## 🛠️ Maintenance

### Weekly Tasks
- [ ] Review and merge PRs
- [ ] Respond to issues
- [ ] Update featured prompts

### Monthly Tasks
- [ ] Update documentation
- [ ] Audit prompt quality
- [ ] Generate statistics report
- [ ] Community highlights

### Quarterly Tasks
- [ ] Major documentation updates
- [ ] Reorganize if needed
- [ ] Solicit feedback
- [ ] Plan new features

## 🆘 Troubleshooting

### Validation Script Fails

```bash
# Check Python version
python --version  # Should be 3.8+

# Run with verbose output
python -v scripts/validate_prompt.py path/to/prompt.md
```

### GitHub Actions Not Running

- Check workflow file syntax
- Ensure Actions are enabled (Settings → Actions)
- Check workflow permissions (Settings → Actions → General)

### Index Not Generating

```bash
# Check for Python errors
python scripts/generate_index.py

# Verify prompts directory exists
ls -la prompts/
```

## 📚 Next Steps

Now that your PromptHub is set up:

1. ✅ Add your first 5-10 prompts
2. ✅ Customize branding and links
3. ✅ Test all functionality
4. ✅ Write announcement post
5. ✅ Share with community
6. ✅ Engage with contributors

## 🎉 Congratulations!

Your PromptHub is ready to go! Start building the world's best prompt library.

---

**Questions?** Open an issue or discussion on GitHub.

**[Back to Main README](README.md)**
