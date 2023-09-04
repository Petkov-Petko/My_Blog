import requests

blog_get_url = "https://api.npoint.io/c790b4d5cab58020d391"

class Post:
    def __init__(self):
        self.all_posts_json = requests.get(blog_get_url).json()

    def get_title(self, nr_of_blog):
        return self.all_posts_json[nr_of_blog]["title"]

    def get_subtitle(self, nr_of_blog):
        return self.all_posts_json[nr_of_blog]["subtitle"]

    def get_body(self, nr_of_blog):
        return self.all_posts_json[nr_of_blog]["body"]