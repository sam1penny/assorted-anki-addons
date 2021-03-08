from aqt import mw
from aqt.reviewer import Reviewer
from anki.hooks import wrap


def setUpShortcuts(self, _old):
    cuts = _old(self)
    return cuts


Reviewer._shortcutKeys = wrap(
    Reviewer._shortcutKeys, setUpShortcuts, "around")
