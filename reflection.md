# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  Attempts allowed displayed in settings is not the same as the one in the game. I expected 8, see both 7 and 8 but in reality there .
  Developer Debug counter for attempts shows 1 attempt completed before even starting. It should say 0.
  Asks to guess number between 1 and 100, I guessed 0 and it said to go lower, guessed 30 said go lower, answer was 25. It should say "go higher" and "go lower" dependsing on if the number submitted is greater or less than the secret number.
  Clicking new game does not clean history or let me resubmit a guess. It should do that.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input    | Expected Behavior    | Actual Behavior                                     | Console Output / Error |
| -------- | -------------------- | --------------------------------------------------- | ---------------------- |
| guess 0  | Output "go higher"   | "go lower"                                          | none                   |
| new game | clear history        | history is not cleared                              | none                   |
| guess 0  | 0 written in history | 0 not written in hisotry, appears after 2nd attempt | none                   |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
