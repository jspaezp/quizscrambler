from random import shuffle
from ruamel import yaml


class QuizQuestion:
    def __init__(self, statement, options, answer=None, answer_code=None):
        self.statement = statement

        if not len(options) > 1:
            raise ValueError("Options provided are not more than 1.")

        self.option_codes = [x for x in options.keys()]
        self.options = [x for x in options.values()]

        if answer is None and answer_code is not None:
            try:
                answer = options[answer_code]
            except KeyError:
                raise ValueError("%s is not a valid answer code. It is not contained in the options" % answer_code)

        if answer not in self.options:
            try:
                answer = options[answer]
            except KeyError:
                raise ValueError("%s is not a valid answer. It is not contained in the options" % answer)

        self.answer = answer
        self.answer_code = self.option_codes[self.options.index(answer)]

    def __repr__(self):
        return('QuizQuestion(**' +
               self.as_dict().__repr__() +
               ')')

    def __str__(self):
        return(yaml.dump(self.as_dict()))

    def shuffle(self):
        shuffle(self.options)
        self.answer_code = self.option_codes[self.options.index(self.answer)]

    def as_dict(self):
        out_dict = {'statement': self.statement,
                    'options': {x:y for x, y in zip(self.option_codes, self.options)},
                    'answer': self.answer}
        return out_dict


def test_quizquestion_io():
    fakequiz = ("1: \n"
                "  statement: Which one is better\n"
                "  options: \n"
                "      a: foo\n"
                "      b: var\n"
                "      c: beer\n"
                "  answer: beer\n"
                "2: \n"
                "  statement: What is one plus one\n"
                "  options: \n"
                "      a: 1\n"
                "      b: Beer\n"
                "      c: 2\n"
                "  answer: 2\n")
    foo = yaml.load(fakequiz)[1]
    fake_question = QuizQuestion(foo['statement'], foo['options'], foo['answer'])

    assert all([x in fake_question.options for x in ['foo', 'var', 'beer']]), \
        "Not all question options were detected"

    foo = yaml.load(fakequiz)[2]
    fake_question = QuizQuestion(foo['statement'], foo['options'], foo['answer'])

    assert all([x in fake_question.options for x in [1, 'Beer', 2]]),\
        "Not all question options were detected after generating QuizQuestion object"

    foo = yaml.load(fakequiz)[2]
    assert QuizQuestion(**foo) == foo, "Dictionary representation of the question is not equal to the parsed YAML"


