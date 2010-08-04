from unittest import TestCase

from peerhealthexchangorg.model.survey import MultipleChoiceQuestion, Survey, MultipleChoiceResponseSummary

class TestMultipleChoiceQuestion(TestCase):
    def test_creation(self):
        q = MultipleChoiceQuestion(id=1, options=["a", "b", "c"])