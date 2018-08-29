# WindowManager
Save the position and size of your application windows to restore them later.

Register your mac applications with the scripts by editing window_manager/window_config/app_config.json
If it is a single-window built in macOS application, it will work out of the box.

For now, non-mac applications require their own get/set functions due to possible inconsistencies in AppleScript interfaces.

It is possible that the interface is more consistent than I think it is. If/when I find out it is, I'll make function generators so those will work too.

Usage:
sw 5 // Save current Window configuration as preset 5.
mw 5 // Move Windows into positions saved in preset 5.

For dev todo, see notes.txt

One might put the following in their bash profile:

# Window Manager
window_env_path=<your path to window-env folder>
function before_window {
        DIR_BEFORE_WINDOW_MANAGER_COMMAND=$(pwd)
        cd $window_env_path
        source ./bin/activate
}
function after_window {
        deactivate
        cd $DIR_BEFORE_WINDOW_MANAGER_COMMAND
}
function sw {
        # Save Windows
        before_window
        python3 ./window_manager/grab.py $1
        after_window
}
function mw {
        # Move Windows
        before_window
        python3 ./window_manager/set.py $1
        after_window
}