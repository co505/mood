import click
import utils_json as json_file
from rich.console import Console

"""

It's probably best to have a group here to create the welcome stage.
With the welcome stage, we can populate the data structure, then push
that to a JSON file.

Furthermore, each creation function is only deployed once, therefore we 
may as well encalpuate it into one big group, rather then have them
scattered and separately called in the main function.


"""

console = Console()


@click.group()
def setup():
    pass


@setup.command(name='c', help="Change your username.")
def create_user():
    username = click.prompt("Enter your name", type=str)
    json_file.create_mood_data(username, f"{username}_mood.json")
    console.print(f"[bold cyan]{username}[/bold cyan] has been created. [bold cyan]Welcome :)[/bold cyan]",
                  style="bold red")
    # Each user should have a specific file for them, rather than one nested variable.
    # Usernames being input into the to get around the issue of two parameters being required for the method.


@setup.command(name='s', help="Input a score.")
def obtain_score():
    score = click.prompt("how do you feel?", type=int)
    if score >= 5:
        console.print("[red]Damn, you feel great![/red]")
    else:
        console.print("[green]Keep going, you're doing well![/green]")

# cli.add_command(obtain_score)
# cli.add_command(create_user)


# @cli.command(name='w', help='welcome page')
# @click.argument('username')
# @click.argument('score')
# def welcome_setup(username, score):
#     click.echo("Welcome page")
#     click.echo("Enter username:")



    """json_file.create_mood_data(username, f"{username}_mood.json")
    click.echo(f"Welcome to mood! {welcome}")
    create_user(username)
    obtain_score(score)"""


# @cli.command(name='w', help='welcome page')
# @click.option('--welcome', default=False)
# def welcome_setup(welcome):
#     click.echo(welcome)
#     username = input("enter user")
#     create_user(username)
#     score = input("enter score")
#     obtain_score(score)

"""
Multiple issues :

1) Welcome function does not work
2) When grouped, the options don't show as options
3) When only one function is called, it only lists that particular function as an option

"""

if __name__ == "__main__":
    setup_commands = ['c', 's']
    setup(args=setup_commands, prog_name='setup')
