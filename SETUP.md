# Spandan-Shah Profile — Installation and Maintenance

This package reproduces the **dark-blue editorial structure** of the uploaded `ashishpatel26` reference, with your own details. It uses **GitHub-style two-column project cards** and **yoshi389111/github-profile-3d-contrib** instead of Snake or Pac-Man.

## Included

- `README.md` — complete profile page, social links, 12 project cards, achievements, research, tech stack and GitHub statistics.
- `assets/project-cards/*.svg` — 12 self-contained project images, already generated. They display immediately after you upload them.
- `scripts/generate_cards.py` — updates the public cards' current language/star/fork data using the GitHub API. It does **not** invent data for non-public projects.
- `.github/workflows/profile-3d.yml` — daily automation for **3D contribution history** and refreshed card metadata.

## Publish it

1. Open **https://github.com/Spandan-Shah/Spandan-Shah**. This is the special public repository that displays your profile README.
2. Download and **extract** the package, then upload the contents of the extracted folder **to the root of your profile repository**, keeping every folder path exactly as supplied. Do not upload the ZIP itself as a single file.
3. Replace the existing `README.md`. If the repository still has `.github/workflows/snake.yml`, `.github/workflows/pacman.yml`, or another older animation workflow you no longer want, remove those files separately to prevent duplicate scheduled jobs.
4. Check **Settings → Actions → General → Workflow permissions**. The Action needs permission to commit updated SVGs. This workflow declares `permissions: contents: write`, but an account/organization restriction may still require adjustment.
5. Run **Actions → GitHub Profile - 3D Contributions and Project Cards → Run workflow** once, on your default branch.
6. After the successful run, check the repository for `profile-3d-contrib/profile-night-view.svg`. The 3D image will then appear under the metrics dashboard. Project-card star and fork numbers also refresh.

## Optional Git command route

From a local clone of `Spandan-Shah/Spandan-Shah`, copy the extracted package's files into the clone without changing paths, then run:

```bash
git add README.md .github/workflows/profile-3d.yml scripts/generate_cards.py assets/project-cards/
git commit -m "feat: refresh GitHub profile and add 3D contributions"
git push
```

If you removed earlier workflows, also stage those deletions with `git add -u .github/workflows` before committing.

## How it works

The 3D graph is generated from your GitHub account's recorded contribution activity using the `yoshi389111` Action (pinned to release `v0.9.3`) and saved into this same repository. The schedule is 22:00 UTC daily, which is **03:30 IST the following day**. GitHub's scheduled runs may be delayed. The workflow can also be run manually.

For **public repositories**, the project-card generator reads the GitHub API using the workflow's built-in, short-lived `GITHUB_TOKEN`. It updates public star/fork numbers; before the first run the prebuilt cards show “Public repository” without claiming a count. **Research/private work** is displayed without a false repository link, fork count or public stars. Edit the project list inside `scripts/generate_cards.py` if the project or visibility changes, and rerun the script before committing. No personal access token is required for the current public-only configuration.

The GitHub stats widgets and typing header are served by external public services. They can sometimes fail, be rate-limited or display cached values; this does not imply a problem with your repository. The action itself also depends on GitHub's API availability. GitHub may not show the 3D graph until the first completed run. Enabling private contribution visibility in your GitHub profile settings may affect the graph's totals, but it **does not** expose private repository code.

## Notes on the reference

The original profile used **Snake**; that workflow is intentionally not included. This profile uses the **3D night-view graph** as requested. GitHub's built-in native **Pinned repositories** area (under the README) is controlled from the profile page; the custom README cards reproduce its look but do not change the official pinned repository selection. You can separately pin up to six repositories through **Customize your pins** on your GitHub profile.
