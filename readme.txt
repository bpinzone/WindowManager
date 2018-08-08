# WindowManager
Save the position and size of your application windows to restore them later.

For dev todo, see notes.txt

One might put the following in their bash_profile

alias save_windows="grab_windows $1"
alias move_windows="set_windows $1"
function grab_windows {
        cd <path to python files>
        python ./grab.py $1

}
function set_windows {
       cd <path to python files>
       python ./set.py $1
}
