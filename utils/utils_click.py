import click
from rich.console import Console
from usr_info.user import logged_in_user
import utils.utils_tinydb as td
import datetime
import os

console = Console()
dt_now = str(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))


@click.group()
def cli():
    pass


def welcome():
    click.echo("Welcome to mood, a mood tracker to help you manage your mood (obviously).")


@cli.command(name='s', help="Input a score.")
def obtain_score():
    score = int(click.prompt("How do you feel?", type=int))
    if score >= 5:
        console.print("[red]Damn, you feel great![/red]")
    else:
        console.print("[green]Keep going, you're doing well![/green]")
    td.write_mood_data(dt_now, score)


@cli.command(name='d', help="Delete User File.")
def delete_user():
    user_input = click.prompt('Are you sure you want to delete this user?', type=click.Choice(['y', 'n']))
    if user_input == 'y':
        td.delete_mood_data()
        os.remove(f"{logged_in_user}.txt") # Deleting the first-time startup check so user can start from scratch.
        console.print(f"[red]Deleted file for {logged_in_user}[/red]")



