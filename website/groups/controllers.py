from . import groups_blueprint
from flask import render_template


@groups_blueprint.route("/math")
def mentor_groups_math():
    return render_template("groups/mentor_groups_math.j2")


@groups_blueprint.route("/stan")
def mentor_groups_stan():
    return render_template("groups/mentor_groups_stan.j2")
