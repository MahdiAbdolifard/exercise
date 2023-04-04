import pytest
from person import Person


class TestPerson:

    @pytest.fixture
    def init (self):
        self.p1 = Person('mahdi', 'abdolifard')
        self.p2 = Person('ali', 'kamrani')

        # yield 'init'
        # return "Done ..."


    def test_fullname(self):
        assert self.p1.fullname() == "mahdi abdolifard"
        assert self.p2.fullname() == "ali kamrani"


    def test_gmail(self):
        assert self.p1.gmail() == "mahdiabdolifard@gmail.com"
        assert self.p2.gmail() == "alikamrani@gmail.com"