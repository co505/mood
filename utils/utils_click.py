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


@cli.command(help="Change your username.")
@click.option("--username", prompt="Enter your name", help="The username to create")
def create_user(username):
    console.print(f"[bold cyan]{username}[/bold cyan] has been created. [bold cyan]Welcome :)[/bold cyan]",
                  style="bold red")
    # Save user to the file


@cli.command(help="Input a score.")
@click.option("--score", prompt="How do you feel on a scale of one to five?", type=int, help="Your score from 1 to 5")
def obtain_score(score):
    if score >= 5:
        console.print("[red]Damn, you feel great![/red]")
    else:
        console.print("[green]Keep going, you're doing well![/green]")


@click.command()
@click.argument('content', required=False)
@click.option('--to_stdout', default=False)
@click.pass_context
def welcome_setup():
    username = click.prompt("Enter your username")
    create_user.invoke(
        create_user(username)
    )
    score = click.prompt("How do you feel on a scale of one to five?", type=int)
    obtain_score.invoke(obtain_score(score))


if __name__ == "__main__":
    cli()