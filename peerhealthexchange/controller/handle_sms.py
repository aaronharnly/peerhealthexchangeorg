import logging
import email
from google.appengine.ext import webapp
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.ext.webapp.util import run_wsgi_app

from peerhealthexchange.inputoutput import SMSSurveyParser, SpreadsheetSurveyUploader
from peerhealthexchange.config import GOOGLE_DOCS_CONFIG

class SMSHandler(InboundMailHandler):
    """
    Receives email sent to the SMS address, attempts to parse it, then hands the
    result off to SurveyHandlers.
    
    @param username
    @param password
    @param spreadsheet_id
    """
    def __init__(self, username, password, spreadsheet_id):
        self._parser = SMSSurveyParser()
        self._handlers = [
            SpreadsheetSurveyUploader(username, password, spreadsheet_id)
        ]
    
    def receive(self, mail_message):
        logging.info("Received a message from: " + mail_message.sender)
        logging.info("Message date: %s" % mail_message.date)
        logging.info("Message to: %s" % mail_message.to)
        logging.info("Message subject: %s" % mail_message.subject)
        logging.info("Message body: %s" % mail_message.body)
        logging.info("Plaintext: %s" % list(map(lambda b: b[1].decode(), mail_message.bodies('text/plain'))))
        survey_summary = self._parser.message_to_summary(mail_message)
        for handler in self._handlers:
            handler.handle_survey_summary(survey_summary)

def main():
    def handler_factory(): 
        return SMSHandler(**GOOGLE_DOCS_CONFIG)
    application = webapp.WSGIApplication([('/_ah/mail/.+', handler_factory)], debug=True)
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
