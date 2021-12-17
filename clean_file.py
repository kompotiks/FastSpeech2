import re

with open('words.csv', 'r', encoding='utf-8') as f:
    corpus = [i for i in f.read().split('\n')]


clean_corpus = []
for i in corpus:
    clean_corpus.append(re.sub('[!(),–\-.:;?"…»«„“”’ */1269<>́‑]', '', i).lower())

with open('text.txt', 'w', encoding='utf-8') as f:
    [f.write(i + '\n') for i in clean_corpus]
