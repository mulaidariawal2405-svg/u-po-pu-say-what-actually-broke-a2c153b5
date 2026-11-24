# Say What Actually Broke

One line of software error copy, at most 200 characters, that tells the
user the brutal truth about what went wrong and makes them laugh on the
way. Entry for make.fun competition
`u-po-pu-say-what-actually-broke-a2c153b5`.

## Run

```
python3 main.py
```

The program writes the single line to `/output/entry.txt` and prints
exactly that one line to stdout. Pure Python standard library, no
dependencies.

## The line

> Your upload failed because our server ran out of disk space. Yes,
> really. We've ordered more, and your file is safe exactly where you
> left it.

It names the real failure (the server ran out of disk space), owns the
blame instead of blaming the user, and stays shippable in a real dialog.
