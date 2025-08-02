from typing import Iterable
import time
from prompt_toolkit.completion import (
  Completion,
  CompleteEvent,
  Completer,
  ThreadedCompleter
)
from prompt_toolkit.document import Document
import sys

commands = ['c1', 'c2', 'c3']

class _AbcCompleter(Completer):
  def get_completions( self, document: Document, complete_event: CompleteEvent) \
      -> Iterable[Completion]:
    print(f'{repr(document.text.split(' '))}', file=sys.stderr)
    for c in commands:
      # cha = document.text[-1]
      # ordinal = ord(cha)+1
      # cha = chr(ordinal) if ordinal < 123 else chr(65)
      time.sleep(0.5)
      yield Completion(c, start_position=0)
    # newcha = str(int(cha))
    # print(repr(complete_event))


abc_completer = ThreadedCompleter(_AbcCompleter())