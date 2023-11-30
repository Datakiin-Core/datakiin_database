""" ROUTES FOR MAIN """
#pylint: disable=E0401
from datetime import datetime
from flask import (
    render_template,
    Blueprint,
)
import pandas as pd
from flask_login import current_user



main_blueprint= Blueprint(
    "main",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@main_blueprint.route('/', defaults={'path': ''})
@main_blueprint.route('/<path:path>')
def home(path):
    """ INDEX PAGE """
    date = datetime.now()
    image_sources = [[...], [...], [...]]
    if current_user.is_authenticated:
        image_sources = current_user.get_images()
        user_name = current_user.name
    else:
        user_name = "Guest"
    data = [image_sources[i:i+3] for i in range(0, len(image_sources), 3)]
    d_f = pd.DataFrame(data)

    html_table = d_f.to_html(escape=False, index=False, header=False)
    return render_template('home.jinja2', date=date, path=path,
                            user_name=user_name, html_table=html_table)


@main_blueprint.route('/home')
def welcome():
    """ Close Login """
    if current_user.is_authenticated:
        image_sources = current_user.get_images()
        user_name = current_user.name
    else:
        user_name = "Guest"
    data = [image_sources[i:i+3] for i in range(0, len(image_sources), 3)]
    d_f = pd.DataFrame(data, columns=None)

    html_table = d_f.to_html(escape=False, index=False)
    return render_template('home.jinja2', user_name=user_name, html_table=html_table)
