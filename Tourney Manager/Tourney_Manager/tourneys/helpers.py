import datetime
from time import strptime


#FUNCTION THAT TAKES A STR AND RETURNS A DATE OBJECT	
def getDateFromString(str_date):
	array = str_date.split(' ')
	month = strptime( array[1] ,'%b').tm_mon
	time = array[4].split(':')
	return datetime.datetime(int(array[3]), month, int(array[2]), int(time[0]), int(time[1]))
