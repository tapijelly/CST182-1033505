translate = {
  "hello": "hallo",
  "thanks": "danke",
  "no": "nein",
  "yes": "ja",
  "delicious": "lecker",
  "week": "woche",
  "today": "heute",
  "tomorrow": "morgen",
  "yesterday": "gestern",
  "do": "machen",
  "go": "gehen",
  "come": "kommen",
  "laugh": "lachen",
  "gut": "good",
  "beautiful": "schön",
  "coffee": "kaffee",
  "beer": "bier",
  "tea": "tee",
  "wine": "wein",
  "water": "wasser",
  "lamb": "lamm",
  "fish": "fisch",
  "nice": "nett",
  "clean": "sauber",
  "fine": "fein",
  "dear": "lieb",
  "love": "liebe",
  "funny": "komisch",
  "great": "klasse",
  "high": "hoch",
  "fantastic": "prima",
  "strong": "stark",
  "long": "lang",
  "bright": "hell",
  "capable": "fähig",
  "short": "kurz",
  "small": "klein",
  "big": "groß",
  "wonderful": "wunderbar",
  "rat": "ratte",
  "dark": "dunkel",
  "bye": "tschüss"
}

s = input("Enter String: ")

# TODO: Enter your solution below

german = " "
word = " "

for char in s:
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'): 
        word += char
    else:
        if word:  
            german += translate[word.lower()] if word.lower() in translate else word
            word = ""  
        german += char  

if word:
    german += translate[word.lower()] if word.lower() in translate else word

print(german)
    

