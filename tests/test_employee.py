from hamcrest import assert_that, empty, equal_to, is_not, less_than, matches_regexp

from apis.post_create.post_create import POSTCreate
from apis.get_employee.get_employee import GETEmployee


def test_create_employee():
    """
    The test verifies the creation of a new employee and the success of its creation
    USED APIs: POST /create, GET employee/{id}
    """
    response_create = POSTCreate().post_create(body='{"name": "test", "salary": "123", "age": "23"}')
    id_record = response_create.json()["data"]["id"]

    assert_that(response_create.status_code, equal_to(200), "Status code isn't correct")
    assert_that(response_create.json(), is_not(empty()), "JSON body response is empty")
    assert_that(response_create.json()["status"], equal_to("success"), "Status in response body isn't success")
    assert_that(response_create.json()["message"], equal_to("Successfully! Record has been added."), "Message in response body isn't correct")
    assert_that(response_create.json()["data"]["name"], equal_to("test"), "Name in response body isn't correct")
    assert_that(response_create.json()["data"]["salary"], equal_to("123"), "Salary in response body isn't correct")
    assert_that(response_create.json()["data"]["age"], equal_to("23"), "Age in response body isn't correct")
    assert_that(str(response_create.json()["data"]["id"]), matches_regexp("[0-9]{4}"), "Id in response body isn't correct")
    assert_that(response_create.elapsed.seconds, less_than(2), "Response answer is too slow")

    response_employee = GETEmployee().get_employee(id_record=id_record)
    assert_that(response_employee.status_code, equal_to(200), "Status code isn't correct")
    assert_that(response_employee.json(), is_not(empty()), "JSON body response is empty")
    assert_that(response_employee.json()["status"], equal_to("success"), "Status in response body isn't success")
    assert_that(response_employee.json()["message"], equal_to("Successfully! Record has been fetched."), "Message in response body isn't correct")
    assert_that(response_employee.json()["data"]["id"], equal_to(id_record), "Id in response body isn't correct")
    assert_that(response_employee.json()["data"]["employee_name"], equal_to("test"), "Name in response body isn't correct")
    assert_that(response_employee.json()["data"]["employee_salary"], equal_to(123), "Salary in response body isn't correct")
    assert_that(response_employee.json()["data"]["employee_age"], equal_to(23), "Age in response body isn't correct")
    assert_that(response_employee.json()["data"]["profile_image"], equal_to(""), "Profile_image in response body isn't correct")
    assert_that(response_employee.elapsed.seconds, less_than(2), "Response answer is too slow")
