from bevyframe import *


def post(r: Request) -> (Response, Page):
    resp = redirect(f'/SendSession.py')
    email = r.form['email'] if '@' in r.form['email'] else f'{r.form["email"]}@hereus.net'
    if resp.login(email, r.form['password']):
        return resp
    else:
        return get(r, message='Credentials didn\\\'t work')


def get(r: Request, message=None) -> Page:
    return Page(
        title="Login - HereUS Account",
        selector=f'body_blank',
        childs=[
            # Place Navbar above Root,
            Root([
                Box(
                    margin=Margin(top=Size.Viewport.height(10), left=Size.auto, right=Size.auto),
                    width=Size.max_content,
                    childs=[
                        Title("Login", width=Size.pixel(400), text_align=Align.center),
                        Form(
                            method="POST",
                            childs=[Line(i) for i in [
                                Label('Username', id='email_label', margin=Margin(bottom=Size.pixel(-10))),
                                Textbox(
                                    name="email",
                                    type="text",
                                    placeholder="Username",
                                    value=r.form.get('email', '')
                                ),
                                Label('Password', margin=Margin(bottom=Size.pixel(-10))),
                                Textbox(
                                    name="password",
                                    type="password",
                                    placeholder="Password",
                                    value=r.form.get('password', '')
                                ),
                                Label('', id='message', color=Color.red, width=Size.pixel(400), text_align=Align.center),
                                Button(innertext="Login")
                            ]]
                        )
                    ]
                )
            ]),
            Widget('script', innertext='', src='/Scripts/Login.js'),
            Widget('script', innertext=f"load_message('{'' if message is None else message}')")
        ]
    )
        