import unittest

from tasks import add_task, complete_task, pending, summary


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


if __name__ == "__main__":
    unittest.main()
