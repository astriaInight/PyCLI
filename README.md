# PyConsole
Simple CLI creator for python.

# Example
```py
# The console.py file needs to be in the same folder for this to work.
from console import console

if __name__ == "__main__":
    app = console(title="Cool command line app")

    def hello():
        app.print("hellooo")

    app.register_command("test", "hello world", hello)

    # Allows the user to input commands
    app.accept_input()

```
