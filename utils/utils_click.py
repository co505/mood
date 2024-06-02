import click
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
def cli():
    pass


@click.command()
@click.option("--name", prompt="Enter your name")
def create_user(name):
    console.print(f"[bold cyan]{name}[/bold cyan] has been created.[bold cyan] Welcome :)[/bold cyan]", style="bold red")
    # Save user to the file.


@click.command()
@click.option("--score", prompt="How do you feel on a scale of one to five?", type=int)
def obtain_score(score):
    if score >= 5:
        console.print("[red] damn u bad [/red]")


@click.command()
@click.option("--welcome", prompt="Welcome Setup", type=str)
def welcome_setup(welcome):
    console.print(f"[green] Welcome, it's  [/green]")
    user_input = click.prompt("Enter your username: ")
    create_user(user_input)
    obtain_score()


if __name__ == "__main__":
    obtain_score()
    welcome_setup()
    create_user()
