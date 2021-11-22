# aliases_for_samples #########################################

_path_to_samples_folder=
_file_to_run=00_test_it.py

function py_test() {
    echo "👉 cd $_path_to_samples_folder"
    cd $_path_to_samples_folder
    echo "👉 python3 $_file_to_run"
    python3 $_file_to_run;
}

function py_swap() {
    echo "👉 cd $_path_to_samples_folder"
    cd $_path_to_samples_folder
    echo "👉 python3 .swap.py $1"
    python3 .swap.py $1;
}

# END aliases_for_samples #####################################
