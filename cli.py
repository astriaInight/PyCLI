# cli.py

import os
import sys


class Console:
    def __init__(self, title="Console", input_text=">> ", enable_defaults=True, enable_tips=True):
        os.system(f"title {title}")
        self.cmds = {}
        self.input_text = input_text

        if enable_defaults:  # If the defaults are enabled, we must insert the standard help and exit commands
            self.register_command(
                "help",
                "Lists all commands",
                self.list_cmds
            )
            self.register_command(
                "exit",
                "exit the application",
                sys.exit
            )

        if enable_tips:
            self._print("To get a list of commands, type help.")

        # Let the user configure it first
        # self.accept_input()

    @staticmethod
    def _error(error_string: str) -> None:
        print(f"Error: {error_string}")

    @staticmethod
    def _print(print_string: str) -> None:
        print(print_string)

    # Recursively retrieves the users input
    def accept_input(self) -> None:
        cmd = input(self.input_text)
        split_cmd = cmd.split(" ")
        cmd_name = split_cmd[0]
        split_cmd.pop(0)
        cmd_args = split_cmd

        if cmd_name in self.cmds:
            target_cmd = self.cmds[cmd_name]

            cmd_func = target_cmd["func"]

            cmd_func(*cmd_args)
        else:
            self._error(f"Invalid command '{cmd_name}'")

        # Run the input again, allowing for recursive checks
        self.accept_input()

    # Creates a new command
    def register_command(self, name: str, desc: str, func) -> None:
        self.cmds[name] = {
            "desc": desc,
            "func": func
        }

    # Fetches a list of commands and sends it back to the user
    def list_cmds(self) -> None:
        cmd_list_str = ""

        # Iterate through commands and append it to our string
        for cmd_name, cmd in self.cmds.items():
            cmd_list_str = f"{cmd_list_str}{cmd_name} - {cmd['desc']}\n"

        self._print(f"\nLIST OF COMMANDS\n{cmd_list_str}\n")
