import click


@click.group()
def time_warrior() -> None:
    """Time Warrior commands."""
    pass


def stop_time_warrior(tw_id: int) -> str:
    """Stop tracking time."""
    return f"Task Name {tw_id}"


def search_time_warrior_id(task_name: str) -> int:
    """Search for a task name."""
    if task_name:
        return 2
    return 1


def stop_all_time_warrior() -> list:
    """Stop all tracking time."""
    return [3, 4, 5]


@click.command()
@click.argument("tw_id", type=str, required=False)
def stop(tw_id: int) -> None:
    """Stop tracking time."""
    task_name = ""
    try:
        twid = int(tw_id)
    except (ValueError, TypeError):
        twid = None
        task_name = tw_id

    if twid:
        task_name = stop_time_warrior(twid)
        click.echo(f"Stop tracking time {twid}. Task {task_name}.")
    elif task_name:
        time_warrior_id = search_time_warrior_id(task_name)
        if time_warrior_id:
            task_name = stop_time_warrior(time_warrior_id)
            click.secho(f"Stop tracking time for {task_name} with id {time_warrior_id}.", fg="green")
        else:
            click.secho(f"Task {task_name} not found.", fg="red")
    else:
        times_stopped = stop_all_time_warrior()
        click.echo(f"Stop all times {times_stopped}.")


@click.command()
def start() -> None:
    """Start tracking time."""
    stop_all_time_warrior()
    click.echo("Start tracking time.")


time_warrior.add_command(stop)
time_warrior.add_command(start)
