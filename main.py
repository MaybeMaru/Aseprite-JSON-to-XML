import json
import os

file_name = 'maru-splash-pixel'

f = open(file_name+'.json')
data = json.load(f)
frameshit = []
count = 0
exportText = ''
frametag = ''
framecount = 0

image_name = os.path.basename(data['meta']['image'])

#Get frame tags data
for i in data['meta']['frameTags']:
  name = i['name']
  from_ = i['from']
  to = i['to']
  frameshit.insert(1, [from_,to,name])

#Get frame data
for i in data['frames']:

  x = data['frames'][i]['frame']['x']
  y = data['frames'][i]['frame']['y']
  w = data['frames'][i]['frame']['w']
  h = data['frames'][i]['frame']['h']
  count = count + 1

  for i in frameshit:
    if (count >= i[0]) and (count <= i[1]):
      new_frametag = i[2]
      if frametag != new_frametag:
        framecount = 0
      frametag = new_frametag
  
  xml_frame = '\n    <SubTexture name="'+str(frametag)+str("{:05d}".format(framecount))+'" x="'+str(x)+'" y="'+str(y)+'" width="'+str(w)+'" height="'+str(h)+'"/>'
  framecount = framecount + 1
  exportText=exportText+xml_frame

#Export the XML
with open(os.path.splitext(image_name)[0]+'.xml', 'w') as xml:
  xml.write('<?xml version="1.0" encoding="utf-8"?>')
  xml.write('\n<TextureAtlas imagePath="'+image_name+'">')
  xml.write('\n    <!-- Made using Maru Aseprite JSON to XML converter -->')
  xml.write(exportText)
  xml.write('\n</TextureAtlas>')

f.close()