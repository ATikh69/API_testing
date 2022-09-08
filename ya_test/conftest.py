import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="It's request's  URL for YA"
    )

    parser.addoption(
        "--status_code",
        default=404,
        help="It's default status code"
    )


@pytest.fixture
def base_url_ya(request):
    return request.config.getoption("--url")

@pytest.fixture
def default_status_code(request):
    return request.config.getoption("--status_code")
