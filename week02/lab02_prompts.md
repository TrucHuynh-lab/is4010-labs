# Lab 02 CLI comparison journal

Do not include passwords, tokens, API keys, or complete authentication output.

## Tool check

### GitHub Copilot CLI

I installed and authenticated GitHub Copilot CLI successfully. The version I verified is 1.0.83.

### Antigravity CLI

I installed and authenticated Antigravity CLI successfully. The version I verified is 1.1.27.

## Shared task

### Shared prompt

Paste the exact prompt you submitted to both CLI tools.

```text
Write the Python function count_vowels(text: str) -> int. It should count the vowels a, e, i, o, and u without regard to case, and it should not count y. Explain your approach briefly.
```

### Copilot CLI observations

Copilot CLI suggested a short solution that converts the text to lowercase and uses a generator expression with sum() to count characters that appear in "aeiou". I liked that the answer was simple and directly matched the requirement that y should not be counted. I would still verify the function with tests for uppercase letters, empty strings, and words with no vowels.

### Antigravity CLI observations

Antigravity CLI gave a very similar solution, but it first inspected the repository files, including the lab instructions, prompt journal, and tests. Its solution used a set of vowels and then counted matching characters after converting the text to lowercase. I liked that it explained why each part worked and connected the solution to the repository context before answering.

### Comparison

Both CLI tools gave a correct and very similar solution for count_vowels. Copilot CLI was more direct and gave a short answer without checking many repository files first. Antigravity CLI spent more time inspecting the lab instructions, prompt journal, and test file before responding, so its answer felt more connected to the assignment. I think Copilot was faster and simpler to use, while Antigravity gave more context and explanation. Both approaches used lowercase conversion and checked whether each character was one of the vowels a, e, i, o, or u. Since their solutions were similar, I would rely on the automated tests to confirm which implementation works correctly in the repository.

## Test-guided implementation

I ran the automated tests from the repository root using pytest. All of the tests for make_greeting, is_even, and count_vowels passed, including tests for multiword names, empty names, positive and negative even numbers, uppercase vowels, text with no vowels, and empty strings. This gave me evidence that the three functions match the required behavior. I did not need to revise the Python code because the function tests already passed. The remaining failed tests were only related to unfinished sections in the prompt journal, not the Python functions. This showed me why the tests are useful because they separated code problems from documentation problems and helped me confirm that the final implementation matches the required function contracts.

## Preferred tool combination

I think each tool fits a different part of my workflow. A browser chat is useful when I need a clear explanation or want to ask follow-up questions. GitHub Copilot in VS Code is helpful while I am actively writing code because it can suggest code without leaving the editor. Copilot CLI is useful when I am already working in the terminal and want a fast answer based on the repository. Antigravity CLI was more detailed because it inspected the repository files before responding. Right now, I prefer using VS Code with Copilot and a browser chat because that combination feels the easiest for me to understand and control. I might choose Antigravity more often if I am working on a larger repository and need more context before making changes.
