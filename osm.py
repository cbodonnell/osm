import requests

if __name__ == '__main__':
    bbox = "40.698843,-73.915201,40.701080,-73.912077"
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = """
    [out:json][timeout:25][bbox:{0}];
    way[highway]->.w1;
    way[highway]->.w2;
    node(w.w1)(w.w2)->.nodes;
    way[highway]->.ways;
    (.nodes; .ways;);
    out body;
    """.format(bbox)
    response = requests.get(overpass_url, params={'data': overpass_query})
    if response.status_code == 200:
        data = response.json()
        elements = data['elements']
        ways = [e for e in elements if e['type'] == 'way']
        for way in ways:
            nodes = way['nodes']
            way['nodes'] = [e for e in elements if (e['type'] == 'node' and e['id'] in nodes)]
        print(ways)
    else:
        print(response.reason)
        print(response.text)
