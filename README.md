# AutoQA.restapi.Example

## Pre requirements

You need installed:
```
Python -> 3.6
```


## Install

First you need to install venv. For unix-system:

```shell
pip3 install -U virtualenv
python3 -m virtualenv venv
source venv/bin/activate
```

For windows-system:

```commandline
Path:\> pip3 install -U virtualenv
Path:\> python3 -m virtualenv venv
Path:\> venv\Scripts\activate.bat
```

In virtual evn need use command for install libraries:
```shell
pip install -r requirements.txt
```

## Tests

Test located in folder 'tests'. For start test use pytest. You can use command for start all tests:
```shell
pytest
```

Or you can start some tests:
```commandline
pytest tests/test_employee.py
```
```commandline
pytest tests/test_employee.py::test_status_code_response_create
```

Or start tests from IDE PyCharm. Just set in -> File -> Settings -> Tools -> Python Integrated Tools params 'Default
test runner' to pytest.

## Settings for tests
Some settings set in pytest.ini.