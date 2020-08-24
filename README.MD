# Email Extractor from a spreadsheet

This program uses **regex** and **ezsheets** modules to extract email from a spreadsheet

---
To use this program visit these web pages and Enable the API:

1.[google-drive-api]( https://console.developers.google.com/apis/library/sheets.googleapis.com/)

2.[google-drive-api]( https://console.developers.google.com/apis/library/drive.googleapis.com/)

---
You’ll also need to obtain three files, which you should save in the same
folder as your .py Python script that uses EZSheets:

* A credentials file named **credentials-sheets.json**

* A token for Google Sheets named **token-sheets.pickle**

* A token for Google Drive named **token-drive.pickle**

The credentials file will generate the token files. The easiest way to
obtain a credentials file is to go to the Google Sheets Python Quickstart
page at [google-drive-api](https://developers.google.com/sheets/api/quickstart/python/) and click the
blue **Enable the Google Sheets API** button

Clicking this button will bring up a window with a **Download Client
Configuration** link that lets you download a **credentials.json** file. Rename
this file to **credentials-sheets.json** and place it in the same folder as your
Python scripts.

---
Once you have a credentials-sheets.json file, run:

```python
import ezsheets
```
The first time you import the EZSheets module, it will open a new
browser window for you to log in to your Google account. **Click Allow**.

---
Documentation from the book:
[Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
