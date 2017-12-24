# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
# 	return 'Hello World!'

# @app.route('/user/<username>')
# def user_index(username):
# 	return 'Hello {}'.format(username)

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
# 	return 'Post {}'.format(post_id)

# if __name__ == '__main__':
# 	app.run()

# from flask import render_template

# @app.route('/user/<username>')
# def user_index(username):
# 	return render_template('user_index.html', username=username)

# if __name__ == '__main__':
# 	app.run()


# from flask import render_template, Flask

# app = Flask(__name__)

# @app.route('/user/<username>')
# def user_index(username):
#     return render_template('user_index.html', username=username)



# from flask import render_template, redirect, url_for, Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
# 	return redirect(url_for('user_index', username='default'))

# @app.route('/user/<username>')
# def user_index(username):
# 	return render_template('user_index.html', username=username)


# from flask import request

# request.headers.get('User-Agent')


# cookies
from flask import make_response, render_template, Flask, request

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'),404
	pass

@app.route('/')
def index():
	username = request.cookies.get('username')
	return 'Hello, {}'.format(username)

@app.route('/user/<username>')
def user_index(username):
	resp = make_response(render_template('user_index.html', username=username))
	resp.set_cookie('username', username)
	return resp

if __name__ == '__main__':
	app.run












  

