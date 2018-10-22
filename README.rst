
=============
quizscrambler
=============

Python command line utility to scramble quizzes and questions

It recieves as a input a quiz writte in yaml and outputs pandoc renderable
markdown or yaml

Install
-------

This package is currently not distributed in pipy but it can still
be used by installing it with pip.

On a terminal run the following:

.. code-block:: bash

    git clone http://github.com/jspaezp/quizscrambler
    cd quizscrambler
    virtualenv venv
    . venv/bin/activate
    pip install --editable .

Usage
-----

You can get the documentation for the usage running the command with the `--help`
flag.

.. code-block:: bash

    $ scramblequiz --help

    Usage: scramblequiz [OPTIONS]

      Simple program that Scrambles quizzes written in YAML format

    Options:
      --input TEXT              YAML formatted quiz that will be scrambled
      --yaml_output TEXT        Name of the file that will be used as an output in
                                yaml format
      --md_output TEXT          Name of the file that will be used as an output in
                                markdown format
      --show_answers            Flag indicating if answers should be shown (only
                                applies to markdown)
      --identifier TEXT         Identifier to be added to the output (md output
                                only)
      --shuffle / --no-shuffle  Flags indicating if shuffling should be done
      --dry                     Logical indicating if files should be written
      --help                    Show this message and exit.


Or on ... as an example a super simple quiz saved as simplequiz.yaml

.. code-block:: yaml

    1:
      statement: Which one is better
      options:
          a: foo
          b: var
          c: beer
      answer: beer
    2:
      statement: What is one plus one
      options:
          a: 1
          b: Beer
          c: 2
      answer: 2


Or on ... as an example a super simple quiz

.. code-block:: bash

    $ scramblequiz --input simplequiz.yaml
    Quiz ID: MASTER

    ### 1. Which one is better
      a. foo
      b. beer
      c. var

    ### 2. What is one plus one
      a. Beer
      b. 2
      c. 1

Or in a little more elaborate example

.. code-block:: bash

    $ scramblequiz --input simplequiz.yaml --show_answers --shuffle
    Quiz ID: MASTER

    ### 1. Which one is better
      ANSWER: b. beer
      a. foo
      b. beer
      c. var

    ### 2. What is one plus one
      ANSWER: a. 2
      a. 2
      b. 1
      c. Beer

Note how the output is actually a markdown document... unless you tell him otherwise


.. code-block:: bash

    $ scramblequiz --input simplequiz.yaml --show_answers --shuffle --yaml_output myout.out
    $ cat myout.out

    1:
      statement: Which one is better
      options:
        a: var
        b: beer
        c: foo
      answer: beer
    2:
      statement: What is one plus one
      options:
        a: 2
        b: Beer
        c: 1
      answer: 2


What to do with the output
--------------------------

I currently use pandoc to render the quizzes to pdf.


