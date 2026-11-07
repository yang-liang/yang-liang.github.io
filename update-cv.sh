#!/bin/bash
# update-cv.sh — copy the latest compiled CV from academic_dossier into the site.
# Afterwards: commit and push as usual.
set -e
cd "$(dirname "$0")"
CV_SRC="../academic_dossier/current/job_market/packet/cv.pdf"
cp "$CV_SRC" static/cv_liang_sdsu.pdf
echo "Copied $CV_SRC -> static/cv_liang_sdsu.pdf"
