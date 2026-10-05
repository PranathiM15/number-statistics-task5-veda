# NOVA — Number Statistics Lab

## Veda Technology — Task 5

A terminal-friendly Python web application for the **Number Statistics** task.

### Task requirements covered

- Identifies even and odd numbers.
- Uses the modulo operator (`%`) to test parity.
- Uses a loop to process each number.
- Finds the largest value with `max()`.
- Finds the smallest value with `min()`.
- Displays separate even and odd lists.
- Uses manually entered numerical data.
- Provides a unique responsive web interface.

### Tools used

- Python
- HTML
- CSS
- JavaScript

**No Jupyter Notebook and no external Python packages are required.**

## Folder structure

```text
number-statistics-task5/
├── app.py
├── index.html
├── style.css
├── script.js
├── requirements.txt
├── README.md
├── DEPLOYMENT.md
├── ROLLBACK.md
└── .gitignore
```

## Run from Terminal / PowerShell

1. Open PowerShell.
2. Move into this folder.
3. Run:

```powershell
py app.py
```

4. Open:

```text
http://127.0.0.1:8000
```

5. Enter numbers such as:

```text
12, 7, 25, 4, 18, 9, 31
```

6. Click **Analyze Dataset**.

### Stop the application

Press:

```text
Ctrl + C
```

## Example result

For:

```text
12, 7, 25, 4, 18, 9, 31
```

Even numbers:

```text
12, 4, 18
```

Odd numbers:

```text
7, 25, 9, 31
```

Largest:

```text
31
```

Smallest:

```text
4
```

## GitHub submission

Create a new **public** GitHub repository and push this folder. See the terminal sequence below or `DEPLOYMENT.md`.

## Interview questions

### 1. How do you check whether a number is even?

Use `number % 2 == 0`. A remainder of zero means the number is even.

### 2. What does the modulo operator do?

The modulo operator `%` returns the remainder after division.

### 3. How can loops be used for data processing?

A loop visits each value in a collection so the same processing logic can be applied to every value.

## Note

This project is intentionally built with Python's standard library so it can be completed directly from the terminal without installing Flask, Jupyter, or other packages.
