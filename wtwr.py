from pprint import pprint
import requests

zipcode = raw_input("Enter zipcode:")
r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=' + zipcode + ',US&appid=b231606340553d9174136f7f083904b3')
#pprint(r.json())


cur_temp = (9/5.0)*(r.json()['main']['temp'] - 273) + 32
cur_wind = r.json()['wind']['speed'] / 0.44704
conditions = str(r.json()['weather'][0]['main']) 
#pprint(r.json()['wind']['speed'])
#print(cur_wind)
#pprint(r.json()['weather'][0]['main'])
#print(conditions)


print "WHAT TO WEAR RUNNING IN" , zipcode
print "-----------------------------------"

if(conditions == "rain" or conditions == "snow"):
	print "You might want to skip on running because of precipitate:" + "(" + conditions + ")"
if(cur_temp > 50):
	print "Shorts and a" ,
	if(cur_wind > 9):
		print "Long Sleeved" ,
	else:
		print "Tee Shirt"
elif(cur_temp > 40):
	if(cur_wind > 8):
		print "quarter zip up, short sleeved tee" ,
	else:
		print "long sleeved tee" , 
	print "capri leggings/thin long leggings"
elif(cur_temp > 20):
	print "long sleeved tee, quarter zip up, gloves, fleece lined leggings, hat" ,
	if(cur_wind > 8): 
		print "and a windbreaker"