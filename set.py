# need to check if app is open...

# read the position file and send commands to all applications. 
import sys
import json
from shell import shell
from tools import *
import pdb

def main(preset_number):
	app_config_d = {}
	load_dict_from_file(CONFIG_FILE, app_config_d)

	running_apps = get_running_apps()

	# get each app.
	for app in app_config_d:
		if app not in running_apps:
            		continue
		if app_config_d[app]["isApple"]:
			set_apple(app, preset_number)
		else:
			globals()['set_' + app](preset_number)


def set_Wunderlist(preset_number):
	apps_pos_d = get_pos_dict()
	wunderlist_data = apps_pos_d["Wunderlist_{}".format(preset_number)]

	commands = [
		"tell application \"Wunderlist\" to activate",
		"set x to {}".format(wunderlist_data["x"]),
		"set y to {}".format(wunderlist_data["y"]),
		"set w to {}".format(wunderlist_data["w"]),
		"set h to {}".format(wunderlist_data["h"]),
		"tell application \"System Events\" to tell process \"Wunderlist\"",
		"tell window 1",
		"set size to {w, h}",
		"set position to {x, y}",
		"end tell",
		"end tell"
	]
	apple_script_cmd = generate_apple_script(commands)
	shell(apple_script_cmd)

def set_Discord(preset_number):
	apps_pos_d = get_pos_dict()
	discord_data = apps_pos_d["Discord_{}".format(preset_number)]

	commands = [
		"tell application \"Discord\" to activate",
		"set x to {}".format(discord_data["x"]),
		"set y to {}".format(discord_data["y"]),
		"set w to {}".format(discord_data["w"]),
		"set h to {}".format(discord_data["h"]),
		"tell application \"System Events\" to tell process \"Discord\"",
		"tell window 1",
		"set size to {w, h}",
		"set position to {x, y}",
		"end tell",
		"end tell"
	]
	apple_script_cmd = generate_apple_script(commands)
	shell(apple_script_cmd)

def set_Spotify(preset_number):
	apps_pos_d = get_pos_dict()
	spotify_data = apps_pos_d["Spotify_{}".format(preset_number)]
	commands = [
		"tell application \"Spotify\" to activate",
		"set x to {}".format(spotify_data["x"]),
		"set y to {}".format(spotify_data["y"]),
		"set w to {}".format(spotify_data["w"]),
		"set h to {}".format(spotify_data["h"]),
		"tell application \"System Events\"",
		"tell process \"Spotify\" to get first window",
		"set spotify_window to result",
		"set position of spotify_window to {x, y}",
		"set size of spotify_window to {w, h}",
		"end tell"
	]
	apple_script_cmd = generate_apple_script(commands)
	shell(apple_script_cmd)




def set_apple(app, preset_number):

	apps_pos_d = get_pos_dict()
	
	app_arg = apps_pos_d["{}_{}".format(app, preset_number)]
	commands = [
		"tell application \"{}\"".format(app),
		"set bounds of front window to {}".format(app_arg),
		"end tell"
	]
	apple_script_cmd = generate_apple_script(commands)
	shell(apple_script_cmd)




if __name__ == "__main__":
    assert(len(sys.argv) == 2)
    main(sys.argv[1])