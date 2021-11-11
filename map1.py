import folium 
import pandas

data = pandas.read_csv("Volcanoes.txt")
longitude = list(data["LON"])
latitude = list(data["LAT"])
elev = list(data["ELEV"])

#function to change the color of the marker based on elevation
def color_produce(ele):
    if ele <1000:
        return "green"
    elif 1000<= ele <3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[80,100], zoom_start =6, tiles ="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(latitude, longitude, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln],radius=6, popup=str(el) +" m",
     fill_color = color_produce(el), color = 'grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding='utf-8-sig').read(), 
style_function= lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] <10000000
 else 'orange' if 10000000 <= x['properties']['POP2005'] <20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("map1.html")






