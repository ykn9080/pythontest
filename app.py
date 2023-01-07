from flask import Flask, render_template
# from Django.shortcuts import render
from producer import *
from consumer import *

app = Flask(__name__)

data=[];
@app.route('/')
@crossdomain(origin='*')
def index():
    print(data)
    return render_template('index.html',headings=("Name","Address","Created At"), data=data)


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
    newdata=get_registerd_data()
    data.append(newdata)
    print (newdata,data)
    
    push_producer(newdata)
    return (data)


if __name__ == "__main__":
    app.run(debug=True)
