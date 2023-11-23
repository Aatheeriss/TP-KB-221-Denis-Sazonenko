import unittest
from unittest.mock import patch
import os
import csv
from lab_02 import (sanitizing, ReadFromFile, printAllList,
                    addNewElement, updateElement, deleteElement, FileSave, main)

class TestLab02(unittest.TestCase):

    def setUp(self):
        self.students_data = [
            {"Name": "John", "Phone": "1", "Mail": "john@example.com", "Age": "25"},
            {"Name": "Alice", "Phone": "9", "Mail": "alice@example.com", "Age": "22"}
        ]
        self.file_name = "test_data.csv"
        with open(self.file_name, "w", newline='') as csvfile:
            fieldnames = ["Name", "Phone", "Mail", "Age"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in self.students_data:
                writer.writerow(row)

    def tearDown(self):
        # Clean up the test file
        try:
            os.remove(self.file_name)
        except FileNotFoundError:
            pass

    def test_sanitizing(self):
        self.assertEqual(sanitizing("  John  "), "John")

    def test_read_from_file(self):
        students = ReadFromFile(self.file_name)
        self.assertEqual(students, self.students_data)

    def test_add_new_element(self):
        with patch('builtins.input', side_effect=['Danya', '1', '1', '1']):
            updated_students = addNewElement(self.students_data)
            expected_students = [
                {"Name": "Alice", "Phone": "9", "Mail": "alice@example.com", "Age": "22"},
                {"Name": "Danya", "Phone": "1", "Mail": "1", "Age": "1"},
                {"Name": "John", "Phone": "1", "Mail": "john@example.com", "Age": "25"}
            ]
            for expected_student in expected_students:
                self.assertIn(expected_student, updated_students)

    def test_update_element(self):
        with patch('builtins.input', side_effect=['John', 'New John', '28', '5', 'newjohn@example.com']):
            updated_students = updateElement(self.students_data)
            expected_students = [
                {"Name": "Alice", "Phone": "9", "Mail": "alice@example.com", "Age": "22"},
                {"Name": "New John", "Phone": "5", "Mail": "newjohn@example.com", "Age": "28"}
            ]
            for expected_student in expected_students:
                # Convert the expected name to lowercase for case-insensitive comparison
                expected_student_name = expected_student["Name"].lower()
                found = any(student["Name"].lower() == expected_student_name for student in updated_students)
                self.assertTrue(found, f"Expected student {expected_student} not found in {updated_students}")


    def test_delete_element(self):
        with patch('builtins.input', return_value='Alice'):
            updated_students = deleteElement(self.students_data)
            expected_students = [{"Name": "John", "Phone": "1", "Mail": "john@example.com", "Age": "25"}]
            for expected_student in expected_students:
                self.assertIn(expected_student, updated_students)

    def test_file_save(self):
        with patch('builtins.input', side_effect=['C', 'Dilan', '2223344', '1', '1', 'X']):
            with patch('sys.argv', ['test_lab_02.py', 'test_data.csv']):
                main('test_data.csv')
                students = ReadFromFile('test_data.csv')
                expected_students = [
                    {"Name": "Alice", "Phone": "9", "Mail": "alice@example.com", "Age": "22"},
                    {"Name": "Dilan", "Phone": "2223344", "Mail": "1", "Age": "1"},
                    {"Name": "John", "Phone": "1", "Mail": "john@example.com", "Age": "25"}
                ]
                for expected_student in expected_students:
                    self.assertIn(expected_student, students)

    def test_main(self):
        with patch('builtins.input', side_effect=['C', 'Dilan', '2223344', '1', '1', 'P', 'X']):
            with patch('sys.argv', ['test_lab_02.py', 'test_data.csv']):
                main('test_data.csv')

if __name__ == '__main__':
    unittest.main()
