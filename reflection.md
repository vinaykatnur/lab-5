1. Which issues were the easiest to fix, and which were the hardest? Why?
•	The easiest issue to fix was the mutable default argument (logs=[]), since it only required changing it to logs=None and initializing it inside the function.
•	The hardest issue was the input validation, because it required checking for both data type and value correctness without breaking existing function logic. This needed careful handling to avoid raising unnecessary exceptions.
2. Did the static analysis tools report any false positives? If so, describe one example.
•	Yes, one example was the “global logs is unused” warning. Although the variable was indeed used inside the function for logging, the tool flagged it as unused because it was defined globally but only accessed within a function scope. This was a minor false positive and didn’t affect functionality.
3. How would you integrate static analysis tools into your actual software development workflow?
•	I would integrate Pylint, Bandit, and Flake8 into the CI pipeline (e.g., GitHub Actions or Jenkins) so every commit or pull request runs these tools automatically.
•	Additionally, I would configure pre-commit hooks locally so developers can detect and fix issues before pushing code to the remote repository.
4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
•	The code became more readable due to consistent spacing, proper logging, and use of f-strings.
•	Error handling became more precise with specific exceptions.
•	The removal of insecure eval improved security, and input validation made the code more robust against invalid data.
•	Overall, the script now follows cleaner coding standards and is less prone to runtime errors.

