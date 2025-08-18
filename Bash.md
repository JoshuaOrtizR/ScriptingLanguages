
#### Current Directory & Listing Contents

* pwd
    * Print current directory path.
* ls
    * List files and directories in the current location.
* ls -a or ls --all
    * List all files and directories, including hidden ones.
* ls -l
    * List files and directories with detailed information (permissions, owner, size, etc.).
* ls -lh or ls
    * List files and directories with detailed information and human-readable file sizes (e.g., 1K, 234M, 2G).
* ls -t
    * List files and directories by modification time, with the newest first.
* stat [file]
    * Display detailed status for a file, including size, timestamps, and permissions.
* tree
    * Recursively list directories and files in a tree-like format.
* tree -a
    * Recursively list all directories and files, including hidden ones.
* tree -d
    * List only directories in a tree-like format.

---

#### Changing Directories

* cd [directory]
    * Change the current directory to the specified one.
* cd or cd 
    * Return to your home directory.
* cd -
    * Go to the last directory you were in.
* pushd [directory]
    * Change to the specified directory and save the current directory to a stack. This is useful for returning to a previous location.
* popd
    * Return to the last directory saved by pushd.
```
