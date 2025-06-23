from flask import render_template, request

from . import main_blueprint

@main_blueprint.route('/', methods=['GET'])
def index():

    username = request.args.get('username')

    return render_template('/index.html', username=username)