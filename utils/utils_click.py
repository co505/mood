import click
import utils.utils_json as json_file
from rich.console import Console
from usr_info.user import logged_in_user
import utils.tiny_database as td
import datetime

console = Console()


@click.group()
def cli():
    pass


@cli.command(name='c', help="Create a file using the current logged in username.")
def create_user():
    if json_file.create_mood_data(logged_in_user, "./"):
        console.print(f"[bold cyan]{logged_in_user}[/bold cyan] has been created. [bold cyan]Welcome :)[/bold cyan]", style="bold red")
    else:
        console.print(f"Oops, a file already exists for [bold cyan]{logged_in_user}[/bold cyan].")


@cli.command(name='s', help="Input a score.")
def obtain_score():
    score = click.prompt("How do you feel?", type=int)
    dt_now = str(datetime.datetime.now())
    if score >= 5:
        console.print("[red]Damn, you feel great![/red]")
    else:
        console.print("[green]Keep going, you're doing well![/green]")
    td.write_mood_date(dt_now, score)


"""

We don't execute the check for a first time user here, we do it in the utils_json.py file. From there, we can check 
from a file-level (?) if the user exists, if not, "Welcome! :) Function should be stored inside main for now, 
just to speed development up slightly.

Why don't we just store the file upon first boot? using the os.getlogin method? We could avoid a "what's your name?"
function to create the user and automatically set the file structure up using the name stored through the login. 
The welcome message could just introduce the user to the program through echo statements, rather then ask them arbitrary 
questions. Security issue though? Maybe transparency is key, e.g."A file has been created for you in your logged-in
name, do you wish to change it?  


"""


