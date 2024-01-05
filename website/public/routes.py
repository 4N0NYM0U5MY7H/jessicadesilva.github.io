# -*- coding: utf-8 -*-
"""Routes for the main section of the website."""
from http import HTTPStatus

from flask import Blueprint, render_template

from website.utils import dev_utils

blueprint = Blueprint("public", __name__, static_folder="../static")


@blueprint.route("/home.html")
def home():
    return render_template("public/home.j2"), HTTPStatus.OK


@blueprint.route("/about.html")
def about():
    return render_template("public/about_me.j2"), HTTPStatus.OK


@blueprint.route("/about/cv.html")
def cv():
    return render_template("public/desilva_cv.j2"), HTTPStatus.OK


@blueprint.route("/news.html")
@dev_utils
def student_news(debug=False):
    return render_template("public/student_news.j2", debug=debug), HTTPStatus.OK
