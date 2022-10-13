from libqtile import layout
from libqtile.config import Match

bdr_focus = "#076678"
bdr_normal = "#282828"

layouts = [
    layout.Max(),
    layout.MonadTall(
        margin=20,
        border_focus=bdr_focus,
        border_normal=bdr_normal,
        border_width=4,
        ratio=0.71,
    ),
    # layout.Columns(border_focus_stack='#d75f5f'),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    border_focus="#754A21",
    border_normal='#282828',
    border_width=4,
    float_rules=[
        # Run `xprop` to see the wm class and name of an X client
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
)
