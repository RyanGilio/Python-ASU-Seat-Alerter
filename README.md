# Python-ASU-Seat-Alerter
Python Script Template that will send a text-message once a seat opens up.
This is for students who are waiting for a seat to open up in a class and want to be alerted when there's an opening.

# How it works

Seat_Finder will log into blackboard and go to the class search where it'll look at the available seats for the class selected. If there are no open seats then it will check again after one minute. If a seat is found it'll send an SMS message to your phone and stop checking (this is to avoid spamming and using up your API calls from Twilio). If you put your machine to sleep it will stop running but will resume once it wakes up.

# How to Set Up

1. Make Sure 'requests' 'lxml' 'bs4' and 'twilio' python libraries are imported.


2. Lines 12-13

    account_sid = <application_sid>
    
    auth_token = <auth_token>
    
    
    If you want to receive text notfications you can sign up for Twilio for a free number and input your SID and Auth token here.
    If you don't want text notifications you can get rid of these lines and lines 49-53.


2. Line 21

    url = <UR_of_Searched_Class>
    
    Pull up a search of the class that you want to check for open seats and then paste the address into the URL variable.


3. Lines 29-30 

    form['username'] = <login_name>
    
    form['password'] = <login_password>
   
   You'll need to put your login name and password into these fields for BlackBoard to verify you and allow access to the class search.
 
 
4. Line 44

     if (x.text.strip() == <Class Number>):
    
     Update Class Number to desired class.


5. Lines 50-52

     to="+<yourNumber>",
    
     from_='+<twilioNumber>',
    
     body= ('Class Has '+ str(seatCount)+ ' open seat(s)')
    
     If you chose to get text notifications put your phone number and twilio number into the to and from respectively.
  
  
  
  
# Future Updates
- Option to be emailed 
- Automatic Class Registration if opening found

