from mako.template import Template

mytemplate = Template("hello, ${name}!")
print(mytemplate.render(name="jack"))