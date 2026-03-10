# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start
  (for example: "the secret number kept changing" or "the hints were backwards").

When I first ran the game it seemed to work as expected, but the hints were backwards once I started playing. If I guessed a number that was too high, the game would still tell me to go higher instead of lower, and vice versa. Another bug was that the New Game button did not actually start a new game. After the game ended, clicking it would freeze the screen and the only way to reset was to reload the whole page. A 3rd bug was that on easy mode, the game said to guess between 1 and 20, but it would still accept guesses outside that range.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude Code in VS Code throughout this project. For a correct suggestion, Claude correctly identified that the hints bug was caused by the secret number being converted to a string on certain guesses, which made the comparison alphabetical instead of numerical. I verified this by running pytest and confirming that check_guess(7, 42) now returns "Too Low" instead of "Too High" like it did with the old code. For a misleading suggestion, Claude's first explanation of the bug was very technical and used words like alphabetical ordering and TypeError fallback that were hard to follow. I had to ask it to simplify the explanation before I understood what was wrong.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was really fixed when I ran pytest and all tests passed, and then confirmed it worked in the live game by playing it manually. The most useful test I ran was a specific pytest case targeting the hints bug: check_guess(7, 42) had to return Too Low, because under the old broken code it would return Too High due to the wrong type of comparison. Running pytest showed all 4 tests passing, which told me the comparison was now working correctly. Claude helped me design that specific test by explaining which exact input values would expose the bug and why.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number kept changing because every time you clicked a button in Streamlit it reruns the whole script from the beginning, so the random.randint line kept generating a new number each click. It's like the page refreshes every single time you interact with it. To explain it to a friend, I would say imagine every time you click a button the whole page reloads and forgets everything it knew before, because that's what Streamlit does unless you use session state. Session state is like memory that survives the rerun, so I wrapped the secret number in a check that only creates it once and saves it there.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to keep is writing a pytest test right after I find a bug, before I fix it, so I can prove the fix worked instead of just assuming it did. Next time I work with AI, I would ask it to explain what a piece of code does before accepting it, because this project showed me that AI can write code that looks fine but has a hidden bug in it that you won't notice until you play the game. This project changed how I think about AI code because I used to assume if the AI wrote it it was probably correct, but now I know AI can introduce bugs just like any other developer and you have to read and test what it gives you.
