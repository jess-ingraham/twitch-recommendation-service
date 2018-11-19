from flask import Flask, render_template, request
import dbconfig as config

app = Flask(__name__)

@app.route("/")
def home():
	##create the file for the homepage and serve it with:
	return render_template("index.html")

@app.route("/search")
def search_result():
	vanityURL = request.args.get("vanityURL")
	##make the request from steam and get the user id, using the endpoints in the config file
	#if the result is 42 then there is an error and render the error page
	#
	#return render_template("error.html", message = "Your Id was not found")
	#
	#otherwise use the steam api to get their information
	#if their profile status is not public show an error page
	#return render_template("error.html", message = "Your profile is private, to see your friends list set your profile to public" )
	#
	##if the search results 
	return render_template("search.html")



@app.errorhandler(404)
def error_page(e):
	return render_template('notFound.html'), 404

app.run(host='0.0.0.0', port=5000, debug=True)

