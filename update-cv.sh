#!/bin/bash
# update-cv.sh — copy the latest compiled CV from always_jm into the site.
# Afterwards: commit and push as usual.
set -e
cd "$(dirname "$0")"
CV_SRC="../always_jm/Current/Yang_Liang_CV.pdf"
cp "$CV_SRC" static/cv_liang_sdsu.pdf
echo "Copied $CV_SRC -> static/cv_liang_sdsu.pdf"
