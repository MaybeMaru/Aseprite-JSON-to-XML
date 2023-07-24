import json
import os

def convert_json(dir):
  f = open(dir)
  data = json.load(f)
  frame_tags = []
  count = 0
  exportText = ''
  frametag = ''
  framecount = 0

  if 'image' in data['meta'] and data['meta']['image'] is not None:
    image_name = os.path.basename(data['meta']['image'])
  else:
    image_name = 'image_not_found'

  #Get frame tags data
  for frame in data['meta']['frameTags']:
    name = frame['name']
    from_ = frame['from']
    to = frame['to']
    frame_tags.insert(1, [from_,to,name])

  #Get frame data
  for frame in data['frames']:
    x = y = w = h = 0
    
    if (type(frame) == str):
      x = data['frames'][frame]['frame']['x']
      y = data['frames'][frame]['frame']['y']
      w = data['frames'][frame]['frame']['w']
      h = data['frames'][frame]['frame']['h']
    else:
      x = frame['frame']['x']
      y = frame['frame']['y']
      w = frame['frame']['w']
      h = frame['frame']['h']
    
    for tag in frame_tags:
      if (count >= tag[0]) and (count <= tag[1]):
        new_frametag = tag[2]
        if frametag != new_frametag:
          framecount = 0
        frametag = new_frametag
  
    xml_frame = '\n\t<SubTexture name="'+str(frametag)+str("{:05d}".format(framecount))+'" x="'+str(x)+'" y="'+str(y)+'" width="'+str(w)+'" height="'+str(h)+'"/>'
    framecount = framecount + 1
    exportText=exportText+xml_frame
    count = count + 1

  # Create XML data
  return_xml = '<?xml version="1.0" encoding="utf-8"?>'
  return_xml += '\n<TextureAtlas imagePath="'+image_name+'">'
  return_xml += '\n\t<!-- Made using Maru Aseprite JSON to XML converter -->'
  return_xml += exportText
  return_xml += '\n</TextureAtlas>'

  return return_xml