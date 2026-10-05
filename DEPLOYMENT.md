# Deployment / Submission Configuration

## Local deployment

This project runs as a Python standard-library web server.

```powershell
py app.py
```

Application URL:

```text
http://127.0.0.1:8000
```

No dependency installation is required.

## GitHub repository submission

Recommended repository name:

```text
number-statistics-task5
```

Make the repository **Public** because the internship submission guidelines request a public GitHub repository.

After creating the repository, from this project folder:

```powershell
git init
git branch -M main
git add .
git commit -m "Complete Task 5 Number Statistics web application"
git remote add origin https://github.com/YOUR-USERNAME/number-statistics-task5.git
git push -u origin main
```

Replace `YOUR-USERNAME` with the GitHub username shown on your account.

## Verification

After pushing:

```powershell
git status
git remote -v
git log --oneline -1
```

Expected status:

```text
nothing to commit, working tree clean
```

The GitHub repository should contain all project files.
