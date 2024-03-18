from pass_gen.core.password_generator import PasswordGenerator


class TestPasswordGenerator:
    """Test cases for the PasswordGenerator class."""

    def test_generate_password_default_length(self):
        """Test generating a password with the default length."""
        generator = PasswordGenerator()
        password = generator.generate_password()
        assert len(password) == 12

    def test_generate_password_custom_length(self):
        """Test generating a password with a custom length."""
        generator = PasswordGenerator()
        password = generator.generate_password(length=16)
        assert len(password) == 16

    def test_generate_password_strength(self):
        """Test generating a password with specific strength requirements."""
        generator = PasswordGenerator()
        password = generator.generate_password(length=20)
        print(password)
        assert any(char.isdigit() for char in password)
        assert any(char.isupper() for char in password)
        assert any(char.islower() for char in password)
        assert any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password)
