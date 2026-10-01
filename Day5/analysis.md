# Day 5 — Serving Models

## 1. Ollama setup

I used Groq in the previous days. Ollama could not be installed
successfully on my Windows machine, so local Ollama runtime measurements
were not collected on this computer.

## 2. Modelfiles

Two Modelfiles were prepared from the same base model. The first uses a
low temperature and a fee-assistant system prompt. The second uses a higher
temperature and an events-announcer system prompt.

## 3. REST API

The api_demo.py program was implemented to demonstrate the /api/tags,
/api/generate, /api/chat, /api/ps and /v1/chat/completions endpoints.
Local execution requires a running Ollama server.

## 4. Benchmarking

bench_models.py compares two local models using identical prompts and
records elapsed time, token count, tokens per second and model load time.

## 5. vLLM

The vLLM section was studied through the provided demonstration or paper
alternative. PagedAttention organizes KV-cache memory in blocks, while
continuous batching allows new requests to enter the batch as earlier
requests finish.

## 6. Observations

[Insert actual screenshots/results here.]

## 7. Conclusion

Day 5 demonstrated the difference between a model client and a model
serving system. Ollama provides local model management and REST interfaces,
while Modelfiles package default behavior without duplicating the model
weights. API streaming affects perceived responsiveness through time to
first token, and vLLM improves serving efficiency through mechanisms such
as PagedAttention and continuous batching.