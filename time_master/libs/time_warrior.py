import subprocess


class TimeWarriorWrapper:
    """Time warrior wrapper."""

    def __init__(self, binary: str = "timew") -> None:
        """Initialize TimeWarriorWrapper."""
        self.bin = binary

    def summary(self, date: str = None) -> list:
        """Get time warrior summary."""
        commands = ["summary"]
        if date:
            commands.append(date)
        summary = self.__run(commands)
        lines = []
        if summary:
            lines = summary.split("\n")
            lines = [line for line in lines if line]

        return lines[2:]

    def __run(self, args: list) -> str:
        return subprocess.run([self.bin] + args, stdout=subprocess.PIPE, check=False).stdout.decode("utf-8")
