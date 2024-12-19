from flask import Flask, request, render_template

app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route("/file")
def view_file():
    name = request.args.get('name', '')
    if name == '':
        return 'No file?'
    else:
        try:
            with open(f'/app/uploads/{name}', 'rb') as f:
                text = f.read().decode('UTF-8').replace('\n', '<br>')
                return render_template("view.html", blog=text, filename=name)
        except FileNotFoundError:
            return 'File not found'
if __name__ == '__main__':
    app.run()
