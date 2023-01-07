from flask import Flask, render_template
# from Django.shortcuts import render
from producer import *
from consumer import *
import json


app = Flask(__name__)

data=[]

strdata="hello"

@app.route('/')
def index():
    
    return render_template('index.html',headings=("Name","Address","Created At"), data=data, consumedata=strdata)


#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return ("nothing")

@app.route('/consumer')
def consumer():
    consumedt=consumer_looping()
    consumedata.append(consumedt)
    str = json.dumps(consumedata).encode("utf-8")
    strdata = str.decode('utf-8')
    print("helloooooooooooooo",strdata)
    return render_template('consume.html',headings=("Name","Address","Created At"), consumedata=strdata)
    # return strdata
 

@app.route('/producer')
def producer_loop():
    newdata=get_registerd_data()
    data.append(newdata)
    print (newdata,data)
    
    push_producer(newdata)
    return (data)


if __name__ == "__main__":
    app.run(debug=True)
