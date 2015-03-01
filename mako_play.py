from mako.template import Template
print(Template("""Content-type: text/html\n\n


hello ${data}!""").render(data="world"))