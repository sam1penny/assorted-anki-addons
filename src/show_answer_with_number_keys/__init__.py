from aqt.reviewer import Reviewer
from anki.hooks import wrap


# function of the shorcut should be different depending on the state of the previewer
def shortcutFunction(self, response: int) -> None:
    if self.state == "question":
        self._getTypedAnswer()
    elif self.state == "answer":
        self._answerCard(response)


def setUpShortcuts(self, _old):
    cuts = _old(self)

    # change the function called by each shorcut
    for i, shortcut in enumerate(cuts):
        if shortcut[0] == "1":
            cuts[i] = ("1", lambda: self.shortcutFunction(1))
        elif shortcut[0] == "2":
            cuts[i] = ("2", lambda: self.shortcutFunction(2))
        elif shortcut[0] == "3":
            cuts[i] = ("3", lambda: self.shortcutFunction(3))
        elif shortcut[0] == "4":
            cuts[i] = ("4", lambda: self.shortcutFunction(4))

    return cuts


Reviewer.shortcutFunction = shortcutFunction
Reviewer._shortcutKeys = wrap(
    Reviewer._shortcutKeys, setUpShortcuts, "around")
