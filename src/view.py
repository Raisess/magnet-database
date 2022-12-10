from jinja2 import Template

class View:
  def __init__(self, filename: str, path: str = "public/"):
    self.__filename = filename
    self.__path = path

  def render(self, parameters: dict[str, any] = {}) -> str:
    file = open(f"{self.__path}/{self.__filename}.html", "r")
    template = Template(file.read())
    file.close()
    return template.render(parameters)
