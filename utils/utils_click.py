import click


i = 0
j = ""
@click.command()
@click.option("--name", prompt="Enter your name")
def create_user(name):
    # click.echo(f"Creating user {name}")
    j = name
    # return name


if __name__ == "__main__":
    create_user()
    print(j)
