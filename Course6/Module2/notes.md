# Module 2: Introduction to Linux commands
## Informational, Navigational and Management Commands
### Overview of Common Linux Shell Commands
- shell: Linux command interpretor
- default shell: bash bourne again shell
- other shells:
        - Zsh
        - sh
        - ksh
        - tcsh
        - fish
- Find the default shell
```sh
printenv
```

The first line of the output is SHELL=/bin/bash

- To switch to the bash shell, if it was not the default one

```sh
bash
```

- Shell command applications:
    - Getting information
    - Navigating and working with files and directories
    - Printing files and string contents
    - File compression and archiving
    - Performaing network operations
    - Monitoring perfoemance and status
    - Running batch jobs such as ETL operations

- Getting information
    - whoami: Get the username
    - id: the userID anf groupID
    - uname: the OS name
    - ps: List running processes with their ids
    - top: list running processes with resources usage including:
        - CPU
        - memory
        - IO
    - df: show mounted files
    - man: reference manual
    - date: the current date

- working with files
    - cp: copy file
    - mv: change file name or path
    - rm: remove file
    - touch: create file, update file timestamp
    - chmod: update/modify file permissions
    - wc: get count of lines, words, characters in a file
    - grep: return lines in file matching a pattern

- Navigating and working with directories:
    - ls: List files and directories
    - find: Find files matching a pattern in the current directory tree
    - pwd: Get the path of the current working directory
    - mkdir: create a directory
    - cd: Change directory
    - rmdir: remove en entire directory


- Printing files and string contents
    - cat: Print file content
    - more: print file content page py page
    - head: print the first N lines of a file
    - head: print the last N lines of a file
    - echo: Print string or variable value

- File compression and archiving
    - tar: archive a set of files
    - zip: compress a set of files
    - unzip: extract files from a compressed zip archive
    
- Networking:
    - hostname: print the hostname
    - ping: Send packets to an URL and get response
    - ifconfig: display/confi network interfaces
    - curl: Display the content of the file at the specified URL
    - wget: download file from= the specified URL

- Running Linux on a Windows machine:
    - Dual boot
    - Install Linux on a Virtual Machine
    - install a Linux emulator such as CygWin:
        - A Linux emulator is a software application that allows users to run Linux or Linux-based applications on a different operating system, such as Windows or macOS. Emulators create a virtual environment that mimics the behavior of a Linux system, enabling users to execute Linux commands, run Linux applications, and interact with the Linux file system without needing to install Linux as a native operating system on their machine
    - use the Windows Subsystem for Linux, a compatibility layer for running Linux binary executables natively on Windows


### Informational commands
whoami
id user and group id

id: both user and group ids
id -u : only user id
id -u -n: the name corresponding to the numerical user id


uname: stands for unix name
 find  the OS informations

uname: find just OS name
 uname -s -r: find OS name and version

uname -v: Get more details on the OS

Using the -a option prints all the system information.

![alt text](image.png)

Displayng disck usage:

df: stands for disk free
Monitor disk usage or check available space

Ex

df -h ~: Show disk usage and available space in the home directory

-h make the output human readable, sisplaying results in G or T instead of bytes

df -h:  for the entire filesystem

Displaying current runnning processes
ps stands for process status, running processes
onlu the processes owned by you

ps -e   list all processes running on the system, regardless of which user started them

It displays infos such as:
CMD: the name of the running process
- PID: the id of the process
- time: the running duration in mn and seconds


Monitoring system health and  status

top: stands for table of processes, acts as a task manager

Show a table with running processes and their resources uage

Use when you need to monitor system performance or identify resource-heavy processes. 

By default tasks are sorted by CPU usage

![alt text](image-1.png)

Printing strings and variable value
echo

echo : print nothing and returns a new line

echo Hello

Best practice: use qupoting strings
echo 'Hello everyone'

Print variable

![alt text](image-2.png)

Getting date info
date: Get the current data and time

date "+%Y %m %d %H %M %S ------ %A Day %j in the year %Y ------- %D" 
2024 08 13 01 39 14 ------ Tuesday Day 226 in the year 2024 ------- 08/13/24

![alt text](image-3.png)


viewing the manual

man: stands for manual; shows reference manual for any command
 

 ex: man ls

 man -k .  see all commands with reference manual

 [Getting Help for Linux Commands](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1MWDAxMTdFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvdjRfbmV3X2NvbnRlbnQvbGFicy9yZWFkaW5ncy9NMl9HZXR0aW5nX0hlbHBfZm9yX0xpbnV4X0NvbW1hbmRzLm1kIiwidG9vbF90eXBlIjoiaW5zdHJ1Y3Rpb25hbC1sYWIiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTcxMTYzODYzOX0.XscqAPLdzDR7CPKG3F2r1J6vHsH19CRoIssmWX5cY-g)


 ### File and Directory Navigation Commands
 ls(list): list files and directories

 ls : list the files and directories in the curent working directory
 ls dir: list files and directories in the specified directory

 ls -l: with more details inlluding  permissions, last modified date and owner

 pwd: print working directory

 cd

 Find: Find files in directory tree, mtching the specified criteria, and print their paths

 find: by default find all files 

 find . -name "a.txt"   find all filles named a.txt in the current directoryand its subdirectories , and print their paths
 find . -iname "a.txt"  a case sensitive search


### File and Directory Management Commands

mkdir make a directory
rm: remove a file ordirectory
rm file.txt
You need to use the -r option to remove a directory
rm -r dir 

use the -i option to ask for confirmation beform removing  enter y to confirm

rmdir : remove empty directory

touch: create an empty text file text

See the last modification date of a file or directory
date -r file

touch changes the last modification date of the file if it exists

cp copy file or directory


copy files
cp file1 file2

copy directories
Use -r option to copy a direcoy
cp -r dir1 dir2

copy file to a directory
copy file dir

mv(move): move file or drectory

Move files
mv file dir

mv directory
mv dir1 dir2

mv file_or_dir_1 file_or_dir_1 file_or_dir_1 dest_dir

Managing file permissions

chmod(change mod) : change file permission

ls -l file

![alt text](image-4.png)

![alt text](image-5.png)

ls -la /etc

make a script file executable

chmode +x script.sh

### Security: Managing File Permisions and Ownership

![alt text](image-6.png)

Making a file private
chmod go-r file_or_dir

Revoke for the group and other users the read access to the specified file or directory.

Revoke read access for all users

chmod -r file 
Grant read access to all users

chmode +r file

Revoke read access for only other users


chmod o-r file

REmove user execute acess 
chmod u-x test

chmod u+x test

without execution acces, write is not enough to create or emove files or directory

Executable files - looking ahead

A shell script is a plain text file that can be interpreted by a shell.

Formally speaking, for a text file to be considered an executable shell script for a given user, it needs to have two things:

Execute permissions set for that user
A directive, called a "shebang", in its first line to declare itself to the operating system as a binary


## Working with Text Files, Networking and Archiving Commands

### Viewing File Content
cat(catenate): print entire file content

cat file.txt

more: print file content page by page

less: scrolling through file content: the diff with more is thta ou can use up and down arrows, and also page up and page down keys

head: print the first n lines of the file

head file.txt   the 10 first lines
head -5 file.txt  or head -n 5 the first 5 lines

tail: print the last n lines of the file
tail file.txt   the last 10 lines

tail -5 file.txt or tail -n 5   the last 5 lines of the file


wc(word count): count characters, words and lines

wc file.txt

wc -l file.txt  count only lines
wc -w file.txt  count only words
wc -c file.txt  count only characters

wc -lw file.txt  count only lines and words
etc

### Useful Commands for Wrangling Text Files

sort  sort lines in a file, alphanumerically

sort file.txt

sort -r file.txt  sort in reverse order

uniq (unique)  filter out (consecutive) repeated lines  ![alt text](image-7.png)

grep (global regular expression print) return lines matching the specified pattern

grep ch file.txt

grep -i ch file.txt

![alt text](image-9.png)
cut Extract a section from each line

cut -c 2-9  file.txt    extract from the 2nd to 9th character from each line

cut -c -5 file.txt extract up to the 5th character from each line ie extract the first 5 characters from each line
cut -c 5- file.txt extract from the 5th character from each line 

cut Extract a field from each line

cut -d ' ' -f2 notes.md  ![alt text](image-8.png)


paste: merge lines from multiple files

Consider you have three files:
first.txt containing people firstnames
last.txt containing people lastnames
yob.txt containing people years of birth

paste first.txt last.txt yob.txt: create a table of firstnames, lastnmes and years of birth

By default tab char is used as deliniter
paste -d ',' first.txt last.txt yob.txt: S[ecify a delimiter]

### Reading (Optional): A Brief Introduction to Networking
[A Brief Introduction to Networking](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1MWDAxMTdFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvdjRfbmV3X2NvbnRlbnQvbGFicy9yZWFkaW5ncy9NMl9BX0JyaWVmX0ludHJvZHV0aW9uX3RvX05ldHdvcmtpbmcubWQiLCJ0b29sX3R5cGUiOiJpbnN0cnVjdGlvbmFsLWxhYiIsImFkbWluIjpmYWxzZSwiaWF0IjoxNzExNDI0MzcwfQ.y1qr1XuwUeBkrqooQeW2gn2PtA9c-FS0MNzzW_rQ2CM)


### Networking Commands

hostname Print the hostname

hostname -i get the ip address of the hostname

ifconfig(interfce configuration) Display or configure network interfaces

ifconfig returns a lot of informations including the ip address, MAC addresses, and the hardware specifications of your communication devices

You can specify a specific device you want ifconfig to inspect, such as en ethernet adapeter called eth0: ifconfig eth0
You can seeee your ip address on line 2 after inet

ping test connectivity to a host or ip address by sending packets of data end printing the resuls of the packets ending

ping google.com

ping -c 5 google.com: the 5 ping results

curl: transfer data to and from url
curl www.google.com   return the entire html content of the page

curl www.google.com -o google.txt  write the content to the specified file
curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt  save it into the curent working dir

wget Download file from URL; support recursive download
Useful when a URL points to a folder that contins several files


### File Archiving and Compression Commands

![alt text](image-10.png)
![alt text](image-11.png)

tar(tape archiver)  archive and extract file

tar -cf archive.tar folder_or_file_to_archive : the last arg can be a list of many files or folders
c means create a new archive
the “f” flag tells tar to interpret its input from the file rather than from the default, which is standard input

tar -cf modules_1_and_2.tar Module1 Module2

archive and compress

tar -czf modules_1_and_2_compressed.tar.gz Module1 Module2

the gz is used to help recognize the file type(compressed)

Checl the content of an archive(or compressed) file

tar -tf file.tar
tar -tf modules_1_and_2.tar 

tar -tf modules_1_and_2_compressed.tar.gz

extract an arhive file

tar -xf archive.tar destination_folder

The destination folder is optional, and should exist if specified

Decompress and extract
tar -xzf file.tar.gz dest

zip compress files and archive them
zip -r archive.zip target_dir

uzip extract and decompress zipped files


unzip file.zip

unzip -l notes.zip   list all files in the zip file

unzip -o bin.zip  o force overwrite

zip compress file before grouping them
tr with z option  group files before compressing 

[Module 2 Cheat Sheet - Introduction to Linux Commands](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1MWDAxMTdFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvdjRfbmV3X2NvbnRlbnQvbGFicy9yZWFkaW5ncy9NMl9DaGVhdF9TaGVldF9JbnRyb190b19MaW51eF9Db21tYW5kcy5tZCIsInRvb2xfdHlwZSI6Imluc3RydWN0aW9uYWwtbGFiIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE3MTE2Mzg2Mzl9.hPGxtLz4kFonOfMyXgeNXoj225Ow7P2-kil58GtJQKM)


