import mailbox
import csv

domains = dict()
emails = dict()
domainEndings = dict()

domainWriter = csv.writer(open("domains.csv", "wb"))
emailWriter = csv.writer(open("emails.csv", "wb"))
tldWriter = csv.writer(open("tld.csv", "wb"))

for message in mailbox.mbox('mail.mbox'):
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
    mailForm = mailFrom.lower()
    email = mailFrom.split("<")
    if len(email) > 1:
        email = email[1].split(">")[0]
    else:
        email = email[0]

    # Count emails
    if email not in emails:
        emails[email] = 1
    else:
        emails[email] +=1 
        
    # Find domain of email
    domain = email.split("@")
    if len(domain) > 1:
        domain = domain[1]
    else:
        domain = domain[0]

    
    ending = domain.split('.')
    if len(ending) > 1:
        ending = ending[len(ending)-1]
    else:
        ending = "None"

    if ending not in domainEndings:
        domainEndings[ending] = 1
    else:
        domainEndings[ending] += 1
    
    # Count domains
    if domain not in domains:
        domains[domain] = 1
    else:
        domains[domain] += 1


tldWriter.writerow(["TLD", "Count"])
for ending in domainEndings:
    tldWriter.writerow([ending, domainEndings[ending]])

domainWriter.writerow(["Domain", "Count"])
for domain in domains:
    domainWriter.writerow([domain, domains[domain]])

emailWriter.writerow(["Email", "Count"])
for email in emails:
    emailWriter.writerow([email, emails[email]])
