import requests

if __name__ == '__main__':
    bbox = "40.698843, -73.915201,40.701080, -73.912077"

    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = """
    [out:json][timeout:25];
    (
      node["highway"]({0});
      way["highway"]({0});
      relation["highway"]({0});
    );
    out body;
    """.format(bbox)

    response = requests.get(overpass_url, params={'data': overpass_query})
    data = response.json()
    print(data)
