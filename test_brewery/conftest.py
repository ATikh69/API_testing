import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://api.openbrewerydb.org/breweries",
        help="It's request's  URL for BREWERY_API"
    )


@pytest.fixture
def base_url_brewery(request):
    return request.config.getoption("--url")
