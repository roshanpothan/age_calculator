
# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request

# creating a Flask app
app = Flask(__name__)
@app.route("/")
def index():
    name = request.args.get("name").lower()   
    persons=[
        {"name":"roshan","age":33}, 
        {"name":"simi","age":30}, 
        {"name":"mathew","age":72},
        {"name":"shiny","age":61} 
    ]
    for person in persons:
        if person['name']==name:
            return jsonify({'age':person['age']}) 
    return jsonify({'Message':f'{name} not found'})  
if __name__ == "__main__":
    app.run(debug = True)
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
# @app.route('/', methods = ['GET', 'POST'])
# def home():
# 	if(request.method == 'GET'):

# 		name = "Roshan"
# 		return jsonify({'age': 33})
	
	

# # A simple function to calculate the square of a number
# # the number to be squared is sent in the URL when we use GET
# # on the terminal type: curl http://127.0.0.1:5000 / home / 10
# # this returns 100 (square of 10)
# @app.route('/home/<int:num>', methods = ['GET'])
# def disp(age):

# 	return jsonify({'age': 33})





# # driver function
# if __name__ == '__main__':

# 	app.run(debug = True)
