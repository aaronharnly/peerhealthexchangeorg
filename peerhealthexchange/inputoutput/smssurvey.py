"""
Handles parsing an emailed SMS survey response into a SurveyResponseSummary model object.
"""

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
        return SurveyResponseSummary(
            timestamp=message.date,
            surveyor=message.sender,
            raw=message.body
        )
