import requests

class Post:
    def __init__(self) -> None:
        response = requests.get("https://api.npoint.io/84fa729d0a6b3c138957")
        response.raise_for_status()
        self.posts = response.json()

    def get_posts(self):
        return self.posts


if __name__ == "__main__":
    posts = Post()
    print(posts.get_posts())