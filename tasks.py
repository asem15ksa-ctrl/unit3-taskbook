"""Core logic for Task Tracker: keep a list of tasks and mark them done."""

MAX_TITLE_LENGTH = 80


def clean_title(title):
    """Return the title without surrounding spaces, or raise ValueError."""
    if not isinstance(title, str):
        raise ValueError(f"Title must be text, got {title!r}")
    title = title.strip()
    if not title:
        raise ValueError("Title must not be empty")
    if len(title) > MAX_TITLE_LENGTH:
        raise ValueError(
            f"Title must be at most {MAX_TITLE_LENGTH} characters, got {len(title)}"
        )
    return title


def add_task(tasks, title):
    """Add a new task (not done yet) and return it."""
    task = {"title": title, "done": False}
    tasks.append(task)
    return task


def complete_task(tasks, number):
    """Mark the task with this 1-based number as done."""
    tasks[number - 1]["done"] = True


def pending(tasks):
    """Return only the tasks that are not done yet."""
    return [task for task in tasks if not task["done"]]


def summary(tasks):
    """Return a short text like '1/3 done'."""
    done = sum(1 for task in tasks if task["done"])
    return f"{done}/{len(tasks)} done"
