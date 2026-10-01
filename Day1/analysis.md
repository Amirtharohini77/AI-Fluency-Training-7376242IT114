# Day 1 Assessment
## Comparing a Plain Chatbot, a Rule-Based Workflow, and an AI Agent

## 1. Scenario

The scenario chosen for this assessment is a private college canteen price assistant. The application contains private canteen price data that is not directly provided to the public language model. The three items used in the scenario are IDLI priced at Rs. 40, BIRYANI priced at Rs. 120, and JUICE priced at Rs. 50.

The same set of questions was given to a plain chatbot, a rule-based workflow, and an AI agent. The questions were about the price of BIRYANI, the discounted total of IDLI and BIRYANI, the price difference between JUICE and IDLI, and a short non-data-related message. An additional challenge question asked which two items could be purchased within a budget of Rs. 150.

## 2. Plain Chatbot

The plain chatbot uses the LLM directly without giving it access to the private canteen price dictionary and without providing any external tools. It receives the user's question and sends it to the language model, which generates a response based on its existing knowledge and the wording of the question.

Because the private canteen prices are not included in the prompt or connected through a tool, the chatbot cannot reliably retrieve the actual prices stored inside the Python program. For Questions 1 to 3, this can result in incorrect or uncertain numerical answers. This demonstrates a limitation of using an LLM alone when the answer depends on private application data. For the fourth question, which does not require private data, the chatbot can generate a suitable response directly.

The main advantage of the chatbot is simplicity. It is easy to implement and can handle open-ended language naturally. Its limitation in this scenario is its lack of direct access to the private canteen data and the possibility of generating confident but incorrect answers.

## 3. Rule-Based Workflow

The rule-based workflow does not use an LLM. Instead, it uses Python code containing predefined rules. The program identifies known canteen items in the question, retrieves their prices from the private dictionary, and applies predefined calculations when the required wording matches one of the implemented rules.

For example, the workflow can correctly retrieve the price of BIRYANI and calculate the discounted total of IDLI and BIRYANI. However, it only supports the situations and patterns that the programmer explicitly implemented. It cannot flexibly understand every possible way a student may ask the question. The budget challenge is outside the predefined rules, so the workflow may return that it does not have a rule for the request.

The workflow is predictable and deterministic for the cases covered by its rules. Its main weakness is rigidity.

## 4. AI Agent

The AI agent combines an LLM, tools, and a loop. The LLM interprets the user's request and decides whether a tool is required. The available tools are a private-data lookup tool and a calculator tool. The Python program executes the selected tool, returns the result to the LLM, and allows the model to continue until it can produce a final response.

For example, for the discounted total question, the agent can call the price lookup tool for IDLI, call the price lookup tool for BIRYANI, and then use the calculator to calculate the discounted total. For the price comparison question, it can retrieve both prices and calculate the difference. For the fourth question, no tool is required because the request does not depend on private data.

The agent is more flexible than the fixed workflow because it can decide which tools are needed based on the user's request. However, its behavior depends on the language model's tool selection and therefore requires safeguards such as a maximum number of steps and careful tool definitions.

## 5. Comparison Table

| Basis for comparison | Plain chatbot | Rule-based workflow | AI agent |
|---|---|---|---|
| Flexibility | High for natural-language conversation, but limited by available knowledge | Low because rules are predefined | High because the LLM can select actions dynamically |
| Decision-making | Generates a response but does not use external tools | Follows fixed programmer-written conditions | LLM decides which tool to use and when |
| Tool usage | No tools | No external LLM tools | Uses private-data lookup and calculator tools |
| Private-data access | No direct access | Yes, through Python variables | Yes, through tools |
| Multi-step task handling | Limited | Limited to predefined steps | Can perform multiple tool calls in a loop |
| Automation | Basic question-answering | Strong for repetitive fixed cases | Strong for flexible multi-step tasks |
| Reliability | Can produce unsupported or incorrect answers for private data | Predictable for implemented rules | Can produce correct tool-based answers, but tool selection can vary |

## 6. Suitability Analysis

For this scenario, the AI agent is the most suitable when the requirement includes natural-language questions, private-data retrieval, calculations, and new combinations of requests. It can use the private price tool and calculator tool as required instead of depending only on information stored in the language model.

The rule-based workflow is suitable when the canteen only needs a small set of fixed operations such as looking up a known item price and calculating a standard discount. Its predictable behavior can be valuable when the allowed questions are tightly controlled.

The plain chatbot is suitable for general conversation and tasks that do not depend on the private canteen database. It is less suitable for exact price queries because the necessary private information is not automatically available to the LLM.

## 7. Conclusion

A plain chatbot is most appropriate when the main requirement is natural-language conversation and the task does not depend on private application data or external actions. A rule-based workflow is appropriate when the required operations are known in advance and predictable, repeatable behavior is important. An AI agent is appropriate when the task requires flexible decision-making, private-data access through tools, multiple steps, and the ability to choose actions based on the user's request.

The comparison shows that the three approaches solve problems differently. The chatbot mainly generates responses using an LLM, the workflow follows predefined rules and conditions, and the agent combines an LLM, tools, and a loop to interpret the task, perform actions, observe the results, and continue until the task is completed.