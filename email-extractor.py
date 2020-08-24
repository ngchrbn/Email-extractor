#! usr/bin/python3

# After obtaining Credentials and Token files
import ezsheets
import re

spreadsheet = ezsheets.Spreadsheet('Insert here the url, id, or name of the spread sheet')

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username
    @                   # @symbol
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-Z]{2,4})   # dot-something
    )''', re.VERBOSE)

list_of_emails = []      # Store the emails from the sheet

# Find all the emails in the sheet and store them
for group in email_regex.findall(str(spreadsheet[0].getRows())):
    list_of_emails.append(group[0])

# Print the email found
for email in list_of_emails:
    print(email)
