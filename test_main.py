import json
import unittest
from contextlib import redirect_stdout
from io import StringIO

from main import collect_metrics, main


class SnapshotTests(unittest.TestCase):
    def test_local_details_are_opt_in(self):
        keys = {"hostname", "executable", "pid"}
        self.assertTrue(keys.isdisjoint(collect_metrics()))
        self.assertTrue(keys <= collect_metrics(True).keys())

    def test_json_output_is_machine_readable(self):
        with redirect_stdout(StringIO()) as out:
            self.assertEqual(main(["--json"]), 0)
        data = json.loads(out.getvalue())
        self.assertIn("python", data)
        self.assertIsInstance(data["monotonic_ns"], int)
