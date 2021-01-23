import json
import re
import pytest

from apis.post_create.post_create import POSTCreate
from apis.get_employee.get_employee import GETEmployee


@pytest.mark.parametrize("employee", [
    {"name": "test", "salary": 123, "age": 23},
    {"name": "test", "salary": "123", "age": "23"},
    {"name": None, "salary": None, "age": None},
    {"name": "", "salary": "", "age": ""},
    {"name": "!@#$%^&*()_+", "salary": "!@#$%^&*()_+", "age": "!@#$%^&*()_+"},
    {"salary": "123", "age": "23"},
    {"name": "test", "age": "23"},
    {"name": "test", "salary": "123"},
    {"name": "test"},
    {"salary": "123"},
    {"age": "23"},
    {"nothing": ""},
    {},
])
def test_create_employee(employee):
    """
    The test verifies the creation of a new employee and the success of its creation
    USED APIs: POST /create, GET employee/{id}
    """
    response_create = POSTCreate().post_create(body=json.dumps(employee))
    id_record = response_create.json()["data"]["id"]
    response_employee = GETEmployee().get_employee(id_record=id_record)

    assert response_create.status_code == 200, "Status code isn't correct"
    assert response_create.json() is not None, "JSON body response is empty"
    assert response_create.json()["status"] == "success", "Status in response body isn't success"
    assert response_create.json()["message"] == "Successfully! Record has been added.", "Message in response body isn't correct"
    if employee["name"] is not KeyError:
        assert response_create.json()["data"]["name"] == employee["name"], "Name in response body isn't correct"
    if employee["salary"] is not KeyError:
        assert response_create.json()["data"]["salary"] == employee["salary"], "Salary in response body isn't correct"
    if employee["age"] is not KeyError:
        assert response_create.json()["data"]["age"] == employee["age"], "Age in response body isn't correct"
    assert re.match("[0-9]{4}", str(response_create.json()["data"]["id"])), "Id in response body isn't correct"
    assert response_create.elapsed.seconds < 2, "Response answer is too slow"

    assert response_employee.status_code == 200, "Status code isn't correct"
    assert response_employee.json() is not None, "JSON body response is empty"
    assert response_employee.json()["status"] == "success", "Status in response body isn't success"
    assert response_employee.json()["message"] == "Successfully! Record has been fetched.", "Message in response body isn't correct"
    assert response_employee.json()["data"]["id"] == id_record, "Id in response body isn't correct"
    if employee["name"] is not KeyError:
        assert response_employee.json()["data"]["employee_name"] == employee["name"], "Name in response body isn't correct"
    if employee["salary"] is not KeyError:
        assert response_employee.json()["data"]["employee_salary"] == employee["salary"], "Salary in response body isn't correct"
    if employee["age"] is not KeyError:
        assert response_employee.json()["data"]["employee_age"] == employee["age"], "Age in response body isn't correct"
    assert response_employee.json()["data"]["profile_image"] == "", "Profile_image in response body isn't correct"
    assert response_create.elapsed.seconds <= 2, "Response answer is too slow"
