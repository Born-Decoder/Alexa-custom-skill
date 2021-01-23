import spacy
nlp = spacy.load('en_core_web_sm')
f = open("D:/Assignment and other works/Docs/out_text.txt","r")
content = f.read()
doc = nlp(content)

candidate_pos = ['NOUN']
sentences = []
for sent in doc.sents:
 selected_words = []
 for token in sent:
  if token.pos_ in candidate_pos and token.is_stop is False:
   selected_words.append(token)
 sentences.append(selected_words)
flat_list = [item for sublist in sentences for item in sublist]
sets = set(str(x) for x in flat_list)
sets = [item.lower() for item in sets]
f= open("D:/Assignment and other works/Docs/doc_keys.txt","r+")
f.write(str(sets))
con=f.read()
