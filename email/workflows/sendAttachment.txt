#!/usr/local/bin/python3


import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base  import MIMEBase
from email.message import Message
from email.mime.message import MIMEMessage

fileName='sendmail.ini'
fp=open(fileName)
lines=fp.read().splitlines()
fp.close()

recipients=lines[0].split(':')
del recipients[0]

ccrecipients=lines[1].split(':')
del ccrecipients[0]

line=lines[2].split(':')
subject=line[1].rstrip()


line=lines[3].split(':')

if (line[1].rstrip() == 'FILE'):
	filename=line[2].rstrip()
	fp1=open(filename)
	message=fp1.read()
	fp1.close()
else:
	message=line[1]

line=lines[4].split(':')

username=line[1].rstrip()


line=lines[5].split(':')

password=line[1].rstrip()


line=lines[6].split(':')

smtphost=line[1].rstrip()


line=lines[7].split(':')

port=line[1].rstrip()


attachments=lines[8].split(':')
del attachments[0]
print ("there are {0} attachments\n".format(len(attachments)))


#message info

sender=username


try:
	msg= MIMEMultipart()
	msg["From"] = sender 
	msg["To"] = ",".join(recipients) 
	msg["Subject"]=subject

	#BODY
	body=MIMEText(message);
	msg.attach(body)
	
	for fileToSend in attachments:
		if(len(attachments)==0):
		    break
		#ATTACHMENT
		ctype,encoding = mimetypes.guess_type(fileToSend)
		if ctype is None or encoding is not None:
			ctype = "application/octet-stream"


		maintype, subtype = ctype.split("/",1)
		
		
		if maintype == "text":
			fp=open(fileToSend)
			attachment=MIMEText(fp.read(),_subtype=subtype)
			fp.close()

		if maintype == "image":
			fp=open(fileToSend,"rb")
			attachment=MIMEImage(fp.read(),_subtype=subtype)
			fp.close()

		if maintype == "audio":
			fp=open(fileToSend,"rb")
			attachment=MIMEAudio(fp.read(),_subtype=subtype)
			fp.close()
		else:
			fp=open(fileToSend,"rb")
			attachment=MIMEBase(maintype,subtype)
			attachment.set_payload(fp.read())
			fp.close()
			encoders.encode_base64(attachment)
			



		attachment.add_header("Content-Disposition","attachment",filename=fileToSend)
		msg.attach(attachment)	




	# SMPT server info

	s = smtplib.SMTP(host=smtphost,port=port)
	s.starttls()
	s.login(username,password)
	s.sendmail(sender,recipients,msg.as_string())
	s.quit()

	print('Successfully sent email')

except SMTPException:
	print('Error: unable to send email')

