from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.tokens import AccessToken

from apps.common.models import BlacklistedToken
from apps.common.response_handler import ResponseHandler


class BlacklistMiddleware(MiddlewareMixin):
    def process_request(self, request):  # noqa
        # Check if the token is in the blacklist
        token = request.headers.get("Authorization", None)
        if token:
            # Extract the token part
            token = token.split(" ")[1]
            access_token = AccessToken(token)
            jti = access_token["jti"]

            # Check if the token's jti is in the blacklist
            if BlacklistedToken.objects.filter(jti=jti).exists():
                return ResponseHandler.error(
                    message="This access token has been revoked.", status_code=401
                )
