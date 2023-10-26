import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)


rss_element = xml_tree.Element('rss',{
  'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd',
'xmlns:googleplay':'http://www.google.com/schemas/play-podcasts/1.0',
'xmlns:atom':'http://www.w3.org/2005/Atom',
'xmlns:media':'http://search.yahoo.com/mrss/',
'xmlns:content':'http://purl.org/rss/1.0/modules/content/',
'version':'2.0'  
})

channel_element = xml_tree.SubElement(rss_element, 'channel')
link_prefix = yaml_data['link']

xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']
xml_tree.SubElement(channel_element, 'subtitle').text = yaml_data['subtitle']
xml_tree.SubElement(channel_element, 'image', {'href':link_prefix + yaml_data['image']})
xml_tree.SubElement(channel_element, 'link').text = link_prefix

for item in yaml_data['item']:
  item_element = xml_tree.SubElement(channel_element, 'item')
  xml_tree.SubElement(item_element, 'title').text = item['title']
  xml_tree.SubElement(item_element, 'author').text = yaml_data['author']
  xml_tree.SubElement(item_element, 'description').text = item['description']

  enclosure = xml_tree.SubElement(item_element, 'enclosure',{
    'url': link_prefix + item['file'],
    'type': 'audio/mp3',
    'length':item['length']
  })

output_tree = xml_tree.ElementTree(rss_element)
output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)
