import logging
import email
from google.appengine.ext import webapp
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.ext.webapp.util import run_wsgi_app

class SMSHandler(InboundMailHandler):
    """
    Receives email sent to the SMS address, and attempts to parse it.
    """
    def receive(self, mail_message):
        logging.info("Received a message from: " + mail_message.sender)

def main():
    application = webapp.WSGIApplication([SMSHandler.mapping()], debug=True)
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
