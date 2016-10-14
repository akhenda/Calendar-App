import os
import json


cal_dict = {}
clear = lambda: os.system('cls')

def file_get():
	with open("calendar.json", "r") as cal:
		try:
			cal_dict = json.load(cal)
		# if the file is empty the ValueError will be thrown
		except ValueError:
			cal_dict = {}

def save_file():
	with open("calendar.json", "w") as cal:
		try:
			json.dump(cal_dict, cal)
		except ValueError:
			cal_dict = {}


class CalendarModels(object):
	
	# def __init__(self, time, date, month, year):
	# 	self.time = time
	# 	self.date = date
	# 	self.month = month
	# 	self.year = year

	def create_cal(self):
		file_get()
		print ("Menu\n" + "-"*4)
		print ("1. View Calendar\n2. Create Calendar\n\n")
		option = input("Choose an option: ")

		if option == str(1):
			clear()
			print ("1. Add Event\n2. List Events\n3. View Last Event\n")
			event_options = str(input("Enter option:"))
			if event_options == '2':
				self.listevents(event_options, cal_dict)
			
		elif option == str(2):
			new_cal_name = raw_input("Give the Calendar a name: ")
			cal_dict[new_cal_name] = {}
			print (cal_dict)

	def add_event(selected_cal):
	# print "\nYou are in the", selected_cal, "Calendar\n"
	date = raw_input("Enter the Date of the event: ")
	name = raw_input("Enter the event name: ")
	start = raw_input("Enter the Start Time: ")
	stop = raw_input("Enter the Stop Time: ")
	description = raw_input("Enter the Description(optional): ")
	location = raw_input("Enter the location of the event(optional): ")
	try:
		cal_dict[selected_cal][date] = {}
		cal_dict[selected_cal][date]["Date"] = date
		cal_dict[selected_cal][date]["Start Time"] = start
		cal_dict[selected_cal][date]["Stop Time"] = stop
		cal_dict[selected_cal][date]["Event Name"] = name
		cal_dict[selected_cal][date]["Description"] = description
		cal_dict[selected_cal][date]["Location"] = location
		cal_dict[selected_cal][date]["Created On"] = str(datetime.now())
		print "Successfuly created the", name, "Event"
	except:
		raise("Something is wrong with the DB")

	def listevents(self, event_options, cal):

		event_name=str(input('Enter name of cal:'))
		for item in cal[event_name]:
			print ("-" * 30)
			print ("Event Name: " + str(cal[event_name][item]['Event Name']))
			print ("\nLocation: " + str(cal[event_name][item]['Location']))
			print ("\nDate: " + str(cal[event_name][item]['Date']))
			print ("\nBetween " + str(cal[event_name][item]['Start Time']) + " and " + str(cal[event_name][item]['Stop Time']))
			print ("\nDescription: " + str(cal[event_name][item]['Description']))

cal = CalendarModels()
cal.create_cal()
