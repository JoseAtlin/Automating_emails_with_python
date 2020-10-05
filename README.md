# Automating_emails_with_python

In this repository, you can see codes related to automating emails using python.
I think of making it more intuitive by creating digital certificates out of an image(certificate).
To complement both of this is, I combined the certificate to be send to the winners or participants
without even having to put an effort to it.


SMTP server is used to connect the source code to the gmail account.


- Better to use a dummy account at the development time.
- Make sure the google account security access for apps is turned on for this purpose : [google securtiy](https://myaccount.google.com/intro/security)
- click on continue to make the access live(it stops when you close the tab) : [Account access](https://accounts.google.com/DisplayUnlockCaptcha)
- Connection to SMTP server through port 465(SMTP_SSL) is done using sender mail id and pass.
- U can also hide the address and password using system environment variables

`EMAIL_ADDRESS = os.environ.get('EMAIL_ADD')`

`EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')`

Check the send_email codes to understand how its done explicitly


### Read_input_file

Contains 2 programs which include reading input data from csv and SQL file. I basically used 
PostgreSQL for the database linking. Also pandas helped in data analysis.

### Send_email

This includes the basic programs to send email using python. image perspective and doc perspective
is provided separate. Though the code for both are just different by couple of lines...

### Create_certificate

Here I read data(csv) using pandas. Each row of the data comprises of the values corresponding to 
a particular certificate. The coordinates of these single data can be calculated from the real 
image(certificate). Then using PIL module to do the image drawing and saves the image in the needed
name and format.

### Automation_final_program

All the above descrbed programs are combined to form the final program. Where I read in data from csv file.
Create specific certificate for every person. Sends the certificate to the email id (given).