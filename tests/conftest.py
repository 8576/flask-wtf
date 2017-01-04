import pytest
from flask import Flask as _Flask, Response, json


class Flask(_Flask):
    testing = True
    secret_key = __name__

    class response_class(Response):
        def get_json(self):
            return json.loads(self.data)

    def make_response(self, rv):
        if rv is None:
            rv = ''

        return super(Flask, self).make_response(rv)


@pytest.fixture
def app():
    app = Flask(__name__)
    return app


@pytest.yield_fixture
def app_ctx(app):
    with app.app_context() as ctx:
        yield ctx


@pytest.yield_fixture
def req_ctx(app):
    with app.test_request_context() as ctx:
        yield ctx


@pytest.fixture
def client(app):
    return app.test_client()
