# Spandan-Shah GitHub Profile — V3 Setup

This update keeps the Ashish-Patel-inspired design, makes all **12** projects visible in one Featured Projects section, expands the icon-based tech stack from the supplied résumé and project descriptions, and ensures the 3D contribution section does not show a broken image before its first successful run.

## Files to copy into `Spandan-Shah/Spandan-Shah`

Copy the contents of this folder into the **root** of the special GitHub profile repository, preserving folders:

- `README.md`
- `.github/workflows/profile-3d.yml`
- `assets/project-cards/*.svg`
- `scripts/generate_cards.py`
- `profile-3d-contrib/profile-night-view.svg` (initial honest placeholder; the workflow overwrites it with real GitHub contributions)

`SETUP.md` is only for setup; it does not need to appear in your public profile.

## Deploy using Windows Command Prompt

```cmd
git status
git add README.md .github/workflows/profile-3d.yml assets/project-cards scripts/generate_cards.py profile-3d-contrib/profile-night-view.svg
git commit -m "Unify project cards, expand skill icons and repair 3D graph setup"
git pull --rebase origin main
git push origin main
```

If `git status` reports a rebase in progress, finish or abort that rebase **before** starting these commands. If `git pull --rebase` reports conflicts, resolve them and continue; never use `git push --force` to bypass them.

## Make the real 3D chart appear

1. Open <https://github.com/Spandan-Shah/Spandan-Shah/actions>.
2. Select **GitHub Profile - 3D Contributions and Project Cards**.
3. Click **Run workflow** and choose `main`. The updated workflow also runs on relevant pushes and daily.
4. If the workflow succeeds, check that this tracked file was replaced by an actual contribution SVG:
   `profile-3d-contrib/profile-night-view.svg`.
5. Open the repository's **Settings → Actions → General → Workflow permissions**. If pushing generated files fails with a `403` permissions error, allow **Read and write permissions** for `GITHUB_TOKEN` where policy permits. The workflow already declares `permissions: contents: write`.

The SVG in the initial package is explicitly a **placeholder**, not fabricated GitHub activity. A README cannot synthesize your real 3D contribution data on its own. If the workflow fails, open the failed run's steps (especially **Generate real GitHub 3D contribution calendar** / **Commit generated SVG files**) and inspect its logs.

## Notes

- This package uses [Skill Icons](https://github.com/tandpfun/skill-icons) for recognizable technology logos. Specialized domains without a suitable icon appear as text labels or Shields.io badges.
- The 12 project cards use tracked SVGs in `assets/project-cards`. Only confirmed public repositories are linked. The four public cards receive stars/forks on successful daily updates; no fictional numbers are added for private/research projects.
- The generator reads public GitHub repository metadata using the built-in `GITHUB_TOKEN` (no personal access token needed for ordinary public data).
- Existing Snake and Pac-Man workflow files can be removed if no longer wanted. This workflow only generates the requested 3D variant.
