from requests_html import HTMLSession
import requests

session = HTMLSession()

url='https://www.umcelpaso.org/register-for-the-covid-19-vaccine'
r = session.get(url)

r.html.render(wait=1)

vaccine_div = r.html.find('div.alert', first=True)
vaccine_strong_element = vaccine_div.find('strong', first = True)
vaccine_html_string = vaccine_strong_element.html
substring = "We have exhausted all available vaccine and appointments for this current allotment."
if substring in vaccine_html_string:
    print("Found!")
else:
    print("Not found!")
