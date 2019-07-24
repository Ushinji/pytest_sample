import pytest
from app.sum import sum


class TestSum():

    def test_answer(self):
        assert sum(1, 2) == 3

    @pytest.mark.parametrize("a, b, expected", [
        (1, 2, 3),
        (2, 3, 5),
        (4, 5, 9)
    ])
    def test_answer_using_parametrize(self, a, b, expected):
        assert sum(a, b) == expected
