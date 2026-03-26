import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param("Pass@word", False, id="no number"),
        pytest.param("password1@", False, id="no capital letter"),
        pytest.param("PASS1@WORD", False, id="no lowercase letter"),
        pytest.param("Pass word1@", False, id="there is a space"),
        pytest.param("Pass@1", False, id="less than 8 characters"),
        pytest.param("Pass@word1word1word", False,
                     id="more than 16 characters"),
        pytest.param("Pass@word1", True, id="all good")
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
