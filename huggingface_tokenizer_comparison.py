
# Tokenizer Comparison Script using Hugging Face

from transformers import GPT2TokenizerFast, BertTokenizerFast, RobertaTokenizerFast
import time

# Sample text
text = """Tokenization plays a critical role in preparing text data for large language models. The choice of tokenizer impacts both performance and accuracy."""

# Load different tokenizers
gpt2_tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
bert_tokenizer = BertTokenizerFast.from_pretrained("bert-base-uncased")
roberta_tokenizer = RobertaTokenizerFast.from_pretrained("roberta-base")

# Tokenizer list for comparison
tokenizers = [
    ("GPT-2 (BPE)", gpt2_tokenizer),
    ("BERT (WordPiece)", bert_tokenizer),
    ("RoBERTa (BPE)", roberta_tokenizer)
]

# Compare performance
print("Tokenizer Comparison:\n")
for name, tokenizer in tokenizers:
    start_time = time.time()
    tokens = tokenizer.tokenize(text)
    encoding_time = time.time() - start_time
    print(f"Tokenizer: {name}")
    print(f"Number of tokens: {len(tokens)}")
    print(f"Tokens: {tokens[:10]}...")
    print(f"Encoding time: {encoding_time:.6f} seconds\n")
