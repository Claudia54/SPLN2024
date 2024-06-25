import spacy
import sys
from collections import Counter

nlp = spacy.load("pt_core_news_lg")


with open(sys.argv[1], encoding="utf-8") as file:
    text = file.read()


doc = nlp(text)

pairs_counter = Counter()


for sentence in doc.sents:
    proper_nouns = [token.text for token in sentence if token.pos_ == "PROPN"]
    
    if len(proper_nouns) > 2:
        pair = tuple(sorted(proper_nouns[:2]))
        pairs_counter.update([pair])

most_common_pairs = pairs_counter.most_common(10)  

print("Most common pairs of proper nouns:")
for pair, frequency in most_common_pairs:
    print(f"{pair[0]}_{pair[1]} - {frequency}")
