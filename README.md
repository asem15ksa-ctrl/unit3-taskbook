# Task Tracker - validated titles

A small command-line program to keep a to-do list: add tasks, list them and
mark them as done.

## What it does

- Add a task with a title
- List all tasks with a [x] mark for finished ones and a "done" counter
- Mark a task as done by its number
- Runs in the terminal, no external libraries needed

## How to run

Requires Python 3.9 or newer.

```bash
python main.py
```

Run the tests:

```bash
python -m unittest -v
```

## Project files

| File | Purpose |
|------|---------|
| `tasks.py` | Core logic (add, complete, pending, summary) |
| `main.py` | Command-line menu |
| `test_tasks.py` | Unit tests |
