from flask import Flask, render_template
import requests
from post import Post

post = Post()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts = post.all_posts_json)

@app.route('/post/<int:nr_of_post>')
def post_show(nr_of_post):
    return render_template("post.html", post_title=post.get_title(nr_of_post),
                           post_subtitle=post.get_subtitle(nr_of_post),
                           post_body=post.get_body(nr_of_post))


if __name__ == "__main__":
    app.run(debug=True)
