from libqtile.config import Key, Group, ScratchPad, DropDown, Match
from libqtile.command import lazy
import os

term_dropdown = "alacritty --config-file " + os.path.expanduser(
    "~/.config/alacritty/dropdown.yml"
)
drop_w = 0.60
drop_h = 0.45
drop_x = 0.197
drop_y = 0.0165
drop_opacity = 1


groups = [
    ScratchPad(
        "scratch",
        [
            DropDown(
                "term",
                term_dropdown + " -t 'TERM-DROPDOWN'",
                width=drop_w,
                height=drop_h,
                x=drop_x,
                y=drop_y,
                opacity=drop_opacity,
                match=Match(title="TERM-DROPDOWN"),
                on_focus_lost_hide=False,
            ),
            DropDown(
                "ranger",
                term_dropdown + " -t 'RANGER-DROPDOWN' -e ranger",
                width=drop_w,
                height=drop_h,
                x=drop_x,
                y=drop_y,
                opacity=drop_opacity,
                match=Match(title="RANGER-DROPDOWN"),
                on_focus_lost_hide=False,
            ),
            DropDown(
                "wifi",
                term_dropdown + " -t 'WIFI-DROPDOWN' -e nmtui",
                width=0.50,
                height=0.6,
                x=0.25,
                y=-0.020,
                opacity=drop_opacity,
                match=Match(title="WIFI-DROPDOWN"),
                on_focus_lost_hide=False,
            ),
            DropDown(
                "sysmon",
                term_dropdown + " -t 'BTM-DROPDOWN' -e btm -b",
                width=drop_w,
                height=drop_h,
                x=drop_x,
                y=drop_y,
                opacity=drop_opacity,
                match=Match(title="BTM-DROPDOWN"),
                on_focus_lost_hide=False,
            ),
        ],
    ),
    Group("a", matches=[Match(wm_class=["firefox"])]),
    Group("s"),
    Group("d"),
    Group("f"),
]

