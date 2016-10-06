import click
import shelve

import util


db_file = "proxyguy_db"


@click.group()
def init():
    pass


@click.command("new")
@click.option('--profile-name', prompt='Profile Name',
              help='The name of the proxy configuration profile')
@click.option('--address', prompt='Proxy Address',
              help='The proxy server address')
@click.option('--port', default=80, prompt='Port Number',
              help='The name of the proxy configuration profile')
@click.option('--username', prompt='Username',
              help='The proxy username')
@click.option('--password', prompt='Password',
              help='The proxy password')
@click.option('--activate', type=click.BOOL, default=False, required=False)
def new_profile(profile_name, address, port, username, password, activate):
    """
    create a network proxy configuration profile
    """
    store = shelve.open(db_file)
    try:
        store[str(profile_name)] = {
            'address' : address,
            'port' : port,
            'username' : username,
            'password' : password
        }
        click.echo("Profile '{}' successfully created".format(profile_name))
    finally:
        store.close()

    if activate:
        activate_profile(profile_name)



def activate_profile(profile_name):
    store = shelve.open(db_file)
    util.write(store[str(profile_name)])
    try:
        store['active'] = str(profile_name)
        click.echo("Profile '{}' successfully activated".format(profile_name))
    except KeyError:
        click.echo("No such profile '{}'".format(str(profile_name)))
    finally:
        store.close()


@click.command()
@click.argument('profile-name')
def activate(profile_name):
    """
    activate a network proxy configuration profile
    """
    activate_profile(profile_name)


@click.command("current")
def current_profile():
    """
    view activated a network proxy configuration profile
    """
    store = shelve.open(db_file)
    try:
        click.echo(store['active'])
    except KeyError:
        click.echo("You have no active profile")
    finally:
        store.close()


@click.command("list")
def list_profiles():
    """
    lists all stored proxy profiles
    """
    store = shelve.open(db_file)
    try:
        [click.echo(s) for s in store if s != "active"]
    finally:
        store.close()


def delete_profile(profile_name):
    pass


def restore_default():
    pass


init.add_command(new_profile)
init.add_command(activate)
init.add_command(list_profiles)
init.add_command(current_profile)

