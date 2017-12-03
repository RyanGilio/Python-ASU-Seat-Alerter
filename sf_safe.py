#seat_finder.py
import requests
import lxml.html
from bs4 import BeautifulSoup
from twilio.rest import Client


import time
import schedule

# SMS Client
account_sid = <application_sid>
auth_token = <auth_token>
client = Client(account_sid,auth_token)




def seatSearch():
    s = requests.session()
    url = <UR_of_Searched_Class>
    login = 'https://weblogin.asu.edu/cas/login?service=https%3A%2F%2Fweblogin.asu.edu%2Fcgi-bin%2Fcas-login%3Fcallapp%3Dhttps%253A%252F%252Fwebapp4.asu.edu%252Fmyasu%252F%253Finit%253Dfalse'
    login = s.get(login)
    login_html = lxml.html.fromstring(login.text)
    hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
    form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
    print('Logging in . . .')

    form['username'] = <login_name>
    form['password'] = <login_password>
    response = s.post('https://weblogin.asu.edu/cas/login?service=https%3A%2F%2Fweblogin.asu.edu%2Fcgi-bin%2Fcas-login%3Fcallapp%3Dhttps%253A%252F%252Fwebapp4.asu.edu%252Fmyasu%252F%253Finit%253Dfalse', data=form)
    print('Logged into:',response.url)

    classNotFound = True;
    while(classNotFound):
        print('Gathering page information . . .')
        response = s.get(url)
        plainTxt = response.text
        soup = BeautifulSoup(plainTxt,'lxml')
        soupClasses = soup.select('.subjectNumberColumnValue')

        rowNumber = 0
        for x in soupClasses:
            if (x.text.strip() == <Class Number>):
                seatRows = soup.findAll('td',style='text-align:right;padding:0px;width:22px; border:none')
                seatCount = int(seatRows[rowNumber].text)

                if (seatCount > 0):
                    client.api.account.messages.create(
                        to="+<yourNumber>",
                        from_='+<twilioNumber>',
                        body= ('Class Has '+ str(seatCount)+ ' open seat(s)')
                    )
                    print('Seat found! Registering!')
                    classNotFound = False
                    quit()
                else:
                    print('No open seats, waiting another 1 minute.')
            rowNumber+=1
        time.sleep(60)


while 1:
    try:
        seatSearch()
    except:
        print('Time out occurred')
