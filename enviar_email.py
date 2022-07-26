from email.message import EmailMessage
import ssl
import smtplib

email_emisor = 'alanjahirmartinez@gmail.com'
email_pasword = 'wylkyhhpzfppngxd'
email_receptor = 'klenbooy7@gmail.com'


asunto = 'Prueba de envio de email'
cuerpo = """
    Probando correo de envip automático en Python
"""

em = EmailMessage()
em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto
em.set_content(cuerpo)

contexto = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
    smtp.login(email_emisor, email_pasword)
    smtp.sendmail(email_emisor, email_receptor, em.as_string())