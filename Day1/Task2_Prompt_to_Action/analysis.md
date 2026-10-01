# Day 1 Assessment
## From Prompt to Action: Understanding LLMs, Tools, and Agents

## 1. Scenario

My chosen scenario is a private college course-fee assistant. The application contains private fee data for three courses: CS101 costs Rs. 12,000, AI202 costs Rs. 18,000, and DS303 costs Rs. 15,000. This information is stored inside the Python application and is not directly provided to the language model.

I compared a plain LLM prompt with the same LLM when it was given access to one external tool called `get_course_fee`.

## 2. What is a Large Language Model?

A Large Language Model generates responses based on patterns learned during training and the information included in the current conversation. It can answer many general questions directly from its knowledge. For example, when I asked "What is 2 + 2?", it could answer without any external tool.

However, the private course-fee data is not part of the model's available information in this experiment. Therefore, when I asked for the AI202 fee without providing the tool, the model could not reliably retrieve the actual private value. The observed answer was:

[WRITE YOUR ACTUAL PLAIN LLM AI202 ANSWER HERE]

This demonstrates that an LLM may answer confidently even when it does not actually have access to the private information.

## 3. What is an Agent?

An agent is an LLM-based system that can use additional capabilities such as tools. Instead of only generating a response, the agent can determine that an external operation is needed, request a tool call, receive the result, and then use that result to produce its final answer.

In this experiment, the plain LLM had no access to the private course data. The tool-enabled version could call `get_course_fee` when the question required the private fee.

## 4. What is a Tool?

A tool is a function that allows the model to obtain information or perform an operation outside the model's normal response generation.

My tool is:

`get_course_fee(course_code)`

The tool schema tells the model the tool's name, what the tool does, and what parameter it expects. The model uses this description to decide when the tool is relevant and what argument it should send.

## 5. What is a Tool Call?

A tool call is the model's request for the application to execute a particular tool with specific arguments.

For the question "What is the fee for AI202?", the tool call was:

`get_course_fee({"course_code": "AI202"})`

The Python program executed the function and returned:

`18000`

The model then used that result to generate the final answer.

## 6. One Tool Call Flow

The process starts with the user's question:

"What is the fee for AI202?"

The LLM receives the question and determines that the private course fee is required. It selects the `get_course_fee` tool and supplies `AI202` as the course code.

The Python program executes the function and returns `18000`. That result is added to the conversation as a tool result. The LLM then receives the tool result and produces the final answer.

The final answer was:

[WRITE YOUR ACTUAL TOOL-ENABLED ANSWER HERE]

## 7. Why Should a Tool Return Text Instead of Raising an Error?

A tool should return an error message as text so the agent can observe the failure and decide what to do next. If the tool raises an exception that stops the entire program, the agent loses the opportunity to handle the problem gracefully.

For example, if the user asks for an unknown course, the tool returns:

`Unknown course code: XXX`

The model can then explain that the course is not available instead of the whole program crashing.

## 8. Comparison Table

| Basis for comparison | Plain LLM prompt (no tool) | LLM with one tool |
|---|---|---|
| Source of the answer | Model's own knowledge and prompt | Model plus tool result |
| Can it fetch or compute information outside its own memory? | No | Yes, through the available tool |
| Reliability on factual or numeric questions | Lower when private information is required | Higher for the information supplied by the tool |
| Transparency | Only the final response is visible | Tool call and tool result can be observed |
| Speed / cost | Usually faster because there is one model response | Slightly more work because a tool call and follow-up response are needed |

## 9. Observation

I tested three questions.

For the AI202 fee question, the plain LLM did not have access to the private fee table. My observed plain LLM response was:

[WRITE ACTUAL RESULT]

The tool-enabled system called `get_course_fee` and received the correct private value of Rs. 18,000. It then used the returned value in its final answer.

For the arithmetic question "What is 2 + 2?", both systems were able to answer without the external tool. No tool call was needed.

For the welcome-message question, both systems could generate a response directly. Again, no tool call was required.

These observations show that the tool is useful when the question depends on information that the model cannot reliably obtain from its own knowledge, while ordinary conversational questions can still be answered directly.

## 10. Suitability

The plain LLM is sufficient for general questions and simple requests where the required information is already available to the model. In this scenario, it was adequate for the arithmetic and welcome-message questions.

The external tool became necessary for the private course-fee question because the exact fee was stored in application data rather than being supplied to the model.

Therefore, a tool-enabled LLM is more appropriate when a problem depends on private, current, or externally stored information that the model cannot reliably provide from memory alone.

## 11. Conclusion

A plain LLM prompt is suitable when the problem can be answered using the information already available to the model and no external operation is required. A tool becomes necessary when the application needs the model to access private data, retrieve external information, perform an operation, or interact with another system.

This experiment demonstrates that adding even one carefully described tool changes the model from a system that only generates text into a system that can recognize when outside help is required, call a function, use the returned result, and then produce a more grounded answer.