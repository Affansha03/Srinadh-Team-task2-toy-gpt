
# ✍️ Blog Post: Building a Toy GPT from Scratch — Tokenization to Text Generation

## 🔍 Introduction

Large Language Models (LLMs) like GPT have revolutionized the way we interact with machines through natural language. But how do they work under the hood?

In this blog post, I’ll walk you through:
- The **fundamentals of tokenization** (how text becomes data)
- The **architecture of GPT**
- A **toy GPT model implemented from scratch** in PyTorch
- Generating text from scratch

---

## 🧩 Part 1: Understanding Tokenization

Tokenization is the process of converting text into tokens — the basic units of meaning a model can process.

### 🔹 Byte Pair Encoding (BPE)
- Merges frequent character pairs into subwords
- Example: `low`, `lowest` → `low`, `est`

### 🔹 WordPiece (used in BERT)
- Probabilistically merges subword units
- Example: `unhappiness` → `un`, `##happy`, `##ness`

### 🔹 SentencePiece
- Language-agnostic tokenizer that works directly on raw text
- Great for non-space-separated languages like Chinese or Japanese

> 📌 Tokenization decides how efficiently your model learns and generalizes.

---

## 🧠 Part 2: Inside GPT Architecture

GPT uses **decoder-only Transformer blocks** and is trained in a **causal (left-to-right) way**.

### 🏗 Architecture Components
- **Token Embedding**: Turns tokens into dense vectors
- **Positional Encoding**: Adds order awareness
- **Masked Multi-Head Attention**: Prevents tokens from "seeing the future"
- **Feedforward Network**: Learns nonlinear transformations
- **Output Layer**: Predicts the next token

![Transformer Architecture](https://jalammar.github.io/images/gpt2/gpt2-large-transformer-block.png)

---

## 💻 Part 3: Code – Building a Tiny GPT in PyTorch

Below is a minimal GPT model trained on a short text (`"To be or not to be."`):

```python
# Initialize and train model
model = TinyGPT(vocab_size=vocab_size, n_embed=16)
x, y = get_batch()
logits, loss = model(x, y)
```

### 🔮 Text Generation Example
```python
generated = model.generate(torch.tensor([[stoi['T']]]), max_new_tokens=20)
print(decode(generated[0].tolist()))
```

> Output Example:
```
Generated text: To be or nor bo ot to
```

---

## 🧪 Key Learnings

- **Tokenization** is critical for vocabulary size and model efficiency.
- Even a **tiny GPT model** can learn basic patterns in text.
- Training from scratch helps us appreciate how powerful even small models can be.

---

## 🎯 Conclusion

While production LLMs involve billions of parameters and massive datasets, understanding and building a **toy GPT** demystifies the architecture and training loop.

✅ **Next Steps**:
- Train on longer datasets (like Tiny Shakespeare)
- Add layers, attention heads
- Experiment with sampling techniques (top-k, nucleus)

---

## 📹 Coming Soon: Video Walkthrough

I'll share a screen recording walking through:
1. The tokenization logic
2. Model building in PyTorch
3. Generating custom text samples
