"""Contains the Options Arguments and Commands for the CLI"""
import click
from pass_gen.core.password_generator import PasswordGenerator


@click.group()
def cli():
    "Click password generator"


@cli.command(name="generate")
@click.option(
    "-len",
    "--length",
    type=int,
    help="Length of the password",
    required=False,
    default=12
)
def generate_password(length):
    "Generates a random password of default 12"
    password = PasswordGenerator().generate_password(length=length)
    click.echo("Here is your password")
    click.echo(password)


cli.add_command(generate_password)
