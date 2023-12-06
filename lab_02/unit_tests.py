import unittest
from unittest.mock import patch
import os
import csv
from lab_02 import (sanitizing, ReadFromFile, printAllList,
                    addNewElement, updateElement, deleteElement, FileSave, main)

class TestLab02(unittest.TestCase):

    def setUp(self):
        self.students_data = [
            {"Name": "Alice", "Phone": "9", "Mail": "alice@example.com", "Age": "22"},
            {"Name": "John", "Phone": "1", "Mail": "john@example.com", "Age": "25"}
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
            addNewElement(self.students_data)
            self.assertEqual(self.students_data[1]["Name"], "Danya")

    def test_update_element(self):
        with patch('builtins.input', side_effect=['John', 'Johan', '28', '5', 'newjohn@example.com']):
            updateElement(self.students_data)
            self.assertEqual(self.students_data[1]["Name"], "Johan")
            
    def test_delete_element(self):
        with patch('builtins.input', return_value='Alice'):
            deleteElement(self.students_data)
            self.assertEqual(self.students_data[0]["Name"], "John")

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
                self.assertListEqual(expected_students, students)

if __name__ == '__main__':
    unittest.main()
