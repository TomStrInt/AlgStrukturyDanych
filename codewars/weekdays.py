#! /usr/bin/python3


day = int(input("podaj numer od 1 do 7:   "))
if day <=7 and day>0:
    week_day = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    print(week_day[day])
else: 
    print( "Wrong, please enter a number between 1 and 7")

