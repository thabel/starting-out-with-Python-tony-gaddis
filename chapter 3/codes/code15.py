# Time calulator
seconds = int(input('enter the number of seconds: '))
SIXTY = 60
WHOLE_HOUR = 3600
WHOLE_DAY = 86400

""" if(seconds>= 0 and seconds <WHOLE_HOUR):
    min = seconds//SIXTY
    sec = seconds%SIXTY
    print(seconds,' = ',min,"minutes and ",sec,'seconds.')
elif(seconds>= WHOLE_HOUR and seconds <WHOLE_DAY):
    hours = seconds//WHOLE_HOUR
    min = (seconds-hours*WHOLE_HOUR)//SIXTY
    sec = (seconds-hours*WHOLE_HOUR-min*SIXTY)%SIXTY
    print(seconds,' = ',hours,'hours,',min,"minutes and ",sec,'seconds.')
else:
    day = seconds//WHOLE_DAY
    hours = (seconds - day*WHOLE_DAY)//WHOLE_HOUR
    min = (seconds - day*WHOLE_DAY-hours*WHOLE_HOUR)//SIXTY
    sec = (seconds - day*WHOLE_DAY-hours*WHOLE_HOUR-min*SIXTY)%SIXTY
    print(seconds,' = ',day,'day(s),',hours,'hours,',min,"minutes and ",sec,'seconds.') """

day = hour=min=sec = 0
day = seconds//WHOLE_DAY
hour = (seconds-day*WHOLE_DAY)//WHOLE_HOUR
min = (seconds-day*WHOLE_DAY-hour*WHOLE_HOUR)//SIXTY
sec = (seconds-day*WHOLE_DAY-hour*WHOLE_HOUR-min*SIXTY)%SIXTY
print(seconds,' = ',day,'day(s),',hour,'hours,',min,"minutes and ",sec,'seconds.')