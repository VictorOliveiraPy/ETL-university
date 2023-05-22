import unittest

from src.domain.entities.university import University


class UniversityTest(unittest.TestCase):
    def setUp(self):
        self.university = University(
            domains="example.com",
            country="USA",
            web_pages="https://example.com",
            name="Example University"
        )

    def test_attributes(self):
        assert self.university.domains == "example.com"
        assert self.university.country == "USA"
        assert self.university.web_pages == "https://example.com"
        assert self.university.name == "Example University"

    def test_str_representation(self):
        expected_str = "University(domains='example.com', country='USA', web_pages='https://example.com', name='Example University')"
        assert str(self.university) == expected_str
