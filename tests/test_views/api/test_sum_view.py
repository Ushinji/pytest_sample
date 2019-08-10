import json
from tests import Base


class TestApiSumViewInNormalCase(Base):
    '''GET /api/sum 正常系のテスト'''

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_return_200(self):
        '''200を返すこと'''
        response = self.api_get('/api/sum', {'a': 1, 'b': 2})
        assert response.status_code == 200

    def test_return_sum(self):
        '''クエリストリングで渡した値の和を返すこと'''
        response = self.api_get('/api/sum', {'a': 1, 'b': 2})
        data = json.loads(response.get_data(as_text=True))

        assert data['result'] == 3
