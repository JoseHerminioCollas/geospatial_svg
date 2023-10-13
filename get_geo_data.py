# populate shape_objects with data from JSON call
def get_geo_data(layers, num):
 shapes_json=[]
 for i in range(0,num):
  feature=layers[i]
  geojson=feature.ExportToJson(True)
  name=geojson['properties']['name']
  if(str(name)!='None'):
   shapes_json.append(geojson)
 return shapes_json