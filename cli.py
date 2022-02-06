import os
import sys

class console():
    def __init__(self, title="Console", input_text=">> ", enable_defaults=True, enable_tips=True):
        os.system(f"title {title}")
        self.cmds = {}
        self.input_text = input_text

        if enable_defaults:
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
            self.print("To get a list of commands, type help.")

        # Let the user configure it first
        #self.accept_input()

    def error(self, error_string):
        print(f"Error: {error_string}")

    def print(self, print_string):
        print(print_string)

    def accept_input(self):
        cmd = input(self.input_text)
        split_cmd = cmd.split(" ")
        cmd_name = split_cmd[0]
        split_cmd.pop(0)
        cmd_args = split_cmd

        if cmd_name in self.cmds:
            target_cmd = self.cmds[cmd_name]

            cmd_func = target_cmd["func"]
            
            cmd_func(*cmd_args)

            # Accept input again after, so the program doesn't just close
            self.accept_input()
        else:
            self.error(f"Invalid command '{cmd_name}'")
            self.accept_input()

    def register_command(self, name, desc, func):
        self.cmds[name] = {
            "desc": desc,
            "func": func
        }

    def list_cmds(self):
        cmd_list_str = ""

        for cmd_name, cmd in self.cmds.items():
            cmd_list_str = f"{cmd_list_str}{cmd_name} - {cmd['desc']}\n"

        self.print(f"\nLIST OF COMMANDS\n{cmd_list_str}\n")
