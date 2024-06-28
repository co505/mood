import click
from rich.console import Console
import datetime
import os
import usr
import database


console = Console()
user = usr.User
dt_now = str(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))


@click.group()
def cli():
    pass


def welcome() -> usr:
    click.echo("Welcome to mood, a mood tracker to help you manage your mood (obviously).")
    user_input = click.prompt('what is your name?')
    score_input = click.prompt('How are you feeling?')
    database_setup = database.initialize_db("mood.json")
    database.first_db_setup(db=database_setup, datetime=dt_now, name=user_input, score=score_input)
    return user(name=user_input, score=score_input)


@cli.command(name='s', help="Input a score.")
def obtain_score():
    score = int(click.prompt("How do you feel?", type=int))
    if score >= 5:
        console.print("[red]Damn, you feel great![/red]")
    else:
        console.print("[green]Keep going, you're doing well![/green]")


@cli.command(name='d', help="Delete User File.")
def delete_user():
    user_input = click.prompt('Are you sure you want to delete this user?', type=click.Choice(['y', 'n']))
    if user_input == 'y':
        database.delete_mood_data()
        os.remove("user.txt") # Deleting the first-time startup check so user can start from scratch.
        console.print(f"[red]Deleted file for {user}[/red]")



