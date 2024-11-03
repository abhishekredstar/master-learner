class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, title, content):
        self.posts.append({"title": title, "content": content})

    def display_posts(self):
        for post in self.posts:
            print(f"Title: {post['title']}\nContent: {post['content']}\n")

# Create a blog instance
ai_blog = Blog()

# Add posts
ai_blog.add_post("The Future of AI", "Exploring how AI will shape various industries.")
ai_blog.add_post("Ethics in AI", "Discussing the importance of ethical considerations in AI development.")
ai_blog.add_post("AI in Everyday Life", "How AI is becoming a part of our daily routines.")

# Display all posts
ai_blog.display_posts()
