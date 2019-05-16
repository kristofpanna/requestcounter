from flask import Flask, render_template, request, redirect

app = Flask(__name__)

counter = {'get_counter': 0, 'post_counter': 0}


@app.route('/')
def route_index():
    return render_template('index.html')


@app.route('/request-counter', methods=['GET', 'POST'])
def request_counter():
    if request.method == 'GET':
        counter['get_counter'] += 1

    elif request.method == 'POST':
        counter['post_counter'] += 1

    return redirect('/')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
