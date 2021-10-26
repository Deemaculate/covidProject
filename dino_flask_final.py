from flask import Flask, render_template

app = Flask(__name__)

all_posts = [{"title": "death toll",
              "content": "May"},

              {"title": "Imports",
               "content": "Righteous"}
              ]


@app.route('/')
def index():
    return render_template('index.html')





@app.route('/posts')
def posts():
    return render_template('posts.html',  posts = all_posts)



if __name__== "__main__":
    app.run(debug=True)
