from main import StudentManagement
import pytest
student_mgmt = StudentManagement()

class TestStudentManagement():

    def test_accept_student(self):
        student_mgmt.clear_students()
        student_mgmt.accept_student("Raj", 20, 1, 1, 8.5)
        student_mgmt.accept_student("Raunak", 20, 2, 4, 9.5)
        assert student_mgmt.display_students() == "Raj 20 1 1 8.5 Raunak 20 2 4 9.5 "

    def test_accept_student_exception(self):
        student_mgmt.clear_students()
        with pytest.raises(Exception):
            student_mgmt.accept_student("Raj", 20, 1, 1, 8.5)
            student_mgmt.accept_student("Raj", 20, 2, 1, 8.5)


    def test_display_students(self):
        student_mgmt.clear_students()
        student_mgmt.accept_student("Raj", 20, 1, 1, 8.5)
        student_mgmt.accept_student("Raunak", 20, 2, 1, 8.5)
        assert student_mgmt.display_students() == "Raj 20 1 1 8.5 Raunak 20 2 1 8.5 "


    def test_search_student(self):
        student_mgmt.clear_students()
        student_mgmt.accept_student("Raj", 20, 1, 1, 8.5)
        student_mgmt.accept_student("Raunak", 20, 2, 1, 8.5)
        assert student_mgmt.search_student(1) == "Raj 20 1 1 8.5"


    def test_search_student_failure(self):
        student_mgmt.clear_students()
        student_mgmt.accept_student("Raj", 20, 1, 1, 8.5)
        student_mgmt.accept_student("Raunak", 20, 2, 1, 8.5)
        assert student_mgmt.search_student(3) == "Student not found"


    def test_delete_student(self):
        student_mgmt.clear_students()
        student_mgmt.accept_student("Raj", 20, 1, 1, 8.5)
        student_mgmt.accept_student("Raunak", 20, 2, 1, 8.5)
        student_mgmt.delete_student(2)
        assert student_mgmt.display_students() == "Raj 20 1 1 8.5 "

    def test_delete_student_failure(self):
        student_mgmt.clear_students()
        student_mgmt.accept_student("Raj", 20, 1, 1, 8.5)
        student_mgmt.accept_student("Raunak", 20, 2, 1, 8.5)
        assert student_mgmt.delete_student(3) == "Student not found"


    def test_update_student(self):
        student_mgmt.clear_students()
        student_mgmt.accept_student("Raj", 20, 1, 1, 8.5)
        student_mgmt.accept_student("Raunak", 20, 2, 1, 8.5)
        student_mgmt.update_student(2, "Karan", 20, 1, 8.5)
        assert student_mgmt.display_students() == "Raj 20 1 1 8.5 Karan 20 2 1 8.5 "
    
    def test_update_student_failure(self):
        student_mgmt.clear_students()
        student_mgmt.accept_student("Raj", 20, 1, 1, 8.5)
        student_mgmt.accept_student("Raunak", 20, 2, 1, 8.5)
        assert student_mgmt.update_student(5, "Karan", 20, 1, 8.5) == "Student not found"

    # Tests for the Validation methods
    def test_validate_name(self):
        student_mgmt.clear_students()
        student_mgmt.accept_student("Raj", 20, 1, 1, 8.5)
        student_mgmt.accept_student("Raunak", 20, 2, 1, 8.5)
        assert student_mgmt.validate_unique_name("Testing")
    
    def test_validate_name_failure(self):
        with pytest.raises(Exception):
            student_mgmt.clear_students()
            student_mgmt.accept_student("Raj", 20, 1, 1, 8.5)
            student_mgmt.accept_student("Raunak", 20, 2, 1, 8.5)
            assert student_mgmt.validate_unique_name("123")
            assert student_mgmt.validate_unique_name("Raj123")

    def test_validate_empty_input(self):
        with pytest.raises(Exception):
            assert student_mgmt.validate_empty_input(0)
            assert student_mgmt.validate_empty_input("")