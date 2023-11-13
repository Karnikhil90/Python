# Two birth date and compare who is big boy

from datetime import datetime

# Constant Value
currentYear = datetime.now().year
currentMonth = datetime.now().month
currentDay = datetime.now().day

# input segment

person1 = ' 21/11/2000 '
person2 = '21/02/2006'

person1Day, person1Month, person1Year = person1.strip().split('/')
person2Day, person2Month, person2Year = person2.strip().split('/')
        
        # Debug
# print(person1Day, person1Month, person1Year)
# print(person2Day, person2Month, person2Year)

# Process Segment
if int(person1Year) != int(person2Year):
  if currentYear - int(person1Year) > currentYear - int(person2Year):
    print(person1 + ' is BIG GUY !')
  else:
    print(person2 + ' is BIG GUY !')
else:
  if int(person1Month) != int(person2Month):
    if currentMonth - int(person1Month) > currentMonth - int(person2Month):
      print(person1 + ' is s BIG GUY !')
    else:
      print(person2 + ' is s BIG GUY !')
  else:
    if int(person1Day) != int(person2Day):
      if currentDay - int(person1Day) > currentDay - int(person2Day):
        print(person1 + ' is BIG GUY !')
      else:
        print(person2 + ' is BIG GUY !')
    else:
      print('Both are same')
