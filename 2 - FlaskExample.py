import flask
from flask import Flask, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#http://localhost:4321/api1?searchparam=param1
@app.route('/api1',methods=['GET'])
def api1():
    paramname = request.args.get("searchparam")
    return str(paramname)

#http://localhost:4321/api2?searchparam1=ABC&searchparam2=100
@app.route('/api2',methods=['GET'])
def api2():
    paramname1 = request.args.get("searchparam1")
    paramname2 = request.args.get("searchparam2")
    return str(paramname1 + paramname2)

if __name__ == "__main__":
    app.run(host='localhost',port=4321,threaded=True)
