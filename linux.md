# Basic Linux Commands

## File Operations

- **ls**: List files and directories.
 - **Options**: `-l` (Long format listing), `-a` (Include hidden files), `-h` (Human-readable file sizes).
 - **Examples**: `ls -l`, `ls -a`, `ls -lh`.

- **cd**: Change directory.
 - **Examples**: `cd /path`.

- **pwd**: Print current working directory.
 - **Examples**: `pwd`.

- **mkdir**: Create a new directory.
 - **Examples**: `mkdir my_directory`.

- **rm**: Remove files and directories.
 - **Options**: `-r` (Remove directories recursively), `-f` (Force removal without confirmation).
 - **Examples**: `rm file.txt`, `rm -r my_directory`, `rm -f file.txt`.

- **cp**: Copy files and directories.
 - **Options**: `-r`
 - **Examples**: `cp -r directory destination`, `cp file.txt destination`.

- **mv**: Move/rename files and directories.
 - **Examples**: `mv file.txt new_name.txt`, `mv file.txt directory`.

- **touch**: Create an empty file or update file timestamps.
 - **Examples**: `touch file.txt`.

- **cat**: View the contents of a file.
 - **Examples**: `cat file.txt`.

- **head**: Display the first few lines of a file.
 - **Options**: `-n` (Specify the number of lines to display).
 - **Examples**: `head file.txt`

- **tail**: Display the last few lines of a file.
 - **Options**: `-n` (Specify the number of lines to display).
 - **Examples**: `tail file.txt`

- **ln**: Create links between files.
 - **Options**: `-s` (Create symbolic (soft) links).
 - **Examples**: `ln -s source_file link_name`.

- **find**: Search for files and directories.
 - **Options**: `-name`  `-type` 
 - **Examples**: `find /path -name "*.txt"`.

## File Permission Commands

- **chmod**: Change file permissions.
 - **Options**: `u` (User/owner permissions), `g` (Group permissions)

- **umask**: Set default file permissions.
 - **Examples**: `umask 022`.

## File Compression and Archiving Commands

- **gzip**: Compress files.
 - **Examples**: `gzip file.txt`.

- **zip**: Create compressed zip archives.
 - **Examples**: `zip archive.zip file1.txt file2.txt`.
