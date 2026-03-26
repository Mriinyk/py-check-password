import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param("A1@aaaa", False, id="too short: 7 chars"),
        pytest.param("A1@aaaaaaaaaaaaaaaa", False, id="too long: 17 chars"),
        pytest.param("password123@", False, id="no uppercase letter"),
        pytest.param("PASSWORD@@@", False, id="no digits"),
        pytest.param("PASSWORD123", False, id="no special symbols"),
        pytest.param("PASS123@", True, id="valid: only upper, digit, special"),
        pytest.param("Pass123@", True, id="valid: all types included"),
        pytest.param("Pass word1@", False, id="forbidden space"),
        pytest.param("Pass123@%", False, id="forbidden symbol '%'"),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
