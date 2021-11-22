
## Goal:
- Create a directory with code sample files with handy aliases to run and manage them.

## Install:
- Clone this repository.
- Setup a path to this directory. Run next command in terminal where a current directory is a directory with this readme file.  
  `sed -i '' 's?^_path_to_samples_folder=*?_path_to_samples_folder='`pwd`'?' ./.bash_aliases.sh`

- Add aliases to ~/.bash_profile or ~/.zshenv file. Run one of the following commands.  
  `cat ./.bash_aliases.sh >> ~/.bash_profile`  
  `cat ./.bash_aliases.sh >> ~/.zshenv`

- Remove remote origin from your local git repository.  
  `git remote remove origin`

## Try to run it.
- Open new terminal.
- Run: `py_test`
- Run: `py_swap new_sample_file`
