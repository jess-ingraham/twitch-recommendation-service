from flask import Flask, render_template, request, url_for, redirect, session
import dbconfig as config
from os import path
import json
from modules import helpers as helpers



dir_path = path.dirname(path.realpath(__file__))

# VanityUrl, steamId, appId = '','',''

# steamApiEndpoints = {
# 	'getUserID': f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=B280DA6909B1E40A67ABADB437979FBD&vanityurl={VanityUrl}'
# 	,'getUserInfo': f' http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=B280DA6909B1E40A67ABADB437979FBD&steamids={steamId}'
# 	,'getFriendsList': f'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=B280DA6909B1E40A67ABADB437979FBD&steamid={steamId}&relationship=friend'
# 	,'getOwnedGames': f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=B280DA6909B1E40A67ABADB437979FBD&steamid={steamId}&format=json'
# 	,'getGameSchema': f'http://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?key=B280DA6909B1E40A67ABADB437979FBD&appid={appId}'
# }

# twitchClientID = 'dcu07oqpaghxhvrwpf7rz85qxzqkik'



app = Flask(__name__, static_folder=dir_path + '\\public')
app.secret_key = "super duper secret. Don't tell anyone"

##functions 
#def redir(message):
#	session['message'] = message
#	return redirect(url_for('.home'))

def makeError(errmessage):
	return render_template('error.html', message = errmessage);

##css pages
@app.route('/css/<path:path>')
def css(path):
	##create the file for the homepage and serve it with:
	return app.send_static_file(f"css/{path}")

@app.route("/")
def home():
	##create the file for the homepage and serve it with:
	results = helpers.getVideosForHomePage()
	return render_template("index.html", games = results)

@app.route('/find-your-url')
def about():
	return app.send_static_file('about.html')

@app.route("/search", methods = ["POST"])
def search_result():

	resp = helpers.checkURL(request.form['url'])

	if resp == 42:
		return makeError("We could not find your userId. If you are using a custom URL make sure it's correct.")
	elif resp == 3:
		return makeError('Make sure your url starts with "http://steamcommunity.com"')


	else:
		username, games = helpers.getResultsPage(resp)
		# for key, value in topGames:
		# 	print(key, value)

		print(games)

		return render_template("results.html",username = username, games = games)
	
	



@app.errorhandler(404)
def error_page(e):
	return render_template('notFound.html'), 404


app.run(host='0.0.0.0', port=5000, debug=True)

