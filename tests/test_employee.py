import re
import pytest

from tests.conftest import id_func

"""
E2e tests for check API POST create employee and API GET employee
"""


@pytest.fixture(scope='module', ids=id_func, params=[
    {'name': 'test', 'salary': 123, 'age': 23},
    {'name': 'test', 'salary': '123', 'age': '23'},
    {'name': None, 'salary': None, 'age': None},
    {'name': '', 'salary': '', 'age': ''},
    {'name': '!@#$%^&*()_+', 'salary': '!@#$%^&*()_+', 'age': '!@#$%^&*()_+'},
    {'salary': '123', 'age': '23'},
    {'name': 'test', 'age': '23'},
    {'name': 'test', 'salary': '123'},
    {'name': 'test'},
    {'salary': '123'},
    {'age': '23'},
    {'nothing': ''},
    {},
])
def param_test(request):
    return request.param


def test_status_code_response_create(setup_create):
    assert setup_create.status_code == 200, \
        'Status code is not correct'


def test_correct_status_response_create(setup_create):
    assert setup_create.json().get('status') == 'success', \
        'Status in response body is not success'


def test_correct_message_response_create(setup_create):
    assert setup_create.json().get('message') == 'Successfully! Record has been added.', \
        'Message in response body is not correct'


def test_correct_name_response_create(setup_create, param_test):
    assert setup_create.json()['data'].get('name') == param_test['name'], \
        'Name in response body is not correct'


def test_correct_salary_response_create(setup_create, param_test):
    assert setup_create.json()['data'].get('salary') == param_test['salary'], \
        'salary in response body is not correct'


def test_correct_age_response_create(setup_create, param_test):
    assert setup_create.json()['data'].get('age') == param_test['age'], \
        'age in response body is not correct'


def test_id_response_create(setup_create):
    assert re.match('[0-9]{4}', str(setup_create.json()['data'].get('id'))), \
        'Id in response body is not correct'


def test_response_speed_response_create(setup_create):
    assert setup_create.elapsed.seconds < 2, \
        'Response answer is too slow'


def test_status_code_response_get_employee(setup_get_employee):
    assert setup_get_employee.status_code == 200, \
        'Status code is not correct'


def test_correct_status_response_get_employee(setup_get_employee):
    assert setup_get_employee.json().get('status') == 'success', \
        'Status in response body is not success'


def test_correct_message_response_get_employee(setup_get_employee):
    assert setup_get_employee.json().get('message') == 'Successfully! Record has been fetched.', \
        'Message in response body is not correct'


def test_correct_id_response_get_employee(setup_get_employee, setup_create):
    assert setup_get_employee.json()['data'].get('id') == setup_create.json()['data'].get('id'), \
        'Id in response body is not correct'


def test_correct_name_response_get_employee(setup_get_employee, param_test):
    assert setup_get_employee.json()['data'].get('employee_name') == param_test['name'], \
        'employee_name in response body is not correct'


def test_correct_salary_response_get_employee(setup_get_employee, param_test):
    assert setup_get_employee.json()['data'].get('employee_salary') == param_test['salary'], \
        'employee_salary in response body is not correct'


def test_correct_age_response_get_employee(setup_get_employee, param_test):
    assert setup_get_employee.json()['data'].get('employee_age') == param_test['employee_age'], \
        'employee_age in response body is not correct'


def test_correct_profile_response_get_employee(setup_get_employee, param_test):
    assert setup_get_employee.json()['data'].get('profile_image') == param_test['profile_image'], \
        'profile_image in response body is not correct'


def test_response_speed_response_get_employee(setup_get_employee, param_test):
    assert setup_get_employee.elapsed.seconds < 2, \
        'Response answer is too slow'
