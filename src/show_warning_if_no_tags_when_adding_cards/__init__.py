from aqt import gui_hooks


def might_reject_empty_tag(optional_problems, note):
    if not any(note.tags):
        optional_problems.append("Add cards without tags?")


gui_hooks.add_cards_might_add_note.append(might_reject_empty_tag)