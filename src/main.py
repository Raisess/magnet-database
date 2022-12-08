#! /usr/bin/env python3

from flask import Flask, redirect, request

from controllers import magnet_link_controller
from view import View

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index() -> str:
  html = View("index")
  return html.render()


@app.route("/create_magnet_link", methods = ["POST", "GET"])
def create_magnet_link() -> str | None:
  try:
    if request.method == "POST":
      name = request.form["name"]
      uri = request.form["uri"]
      magnet_link_controller.create_magnet_link(name, uri)
      return redirect(f"/search_magnet_links?name={name}")

    html = View("pages/magnet_link/create_magnet_link")
    return html.render()
  except Exception as exception:
    return "ERROR: " + str(exception)


@app.route("/search_magnet_links", methods = ["GET"])
def search_magnet_links() -> str:
  try:
    name = request.args.get("name")
    result = magnet_link_controller.search_magnet_links(name)
    html = View("pages/magnet_link/search_magnet_links")
    return html.render({ "magnet_links": result })
  except Exception as exception:
    return "ERROR: " + str(exception)


if __name__ == "__main__":
  app.run()
