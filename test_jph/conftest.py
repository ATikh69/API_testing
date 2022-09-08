import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://jsonplaceholder.typicode.com",
        help="It's request's  URL for JsonPlaceholder"
    )


@pytest.fixture
def base_url_jph(request):
    return request.config.getoption("--url")
