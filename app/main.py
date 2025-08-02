import subprocess
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory
from rich import print
import shlex

from .abc_completer import abc_completer
from .key_binds import bindings


def run_az_command(command: str):
  try:
    interactive = command.strip().__contains__('login')

    result = subprocess.run(
      ["az"] + shlex.split(command),
      capture_output=not interactive,
      text=True
    )

    if not interactive:
      if result.stdout:
        print(f"[green]{result.stdout}[/green]")
      if result.stderr:
        print(f"[red]{result.stderr}[/red]")
  except Exception as e:
    print(f"[bold red]Error:[/bold red] {e}")

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
      # cmd_parts = text.split(' ')
      # if len(cmd_parts) > 1:
      #   print('[bold red]Invalid[/bold red]')
      #   continue
      # if cmd_parts[0] not in commands:
      #   print('[bold red]Invalid[/bold red]')
      #   continue
      run_az_command(text) 
    except KeyboardInterrupt:
      break
    except EOFError:
      break

  print("Exiting...")

if __name__ == "__main__":
  main()