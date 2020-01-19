import unittest

from component import Component
from assembly import Assembly

class TestComponentMethods(unittest.TestCase):

    def setUp(self):

        self.component1 = Component("Place Holder 1")
        self.component2 = Component("Place Holder 2")

        self.component1.set_type("Closure")
        self.component1.add_size("08")
        self.component1.add_rating("1500")
        self.component1.set_material("A350 LF2")
        self.component1.add_feature("RTJ")
        self.component1.set_part_number("02-08-15-001-002")
        self.component1.update_description()

    def test_set_type(self):
        self.component2.set_type("Test Name")
        self.assertEqual(self.component2.get_type(), "Test Name")

    def test_remove_size(self):
        self.component1.add_size("06")
        self.component1.remove_size("08")
        self.assertEqual(self.component1.get_sizes(), ["06"])

    def test_remove_rating(self):
        self.component1.add_rating("900")
        self.component1.remove_rating("1500")
        self.assertEqual(self.component1.get_ratings(),["900"])

    def test_set_material(self):
        self.component1.set_material("316 SS")
        self.assertEqual(self.component1.get_material(),"316 SS")

    def test_remove_feature(self):
        self.component1.add_feature("PEP Assembly")
        self.component1.remove_feature("RTJ")
        self.assertEqual(self.component1.get_features(),["PEP Assembly"])

    def test_set_part_number(self):
        self.component1.set_part_number("02-08-15-001-004")
        self.assertEqual(self.component1.get_part_number(),"02-08-15-001-004")

    def test_update_description(self):
        self.assertEqual(self.component1.get_description(), "Closure, 8\", 1500, A350 LF2, RTJ")
        self.component1.set_material("316 SS")
        self.component1.add_feature("PEP Assembly")
        self.component1.update_description()
        self.assertEqual(self.component1.get_description(), "Closure, 8\", 1500, 316 SS, PEP Assembly, RTJ")



if __name__ == '__main__':
    unittest.main()