import spacy

nlp = spacy.load("en_core_web_sm")

def analyze_sentence(text):
    doc = nlp(text)
    return [
        {
            "text": token.text,
            "lemma": token.lemma_,
            "pos": token.pos_,
            "value": token.tag_
        }
        for token in doc
    ]

def main():
    text = input("Introduza o seu texto: ")
    result = analyze_sentence(text)
    print("Este é o seu resultado:")
    for token_info in result:
        print(f"Text: {token_info['text']}, Lemma: {token_info['lemma']}, POS: {token_info['pos']}, Value: {token_info['value']}")

if __name__ == "__main__":
    main()
