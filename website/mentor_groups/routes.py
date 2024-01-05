# -*- coding: utf-8 -*-
"""Routes for the mentor groups section of the website."""
from flask import Blueprint, render_template

blueprint = Blueprint(
    "mentor_groups", __name__, url_prefix="/mentor_groups", static_folder="../static"
)


@blueprint.route("/math.html")
def math():
    return render_template("mentor_groups/math.j2")


@blueprint.route("/stan.html")
def stan():
    return render_template("mentor_groups/stan.j2")
