from app.sum import sum


class TestSum():

    def test_answer(self):
        assert sum(1, 2) == 3
