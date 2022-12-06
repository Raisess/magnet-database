from jinja2 import Template

class View:
  def __init__(self, filename: str):
    self._filename = filename

  def render(self, parameters: dict[str, any] = {}) -> str:
    file = open(f"./src/view/{self._filename}.html", "r")
    template = Template(file.read())
    file.close()
    return template.render(parameters)
