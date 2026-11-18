import unittest

from tasks import MAX_TITLE_LENGTH, add_task, clean_title, complete_task, pending, summary


class TestTasks(unittest.TestCase):
    def test_add_task_starts_not_done(self):
        tasks = []
        add_task(tasks, "Buy milk")
        self.assertEqual(tasks, [{"title": "Buy milk", "done": False}])

    def test_complete_task_uses_one_based_number(self):
        tasks = []
        add_task(tasks, "A")
        add_task(tasks, "B")
        complete_task(tasks, 2)
        self.assertEqual([t["done"] for t in tasks], [False, True])

    def test_pending_hides_done_tasks(self):
        tasks = []
        add_task(tasks, "A")
        add_task(tasks, "B")
        complete_task(tasks, 1)
        self.assertEqual([t["title"] for t in pending(tasks)], ["B"])

    def test_summary(self):
        tasks = []
        add_task(tasks, "A")
        add_task(tasks, "B")
        complete_task(tasks, 1)
        self.assertEqual(summary(tasks), "1/2 done")


class TestTitleValidation(unittest.TestCase):
    def test_trims_surrounding_spaces(self):
        self.assertEqual(clean_title("  Buy milk  "), "Buy milk")

    def test_accepts_max_length(self):
        title = "x" * MAX_TITLE_LENGTH
        self.assertEqual(clean_title(title), title)

    def test_rejects_empty_and_blank(self):
        for bad in ("", "   ", "\t\n"):
            with self.assertRaises(ValueError):
                clean_title(bad)

    def test_rejects_too_long_and_non_text(self):
        for bad in ("x" * (MAX_TITLE_LENGTH + 1), None, 5):
            with self.assertRaises(ValueError):
                clean_title(bad)

    def test_add_task_rejects_bad_title_and_keeps_list_clean(self):
        tasks = []
        with self.assertRaises(ValueError):
            add_task(tasks, "   ")
        self.assertEqual(tasks, [])

    def test_add_task_stores_trimmed_title(self):
        tasks = []
        add_task(tasks, "  Study  ")
        self.assertEqual(tasks[0]["title"], "Study")


if __name__ == "__main__":
    unittest.main()
