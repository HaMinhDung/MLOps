#!/usr/bin/env pwsh

# GitHub Push Script for PowerShell
# This script helps you push your MLOps project to GitHub

Write-Host "🚀 MLOps Project GitHub Setup" -ForegroundColor Green
Write-Host "==============================" -ForegroundColor Green

# Check if git is configured
$gitUser = git config user.name
$gitEmail = git config user.email

if (-not $gitUser -or -not $gitEmail) {
    Write-Host "❌ Git user not configured!" -ForegroundColor Red
    Write-Host "Please run the following commands first:" -ForegroundColor Yellow
    Write-Host "git config user.name 'Your Name'" -ForegroundColor Yellow
    Write-Host "git config user.email 'your.email@example.com'" -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Git configured for: $gitUser ($gitEmail)" -ForegroundColor Green

# Get GitHub username and repository name
$githubUsername = Read-Host "Enter your GitHub username"
$repoName = Read-Host "Enter repository name (default: iris-mlops-pipeline)" 

if (-not $repoName) {
    $repoName = "iris-mlops-pipeline"
}

$repoUrl = "https://github.com/$githubUsername/$repoName.git"

Write-Host "`n🔗 Repository URL: $repoUrl" -ForegroundColor Cyan

# Confirm before proceeding
$confirm = Read-Host "`nProceed with GitHub setup? (y/N)"
if ($confirm -ne "y" -and $confirm -ne "Y") {
    Write-Host "❌ Cancelled by user" -ForegroundColor Red
    exit 0
}

try {
    # Add remote origin
    Write-Host "`n📡 Adding remote origin..." -ForegroundColor Blue
    git remote add origin $repoUrl
    
    # Rename branch to main
    Write-Host "🌿 Renaming branch to main..." -ForegroundColor Blue
    git branch -M main
    
    # Push to GitHub
    Write-Host "⬆️ Pushing to GitHub..." -ForegroundColor Blue
    git push -u origin main
    
    Write-Host "`n🎉 Successfully pushed to GitHub!" -ForegroundColor Green
    Write-Host "🌐 Your repository is now available at: https://github.com/$githubUsername/$repoName" -ForegroundColor Cyan
    
    # Open repository in browser
    $openBrowser = Read-Host "`nOpen repository in browser? (y/N)"
    if ($openBrowser -eq "y" -or $openBrowser -eq "Y") {
        Start-Process "https://github.com/$githubUsername/$repoName"
    }
    
} catch {
    Write-Host "`n❌ Error occurred: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "`n💡 Troubleshooting tips:" -ForegroundColor Yellow
    Write-Host "1. Make sure the repository exists on GitHub" -ForegroundColor Yellow
    Write-Host "2. Check your GitHub authentication (username/password or token)" -ForegroundColor Yellow
    Write-Host "3. Verify the repository URL is correct" -ForegroundColor Yellow
    Write-Host "4. See GITHUB_SETUP.md for detailed instructions" -ForegroundColor Yellow
}

Write-Host "`n📋 Next steps:" -ForegroundColor Magenta
Write-Host "1. Verify all files are uploaded correctly on GitHub" -ForegroundColor White
Write-Host "2. Enable GitHub Actions (should work automatically)" -ForegroundColor White
Write-Host "3. Create releases for versioning" -ForegroundColor White
Write-Host "4. Set up branch protection rules" -ForegroundColor White
Write-Host "5. Add collaborators if needed" -ForegroundColor White

Read-Host "`nPress Enter to exit"
