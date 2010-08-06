from xml.etree import ElementTree
import logging

import gdata.spreadsheet
import gdata.spreadsheet.service
import gdata.service
import atom
import atom.service

from pheio.dateformat import DEFAULT_DATE_FORMATTER

class SpreadsheetUploader(object):
    """
    Adds the given SurveyResponseSummary to a GDocs spreadsheet

    @param username
    @param password
    @param spreadsheet_id
    @param worksheet_index: Default is 0, i.e. the first worksheet
    
    TODO: what it says
    """
    _DATE_COLUMN = 'date'
    _FROM_COLUMN = 'from'
    _TEXT_COLUMN = 'text'

    def __init__(self, username, password, spreadsheet_id, worksheet_index=0):
        self._date_formatter = DEFAULT_DATE_FORMATTER
        self._username = username
        self._password = password
        self._spreadsheet_id = spreadsheet_id
        self._worksheet_index = worksheet_index
        self._client = self._login()
        self._worksheet_id = self._fetch_worksheet_id()
        
    def insert_survey_response(self, survey_response):
        """
        Append the given response to the spreadsheet.
        """
        date_text = self._date_formatter.date_to_text(survey_response.timestamp)
        from_text = survey_response.surveyor
        raw_text = survey_response.raw or ""
        row = {
            self._DATE_COLUMN: date_text,
            self._FROM_COLUMN: from_text,
            self._TEXT_COLUMN: raw_text
        }
        self._insert_row(row)
        
    def _insert_row(self, row):
        self._client.InsertRow(row, self._spreadsheet_id, self._worksheet_id)
        
    def _create_client(self):
        client = gdata.spreadsheet.service.SpreadsheetsService()
        client.email = self._username
        client.password = self._password
        client.source = self.__class__.__name__
        return client
        
    def _login(self):
        client = self._create_client()
        client.ProgrammaticLogin()
        return client
        
    def _fetch_worksheet_id(self):
        worksheets = self._client.GetWorksheetsFeed(self._spreadsheet_id)
        worksheet = worksheets.entry[self._worksheet_index]
        id = self._id_from_atom(worksheet.id)
        return id
        
    @classmethod
    def _id_from_atom(cls, atom_element):
        """Parses an 'id' atom element to extract just the unique ID"""
        return atom_element.text.rsplit('/', 1)[1]

