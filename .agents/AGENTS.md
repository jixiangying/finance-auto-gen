# Antigravity AI Agent Rules for Finance Auto Gen

This file defines the project-scoped rules that all Antigravity AI agents (including the daily automated pipelines) MUST strictly follow in this workspace.

## 🛡️ Git Safety & Exclusions

To prevent sensitive information leaks or committing of local development artifacts, you must adhere to the following rules:

### 1. Pre-Commit Review & Verification
- **NO Local Paths**: Before running `git commit`, inspect the diff. You MUST ensure that no files being committed contain local system absolute paths (e.g., `/Users/username/...` or `/tmp/...`).
- **NO Environment Credentials**: Never stage or commit files containing API keys, OAuth tokens, client secrets, or cookies.
- **NO Launchd plists or Scripts**: Ensure `.plist` configurations or background runner wrapper scripts (`run_pipeline.sh`) are kept local and never pushed to GitHub.

### 2. Automatic .gitignore Enforcement
If the CLI, python tools, or browser scripts generate new files or directories in the project workspace, you MUST proactively verify if they are in `.gitignore`.
If not, append them to `.gitignore` immediately before staging. Examples of files that should be ignored:
- Project cache directories (e.g., `cache/`, `.vitepress/cache/`)
- Trajectory logs or print logs (`*.log`)
- Temporary files (`tmp/`, `scratch/`)

### 3. Git Staging Command Restrictions
- **NEVER use `git add .`** or `git add -A` blindly in pipeline scripts or manual commands.
- Always use precise file paths (e.g., `git add reports/YYYY-MM-DD-morning.md`) to prevent accidental staging of untracked files.
