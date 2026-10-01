# Day 4 — Model Memory, Quantization and Licensing

## 1. Memory Formula

The lab uses the following approximate formula:

weights (GB) = parameters in billions × bytes per parameter

KV cache (GB) = parameters in billions × context in K tokens × 0.02

total (GB) = (weights + KV cache) × 1.10

These values are estimates intended to decide whether a model is likely to fit rather than predict exact runtime memory.

## 2. Hand Estimates

| Model | Precision | Weights | KV | Total |
|---|---|---:|---:|---:|
| 1.5B | Q4_K_M | 0.85 | 0.24 | 1.20 |
| 8B | Q4_K_M | 4.56 | 1.28 | 6.42 |
| 8B | FP16 | 16.00 | 1.28 | 19.01 |
| 30B | Q4_K_M | 17.10 | 4.80 | 24.09 |
| 70B | Q4_K_M | 39.90 | 11.20 | 56.21 |

## 3. Context Length

Increasing context length does not change the model weights, but it increases the KV cache. Therefore total memory increases as more tokens must be kept available. This is important for agent systems because tool results and previous conversation messages contribute to the context.

## 4. Quantization

For an 8B model at 8K context, Q3_K_M, Q4_K_M and Q5_K_M require progressively more memory, while Q8_0 and FP16 require substantially more memory. Lower-bit quantization reduces memory requirements at the cost of some model fidelity.

## 5. My Machine

Available memory: [YOUR ACTUAL VALUE]

Model I considered: [YOUR MODEL]

Precision: [YOUR PRECISION]

Context: [YOUR CONTEXT]

Estimated total: [YOUR TOTAL]

Fits: [Y/N]

## 6. Estimate vs Reality

| Model | Ollama list | Ollama ps | Estimate |
|---|---|---|---|
| [MODEL] | [VALUE] | [VALUE] | [VALUE] |
| [MODEL] | [VALUE] | [VALUE] | [VALUE] |

The differences can occur because the estimate assumes a particular context size and KV-cache behavior, while the runtime may use a different context, architecture, memory reservation or loading strategy.

## 7. Four-Model Comparison

| Field | Qwen3-8B | Mistral-7B-Instruct-v0.3 | Granite 4.0 3B | gpt-oss 20B |
|---|---|---|---|---|
| Publisher | Qwen | Mistral AI | IBM | OpenAI |
| Size | 8.2B | 7B | 3B | 20.9B |
| Context | 32K native | 32K | 128K | 128K |
| Licence | Apache-2.0 | Apache-2.0 | Apache 2.0 | Apache 2.0 |
| Commercial use | Check licence terms | Check licence terms | Check licence terms | Check licence and usage policy |
| Tool calling | Yes | Yes | Yes | Yes |
| Ollama available | Yes | Yes | Yes | Yes |

## 8. Recommendations

### 8 GB laptop

[Write your chosen model, quantization, estimated memory and reason.]

### 24 GB GPU server

[Write your chosen model, quantization, context and concurrency reason.]

### Public capstone

[Write your chosen model, licence and distribution reason.]

## 9. Discussion

### Why can the same model stop fitting?

The model weights remain fixed, but KV-cache memory grows with context length. Runtime overhead and memory allocation can also increase the actual memory used.

### Q4 14B vs Q8 8B

I would test both on the target task and hardware. The comparison should include actual memory use, speed, context length, output quality and task performance instead of relying only on parameter count.

### Why can the estimate differ from ollama ps?

Possible reasons include a different context size, architecture-specific KV-cache behavior, runtime memory reservation, and implementation differences.

### Does an open model with restricted licensing become useless?

No. It may still be usable for non-commercial experiments or other uses permitted by its licence. The exact allowed use must be checked against the licence terms.

### What is lost when using a cloud model?

The main trade-offs include dependence on an external service and the need to send prompts or data to the provider rather than keeping inference fully local.

## 10. Conclusion

The experiments demonstrate that model size alone does not determine whether a model will run. Quantization reduces weight memory, while context length increases KV-cache memory. Runtime behavior can differ from simple estimates, so actual measurements are useful. Licence and tool-calling information also matter when selecting a model for an application.