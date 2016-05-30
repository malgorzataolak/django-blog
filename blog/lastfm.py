import urllib
import urllib.request as urllib2
import json

URL="http://ws.audioscrobbler.com/2.0/"
KEY="053c665cb61bf209d442c5a36fb71f9a"
periods=["overall", "1month", "6month", "12month"]
limit="5"
period="overall"
user="margo121"

def is_user(**kwargs):
    kwargs.update({
        "method": "user.getInfo",
        "api_key": KEY,
        "user": user,
        "format": "json"
        })

    url_send=URL+"?"+urllib.parse.urlencode(kwargs)
    data=urllib2.urlopen(url_send)
    res=json.loads(data.read().decode('utf-8'))
    if 'message' in res:
        if res['message']=="User not found":
            return False
        else:
            True
    return True

def get_top_artists(**kwargs):
	kwargs.update({
        "method": "user.getTopArtists",
        "api_key": KEY,
        "user": user,
        "limit": limit,
        "period" : period,
        "format": "json"})
	url_send=URL+"?"+urllib.parse.urlencode(kwargs)
	data=urllib2.urlopen(url_send)
	res=json.loads(data.read().decode('utf-8'))
	return res
	data.close()

def generate_albums(**kwargs):
    kwargs.update({
        "method": "user.getTopAlbums",
        "api_key": KEY,
        "user": user,
        "limit": limit,
        "period" : period,
        "format": "json"
        })

    url_send=URL+"?"+urllib.parse.urlencode(kwargs)
    data=urllib2.urlopen(url_send)
    res=json.loads(data.read().decode('utf-8'))
    return res

def generate_tracks(**kwargs):
    kwargs.update({
        "method": "user.getTopTracks",
        "api_key": KEY,
        "user": user,
        "limit": limit,
        "period" : period,
        "format": "json"
        })

    url_send=URL+"?"+urllib.parse.urlencode(kwargs)
    data=urllib2.urlopen(url_send)
    res=json.loads(data.read().decode('utf-8'))
    data.close()
    return res