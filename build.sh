pipenv run python render.py ./style/template.jinja $1
pandoc -c ./style/pandoc.css out.md -f markdown -t html -s -o out.html
pandoc --latex-engine=xelatex out.html -o out.pdf
