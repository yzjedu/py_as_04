import unittest
from io import StringIO
import sys

class TestIntNameConversion(unittest.TestCase):

    def run_program_with_input(self, user_input):
        '''Runs the assignment.py program with the given input and returns the output.'''
        # Backup the original stdin and stdout
        original_stdin = sys.stdin
        original_stdout = sys.stdout

        # Redirect stdin and stdout
        sys.stdin = StringIO(user_input)
        sys.stdout = StringIO()

        # Run the script
        try:
            from assignment import main  # Import the main function
            main()  # Call the main function
            output = sys.stdout.getvalue()  # Capture the output
        finally:
            # Restore the original stdin and stdout
            sys.stdin = original_stdin
            sys.stdout = original_stdout

        return output.strip()

    def test_single_digit(self):
        output = self.run_program_with_input("7\n")
        self.assertIn("seven", output)

    def test_two_digit(self):
        output = self.run_program_with_input("42\n")
        self.assertIn("forty two", output)

    def test_three_digit(self):
        output = self.run_program_with_input("319\n")
        self.assertIn("three hundred nineteen", output)

    def test_teen_number(self):
        output = self.run_program_with_input("13\n")
        self.assertIn("thirteen", output)

    def test_edge_case_zero(self):
        output = self.run_program_with_input("0\n")
        self.assertIn("", output)  # Output should be empty as there's no name for zero

if __name__ == "__main__":
    unittest.main()