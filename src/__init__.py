from bevyframe import *


@login_required
def get(r: Request) -> Page:
    return Page(
        title="HereUS Account",
        selector=f'body_{r.user.id.settings.theme_color}',
        childs=[
            Root([
                Container(
                    margin=Margin(right=Size.auto, left=Size.auto, top=Size.Viewport.height(20)),
                    width=Size.max_content,
                    childs=[
                        Image(
                            src=r.user.id.profile_photo,
                            alt='Profile Picture',
                            width=Size.pixel(100)
                        )
                    ]
                ),
                Title(f"Welcome, {r.user.id.name} {r.user.id.surname}", width=Size.Viewport.width(100), text_align=Align.center),
                Label(r.email, width=Size.Viewport.width(100), text_align=Align.center, margin=Margin(top=Size.pixel(-30))),
                SubTitle("This page is under maintenance, please use LAST for now.", width=Size.Viewport.width(100), text_align=Align.center),
            ])
        ]
    )
        