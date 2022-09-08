import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://dog.ceo/api",
        help="It's request's  URL for DOG_API"
    )


@pytest.fixture
def base_url_dog(request):
    return request.config.getoption("--url")
