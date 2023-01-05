from flask import Flask, render_template
# from Django.shortcuts import render
from producer import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


#rendering the HTML page which has the button
@app.route('/json')
def json():
    return render_template('json.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return ("nothing")

@app.route('/producer')
def producer_loop():
    print (get_registerd_data())
    push_producer()
    return ("nothing")


if __name__ == "__main__":
    app.run(debug=True)
