from unittest import TestCase

from peerhealthexchange.model.survey import MultipleChoiceQuestion, Survey, MultipleChoiceResponseSummary

class TestMultipleChoiceQuestion(TestCase):
    def test_creation(self):
        q = MultipleChoiceQuestion(id=1, options=["a", "b", "c"])
        self.assertEqual(q.id, 1)
        self.assertEqual(q.options, ("a", "b", "c"))
        
    def test_equality(self):
        q1 = MultipleChoiceQuestion(id=1, options=["a", "b", "c"])
        q2 = MultipleChoiceQuestion(id=1, options=["a", "b", "c"])
        self.assertEqual(q1, q2)

    def test_inequality__id(self):
        q1 = MultipleChoiceQuestion(id=1, options=["a", "b", "c"])
        q2 = MultipleChoiceQuestion(id=2, options=["a", "b", "c"])
        self.assertNotEqual(q1, q2)

    def test_inequality__options(self):
        q1 = MultipleChoiceQuestion(id=1, options=["a", "b", "c"])
        q2 = MultipleChoiceQuestion(id=1, options=["a", "b", "d"])
        self.assertNotEqual(q1, q2)
        
    def test_with_n_options(self):
        q = MultipleChoiceQuestion.with_n_options(1, 5)
        self.assertEqual(
            q,
            MultipleChoiceQuestion(id=1, options=["a", "b", "c", "d", "e"])
        )

class TestSurvey(TestCase):
    def test_creation(self):
        q1 = MultipleChoiceQuestion(id=1, options=["a", "b", "c"])
        q2 = MultipleChoiceQuestion(id=2, options=["a", "b", "c"])
        s = Survey(id=1, questions=[q1, q2])
        self.assertEqual(s.id, 1)
        self.assertEqual(s.questions, (q1, q2))