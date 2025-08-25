# GitHub Setup Instructions

## Step 1: Create GitHub Repository

1. Go to [GitHub.com](https://github.com) and log in to your account
2. Click the "+" icon in the top right corner and select "New repository"
3. Set the repository name: `iris-mlops-pipeline` (or your preferred name)
4. Set description: `Complete MLOps pipeline for Iris flower classification with MLflow tracking, FastAPI, and Docker deployment`
5. Choose visibility: Public or Private
6. **DO NOT** initialize with README, .gitignore, or license (we already have these)
7. Click "Create repository"

## Step 2: Connect Local Repository to GitHub

After creating the repository on GitHub, run these commands in PowerShell:

```powershell
# Add the remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/iris-mlops-pipeline.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Verify Upload

After pushing, verify that all files are uploaded correctly on GitHub:

- ✅ README.md with project description and badges
- ✅ Source code in `src/` directory
- ✅ Trained models in `models/` directory  
- ✅ Docker configuration files
- ✅ Documentation in `docs/` directory
- ✅ GitHub Actions CI/CD pipeline
- ✅ Tests and Postman collection

## Alternative: Using GitHub CLI

If you have GitHub CLI installed, you can create and push in one command:

```powershell
# Create repository and push (replace with your preferred name)
gh repo create iris-mlops-pipeline --public --source=. --remote=origin --push
```

## Repository Features

Your repository will include:

- 🤖 **ML Models**: Random Forest & SVM with 93.33% accuracy
- 📊 **MLflow Integration**: Experiment tracking and model registry
- 🚀 **FastAPI**: RESTful API with automatic documentation
- 🐳 **Docker**: Multi-container deployment setup
- 🧪 **Testing**: Comprehensive test suite and Postman collection
- 📚 **Documentation**: Complete setup and deployment guides
- ⚙️ **CI/CD**: GitHub Actions workflow for automated testing

## Next Steps

After pushing to GitHub:

1. Enable GitHub Actions (should work automatically)
2. Create releases for versioning
3. Set up branch protection rules for main branch
4. Add collaborators if needed
5. Consider setting up GitHub Pages for documentation

## Troubleshooting

If you encounter authentication issues:

1. **HTTPS**: You may need to use a Personal Access Token instead of password
2. **SSH**: Set up SSH keys for authentication
3. **GitHub CLI**: Use `gh auth login` for easier authentication

For detailed authentication setup, see: https://docs.github.com/en/authentication
