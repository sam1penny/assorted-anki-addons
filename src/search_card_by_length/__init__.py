from aqt import gui_hooks


def customSearch(context):
    if context.card_ids is not None:
        return

    if context.search.startswith("\"min:"):
        n = int(context.search.split("min:")[1].split(" ")[0][:-1])
        context.search = '"front:' + "_" * n + '*"'
    elif context.search.startswith("\"len:"):
        n = int(context.search.split("len:")[1].split(" ")[0][:-1])
        context.search = '"front:' + "_" * n + '"'
    elif context.search.startswith("\"max:"):
        n = context.search.split("max:")[1].split(" ")[0][:-1]
        context.search = '\"front:re:^.{{1, {}}}$\"'.format(n)


gui_hooks.browser_will_search.append(customSearch)
