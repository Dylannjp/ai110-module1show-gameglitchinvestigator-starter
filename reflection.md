# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  2. You can't actually restart, I just reloaded the page. It should've just restarted the game when I clicked new game.
  3. Difficulties are messed up.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Claude.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - fixing the bugs around the code, there's plenty of easy ones so it found them easily. like the check guess giving the wrong hint.
  - also helped point the logic_utils.py by making conftest.py, that was pretty cool.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - none, maybe with a more complicated question it would get it wrong.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - testing it.
- Describe at least one test you ran (manual or using pytest) 
  and what it showed you about your code.
  - the higher/lower logic got fixed, by playing the game.
- Did AI help you design or understand any tests? How?
  - yeah, just ask away and it'll do so. with knowledge on what it should look like, its easy to confirm correctness

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  - because secret rerolls whenever you press submit and streamlit reruns the code.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - the page reruns after each interaction, so stuff might change if you don't code it specifically to persist in between interactions.
- What change did you make that finally gave the game a stable secret number?
  - by using session_state.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    - Just prompt it more on everything, ask for suggestions.
- What is one thing you would do differently next time you work with AI on a coding task?
  - not much, be aware and don't let it do all the work for you is all.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - not much, just reinforces ideas i already had.
