#! usr/bin/python3

# After obtaining Credentials and Token files
import ezsheets
import re

spreadsheet = ezsheets.Spreadsheet('Insert here th url, id, or name of the sheet')

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username
    @                   # @symbol
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-Z]{2,4})   # dot-something
    )''', re.VERBOSE)

list_of_email = []
for group in email_regex.findall(str(spreadsheet[0].getRows())):
    list_of_email.append(group[0])

for email in list_of_email:
    print(email)
