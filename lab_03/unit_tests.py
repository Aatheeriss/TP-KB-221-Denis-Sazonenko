import unittest
from unittest.mock import patch
from filemgmt import FileMGMT
from studentList import StudentList
from student import Student
from utils import Utils
import csv
import io
import os

class TestFileMGMT(unittest.TestCase):

    def test_read_from_file(self):
        #Create a temporary CSV file with sample data
        file_name = 'test_read_from_file.csv'
        with open(file_name, 'w', newline='') as csvfile:
            fieldnames = ["name", "phone", "mail", "age"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({"name": "John", "phone": "123456789", "mail": "john@example.com", "age": "25"})

        student_list = FileMGMT.ReadFromFile(file_name)
        self.assertTrue(student_list.students)

        os.remove(file_name)

    def test_file_save(self):
        #Create a sample student list
        student_list = StudentList()
        student_list.students.append(Student("John", "123456789", "john@example.com", "25"))
        file_name = 'test_file_save.csv'
        FileMGMT.FileSave(student_list, file_name)

        # Read the saved file and check if it contains the expected data
        with open(file_name, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)

            self.assertEqual(rows[0]["name"], "John")
            self.assertEqual(rows[0]["phone"], "123456789")
            self.assertEqual(rows[0]["mail"], "john@example.com")
            self.assertEqual(rows[0]["age"], "25")
  
        os.remove(file_name)

class TestStudentList(unittest.TestCase):

    def setUp(self):
        #Create a sample student list for testing
        self.student_list = StudentList()
        self.sample_student = Student("John", "123456789", "john@example.com", "25")

    def test_add_new_element(self):
        self.student_list.students.append(self.sample_student)
        #Call the addNewElement function and check if the elem has been added properly
        with patch('builtins.input', side_effect=["Ken", "987654321", "jane@example.com", "30"]):
            self.student_list.addNewElement()

        created_student = self.student_list.students[1]
        self.assertEqual(created_student.name, "Ken")
        self.assertEqual(created_student.phone, "987654321")
        self.assertEqual(created_student.mail, "jane@example.com")
        self.assertEqual(created_student.age, "30")

    def test_update_element(self):
        self.student_list.students.append(self.sample_student)

        # Call the updateElement function and check if the student information is updated
        with patch('builtins.input', side_effect=["John", "Jane", "987654321", "jane@example.com", "30"]):
            self.student_list.updateElement()

        updated_student = self.student_list.students[0]
        self.assertEqual(updated_student.name, "Jane")
        self.assertEqual(updated_student.phone, "987654321")
        self.assertEqual(updated_student.mail, "jane@example.com")
        self.assertEqual(updated_student.age, "30")

    def test_delete_element(self):
        # Add a sample student to the list
        self.student_list.students.append(self.sample_student)

        # Call the deleteElement function and check if the student is removed from the list
        with patch('builtins.input', return_value="John"):
            self.student_list.deleteElement()

        self.assertFalse(self.student_list.students)

    def test_print_all_list(self):
        #Redirect stdout to capture print output
        with io.StringIO() as buffer, patch('sys.stdout', buffer):
            #Call the printAllList function and check if the output contains the expected student information
            self.student_list.students.append(self.sample_student)
            self.student_list.printAllList()
            output = buffer.getvalue()

        self.assertIn("Student name is John, Phone is 123456789, Mail is john@example.com, Age is 25", output)

class TestUtils(unittest.TestCase):

    def test_sanitizing(self):
        #Call the sanitizing function and check if the input is sanitized correctly
        sanitized_input = Utils.saniitizing("  john  ")
        self.assertEqual(sanitized_input, "John")

if __name__ == '__main__':
    unittest.main()
