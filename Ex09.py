frase = "um dois dois três três três"
palavras = frase.split()
contagens = {p: palavras.count(p) for p in set(palavras)}
print(contagens)