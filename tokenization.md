## Explanation for the tokenization algorithm

- Codes in the program demonstrates how the tokenization in LLM algorithm works.

## Description
1.  Input sentences are "hello world", "find the most closest cafe near me", "give me the address"
2.  This sentences are split by words and sorted as follow: ["<PAD>", "<UNK>", "address", "cafe", "closest", "find", "give", "hello", "me", "most", "near", "the", "world"]
3.  Each tokens are number-labeled
4.  "Closest cafe" are encoded based on the number of the tokens. Based on the list above, the encoding will be 3 and 4.


