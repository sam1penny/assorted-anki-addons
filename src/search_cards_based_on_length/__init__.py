import aqt
from aqt import gui_hooks
from aqt import mw
from typing import List
import anki


def createSearchString(stype: str, n: int) -> str:
    fields: List[str] = config["fields"]
    s = ''
    for i, fld in enumerate(fields):
        if stype == "min":
            s += '{}:{}*'.format(fld, "_" * n)
        elif stype == "len":
            s += '{}:{}'.format(fld, "_" * n)
        elif stype == "max":
            s += '"{}:re:^.{{1, {}}}$"'.format(fld, n)
        if i != len(fields)-1:
            s += ' OR '
    return s


def modifySearchStringIfNecessary(context: aqt.browser.SearchContext) -> None:
    if context.search.startswith("min:"):
        n = int(context.search.split("min:")[1].split(" ")[0])
        context.search = createSearchString("min", n)

    elif context.search.startswith("len:"):
        n = int(context.search.split("len:")[1].split(" ")[0])
        context.search = createSearchString("len", n)

    elif context.search.startswith("max:"):
        n = context.search.split("max:")[1].split(" ")[0]
        context.search = createSearchString("max", n)


if anki.version >= "2.1.45":
    def customSearch(context: aqt.browser.SearchContext) -> None:
        if context.ids is not None:
            return

        modifySearchStringIfNecessary(context)

else:
    def customSearch(context: aqt.browser.SearchContext) -> None:
        if context.card_ids is not None:
            return

        modifySearchStringIfNecessary(context)


config = mw.addonManager.getConfig(__name__)

gui_hooks.browser_will_search.append(customSearch)