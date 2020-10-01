'''
Adrian Perez
9/24/2020
Python Vacation Trip Planner
'''
'''
#Make A Greeting
print(24%-22)
print("Welcome To Vacation Planner")
customer_name = input("What is your name?")
destination=input("Nice to meet you "+ customer_name+  " where are you traveling to?")
print("Great! "+ destination + " Sounds like a great trip!")
print("*******")
number_of_days = input(" How many days are you gonna spend traveling? ")
integer_number_of_days = int(number_of_days)
budget = int(input("How much money are you gong to spend on this trip?"))
currency = input( ' What is the the letter currency symbol for your travel destination? ' )
conversion_rate = float(input('How many MXC are there in 1 USD'))
hours = number_of_days * 24
minuets = hours * 60
print(f' If you are traveling for {number_of_days}  days that is the same as {hours} or {minuets} minuets')


daily_budget = budget/number_of_days
print(f'If you are trying to spend {budget} {currency} that means per day you can spend up to {daily_budget} {currency}')
if time_difference + 12 is <= 24
midnight = 8
noon = 12
'''


def time_change():
  time_difference = input(int( 'What is the time difference ,in hours, between your home and your destination ')
  noon=12
  midnight = 8
  # so the time difference could be + or -
  # convert the string to a int
  int_time_difference = int('time_difference')
  difference_hrs_noon = noon + int_time_difference
  difference_hr_midnight = midnight + int_time_difference
  print(difference_hrs_noon, difference_hr_midnight)


  # calculate from noon
  difference_hrs = noon + int_time_difference
  difference_hrs_midnight = midnight + int_time_difference
  print(difference_hrs_noon, "Difference Hours Noon",  )
  these two condisions are on different days
  # use % to get how many hours over into the next day could be + or -
  adjusted_noon = difference_hr_noon%24
  adjusted_midnight = difference_hr_midnight%24
  print(adjusted_noon, "This is adjusted noon")
  print(adjusted_midnight, "This is adjusted midnight")
  if difference_hrs_noon <= 24 and difference_hrs_noon >=0
      print(difference_hrs_noon)
      print("Destination time is ",difference_hrs_noon,":00 from noon 12:00")
  if difference_hrs_noon > 24:
      print (f"Destination time is  {adjusted_noon}:00 hrs(s) on the next day from noon 12:00")
  if difference_hrs_noon < 0
      print(f"Destination time is {adjusted_noon}:00 hrs on the previous days from 12:00")


  if difference_hrs_midnight <= 24 and difference_hrs_midnight >=0
      print("Destinatio time is" ,  difference_hrs_midnight ":00 from midnight 0:00)\
  if difference_hrs_midnight > 24:
      print (f"Destination time is  {adjusted_midnight}:00 hrs(s) on the next day from noon 0:00")
  if difference_hrs_noon < 0
      print(f"Destination time is {adjusted_midnight}:00 hrs on the previous days from 0:00")
  time_change()
















