# Day 3 Lab
## Building and Guarding a ReAct Agent

## 1. Aim

The aim of this exercise was to build a ReAct agent from scratch in Python using a calculator tool and a web-page/local-file reader. Three failure modes were deliberately triggered and then fixed using safeguards.

## 2. Tools

The first tool was a safe calculator. It evaluates arithmetic expressions without using eval(). The second tool was a webpage reader that can read local HTML/text files and real URLs. The reader removes HTML tags, script content and style content and limits the size of the returned observation.

## 3. Normal Agent

The unguarded agent followed a ReAct loop consisting of reasoning, recording the tool call, acting through Python, observing the result and continuing until a final answer was produced.

For the normal fee question, the agent read notice.html, obtained the fee information, and used the calculator to determine the discounted total.

## 4. Failure 1: Repeating Loop

When the agent was asked to read the nonexistent fees.html file, the reader returned an error message. The model repeatedly requested the same tool call instead of changing its approach. The unguarded agent continued until max_steps was reached.

This showed why repeat detection is needed. A loop can waste LLM calls and time even when the model is not making a new information request.

## 5. Failure 2: Unknown Tool

The system prompt was deliberately changed to mention a nonexistent send_email tool. The model attempted to use the unknown tool. The safe registry lookup using .get() returned an error message instead of crashing.

When the unsafe dictionary lookup TOOL_FUNCTIONS[name] was used, the program crashed with KeyError. This demonstrated why an agent should handle an unknown tool safely.

## 6. Failure 3: Context Overflow

A large HTML page was created and the truncation limit was temporarily increased. The large observation could produce a context-length error, very slow processing, a rate limit, or another long-context problem.

This demonstrated that external content must be bounded before being placed into the model conversation.

## 7. Guards Added

Three guards were added. Repeat detection counts identical tool calls and stops the run when the same call is repeated three times without progress. Observation truncation limits one tool result to 1500 characters. The character budget stops a run when the total amount of content sent to the model becomes too large.

## 8. Observations

### Step Counts

| Question | Steps Used | Tools Called |
|---|---:|---|
| Merit scholarship total | [YOUR RESULT] | [YOUR RESULT] |
| Hostel student total | [YOUR RESULT] | [YOUR RESULT] |
| 15% of AI202 | [YOUR RESULT] | [YOUR RESULT] |
| Welcome message | [YOUR RESULT] | [YOUR RESULT] |

### Failure Log

| Failure | Observation | Cost |
|---|---|---|
| Repeating loop | [YOUR RESULT] | [YOUR RESULT] |
| Unknown tool with .get() | [YOUR RESULT] | [YOUR RESULT] |
| Unknown tool with [] | [YOUR RESULT] | [YOUR RESULT] |
| Context overflow | [YOUR RESULT] | [YOUR RESULT] |

### After Fixes

| Failure | Behaviour | Guard |
|---|---|---|
| Repeating loop | [YOUR RESULT] | Repeat detection |
| Unknown tool | [YOUR RESULT] | Safe registry lookup |
| Context overflow | [YOUR RESULT] | Observation truncation / budget |

## 9. Chosen Limits

| Setting | Value | Justification |
|---|---|---|
| max_steps | 6 | [YOUR JUSTIFICATION] |
| MAX_TOOL_CHARS | 1500 | [YOUR JUSTIFICATION] |
| CHAR_BUDGET | 30000 | [YOUR JUSTIFICATION] |
| Repeat threshold | 3 | [YOUR JUSTIFICATION] |

## 10. Discussion

The repeating loop was primarily a control-flow problem rather than a factual error. The fix belongs in the agent loop because the loop is responsible for deciding when progress has stopped.

An unknown-tool message is safer than a crash because an agent should continue or terminate gracefully when the model requests an unavailable capability.

Truncating tool output protects the model context, although truncation can hide useful information. A production reader could provide paging or search so the agent can request another part of a large document.

The character budget is only an approximation of token or monetary cost, but it provides a practical stopping condition before the conversation becomes too large.

## 11. Conclusion

This exercise showed that a working ReAct loop needs more than an LLM and tools. It also needs safeguards. Repeat detection prevents endless repeated actions, observation truncation limits the size of external information, and a character budget prevents runaway context growth. These guards make an agent more predictable and safer to operate.