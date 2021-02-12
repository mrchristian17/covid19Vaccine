from requests_html import HTMLSession
import requests

session = HTMLSession()

url='https://www.umcelpaso.org/register-for-the-covid-19-vaccine'
r = session.get(url)

r.html.render(wait=1)

vaccine_div = r.html.find('div.aler', first=True)
if vaccine_div is None:
    return false


# print(f'{vaccine_div.html}')
