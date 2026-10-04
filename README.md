# Personal Website

Source for https://yang-liang.github.io, a one-page Hugo site (PaperMod theme, heavily trimmed).
Pushing to `main` triggers GitHub Actions (`.github/workflows/hugo.yml`), which builds and publishes the site in about a minute.

## Updating the site

1. **Papers / links**: edit `config.yml` (`workingPapers`, `acceptedPublications`, `bookChaptersPolicyWork`, `socialIcons`).
   Each paper can have an optional `mediaCoverage` list of `{ name, url }`.
2. **CV**: recompile `cv_liang_sdsu.tex` in `always_jm/CV`, then run `./update-cv.sh` (expects `always_jm` cloned next to this repo).
3. **Preview** (optional): `hugo server`, then open http://localhost:1313
4. **Publish**: commit and push. Check progress in the repo's **Actions** tab.

New computer: clone this repo, `brew install hugo`, and you're set.

## Where things are

| What | File |
|---|---|
| All page content | `config.yml` |
| Page layout | `layouts/partials/index_profile.html` |
| Styling | `assets/css/common/profile-mode.css` |
| Photo, favicons, CV | `static/` |
| Header / footer / analytics / math | `layouts/partials/` |

## Attribution
Started from Pascal Michaillat's academic Hugo template, based on [PaperMod](https://github.com/adityatelange/hugo-PaperMod).
Custom content: MIT. Theme: see `themes/PaperMod/LICENSE`.
