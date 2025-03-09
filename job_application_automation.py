import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
sender_email = "prakashvenkat148@gmail.com"
sender_password = "jlzn yyji zizl eijn" 
receiver_email = input("Enter the recipient's email address: ")
company_name = input("Enter the company name: ")
subject = "Job Application for Web Developer Position"
body = f"""
Hi Recipient's,

I hope you're doing well. My name is Prakash, and I'm very interested in the Web Developer position at {company_name}. With over one year of experience in web development, I have worked with technologies such as HTML5, CSS, JavaScript, AngularJS, and Java, building responsive and user-friendly web applications.

I'm impressed by the innovative work your team does, and I believe my skills align well with your needs.
I’m excited about the opportunity to contribute and grow within your organization.

I attached my Resume.
Best regards,  
Prakash  
prakashvenkat148@gmail.com  
+91-8489529876  
"""
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))
resume_filename = r".\\PRAKASHSD.pdf"
try:
    with open(resume_filename, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename="{resume_filename}"')
        msg.attach(part)
except FileNotFoundError:
    print(f"Error: The file {resume_filename} was not found.")
smtp_server = "smtp.gmail.com"
smtp_port = 465

try:
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {str(e)}")
finally:
    try:
        server.quit()
    except NameError:
        pass
