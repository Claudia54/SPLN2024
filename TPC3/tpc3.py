import jinja2, os, json 
from glob import glob

mods = glob("*.py")

if len(mods) >= 1:
    name = mods[0]
pp = jinja2.Template("""

[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "{{name}}"
authors = [
    {name = "{{autor}}", email="{{email}}"},
]
classifiers = [
    "License :: OSI Approved :: MIT License",
]
requires-python = ">=3.8"
dynamic = ["version", "description"]

[project.scripts]
{{name}} = "{{name}}:main"
                     
""")

metadata_path = str(os.path.expanduser('n.json'))
file = open(metadata_path)
data = json.load(file)
autor = data["Author"]
email = data["Email"]

out  = pp.render({"name":name,"author":autor, "email":email})

file_output = open("proje.toml","w")
file_output.write(out)