import jinja2


quiz_template = jinja2.Template(""
                                "Quiz ID: {{ id }}\n\n"
                                "{% for questionnumber, question in quiz.questions.items() %}"
                                "### {{ str(questionnumber) }}. {{ question.statement }} \n"
                                "{{ '  ' + 'ANSWER: ' + str(question.answer_code) + '. '"
                                " + str(question['answer']) + '\n' if show_answers  }}"
                                "{% for option , optioncode in zip(question.options, question.option_codes) %}"
                                "  {{ str(optioncode) }}. {{ str(option) }} \n"
                                "{% endfor %}"
                                "\n"
                                "{% endfor %}")


#print(t.render(quiz = fake_quiz, id = 'MASTER', show_answer = True, zip = zip, str = str))
#print(t.render(quiz = fake_quiz, id = 'MASTER', show_answer = False, zip = zip, str = str))