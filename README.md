# Assorted Anki Addons
This repository contains a collection of smaller anki add-ons that I have written.

# Details

### [Show Answer With Number Keys](https://ankiweb.net/shared/info/188886658)
This add-on remaps the number keys (1, 2, 3, 4) to be able to show the answer of a card as well as answering it. A card can then be fully answered by simply double clicking the number key.

### [Search Cards By Length](https://ankiweb.net/shared/info/819294114)
Find cards with a field of a given exact/maximum/minimum length in the browser.

### [Show Warning If No Tags When Adding Cards]()
Based on the add-on from [this reddit post](https://www.reddit.com/r/Anki/comments/coc6wp/comment/ewi7m2m/?utm_source=share&utm_medium=web2x&context=3), ported to use hooks rather than fragile monkey patching. Works on Anki 2.1.55+ using the hook introduced in [this commit](https://github.com/ankitects/anki/commit/56f806146c5ba79377f26f082bfca25dc8417bac)

Currently no listing on ankiweb, so must be manually installed.

# Manual Installation

In a new terminal, clone the repository and use the provided build script:

```
Usage: build.sh [-h] [-a] [-f directory_name]

Available options:
-h                    Print this help message
-a                    Build all of the add-ons
-f directory_name     Build the add-on with the provided directory name
```

Once the add-on is built, open Anki and navigate to `Tools -> Add-ons -> Install from file` and select the newly-built `.ankiaddon` file to install the add-on.

# Other add-ons I have created

### [Countdown to events](https://ankiweb.net/shared/info/1143540799)

### [Rendered Browser](https://ankiweb.net/shared/info/993394845)