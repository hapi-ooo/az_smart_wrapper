from typing import Iterable
import time
from prompt_toolkit.completion import (
  Completion,
  CompleteEvent,
  Completer,
  ThreadedCompleter
)
from prompt_toolkit.document import Document
from .commands import commands
# import sys

class _AbcCompleter(Completer):
  def get_completions( self, document: Document, complete_event: CompleteEvent) \
      -> Iterable[Completion]:
    text = document.text.lstrip()
    text_parts = text.split(' ')
    for c, sc in commands.items():
      # NETWORK MOCK
      time.sleep(0.2)
      if c.__contains__(text_parts[0].strip()) and len(text_parts) < 2 and c != text_parts[0].strip():
        replace_word = document.get_word_before_cursor()
        yield Completion(c + ' ', start_position=-len(replace_word))
      elif len(text_parts) > 1:
        for scc in sc:
          if not text_parts[1] or scc.__contains__(text_parts[1].strip()):
            replace_word = document.get_word_before_cursor()
            yield Completion(scc + ' ', start_position=-len(replace_word))


abc_completer = ThreadedCompleter(_AbcCompleter())