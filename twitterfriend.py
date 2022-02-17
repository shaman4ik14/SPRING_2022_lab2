import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import folium



def crearte_map(name):
    # https://apps.twitter.com/
    # Create App and get the four strings, put them in hidden.py

    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE


    acct = name
    url = twurl.augment(TWITTER_URL,
                    {'screen_name': acct, 'count': '200'})
    # print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    # print(json.dumps(js, indent=2, ensure_ascii=False))
    data_users = js['users']
    users_info = []
    for local_user in data_users:
        local_info = (local_user['screen_name'], local_user['location'])
        users_info.append(local_info)

    map = folium.Map(location=[49.817545, 24.023932], zoom_start=3, tiles="Stamen Toner")
    data_with_coord = dict()

    geolocator = Nominatim(user_agent="user_agent")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    for point in users_info:
        try:
            location = geolocator.geocode(point[1])
            current_coord = (location.latitude, location.longitude)
            data_with_coord[current_coord] = data_with_coord.get(current_coord, []) + [point[0], point[1]]
        except:
            pass


    info_about_coordinate = [(k, v) for k, v in data_with_coord.items()]
    points_data = info_about_coordinate[:100]

    html = """screen_name: {}<br>
    Location: {}
    """
    fg = folium.FeatureGroup(name=acct)
    fg1 = folium.FeatureGroup(name='Collegium')
    for elements in points_data:
        iframe = folium.IFrame(html=html.format(elements[1][0], elements[1][1]),
                               width=300, height=55)
        fg.add_child(folium.Marker(location=[elements[0][0], elements[0][1]],
                                   popup=folium.Popup(iframe),
                                   icon=folium.Icon(color='red')))

        fg1.add_child(folium.CircleMarker(location=[49.817545, 24.023932], radius=10,
                                      popup='UCU Campus', fill_color='orange',
                                      color='yellow', fill_opacity=0.8))

    map.add_child(fg)
    map.add_child(fg1)
    map.add_child(folium.LayerControl())
    return map