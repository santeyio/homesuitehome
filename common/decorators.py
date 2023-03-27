from knox.auth import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

def require_auth(method_func):
    def wrapper(self, data, *args, **kwargs):
        # we are authenticated, so no need to continue
        if self.scope['user'].id:
            print('--- pass require_auth()')
            pass

        # if we are not authenticated, look for a token
        try:
            if 'token' in data.keys():
                TA = TokenAuthentication()
                # this knox method calls .decode on the token value we pass,
                # so to avoid failure we need to encode the token.
                user, token = TA.authenticate_credentials(data['token'].encode())
                self.scope['user'] = user
                self.scope['token'] = token
                print('-------------- HAD TO RUN TOKEN AUTH ON WEBSOCKETS CONNECTION ---------------')

        except AuthenticationFailed:
            print('Websockets Authorization failed')
            print(e)

        return method_func(self, data, *args, **kwargs)

    return wrapper
