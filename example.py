#!/usr/bin/env python
from __future__ import print_function
from alchemyapi import AlchemyAPI
import json

demo_text = 'Yesterday dumb Bob destroyed my fancy iPhone in beautiful Denver, Colorado. I guess I will have to head over to the Apple Store and buy a new one.'
demo_url = 'http://blog.programmableweb.com/2011/09/16/new-api-billionaire-text-extractor-alchemy/'
demo_html = '<html><head><title>Python Demo | AlchemyAPI</title></head><body><h1>Did you know that AlchemyAPI works on HTML?</h1><p>Well, you do now.</p></body></html>'


print('')
print('')
print('            ,                                                                                                                              ') 
print('      .I7777~                                                                                                                              ')
print('     .I7777777                                                                                                                             ')
print('   +.  77777777                                                                                                                            ')
print(' =???,  I7777777=                                                                                                                          ')
print('=??????   7777777?   ,:::===?                                                                                                              ')
print('=???????.  777777777777777777~         .77:    ??           :7                                              =$,     :$$$$$$+  =$?          ')
print(' ????????: .777777777777777777         II77    ??           :7                                              $$7     :$?   7$7 =$?          ')
print('  .???????=  +7777777777777777        .7 =7:   ??   :7777+  :7:I777?    ?777I=  77~777? ,777I I7      77   +$?$:    :$?    $$ =$?          ')
print('    ???????+  ~777???+===:::         :7+  ~7   ?? .77    +7 :7?.   II  7~   ,I7 77+   I77   ~7 ?7    =7:  .$, =$    :$?  ,$$? =$?          ')
print('    ,???????~                        77    7:  ?? ?I.     7 :7     :7 ~7      7 77    =7:    7  7    7~   7$   $=   :$$$$$$~  =$?          ')
print('    .???????  ,???I77777777777~     :77777777~ ?? 7:        :7     :7 777777777:77    =7     7  +7  ~7   $$$$$$$$I  :$?       =$?          ')
print('   .???????  ,7777777777777777      7=      77 ?? I+      7 :7     :7 ??      7,77    =7     7   7~ 7,  =$7     $$, :$?       =$?          ')
print('  .???????. I77777777777777777     +7       ,7???  77    I7 :7     :7  7~   .?7 77    =7     7   ,77I   $+       7$ :$?       =$?          ')
print(' ,???????= :77777777777777777~     7=        ~7??  ~I77777  :7     :7  ,777777. 77    =7     7    77,  +$        .$::$?       =$?          ')
print(',???????  :7777777                                                                                77                                       ')
print(' =?????  ,7777777                                                                               77=                                        ')
print('   +?+  7777777?                                                                                                                           ')
print('    +  ~7777777                                                                                                                            ')
print('       I777777                                                                                                                             ')
print('          :~                                                                                                                               ')
	 

alchemyapi = AlchemyAPI()

print('')
print('')
print('############################################')
print('#   Entity Extraction Example              #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.entities('text',demo_text, { 'sentiment':1 })

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Entities ##')
	for entity in response['entities']:
		print('text: ', entity['text'])
		print('type: ', entity['type'])
		print('relevance: ', entity['relevance'])
		print('sentiment: ', entity['sentiment']['type'] + ' (' + entity['sentiment']['score'] + ')')
		print('')
else:
	print('Error in entity extraction call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Sentiment Analysis Example             #')
print('############################################')
print('')
print('')

print('Processing html: ', demo_html)
print('')

response = alchemyapi.sentiment('html',demo_html)

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))

	print('')
	print('## Document Sentiment ##')
	print('type: ', response['docSentiment']['type'])
	print('score: ', response['docSentiment']['score'])
else:
	print('Error in sentiment analysis call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Keyword Extraction Example             #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.keywords('text',demo_text, { 'sentiment':1 })

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Keywords ##')
	for keyword in response['keywords']:
		print('text: ', keyword['text'])
		print('relevance: ', keyword['relevance'])
		print('sentiment: ', keyword['sentiment']['type'] + ' (' + keyword['sentiment']['score'] + ')')
		print('')
else:
	print('Error in keyword extaction call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Concept Tagging Example                #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.concepts('text',demo_text)

if response['status'] == 'OK':
	print('## Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Concepts ##')
	for concept in response['concepts']:
		print('text: ', concept['text'])
		print('relevance: ', concept['relevance'])
		print('')
else:
	print('Error in concept tagging call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Relation Extraction Example            #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.relations('text',demo_text)

if response['status'] == 'OK':
	print('## Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Relations ##')
	for relation in response['relations']:
		if 'subject' in relation:
			print('Subject: ', relation['subject']['text'] )
		
		if 'action' in relation:
			print('Action: ', relation['action']['text'])
		
		if 'object' in relation:
			print('Object: ', relation['object']['text'])
		
		print('')
else:
	print('Error in relation extaction call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Text Categorization Example            #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.category('text',demo_text)

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Category ##')
	print('text: ', response['category'])
	print('score: ', response['score'])
	print('')
else:
	print('Error in text categorization call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Language Detection Example             #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.language('text',demo_text)

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Language ##')
	print('language: ', response['language'])
	print('iso-639-1: ', response['iso-639-1'])
	print('native speakers: ', response['native-speakers'])
	print('')
else:
	print('Error in language detection call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Author Extraction Example              #')
print('############################################')
print('')
print('')

print('Processing url: ', demo_url)
print('')

response = alchemyapi.author('url',demo_url)

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))

	print('')
	print('## Author ##')
	print('author: ', response['author'])
	print('')
else:
	print('Error in author extraction call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Feed Detection Example                 #')
print('############################################')
print('')
print('')

print('Processing url: ', demo_url)
print('')

response = alchemyapi.feeds('url',demo_url)

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))

	print('')
	print('## Feeds ##')
	for feed in response['feeds']:
		print('feed: ', feed['feed'])
else:
	print('Error in feed detection call: ', response['statusInfo'])

print('')
print('')

