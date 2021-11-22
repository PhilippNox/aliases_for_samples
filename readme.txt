######## py_samples_runner ########


# 0. The goal: to have a handy alias for creating small sample scripts.
#
# 1.  Setup the variable below after line with tag 🔹:
#       _path_to_samples_folder - this is the folder where the sample scripts will be stored.
#
# 2.  Add a bash code (of this readme file)
#     after line with tag 🔻 to your ~/.bash_profile or ~/.zshenv file:
#       - Open terminal.
#       - Change the current directory to a directory with this readme file.
#       - Run one of the following commands:
#           cat readme.txt >> ~/.bash_profile
#           cat readme.txt >> ~/.zshenv
#
# 3.  Create first sample file:
#       - Open new terminal.              # new aliases should be available in the new terminal
#       - Run next command to create a directory for samples (if it doesn't exist):
#           mkdir $_path_to_samples_folder
#       - Run next command to create a first sample file with name "00_test.py":
#           echo "print('use aliases \"py_test\", \"py_swap _\"')\n" >> $_path_to_samples_folder/00_test.py
#
# 4.  How to use it.
#       After reload terminal. Two new commands will be available in terminal.
#       py_test - it will change current directory to sample directory and run 00_test.py
#       py_swap _new_sample_name - it will move file 00_test.py to _new_sample_name and will recreate 00_test.py


# 🔻 Below is the code to save in your ~/.bash_profile or ~/.zshenv file.
# 🔹 variable to setup
_path_to_samples_folder=~/Desktop/python_test

function py_test() {
    echo "👉 cd $_path_to_samples_folder"
    cd $_path_to_samples_folder
    echo "👉 python3 00_test.py"
    python3 00_test.py;
}

function py_swap() {
    run="ok"

    if [ -z "$1" ]; then
        echo "🔻 no argument supplied, no destiantion"
        run=""
    fi

    if [[ $1 = "00_test.py" ]]; then
        echo "🔻 restrict name - 00_test.py"
        run=""
    fi

    if [[ $run = "ok" ]]; then
        echo "👉 cd $_path_to_samples_folder"
        cd $_path_to_samples_folder
        echo "👉 mv -n 00_test.py $1"
        mv -n 00_test.py $1

        if [[ -f "00_test.py" ]]; then
            echo "🔻 00_test.py didn't move, check destination - $1"
        else
            echo "👉 \"print('use aliases \"py_test\", \"py_swap _\"')\" > 00_test.py"
            echo "print('use aliases \"py_test\", \"py_swap _\"')" > 00_test.py
        fi
    fi
}

######## py_samples_runner END ########
