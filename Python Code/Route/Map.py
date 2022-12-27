from turtle import color
import folium
from ast import With
from cgi import test
from Data import *

m = folium.Map(location=[53.941, 103.4864], tiles="Stamen Toner", zoom_start=5)

folium.PolyLine(
    [
        coordinates2,
        coordinates1,
    ],
    color="red",
    weight=2,
).add_to(m)

m.save("Map.html")
