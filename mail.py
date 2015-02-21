import mailbox
import csv

writer = csv.writer(open("mail.csv", "wb"))

for message in mailbox.mbox('mail.mbox'):

    fullDate = (str(message['date'])).split(",")

    # Grab appropriate date
    if len(fullDate) > 1:
        date = fullDate[1].split(' +')
        if len(date) < 2:
            date = fullDate[1].split(' -')

    # Grab subject
    subject = message['subject']
    if subject is None:
        subject = "None"
    
    # Grab label
    label = subject.split('[')
    if len(label) > 1:
        label = label[1].split(']')
        label = label[0]
    else:
        label = 'None'

    # Remove tag from subject
    subject = subject.split(']')
    if len(subject) > 1:
        subject = subject[1]
        # Remove re
        subject = subject.split('RE: ')
        if len(subject) > 1:
            subject = subject[1]
        else:
            subject = subject[0]

        # Remove fwd
        subject = subject.split('Fwd: ')
        if len(subject) > 1:
            subject = subject[1]
        else:
            subject = subject[0]        
    else:
        subject = subject[0]
    
    if subject.find("=") is not -1:
        subject = "None"


    mailFrom = message['from']

    if mailFrom is None:
        mailFrom = "None"

    # Format email from, remove quote, and '=' signs
    mailFrom = mailFrom.replace('\"', "")
    mailFrom = mailFrom.split("=")
    if len(mailFrom) > 1:
        mailFrom = mailFrom[len(mailFrom)-1]
    else:
        mailFrom = mailFrom[0]

    # Find only the name in the email (if it exists)
    name = mailFrom.split("<")[0]

    # Find email only 
    email = mailFrom.split("<")
    if len(email) > 1:
        email = email[1].split(">")[0]
    else:
        email = email[0]

    # Find domain of email
    domain = email.split("@")
    if len(domain) > 1:
        domain = domain[1]
    else:
        domain = domain[0]

    row = [date[0], label.lower(), subject, name.lower(), email, domain]

    # Generate a list of everyone this email was sent to
    mailTo = message['to']
    if mailTo is None:
        mailTo = "None"
    mailTo = mailTo.replace('\r', "")
    mailTo = mailTo.replace('\n', "")
    mailTo = mailTo.replace(" ", "")
    mailTo = mailTo.replace('\"', "")
    
    mailTo = mailTo.split(",")
    for email in mailTo:
        email = email.split("<")
        if len(email) > 1:
            email = email[1].split(">")[0]
        else:
            email = email[0]
        if email.find("@") is not -1:
            row.append(email.lower())

    writer.writerow(row)
