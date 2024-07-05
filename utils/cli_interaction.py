import click
from rich.console import Console
import datetime
import os
from usr.user import User
import utils.database as database


console = Console()
dt_now = str(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
db = None


@click.group()
def cli():
    pass


def welcome():
    click.echo("Welcome to mood, a mood tracker to help you manage your mood (obviously).")
    user_input = click.prompt('what is your name?')
    score_input = click.prompt('How are you feeling?')
    user_info = User(name=user_input, score=score_input)
    User.set_current_user(user_input)
    global db
    db = database.initialize_db()
    database.first_db_setup(datetime=dt_now, name=user_info.name, score=user_info.score)


@cli.command(name='s', help="Input a score.")
def obtain_score():
    score = int(click.prompt("How do you feel?", type=int))
    if score >= 5:
        console.print("[red]Damn, you feel great![/red]")
    else:
        console.print("[green]Keep going, you're doing well![/green]")
    database.write_mood_data(score=score)


@cli.command(name='d', help="Delete User File.")
def delete_user():
    user_input = click.prompt('Are you sure you want to delete this user?', type=click.Choice(['y', 'n']))
    if user_input == 'y':
        database.delete_mood_data()
        os.remove("user.txt") # Deleting the first-time startup check so user can start from scratch.
        console.print(f"[red]Deleted file for {os.getlogin()}[/red]")



