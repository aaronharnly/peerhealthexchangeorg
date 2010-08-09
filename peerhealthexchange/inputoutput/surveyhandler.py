import logging
import traceback

class SurveyHandler(object):
    """
    Abstract base class for things that do stuff with survey summaries.
    ^ Wow, great documentation, Aaron.
    """
    def handle_survey_summary(self, survey_summary):
        """
        @param survey_summary: a SurveyResponseSummary object
        """
        try:
            logging.info("%s is handling a survey summary: %s" % (self._name, survey_summary))
            self._handle_survey_summary(survey_summary)
        except:
            logging.error("%s encountered an error: %s" % (self._name, traceback.format_exc()))
            
    @property
    def _name(self):
        return self.__class__.__name__

    def _handle_survey_summary(self, survey_summary):
        """
        @param survey_summary: a SurveyResponseSummary object
        """
        raise NotImplementedError