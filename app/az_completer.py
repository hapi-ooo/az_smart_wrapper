from prompt_toolkit.document import Document
from prompt_toolkit.completion import (
  Completion,
  CompleteEvent,
  Completer,
  ThreadedCompleter
)
from typing import Iterable
import time
from .commands import commands

class _AzCompleter(Completer):
  def get_completions(
      self,
      document: Document,
      complete_event: CompleteEvent) -> Iterable[Completion]:

    text = document.text.lstrip()
    text_parts = text.split(' ')
    keys = []

    for idx, part in enumerate(text_parts):

      relevant_commands = commands

      # for every key we already know, set our 'commands' depth appropriately
      for jdx in range(idx):

        # only traverse lower if we have a key for text_part idx
        if len(keys) > jdx and len(keys[jdx]) == 1:
          deeper_commands = relevant_commands[keys[jdx][0]]

          # break if deeper_commands is a leaf node
          if deeper_commands.get('param'):
            break

          # otherwise update and continue deeper
          relevant_commands = deeper_commands

      keys.append([k for k in relevant_commands.keys() if part in k])

    for k in keys[-1]:
      if k in text_parts:
        continue
      replace_word = document.get_word_before_cursor()
      yield Completion(k + ' ', start_position=-len(replace_word))    

az_completer = ThreadedCompleter(_AzCompleter())
