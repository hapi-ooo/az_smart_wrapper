from prompt_toolkit.key_binding import KeyBindings

bindings = KeyBindings()

@bindings.add("tab")
def _(event):
    buff = event.app.current_buffer
    complete_state = buff.complete_state

    if complete_state:
        completion = complete_state.current_completion

        # If no completion is selected yet, select the first one
        if completion is None and complete_state.completions:
            completion = complete_state.completions[0]

        if completion:
            buff.apply_completion(completion)
        else:
            # fallback: move to next completion or ignore
            event.app.output.bell()
    else:
        buff.start_completion(select_first=True)
