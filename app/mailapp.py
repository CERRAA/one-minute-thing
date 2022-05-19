# from flask import render_template
# from app import mail
# import os

# def mail_message(subject, template, to, **kwargs):
#     sender_mail = 'cerraangie113@gmail.com'
#     email = Message(subject, sender=sender_mail, recipients=[to])
#     email.body = render_template(f'{template}.txt', **kwargs)
#     email.html = render_template(f'{template}.html', **kwargs)
#     mail.send(email)aa