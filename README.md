# i suck at wordle

I have a complete inability to make 5 letter words apparently. I wrote this because I suck at it.

The `guess` list variable contain your "guess" (e.g. yellow characters). Any missing letters can have a `#` added to it.

I haven't made this work for green characters, so I assume they're all yellow for now.
If I get frustrated on another day I may make a green letter compatible version.

The "cheating" part comes because I use a spellchecker at the end. You could (read: should) not and just read the output dictionary for every permutation if you don't want to cheat. I don't really recommend not cheating with the output though.

run with `python wordle.py`. 
for the day I wrote this, the output looks like this:
```
{'ricki', 'crike', 'prick', 'frick', 'trick', 'ricky', 'brick', 'ricks', 'crick'}
```

Needs the [pyspellchecker](https://pyspellchecker.readthedocs.io/en/latest/) library.

