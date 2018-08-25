from .quizquestions import QuizQuestion
from .render import quiz_template
from random import shuffle
from ruamel import yaml

class Quiz:
    def __init__(self, questions):
        self.questions = {x:QuizQuestion(**y) for x, y in questions.items()}
        assert all([type(x) == QuizQuestion for x in self.questions.values()])

    def shuffle(self, shuffle_questions=True, shuffle_answers=True):
        questions = list(self.questions.values())

        if shuffle_questions:
            shuffle(questions)
        if shuffle_answers:
            for question in questions:
                question.shuffle()

        self.questions = {x: y for x, y in zip(self.questions.keys(), questions)}

    def __repr__(self):
        return('Quiz(' +
               self.as_dict().__repr__() +
               ')')

    def __str__(self):
        dump = yaml.dump(self.as_dict())
        return dump

    def as_dict(self):
        out_dict = {x: y.as_dict() for x, y in self.questions.items()}
        return out_dict

    def render_md(self, id = "MASTER", show_answers=False, *args, **kwargs):
        """
        quiz = fake_quiz, id = 'MASTER', showanswer = True, zip = zip, str = str
        :param id: an id to give to the rendering of the quiz
        :param show_answers: logical indicating if the answers should be shown
        :return: markdown formatted string that will be converted using pandoc
        """
        out = quiz_template.render(quiz=self, id=id, zip=zip, str=str, show_answers=show_answers, *args, **kwargs)
        return out

    def answer_keys(self):
        keys = [x.values().answer_code for x in self.questions.values()]
        return(keys)


def test_quizq_io():
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
    foo = yaml.load(fakequiz, Loader=yaml.Loader)
    fake_quiz = Quiz(foo)



