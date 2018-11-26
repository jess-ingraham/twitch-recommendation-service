
IP = '35.237.23.200'
PORT = '3306'
USER = 'root'
PASS = '2x2rj0qydKmO42jG'
DB = 'develop'

STEAMKEY = 'B280DA6909B1E40A67ABADB437979FBD'

steamApiEndpoints = {
	getUserID: f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=B280DA6909B1E40A67ABADB437979FBD&vanityurl={VanityUrl}'
	,getUserInfo: f' http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=B280DA6909B1E40A67ABADB437979FBD&steamids={steamId}'
	,getFriendsList: f'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=B280DA6909B1E40A67ABADB437979FBD&steamid={steamId}&relationship=friend'
	,getOwnedGames: f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=B280DA6909B1E40A67ABADB437979FBD&steamid={steamId}&format=json'
	,getGameSchema: f'http://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?key=XXXXXXXXXXXXXXXXX&appid={appId}'
}
