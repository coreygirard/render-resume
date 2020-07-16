# render-resume

Renders (potentially) beautiful resumes from three text files:

- Resume data in the [JSON Resume](https://jsonresume.org/) format
- Template in the [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/templates/) format. This is responsible for the large-scale page layout, and should output a valid Markdown file
- Styling via CSS. You know what CSS is. This is used by `pandoc` to render intermediate HTML to the final PDF

## Usage

Run `build.sh`, passing the resume data path, IE:

```
bash build.sh ./data/example.json
```

## Flow

- Jinja2 template and JSON data are rendered into intermediate Markdown
- Markdown is rendered to intermediate HTML via `pandoc`
- HTML plus CSS is rendered to PDF via `pandoc`
