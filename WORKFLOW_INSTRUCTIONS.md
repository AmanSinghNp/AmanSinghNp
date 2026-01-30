# GitHub Actions Workflow Instructions

This repository contains two GitHub Actions workflows that generate visual assets for your GitHub profile.

## Workflows

### 1. Generate Snake Animation (`snake.yml`)
Generates an animated snake eating your GitHub contributions.

- **Schedule**: Runs daily at midnight UTC (`0 0 * * *`)
- **Manual Trigger**: ✅ Enabled via `workflow_dispatch`
- **Outputs**:
  - `github-contribution-grid-snake.svg` (light theme)
  - `github-contribution-grid-snake-dark.svg` (dark theme)
- **Location**: Pushed to the `output` branch

### 2. GitHub 3D Profile Contribution (`profile-3d.yml`)
Generates a 3D visualization of your GitHub contributions.

- **Schedule**: Runs daily at 6 PM UTC (`0 18 * * *`)
- **Manual Trigger**: ✅ Enabled via `workflow_dispatch`
- **Output**: Creates 3D contribution profile in `profile-3d-contrib/` directory
- **Location**: Committed to the main branch

## How to Trigger Workflows Manually

### Option 1: GitHub Web Interface
1. Go to the [Actions tab](https://github.com/AmanSinghNp/AmanSinghNp/actions)
2. Select the workflow you want to run:
   - "Generate Snake" for the snake animation
   - "GitHub-Profile-3D-Contrib" for the 3D profile
3. Click the "Run workflow" button
4. Select the branch (usually `main`)
5. Click "Run workflow" to confirm

### Option 2: GitHub CLI (gh)
If you have the GitHub CLI installed and authenticated:

```bash
# Trigger the Snake workflow
gh workflow run snake.yml --ref main

# Trigger the 3D Profile workflow
gh workflow run profile-3d.yml --ref main
```

### Option 3: GitHub API
Using curl with a personal access token:

```bash
# Trigger the Snake workflow
curl -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer YOUR_GITHUB_TOKEN" \
  https://api.github.com/repos/AmanSinghNp/AmanSinghNp/actions/workflows/snake.yml/dispatches \
  -d '{"ref":"main"}'

# Trigger the 3D Profile workflow
curl -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer YOUR_GITHUB_TOKEN" \
  https://api.github.com/repos/AmanSinghNp/AmanSinghNp/actions/workflows/profile-3d.yml/dispatches \
  -d '{"ref":"main"}'
```

## Viewing Workflow Results

After the workflows complete:

- **Snake animations**: Available at:
  - `https://raw.githubusercontent.com/AmanSinghNp/AmanSinghNp/output/github-contribution-grid-snake.svg`
  - `https://raw.githubusercontent.com/AmanSinghNp/AmanSinghNp/output/github-contribution-grid-snake-dark.svg`

- **3D Profile**: Available in the `profile-3d-contrib/` directory on the main branch

## Recent Fix

✅ **Fixed**: Updated snake.yml to use a more reliable GitHub Pages action:
- Original (main branch): `peaceiris/actions-gh-pages@v3`
- Changed to: `crazy-max/ghaction-github-pages@v4.2.0`

This change uses the latest version of the crazy-max action which is better maintained and resolves potential deployment issues.

## Troubleshooting

If workflows fail:
1. Check the [Actions tab](https://github.com/AmanSinghNp/AmanSinghNp/actions) for error logs
2. Ensure the `GITHUB_TOKEN` has appropriate permissions
3. Verify that the `output` branch exists for snake workflow
4. Check that dependencies (actions) are available and up-to-date
