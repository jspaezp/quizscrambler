import click
from ruamel import yaml
from .quiz import Quiz


@click.command()
@click.option('--input', help='YAML formatted quiz that will be scrambled')
@click.option('--yaml_output', default=None, help='Name of the file that will be used as an output in yaml format')
@click.option('--md_output', default=None, help='Name of the file that will be used as an output in markdown format')
@click.option('--show_answers',
              is_flag=True,
              help='Flag indicating if answers should be shown (only applies to markdown)')
@click.option('--identifier',
              default="MASTER",
              help='Identifier to be added to the output (md output only)')
@click.option('--shuffle/--no-shuffle', default=True, help='Flags indicating if shuffling should be done')
@click.option('--dry', is_flag=True, help='Logical indicating if files should be written')
def scramblequiz(input, yaml_output, md_output, show_answers, shuffle,identifier, dry):
    """Simple program that Scrambles quizzes written in YAML format"""
    with open(input, 'r') as f:
        quiz = f.read()
        yamlquiz = yaml.load(quiz, Loader=yaml.RoundTripLoader)

    foo = Quiz(yamlquiz)

    if shuffle:
        foo.shuffle()

    dump = yaml.dump(foo.as_dict(), Dumper=yaml.RoundTripDumper)
    # print(dump)

    if yaml_output is not None and not dry:
        with open(yaml_output, 'w') as f:
                f.write(dump)

    dump = foo.render_md(id=identifier, show_answers=show_answers)
    print(dump)

    if md_output is not None and not dry:
        with open(md_output, 'w') as f:
            f.write(dump)

    return 0


