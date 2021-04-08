from flask import Flask

import folium

app = Flask(__name__)


@app.route('/')
def index():
    folium_map = folium.Map(location=[32.715736, -117.161087], tiles="OpenStreetMap", zoom_start=10)
    folium.Marker(
    location=[32.715736, -117.161087],
    popup="San Diego",
    icon=folium.Icon(icon="fire", color="red"),
    ).add_to(folium_map)

    return folium_map._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)