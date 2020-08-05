from flask import jsonify, render_template, request, redirect, url_for
from thebookofinternet import app, db, limiter
from thebookofinternet.models import Post


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/get_post_count', methods=['GET'])
def get_post_count():
    return jsonify({'count': Post.query.count()})


@app.route('/get_posts', methods=['GET'])
def get_posts():
    down_to = int(request.args['down_to'])
    posts = []
    for i in range(10):
        posts.append(Post.query.get(down_to-i).to_dict())

    return jsonify({'posts': posts})


@app.route('/upload_post', methods=['POST'])
@limiter.limit('1/minute')
def upload_post():
    title = request.form['title']
    username = request.form['username']
    post = request.form['post']

    new_post = Post(
        title=title,
        username=username,
        post=post
    )
    db.session.add(new_post)
    db.session.commit()

    return render_template('index.html')