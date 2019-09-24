from flask import Blueprint, render_template

web_bp = Blueprint('web', __name__, template_folder="../template")

@web_bp.route("/")
def render():
    return render_template('lottery.html')