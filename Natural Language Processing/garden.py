# Import the spaCy library
import spacy 

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Define a list of sentences to be processed
gardenpathSentences = [
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi.",
    "The horse raced past the barn fell.",
    "The old man the boat."
]

# Tokenize each sentence and store the tokens in a list
tokenized_sentences = []

# Loop through each sentence in the list
for sentence in gardenpathSentences:
    # Process the sentence using spaCy's NLP pipeline
    doc = nlp(sentence)
    
    # Extract the text of each token and store in the list
    tokens = [token.text for token in doc]
    tokenized_sentences.append(tokens)

# Print the tokenized sentences
for i, tokens in enumerate(tokenized_sentences, 1):
    print(f"Tokens for sentence {i}: {tokens}")

# Perform Named Entity Recognition (NER) on each sentence
ner_results = []

# Loop through each sentence in the list
for sentence in gardenpathSentences:
    # Process the sentence using spaCy's NLP pipeline
    doc = nlp(sentence)
    
    # Extract named entities (text and label) and store in a list
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    ner_results.append(entities)

# Print the named entities for each sentence
for i, entities in enumerate(ner_results, 1):
    print(f"Named entities for sentence {i}: {entities}")

# Print named entities with explanations for each sentence
for i, entities in enumerate(ner_results, 1):
    print(f"Named entities for sentence {i}: {entities}")
    for entity, label in entities:
        # Look up and print the explanation for the entity label
        explanation = spacy.explain(label)
        print(f"   - {entity}: {label} ({explanation})")
print('''
 Jill is an entity, with explaination stating it could be a real or fictious.
 Missisipy is an entity, with explaination stating it could be a country city or state 
''')
