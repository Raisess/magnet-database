#! /usr/bin/env python3

from flask import Flask, redirect, url_for
from app.magnet_link.create_magnet_link import CreateMagnetLink
from controllers.magnet_link_controller import MagnetLinkController
from repositories.magnet_link_repository import MagnetLinkRepository

app = Flask(__name__)

# utils
@app.route("/success", methods = ["GET"])
def success() -> str:
  return "OK"

@app.route("/fail", methods = ["GET"])
def fail() -> str:
  return "ERROR"


# magnet link related
@app.route("/create_magnet_link", methods = ["POST"])
def create_magnet_link() -> str:
  try:
    controller = MagnetLinkController(CreateMagnetLink(MagnetLinkRepository()))
    controller.create_magnet_link()
    redirect(url_for("success"))
  except:
    redirect(url_for("fail"))


if __name__ == "__main__":
  app.run()
