from mako.template import Template
print(Template("Content-type: text/html\n\nhello ${data}!").render(data="world"))