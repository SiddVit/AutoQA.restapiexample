import json

import pytest

from apis.get_employee.get_employee import GETEmployee
from apis.post_create.post_create import POSTCreate


@pytest.fixture(scope='module')
def setup_create(param_test):
    response_create = POSTCreate().post_create(body=json.dumps(param_test))
    return response_create


@pytest.fixture(scope='module')
def setup_get_employee(setup_create):
    id_record = setup_create.json()['data'].get('id')
    response_employee = GETEmployee().get_employee(id_record=id_record)
    return response_employee


def id_func(fixture_value):
    return f'Param test: {str(fixture_value)}'
