import subprocess
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory
from rich import print
import shlex

from .abc_completer import abc_completer
from .key_binds import bindings

def main():
  # p1 = subprocess.run('which az', shell=True, capture_output=True, text=True)
  # if p1.returncode != 0:
  #   print('[bold red]az command not found- please ensure az is in your path[/bold red]')
  #   # return -1

  session = PromptSession(
    history=FileHistory('.az_wrapper_history'),
    key_bindings=bindings,
    completer=abc_completer,
    complete_while_typing=True
    )
  print("[bold blue]Azure CLI Interactive Wrapper[/bold blue]")
  print("Type 'exit' or Ctrl-D to quit")

  while True:
    try:
      text = session.prompt("> ")
      if text.strip().lower() in ["exit", "quit"]:
        break
      if not text.strip():
        continue
    except KeyboardInterrupt:
      break
    except EOFError:
      break

  print("Exiting...")

if __name__ == "__main__":
  main()