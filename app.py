from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    output = render_template('index.html')
    return output


@app.route('/from/<direction>/')
def direction(direction):
    output = render_template('direction.html')
    return output


@app.route('/tours/<id>/')
def tour(id):
    output = render_template('tour.html')
    return output


if __name__ == '__main__':
    app.run()
