from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

mainUrl= "https://www.google.com/maps/search/Escape+room+in+"
cities = ["Seattle,+WA","Palm+Springs,+CA","Milwaukee,+WI"]
city = ["Seattle, WA","Palm Springs, CA","Milwaukee, WI"]

name=[]

class list:
	size =0
	name = None
	avg_rating = None
	web_url = None
	location = None
	city =None
	contact = None
	hid_url=None

all_data =[]

for i in range(0,len(cities)):
	all_data.append(list())
	all_data[i].name=[]
	all_data[i].avg_rating=[]
	all_data[i].web_url=[]
	all_data[i].location=[]
	all_data[i].city=[]
	all_data[i].contact=[]
	all_data[i].hid_url=[]

driver = webdriver.Safari()
driver.maximize_window()
i=0

for x in cities:

	driver.get(mainUrl+x)

	time.sleep(2)

	options = driver.find_elements_by_class_name('MVVflb-haAclf')
	new_options = driver.find_elements_by_class_name('siAUzd-neVct-H9tDt')
	while(new_options!=options):
		options=new_options
		for opt in options:
			driver.execute_script("arguments[0].scrollIntoView();", opt)
			time.sleep(0.2)
			new_options = driver.find_elements_by_class_name('MVVflb-haAclf')
	new_options = driver.find_elements_by_class_name('MVVflb-haAclf')
	hidden= driver.find_elements_by_class_name('a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd')

	f= True
	k =0

	for option in new_options:
		nm = option.get_attribute("aria-label")
		all_data[i].name.append(nm)
		all_data[i].city.append(city[i])
		url  = hidden[k].get_attribute("href")
		all_data[i].hid_url.append(url)

		try:
			rat = option.find_element_by_class_name('ZkP5Je')
		except:
			rat = "No Reviews"

			f= False

		if f:
			rating = rat.get_attribute("aria-label")
			all_data[i].avg_rating.append(rating)
		else:
			all_data[i].avg_rating.append(rat)


		if type(all_data[i].avg_rating[len(all_data[i].avg_rating)-1])!=type("1"):
			all_data[i].avg_rating.pop()
			all_data[i].name.pop()
			all_data[i].city.pop()
			all_data[i].hid_url.pop()

		all_data[i].avg_rating[len(all_data[i].avg_rating)-1] = all_data[i].avg_rating[len(all_data[i].avg_rating)-1][0:6]

		k+=1

	nextButton = driver.find_element_by_id('ppdPk-Ej1Yeb-LgbsSe-tJiF1e')

	stop =True

	try :
		nextButton.click()
	except :
		stop = False

	while(stop):
		try :

			time.sleep(3)
			options = driver.find_elements_by_class_name('MVVflb-haAclf')
			new_options = driver.find_elements_by_class_name('siAUzd-neVct-H9tDt')

			while(new_options!=options):
				options=new_options
				for opt in options:
					driver.execute_script("arguments[0].scrollIntoView();", opt)
					time.sleep(0.2)
					new_options = driver.find_elements_by_class_name('MVVflb-haAclf')
			new_options = driver.find_elements_by_class_name('MVVflb-haAclf')
			hidden = driver.find_elements_by_class_name('a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd')

			k=0

			for option in new_options:
				nm = option.get_attribute("aria-label")
				all_data[i].name.append(nm)
				all_data[i].city.append(city[i])
				url  = hidden[k].get_attribute("href")
				all_data[i].hid_url.append(url)
				f= True

				try:
					rat = option.find_element_by_class_name('ZkP5Je')
				except:
					rat = "No Reviews"

					f= False

				if f:
					rating = rat.get_attribute("aria-label")
					all_data[i].avg_rating.append(rating)
				else:
					all_data[i].avg_rating.append(rat)


				if type(all_data[i].avg_rating[len(all_data[i].avg_rating)-1])!=type("1"):
					all_data[i].avg_rating.pop()
					all_data[i].name.pop()
					all_data[i].hid_url.pop()
					all_data[i].city.pop()
				all_data[i].avg_rating[len(all_data[i].avg_rating)-1] = all_data[i].avg_rating[len(all_data[i].avg_rating)-1][0:6]
				k+=1

			# for rat in rating:
			# 	all_data[i].avg_rating.append(rat.get_attribute("aria-label"))
			nextButton = driver.find_element_by_id('ppdPk-Ej1Yeb-LgbsSe-tJiF1e')
			nextButton.click()
		except :
			stop = False

	i+=1

for i in range(0,len(all_data)):
	for j in range(0,len(all_data[i].hid_url)):
		driver.get(all_data[i].hid_url[j])
		time.sleep(1)
		address =" "
		try:
			loc = driver.find_element_by_class_name("AeaXub")
			loc1 = loc.find_element_by_class_name("QSFF4-text").text
			address = loc1
		except:
			address ="No Address"
		all_data[i].location.append(address)
		url = " "
		try:
			url2 = driver.find_element_by_class_name("HY5zDd")
			url1 = url2.find_element_by_class_name("QSFF4-text").text
			url = url1
		except:
			url = "No Website Found"
		all_data[i].web_url.append(url)
		contact =""
		try:
			cont = driver.find_elements_by_tag_name('button')
			for y in cont:
				if(y.get_attribute('data-tooltip')=="Copy phone number"):
					contact = y.get_attribute("aria-label")
					break
			if(contact!=""):
				z = len(contact)
				contact = contact[7:z]
			if(contact==""):
				contact ="No contact details found"
		except:
			contact ="No contact details found"
		all_data[i].contact.append(contact)



for i in range(0,len(all_data)):
	for j in range(0,len(all_data[i].name)):
		print(all_data[i].name[j],end=' ')
		print(all_data[i].contact[j],end=' ')
		print(all_data[i].city[j],end=' ')
		print(all_data[i].location[j],end=' ')
		print(all_data[i].web_url[j],end=' ')
		print(all_data[i].avg_rating[j],end='\n')
driver.close()

