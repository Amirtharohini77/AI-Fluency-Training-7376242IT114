# Day 2 Assessment
## Reasoning and Acting: Direct Prompting, Chain-of-Thought and ReAct

## 1. Scenario

My chosen scenario is a college library assistant. The application contains library availability information for books AI202, PY101 and DB201. This information is available to the ReAct agent through a tool but is not directly provided to the language model during direct prompting or Chain-of-Thought prompting.

The main tool-based question asks how many AI202 copies are available and how many students cannot borrow the book when five students request it. The reasoning questions involve time calculation, counting student sittings and ordering people by the number of pages they read.

## 2. Direct Prompting

Direct prompting sends the user's question directly to the language model and asks for an immediate answer. No tool is available and there is no visible step-by-step reasoning.

For reasoning-only questions, the model can answer directly using the information contained in the question. However, for the library availability question, the exact number of copies cannot be reliably retrieved because the private library data is not provided to the model.

In this scenario, direct prompting is simple and fast, but it is not suitable for questions that require unavailable external information.

## 3. Chain-of-Thought

Chain-of-Thought prompting asks the model to solve the question step by step before producing the final answer. This gives the model more opportunity to perform intermediate calculations and organize its reasoning.

For the time, counting and ordering questions, the step-by-step prompt can make multi-step reasoning clearer and may improve accuracy. However, Chain-of-Thought does not provide access to the library database. Therefore, it cannot reliably answer the AI202 availability question when the necessary fact is not supplied.

## 4. ReAct Agent

The ReAct agent combines an LLM with tools and a loop. It first interprets the question, decides whether a tool is necessary, calls the appropriate tool, observes the returned result and continues until it can answer.

For the AI202 question, the agent can call the get_book_copies tool and retrieve the actual number of available copies. It can then use the calculator tool to determine how many students cannot borrow the book.

For questions that do not require library information, the agent can answer without calling a tool.

## 5. Comparison Table

| Basis | Direct prompting | Chain-of-Thought | ReAct agent |
|---|---|---|---|
| Reasoning depth | Low / immediate | Higher because intermediate steps are requested | High because reasoning and actions are interleaved |
| Tool usage | None | None | Uses library lookup and calculator tools |
| Reliability on multi-step questions | Depends on the model | Can improve on multi-step reasoning | Can use tools plus reasoning |
| Transparency | Final answer only | More explanation of steps | Tool calls and observations are visible |
| Speed / cost | Usually fastest | Longer response | Usually slower because of tool calls |
| Consistency | Depends on temperature and model | Can vary across reasoning paths | Tool-based results are grounded, but model decisions can vary |

## 6. Self-Consistency Observation

I ran the same Chain-of-Thought question five times with a non-zero temperature. The answers were:

1. [actual answer]
2. [actual answer]
3. [actual answer]
4. [actual answer]
5. [actual answer]

The majority answer was [actual majority answer], appearing [number] times.

I then changed the temperature to 0. The responses became [actual observation].

This experiment showed that non-zero temperature can produce different reasoning paths, while temperature 0 makes the responses much more consistent.

## 7. Suitability Analysis

For my scenario, the ReAct approach is suitable when the request requires access to current or private library information together with reasoning or calculations. Direct prompting is useful for simple questions that do not require external information. Chain-of-Thought is useful for reasoning-only problems where the required facts are already present in the question.

The ReAct approach has the additional ability to obtain information through tools and then use the returned information in subsequent reasoning steps. Its disadvantage is that it requires more processing and depends on correct tool selection.

## 8. Conclusion

Direct prompting is appropriate for simple questions where the model already has the required information and a fast answer is sufficient. Chain-of-Thought is useful for multi-step reasoning problems where all required information is already available in the prompt. ReAct is appropriate when a problem combines reasoning with external information retrieval, calculations or other actions.

The experiment demonstrates that reasoning alone cannot supply missing facts. Tools provide the missing connection to external information, while the ReAct loop allows the model to reason, act, observe results and continue until the task is completed.