from unittest.mock import MagicMock

def test_login_use_case_directly():
    from apps.auth.domain.entities import AuthCredentials
    from apps.auth.application.commands.login_user import LoginUserUseCase

    # Arrange
    mock_repo = MagicMock()
    mock_service = MagicMock()

    credentials = AuthCredentials(email="cesargonzalez390@gmail.com", password="Tel.domasclideo001")
    mock_user = MagicMock(uuid="user-uuid", email="cesargonzalez390@gmail.com", password="Tel.domasclideo001")

    mock_repo.get_by_email.return_value = mock_user
    mock_service.create_token.return_value = "fake.jwt.token"  # <- Este es el método correcto

    use_case = LoginUserUseCase(mock_repo, mock_service)

    # Act
    token = use_case.execute(credentials)

    # Assert
    assert token == "fake.jwt.token"
