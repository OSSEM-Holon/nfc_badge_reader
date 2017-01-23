#! /usr/bin/python
import nxppy
import time
import urllib, urllib2
import json 

mifare = nxppy.Mifare()
while True:
    try:
	data_dict = {'action':'processCheckIn','rfid':''}
        uid = mifare.select()
        data_dict['rfid'] = str(uid)
	encoded_dict = urllib.urlencode(data_dict)
	path = "http://10.10.133.14/crm/api/query.php"
	full_url = path + "?" + encoded_dict
	print full_url
	req = urllib2.Request(full_url)
	page=urllib2.urlopen(req)
	the_page = page.read()
	print the_page
	data = json.loads(the_page)
        print(data["firstName"])
	

    except nxppy.SelectError:
        # SelectError is raised if no card is in the field.
        pass

    time.sleep(2)

#  



