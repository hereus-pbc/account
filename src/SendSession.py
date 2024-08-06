from bevyframe import *


def get(r: Request) -> Response:
    return redirect(f'https://search.hereus.net/get_session?token={r.cookies['s']}')  # Redirect 1
        