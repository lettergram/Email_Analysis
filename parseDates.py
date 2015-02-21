import mailbox
import csv

def parseDate(dateMessage):
    if dateMessage is None:
        return "None", "None"
    fullDate = dateMessage.split(",")
    day = (fullDate[0]).lower()
    # Update days                                                                                  
    if day is None or len(day) < 1 or len(day) > 5 or day is "none":
        day = "None"

    # Grab appropriate date
    if len(fullDate) > 1:
        date = fullDate[1].split(' +')
        if len(date) < 2:
            date = fullDate[1].split(' -')
    else:
        date = fullDate[0]
        if date is None:
            if len(fullDate) < 2:
                date = "None"
        else:
            date = date.split("-")[0]

    date = date[0]
    if date[0].find(":") is not -1:
        date = date[:-9]

    date = date[1:12]

    date = date.replace(" ", "-")
    date = date.replace(":", "")
    if date.find("-") is 0:
        date = date[1:len(date)]

    # Replaces year
    date = date.replace("2009", "09")
    date = date.replace("2010", "10")
    date = date.replace("2011", "11")
    date = date.replace("2012", "12")
    date = date.replace("2013", "13")
    date = date.replace("2014", "14")
    date = date.replace("2015", "15")

    if date.find('-') is 1:
        date = "0" + date[:-1]

    return day, date


''' ___MAIN___ '''
writer = csv.writer(open("mailDates.csv", "wb"))
dayWriter = csv.writer(open("mailDays.csv", "wb"))

dates = dict()
days = dict()

for message in mailbox.mbox('mail.mbox'):

    day, date = parseDate(message['date'])

    # Count for each day
    if day not in days:
        days[day] = 1
    else:
        days[day] += 1

    # Count for each date
    if date not in dates:
        dates[date] = 1
    else:
        dates[date] += 1

for date in dates:
    writer.writerow([date, dates[date]])

for day in days:
    dayWriter.writerow([day, days[day]])
