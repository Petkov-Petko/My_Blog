from flask import Flask, render_template

from post import Post

post = Post()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts = post.all_posts_json)

@app.route('/post/<int:number_post>')
def post_show(number_post):
    return render_template("post.html", post_title=post.get_title(number_post),
                           post_subtitle=post.get_subtitle(number_post),
                           post_body=post.get_body(number_post))


if __name__ == "__main__":
    app.run(debug=True)
