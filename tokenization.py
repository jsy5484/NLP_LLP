class SimpleTokenizer:
   # initialization 
    def __init__(self):
        self.vocab = {}
        self.reverse_vocab = {}

   # build vocab from the input
    def build_vocab(self, texts):
        unique_tokens = set()
        for text in texts:
            unique_tokens.update(text.strip().split())
        self.vocab = {word: idx+2 for idx, word in enumerate(sorted(unique_tokens))}
        self.vocab["<PAD>"] = 0
        self.vocab["<UNK>"] = 1
        self.reverse_vocab = {idx: word for word, idx in self.vocab.items()}
    
    def encode(self, text):
        return [self.vocab.get(word, self.vocab["<UNK>"]) for word in text.strip().split()]
    
    def decode(self, ids):
        return ' '.join([self.reverse_vocab.get(idx, "<UNK>") for idx in ids])
    

    
tokenizer = SimpleTokenizer()
senten = ["hello world", "find the most closest cafe near me", "give me the address"]
tokenizer.build_vocab(senten)

encoded = tokenizer.encode("closest cafe")

print("Encoded:", encoded)  
print("Decoded:", tokenizer.decode(encoded)) 
