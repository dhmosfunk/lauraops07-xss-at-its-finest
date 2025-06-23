from flask import render_template, request

from . import main_blueprint

comments = []

@main_blueprint.route('/', methods=['GET'])
def index():

    username = request.args.get('username')

    return render_template('/index.html', username=username)

@main_blueprint.route('/feedback', methods=['GET', 'POST'])
def feedback():

    if request.method == 'POST':

        username = request.form.get('username')
        message = request.form.get('message')
        
        if username and message:
            comments.append({'username': username, 'message': message})

        return '', 204  

    return render_template('/feedback.html', comments=comments)

@main_blueprint.route('/clear', methods=['GET'])
def clear():
    comments.clear()
    return '', 204 