class Question(object):
    """
    @param id: some unique identifier
    """
    def __init__(self, id):
        self.id = id
        
    def __eq__(self, other):
        return self.id == other.id
        
    def __ne__(self, other):
        return not self == other
        
    def __hash__(self):
        return hash(self.id)
        
    def __str__(self):
        return "Question %d" % self.id

class MultipleChoiceQuestion(Question):
    """
    A question with a finite set of possible responses.
    
    @param id: some unique identifier
    @param options: an iterable of strings representing the possible responses
    """
    def __init__(self, id, options):
        Question.__init__(self, id)
        self.options = frozenset(options)
        
    def __eq__(self, other):
        return (
            Question.__eq__(self, other) and
            self.options == other.options
        )
        
    def __hash__(self):
        return hash((self.id, self.options))

class Survey(object):
    """
    An ordered sequence of questions.
    
    @param id: some unique identifier
    @param questions: an iterable of Questions
    """
    def __init__(self, id, questions):
        self.id = name
        self.questions = tuple(questions)
        
    def __eq__(self, other):
        return (
            self.id == other.id and
            self.questions == other.questions
        )
        
    def __ne__(self, other):
        return not self == other
        
    def __hash__(self):
        return hash(self.questions)
        
    def __str__(self):
        return "Survey(id=%s, questions=%s)" % (
            self.id,
            self.questions
        )

class QuestionResponseSummary(object):
    """
    Abstract base class.
    How did a set of participants respond to a particular question?
    
    @param question: Which question are we summarizing the responses to?
    """
    def __init__(self, question):
        self.question = question
        
    def __eq__(self, other):
        # NB subclasses *must* specify other conditions, e.g. the counts of different responses being the same
        return self.question == other.question

    def __ne__(self, other):
        return not self == other
        
    def __hash__(self):
        return hash(self.question)
        
class MultipleChoiceResponseSummary(QuestionResponseSummary):
    """
    How did a set of participants respond to a particular multiple choice question?

    @param question: Which MultipleChoiceQuestion are we summarizing the responses to?
    @param option_counts: A dict mapping from the possible responses to the question, to how many people chose that response.
    Options with no entry in this dict will be assumed to have a count of 0. 
    Options supplied but not among the question's options will be ignored.
    """
    def __init__(self, question, option_counts):
        QuestionResponseSummary.__init__(self, question)
        self._counts = dict((
            (option, option_counts.get(option, 0))
            for option in question.options
        ))
        
    @property
    def question_id(self):
        return self.question.id
    
    @property
    def total(self):
        return sum(self._counts.values())
        
    @property
    def counts(self):
        return self._counts
    
    def __getitem__(self, key):
        return self._counts[key]
        
    def __eq__(self, other):
        return (
            QuestionResponseSummary.__eq__(self, other) and
            self.counts == other.counts
        )
        
    def __hash__(self):
        return hash((self.question, tuple(self.counts.items())))
        
    def __str__(self):
        return "Response(question_id=%s, counts=%s)" % (
            self.question_id,
            self.counts
        )

class SurveyResponseSummary(object):
    """
    How did a set of participants respond to a particular survey?
    """
    pass