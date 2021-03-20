from aqt import gui_hooks
from aqt import mw


def createSearch(stype, n):
    fields = config["fields"]
    s = ''
    for i, fld in enumerate(fields):
        if stype == "min":
            s += '"{}:{}*"'.format(fld, "_" * n)
        elif stype == "len":
            s += '"{}:{}"'.format(fld, "_" * n)
        elif stype == "max":
            s += '\"{}:re:^.{{1, {}}}$\"'.format(fld, n)
        if i != len(fields)-1:
            s += ' OR '

    return s


def customSearch(context):
    if context.card_ids is not None:
        return

    if context.search.startswith("\"min:"):
        n = int(context.search.split("min:")[1].split(" ")[0][:-1])
        context.search = createSearch("min", n)

    elif context.search.startswith("\"len:"):
        n = int(context.search.split("len:")[1].split(" ")[0][:-1])
        context.search = createSearch("len", n)

    elif context.search.startswith("\"max:"):
        n = context.search.split("max:")[1].split(" ")[0][:-1]
        context.search = createSearch("max", n)


config = mw.addonManager.getConfig(__name__)

gui_hooks.browser_will_search.append(customSearch)
