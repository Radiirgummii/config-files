import os
import re
import socket
import subprocess
from libqtile import hook
from libqtile import qtile
from typing import List
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import Spacer, Backlight
from libqtile.widget.image import Image
from libqtile.dgroups import simple_key_binder

import colors

# Variables
mod = "mod4"
scratchpad_key = "mod1"

musik = "flatpak run dev.alextren.Spot"
browser = 'firefox'
terminal = 'alacritty'
text_editor = "gnome-text-editor"
file_manager1 = 'thunar'
file_launcher1 = 'rofi -show drun'
file_launcher2 = 'dmenu_run'
email_cliant = 'thunderbird'
process_viewer = terminal + ' -e bpytop'
python_shell = terminal+" + -e python"
soundmixer = "qpwgraph"
password_manager = "bitwarden-desktop"
network_monitor = terminal + " -e bpytop -b net"

wallpaper = "/usr/share/backgrounds/archlinux/archbtw.png"

mbfs = colors.mbfs()
doomOne = colors.doomOne()
dracula = colors.dracula()
everforest = colors.everforest()
nord = colors.nord()
gruvbox = colors.gruvbox()

# Choose colorscheme
colorscheme = dracula

# Colorschme funcstion
colors, backgroundColor, foregroundColor, workspaceColor, foregroundColorTwo = colorscheme



# KEYBINDINGS

# Window keybindings
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "space", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Close windows
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),

    # Close, logout and reset Qtile
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Applications

    # Open Terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Browser
    Key([mod, "shift"], "b", lazy.spawn(browser), desc="Launch browser"),

    # Text editor
    Key([mod, "shift"], "n", lazy.spawn(text_editor), desc="Launch Neovim"),

    # Email cliant
    Key([mod], "e", lazy.spawn(email_cliant), desc="Launch thunderbird"),

    # File manager
    Key([mod, "shift"], "f", lazy.spawn(file_manager1),
        desc="Lauch primary file manager"),

    # Rofi
    Key([mod, ], "d", lazy.spawn(file_launcher1), desc="Launch rofi launcher"),

    # Rofi Bash scripts
    Key([mod, "control"], "d", lazy.spawn(
        file_launcher2), desc="Launch dmenu launcher"),

    # Backup run launcher
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Hardware/system control
    # Sound
    Key([mod], "v", lazy.spawn("pactl set-sink-volume 0 +5%")),
    Key([mod, "shift"], "v", lazy.spawn("pactl set-sink-volume 0 -5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("lux -a 10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("lux -s 10%")),
]

groups = [Group("1", layout='bsp'),
          Group("2", layout='bsp'),
          Group("3", layout='bsp'),
          Group("4", layout='bsp'),
          Group("5", layout='bsp'),
          Group("6", layout='bsp'),
          Group("7", layout='bsp'),
          Group("8", layout='bsp'),
          Group("9", layout='bsp'),
          Group("0", layout='bsp')]

dgroups_key_binder = simple_key_binder(mod)


# Append scratchpad with dropdowns to groups
groups.append(ScratchPad('scratchpad', [
    DropDown('musik', musik, match=Match(wm_class="spot"),
             width=0.8, height=0.8, x=0.1, y=0.1),
    DropDown('terminal', terminal, width=0.8,
             height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown('file_manager', file_manager1, width=0.8,
             height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown('text_editor', text_editor, width=0.8,
             height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown('process_viewer', process_viewer, width=0.8,
             height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown('network_monitor', network_monitor, width=0.29,
             height=0.8, x=0.67, y=0.1, opacity=0.9),
    DropDown('soundmixer', soundmixer,match=Match(wm_class="qpwgraph"), width=0.8,
             height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown('password_manager', password_manager, width=0.8,
             height=0.8, x=0.1, y=0.1, opacity=0.9),

]))
# extend keys list with keybinding for scratchpad
keys.extend([
    Key([scratchpad_key], "m", lazy.group['scratchpad'].dropdown_toggle('musik')),
    Key([scratchpad_key], "t", lazy.group['scratchpad'].dropdown_toggle('terminal')),
    Key([scratchpad_key], "f", lazy.group['scratchpad'].dropdown_toggle('file_manager')),
    Key([scratchpad_key], "n",
        lazy.group['scratchpad'].dropdown_toggle('text_editor')),
    Key([scratchpad_key], "y",
        lazy.group['scratchpad'].dropdown_toggle('process_viewer')),
    Key([scratchpad_key], "n", lazy.group['scratchpad'].dropdown_toggle('network_monitor')),
    Key([scratchpad_key], "s", lazy.group['scratchpad'].dropdown_toggle('soundmixer')),
    Key([scratchpad_key], "x", lazy.group['scratchpad'].dropdown_toggle('password_manager')),
])

layouts = [
    layout.MonadTall(
        border_focus=colors[0], border_normal=colors[0], border_width=1, margin=8),
    # layout.Bsp(border_focus = colors[4], margin = 5),
    # layout.RatioTile(border_focus = colors[4], margin = 2),
    # layout.TreeTab(border_focus = colors[4], margin = 2),
    # layout.Tile(border_focus = colors[4], margin = 2),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Hack Nerd Font Bold',
    fontsize=14,
    padding=2,
    background=colors[0]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper=wallpaper,
        wallpaper_mode='stretch',
        top=bar.Bar(
            [
                widget.Image(
                    filename='~/.config/qtile/icons/python.png',
                    scale='False',
                    margin_x=8,
                    mouse_callbacks={
                        'Button1': lambda: qtile.cmd_spawn(file_launcher2)}
                ),
                widget.GroupBox(
                    padding=4,
                    active=colors[2],
                    inactive=colors[1],
                    highlight_color=[backgroundColor, workspaceColor],
                    highlight_method='line',
                ),
                widget.Prompt(
                ),
                widget.TextBox(
                    text='\u25e2',
                    padding=0,
                    fontsize=50,
                    background=backgroundColor,
                    foreground=workspaceColor),
                widget.CurrentLayout(
                    scale=0.7,
                    background=workspaceColor,
                ),
                widget.TextBox(
                    text='\u25e2',
                    padding=0,
                    fontsize=50,
                    background=workspaceColor,
                    foreground=backgroundColor
                ),
                widget.WindowName(
                    foreground=colors[5],
                ),
                widget.Chord(
                    chords_colors={
                        'launch': (foregroundColor, foregroundColor),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(
                    text='\u25e2',
                    padding=0,
                    fontsize=50,
                    background=backgroundColor,
                    foreground=foregroundColorTwo
                ),
                widget.TextBox(
                    text='\u25e2',
                    padding=0,
                    fontsize=14,
                    background=foregroundColorTwo,
                    foreground=foregroundColorTwo
                ),
                widget.Net(
                    interface="wlp4s0",
                    format=' {down} ↓↑ {up}',
                    foreground=colors[7],
                    background=foregroundColorTwo,
                    padding=8
                ),
                widget.CheckUpdates(
                    update_interval=3600,
                    distro="Ubuntu",
                    display_format="Updates: {updates} ",
                    no_update_string=" No Updates",
                    colour_have_updates=colors[9],
                    colour_no_updates=colors[5],
                    padding=8,
                    background=foregroundColorTwo
                ),
                widget.Volume(
                    foreground=colors[4],
                    background=foregroundColorTwo,
                    fmt='Volume: {}',
                    padding=8
                ),
                widget.TextBox(
                    text='\u25e2',
                    padding=0,
                    fontsize=50,
                    background=foregroundColorTwo,
                    foreground=backgroundColor
                ),
                widget.Clock(format=' %a, %d. %m. %Y.',
                             foreground=colors[10],
                             background=backgroundColor,
                             padding=8
                             ),
                widget.Clock(format=' %I:%M %p',
                             foreground=colors[5],
                             background=backgroundColor,
                             padding=8
                             ),
                widget.QuickExit(
                    fmt=' Exit',
                    foreground=colors[9],
                    padding=8
                ),
            ],
            20,
        ),),
    Screen(
        wallpaper=wallpaper,
        wallpaper_mode='stretch',
        top=bar.Bar(
            [
                widget.Image(
                    filename='~/.config/qtile/icons/python.png',
                    scale='False',
                    margin_x=8,
                    mouse_callbacks={
                        'Button1': lambda: qtile.cmd_spawn(file_launcher2)}
                ),
                widget.GroupBox(
                    padding=4,
                    active=colors[2],
                    inactive=colors[1],
                    highlight_color=[backgroundColor, workspaceColor],
                    highlight_method='line',
                ),
                widget.Prompt(
                ),
                widget.TextBox(
                    text='\u25e2',
                    padding=0,
                    fontsize=50,
                    background=backgroundColor,
                    foreground=workspaceColor),
                widget.CurrentLayout(
                    scale=0.7,
                    background=workspaceColor,
                ),
                widget.TextBox(
                    text='\u25e2',
                    padding=0,
                    fontsize=50,
                    background=workspaceColor,
                    foreground=backgroundColor
                ),
                widget.WindowName(
                    foreground=colors[5],
                ),
                widget.Chord(
                    chords_colors={
                        'launch': (foregroundColor, foregroundColor),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(
                    text='\u25e2',
                    padding=0,
                    fontsize=50,
                    background=backgroundColor,
                    foreground=foregroundColorTwo
                ),
                widget.TextBox(
                    text='\u25e2',
                    padding=0,
                    fontsize=14,
                    background=foregroundColorTwo,
                    foreground=foregroundColorTwo
                ),
                widget.Net(
                    interface="wlp4s0",
                    format=' {down} ↓↑ {up}',
                    foreground=colors[7],
                    background=foregroundColorTwo,
                    padding=8
                ),
                widget.CheckUpdates(
                    update_interval=3600,
                    distro="Ubuntu",
                    display_format="Updates: {updates} ",
                    no_update_string=" No Updates",
                    colour_have_updates=colors[9],
                    colour_no_updates=colors[5],
                    padding=8,
                    background=foregroundColorTwo
                ),
                widget.Volume(
                    foreground=colors[4],
                    background=foregroundColorTwo,
                    fmt='Volume: {}',
                    padding=8
                ),
                widget.TextBox(
                    text='\u25e2',
                    padding=0,
                    fontsize=50,
                    background=foregroundColorTwo,
                    foreground=backgroundColor
                ),
                widget.Clock(format=' %a, %d. %m. %Y.',
                             foreground=colors[10],
                             background=backgroundColor,
                             padding=8
                             ),
                widget.Clock(format=' %I:%M %p',
                             foreground=colors[5],
                             background=backgroundColor,
                             padding=8
                             ),
                widget.QuickExit(
                    fmt=' Exit',
                    foreground=colors[9],
                    padding=8
                ),
            ],
            20,
        ),)
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

# dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(border_focus=colors[4], float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class="qjackctl")
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

lazy.spawn("/home/radiirgummii/.screenlayout/screens.sh")

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
