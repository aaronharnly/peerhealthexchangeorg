from datetime import datetime

class DateFormatter(object):
    """
    @param format
    """
    def __init__(self, format):
        self.format = format
    
    def date_to_text(self, date):
        return date.strftime(self.format)
        
    def date_from_text(self, text):
        return datetime.strptime(text, self.format)

DEFAULT_DATE_FORMATTER = DateFormatter('%a, %d %b %Y %H:%M:%S %Z')

