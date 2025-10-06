mkdir -p docs && for f in Slides/*.md; do npx @marp-team/marp-cli "$f" -o "docs/$(basename "$f" .md).html"; done

