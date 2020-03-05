import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 465  # For starttls
sender_email = "galvramon44@gmail.com"
receiver_email = "galvramon44@gmail.com"
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""
# Create a secure SSL context
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
# # Try to log in to server and send email
# try:
#     server = smtplib.SMTP(smtp_server,port)
#     server.ehlo() # Can be omitted
#     server.starttls(context=context) # Secure the connection
#     server.ehlo() # Can be omitted
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)
#     # TODO: Send email here
# except Exception as e:
#     # Print any error messages to stdout
#     print(e)
# finally:
#     server.quit() 