import datetime

time_str = input("enter time in this format yyyy-mm-dd : ")

time=datetime.datetime.strptime(time_str, "%Y-%m-%d") 
print(time)