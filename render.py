import json
import sys

from jinja2 import Template


def load_template(filename):
    with open(filename, "r") as f:
        data = f.read()
    return Template(data)


def load_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data


def render(template, data):
    return template.render(**data)


def write_markdown(out):
    with open("out.md", "w") as f:
        f.write(out)


if __name__ == "__main__":
    template = load_template(sys.argv[1])
    data = load_data(sys.argv[2])
    out = render(template, data)
    write_markdown(out)
