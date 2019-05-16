from flask import Flask, render_template, request, redirect

app = Flask(__name__)

counter = {'GET': 0, 'POST': 0, 'DELETE': 0, 'PUT': 0}


@app.route('/')
def route_index():
    return render_template('index.html')


@app.route('/request-counter', methods=['GET', 'POST'])
def request_counter():
    if request.method == 'GET':
        counter['GET'] += 1

    elif request.method == 'POST':
        counter['POST'] += 1

    return redirect('/')

@app.route('/statistics')
def route_statistics():
    return render_template('statistics.html', counter=counter)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
