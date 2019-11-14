import folium
sg_map = folium.Map(location=[1.38, 103.8], zoom_start=12)

sg_map


sg_map.save("fmap.html")
