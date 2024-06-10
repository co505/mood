from utils.utils_click import cli
from utils.tiny_database import create_structure

if __name__ == "__main__":
    create_structure()
    cli()