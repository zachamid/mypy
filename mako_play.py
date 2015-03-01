from mako.template import Template

mytemplate = Template("""Content-type: text/html\n\n


<html>hello, ${name}!</html>""")
print(mytemplate.render(name="jack"))