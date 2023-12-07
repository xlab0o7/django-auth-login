from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.contrib.auth.tokens import default_token_generator
# from django.contrib.auth.models import User
from six import text_type

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp: int) -> str:
        return (
            text_type(user.pk) + text_type(timestamp)
        )

generate_token = TokenGenerator()

# user = User.objects.all()
# token = default_token_generator.make_token(user)