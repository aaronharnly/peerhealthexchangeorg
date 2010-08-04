import logging
import email
from google.appengine.ext import webapp
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.ext.webapp.util import run_wsgi_app

class SMSHandler(InboundMailHandler):
    """
    Receives email sent to the SMS address, attempts to parse it, then hands the
    result off to SurveyHandlers.
    """
    def receive(self, mail_message):
        logging.info("Received a message from: " + mail_message.sender)
        logging.info("Received a message: %s" % mail_message.subject)
        logging.info("Received a message: %s" % mail_message.to)
        logging.info("Received a message: %s" % mail_message.body)
        logging.info("Received a message: %s" % mail_message.date)
        logging.info("Received a message: %s" % mail_message.to_mime_message())
        logging.info("message has: %s" % dir(mail_message))

def main():
    application = webapp.WSGIApplication([SMSHandler.mapping()], debug=True)
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
