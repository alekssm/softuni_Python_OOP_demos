from project.student import Student


import unittest

# Should've setup default student, but wanted to test it differently this time
class StudentTests(unittest.TestCase):
    def test_init__with_courses__expected_correct_initialization(self):
        student = Student("Test", {"Soft": ["python", "java script"]})
        self.assertEqual("Test", student.name)
        self.assertEqual({"Soft": ["python", "java script"]}, student.courses)

    def test_init__without_courses__expected_correct_initialization(self):
        student = Student("Test")
        self.assertEqual("Test", student.name)
        self.assertEqual({}, student.courses)

    def test_enroll__when_course_already_added__expected_update_course_and_course_notes(self):
        student = Student("Test", {"Soft": ["python", "java script"]})
        result = student.enroll("Soft", ["c#"], "Y")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertTrue("Soft" in student.courses)
        self.assertEqual(["python", "java script", "c#"], student.courses["Soft"])

    def test_enroll__when_course_not_added_and_add_notes_is_Y__expected_update_with_added_notes(self):
        student = Student("Test", {"Soft": ["python", "java script"]})
        result = student.enroll("UNI", ["c#"], "Y")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue("Soft" and "UNI" in student.courses)
        self.assertEqual(["python", "java script"], student.courses["Soft"])
        self.assertEqual(["c#"], student.courses["UNI"])

    def test_enroll__when_course_not_added_and_add_notes_is_empty_string__expected_update_with_added_notes(self):
        student = Student("Test", {"Soft": ["python", "java script"]})
        result = student.enroll("UNI", ["c#"], "")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue("Soft" and "UNI" in student.courses)
        self.assertEqual(["python", "java script"], student.courses["Soft"])
        self.assertEqual(["c#"], student.courses["UNI"])

    def test_enroll__when_course_not_added_and_add_notes_is_not_empty_string_or_Y__expected_empty_new_course(self):
        student = Student("Test", {"Soft": ["python", "java script"]})
        result = student.enroll("UNI", ["c#"], "java")

        self.assertEqual("Course has been added.", result)
        self.assertTrue("Soft" and "UNI" in student.courses)
        self.assertEqual(["python", "java script"], student.courses["Soft"])
        self.assertEqual([], student.courses["UNI"])

    def test_add_notes__when_course_not_in_courses__expected_raise_exception(self):
        student = Student("Test", {"Soft": ["python", "java script"]})
        with self.assertRaises(Exception) as context:
            student.add_notes("UNI", "c#")
        self.assertIsNotNone(context.exception)

    def test_add_notes__when_course_in_courses__expected_update_course_notes(self):
        student = Student("Test", {"Soft": ["python", "java script"]})
        result = student.add_notes("Soft", "c#")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["python", "java script", "c#"], student.courses["Soft"])

    def test_leave_course__when_course_not_in_courses__expected_raise_exception(self):
        student = Student("Test", {"Soft": ["python", "java script"]})
        with self.assertRaises(Exception) as context:
            student.leave_course("UNI")
        self.assertIsNotNone(context.exception)

    def test_leave_course__when_course_in_courses__expected_update_remove_course_from_courses(self):
        student = Student("Test", {"Soft": ["python", "java script"]})
        result = student.leave_course("Soft")
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, student.courses)
