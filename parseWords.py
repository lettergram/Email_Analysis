import mailbox
import csv
import parseDates

''' ___MAIN___ '''

writer = csv.writer(open("wordFrequency.csv", "wb"))

words = dict()
dates = dict()
days = dict()

for message in mailbox.mbox('mail.mbox'):

    day, date = parseDates.parseDate(message['date'])

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
