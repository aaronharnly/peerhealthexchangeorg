"""
Handles parsing an emailed SMS survey response into a SurveyResponseSummary model object.
"""
from email.utils import parseaddr
from dateutil.parser import parse

from peerhealthexchange.model import SurveyResponseSummary

class SMSSurveyParser(object):
    """
    @param surveys: a Surveys object, which is a queryable collection of Survey instances.
    """
    def message_to_summary(self, mail_message):
        """
        Attempts to parse the given message as a SurveyResponseSummary.
        If parsing fails, the summary will just contain a 'raw' portion, with no associated Survey object or QuestionResponses.
        
        @param mail_message
        """
        timestamp = parse(mail_message.date)
        plaintext_bodies = map(lambda b: b[1].decode(), mail_message.bodies('text/plain'))
        plaintext_body = plaintext_bodies[0]
        sender_name = parseaddr(mail_message.sender)[0]
        
        return SurveyResponseSummary(
            timestamp=timestamp,
            surveyor=sender_name,
            raw=plaintext_body
        )
