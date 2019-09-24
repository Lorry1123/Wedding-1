from flask import Blueprint, render_template

web_bp = Blueprint('web', __name__, url_prefix="/lottery", template_folder="../template", static_folder="../static")

@web_bp.route("/")
def render():
    return render_template('lottery.html')