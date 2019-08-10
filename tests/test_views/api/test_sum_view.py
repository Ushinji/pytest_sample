import json
from parameterized import parameterized_class
from tests import Base


@parameterized_class(('a', 'b', 'expected_sum'), [
    (1, 2, 3),
    (2, 3, 5),
    (4, 5, 9),
])
class TestApiSumViewInNormalCase(Base):
    '''GET /api/sum 正常系のテスト'''

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_return_200(self):
        '''200を返すこと'''
        response = self.api_get('/api/sum', {'a': self.a, 'b': self.b})
        assert response.status_code == 200

    def test_return_sum(self):
        '''クエリストリングで渡した値の和を返すこと'''
        response = self.api_get('/api/sum', {'a': self.a, 'b': self.b})
        data = json.loads(response.get_data(as_text=True))

        assert data['result'] == self.expected_sum


@parameterized_class(('a', 'b'), [
    ('A', 'B'),
])
class TestApiSumViewInAbNormalCase(Base):
    '''GET /api/sum 異常系のテスト'''

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_return_422(self):
        '''422を返すこと'''
        response = self.api_get(
            '/api/sum', {'a': self.a, 'b': self.b})
        assert response.status_code == 422

    def test_return_error_message(self):
        '''エラーメッセージを返すこと'''
        response = self.api_get(
            '/api/sum', {'a': self.a, 'b': self.b})
        data = json.loads(response.get_data(as_text=True))

        err_msg = f'Query strings must be integer. a: {self.a}, b: {self.b}'
        assert data['errors'] == err_msg
