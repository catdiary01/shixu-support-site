# Shixu support site

Official support and privacy site for the Shixu (时序) iPhone app.

## Structure

- `index.html`, `support/index.html`, `privacy/index.html`: Simplified Chinese pages.
- `en/`: matching U.S. English pages.
- `assets/css/site.css`: shared responsive design. No external fonts, scripts, analytics, or runtime dependencies.
- `404.html`: custom page for the intended GitHub Pages project path.
- `build.py`: standard-library generator for all six HTML pages.

## Local preview

From this directory, run `python3 -m http.server 8000` and open `http://localhost:8000/`. For a project-path simulation, serve the parent workspace and open `http://localhost:8000/shixu-support-site/`. The 404 page's home link uses the intended project path and works in that simulation.

## Deployment

Publish reviewed static files through GitHub Pages from `main` at the repository root. Verify HTTPS, all six intended URLs, the 404 page, and the policy effective date after each release. Support and privacy inquiries share `grippe-bearded9p@icloud.com`. Compare privacy statements with the submitted App build before each release. Do not copy iOS source, builds, certificates, profiles, logs, or credentials into this repository.

## Maintenance

For each App release, compare its actual data handling and help content with both language versions. Update `build.py`, regenerate pages, inspect the diff, preview desktop and mobile layouts, check local links, then deploy only reviewed content. Record the release, policy effective date, and verified URLs in the site's history and the designated Obsidian publishing checklist. A change to storage, sync, notifications, third-party code, or support email handling requires a privacy policy review.

