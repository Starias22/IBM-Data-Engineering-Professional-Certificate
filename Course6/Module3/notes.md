# Module 3: Introduction to Shell Scripting
## Shell Scripting Basics
- Script:
    - A list of commands that can be interpreted and run by a program called scripting language
    - Can be entered in a terminal or listed in a text file
    - Scripting languages are:
        - interpreted at runtime
        - slower to run but feasier and aster to develop
        - Script usages:
            - autmomate: processes
                - ETL jobs
                - Files backups and archiving
                - System administration tasks
            - computational tasks:
                - application integration
                -  plug-in and web application development
- A shell script:
    - An executable text file with  an interpretor directive, aka shedbang directive: ![alt text](image.png)
    - Shell scripting directive examples
    ```sh
    #! /bin/sh
    #! /bin/bash
    ```
    - Python scripting directive
    ```sh
    #! /usr/bin/env python3
    ```
    - Hello worls shell script
        - Create the file

        ```sh
        touch hello_world.sh
        ```
        - Edit the file
        ```sh
        #!bin/bash
        echo "Hello World!"
        ```
        - Make the file executable for all users
        ```sh
        chmod +x hello_world.sh
        ```
        - Execute the file
        ```sh
        ./hello_world.sh
        ```

## Reading: A Brief Introduction to Shell Variables 

[A Brief Introduction to Shell Variables](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1MWDAxMTdFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvdjRfbmV3X2NvbnRlbnQvbGFicy9yZWFkaW5ncy9NM19BX0JyaWVmX0ludHJvZHVjdGlvbl90b19TaGVsbF9WYXJpYWJsZXMubWQiLCJ0b29sX3R5cGUiOiJpbnN0cnVjdGlvbmFsLWxhYiIsImFkbWluIjpmYWxzZSwiaWF0IjoxNzExNjM4NjQwfQ.m3khqoYnWjvom6kBhP68_xb3tkdllQWK_Z4Is8wL9ME)

firstname=John
echo $firstname
read $lastname  or read lastname
echo $lastname
 echo You are $firstname $lastname  

 which bash  fnd the path of the bash cmd: /bin/bash
 the -n option of echo avoid printing the new line character at the end of the string

 ## Filters, Pipes, and Variables

- Filters:
    - Shell commands that takes input from stdin and return output to stdout
    - Ex: wc, cat, head, tail, mmore, less, ls, etc
    - They can be chained together

- pipe comand:
    -  denoted by a vertical slash ie | (vertical bar)
    - a command used to chain a sequences of filters commands together
    - pipe stands for pipeline
    - cmd1 | cmd2 : the ouptut of the command 1 become the input of the command 2
    - Ex: ls | sort -r  to list all files in the current working directory in a reverse order

- Shell variables:
    - Vaariables with a scope limited to the current shell: They can not be accessed from other shell
    - Declaration: my_var=value: note ther is no space around the = sign
    - List shell variales:
        - Use set to list all shell variales with tehir defiitions
        - For ex set | head -4 to see the first 4 shell varaibales with their definitions
    - Remove a variable:
        - unset my_var
        - the variable won't be accessible anymore
- Environment variables:
    - Variables with extended scope
    - They persist in any child processes spawned by the shell in which they originate 
    - To extend a shell variable to env variable use export my_var
    - Tolist env variables, use env

## Readin: Examples of Pipes
[Examples of Pipes](https://www.coursera.org/learn/hands-on-introduction-to-linux-commands-and-shell-scripting/ungradedWidget/RaPeL/reading-examples-of-pipes)

# Useful Features of the Bash Shell
- Metacharacters:
    - The pound symvole for commments diese
    - semicolon; seperate comands typed on the same line
    - asterisc * any consecutive number of characters within a filename patthern
    -  ? a single character within a filename patthern

- Quoting:
    - \ escape unique character interpetation; ex escape $,\ 
    - " " interprets litterally but evaluate metacharacters
    -' ' interprets litterally but do not evaluate metacharacters
    - ![alt text](image-1.png)

- I/0 redirection:
    - A set of features used for redirecting either the standard input, the keyboard, or the standard output, the terminal
    - Symbols:
        - >  redirect output to the file
        - >> append output to the file
        - 2> redirect standard errror to a file ie if the cmd generates an error, do not print it but write it to the specified file: xx 2>fic.tx
        - 2>> append standard errror to a file
        - < redirect file content to stdin
- Command substitution:
    - Replace a commad by its output
    - How? 2 equivalent possiblitie:
        -  $(command) 
        - `command`
    - ex: here=$(pwd) ; echo $here

- Command line arguments:
    - way to pass aruments to shell script
    - Ex: ./script.sh arg1 arg2
- Batch versus concurent modes:
    - bach mode:
        - commands runed in sequential ie one after the other
        - Syntax cmd1; cmd2 
    - concurrent mode:
        - commands executed in parallel ie at the same time ie simulatneously
        - Syntax: cmd1 & cmd2

## Reading: Examples of Bash Shell Features

[Examples of Bash Shell Features](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1MWDAxMTdFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvdjRfbmV3X2NvbnRlbnQvbGFicy9yZWFkaW5ncy9NM19Vc2VmdWxfRmVhdHVyZXNfb2ZfdGhlXy5tZCIsInRvb2xfdHlwZSI6Imluc3RydWN0aW9uYWwtbGFiIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE3MTE2Mzg2NDF9.jKv2XIzmqV5JubTa8JEBBtnL5lAK13Sm7dRSLf8mzXo)

## Reading: Introduction to Advanced Bash Scripting

[Introduction to Advanced Bash Scripting](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1MWDAxMTdFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvRmluYWwlMjBQcm9qZWN0L0ludHJvZHVjdGlvbl90b19BZHZhbmNlZF9CYXNoX1NjcmlwdGluZy5tZCIsInRvb2xfdHlwZSI6Imluc3RydWN0aW9uYWwtbGFiIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE3MTE2Mzg2NDF9.eXIrS1be5yVXJT0Y51u20pRdPalagFy0sl9PH4yhQjY)

### Conditionals and Logical operators
- Conditions:
    - if [[ condition ]]
    - if  then  elif then else fi 
    -

- List of logical operators
    - == if [ value1==value2 ]
    - !=  if [ value1!=value2 ]
    - && if [ condition1 ] && [ condition2 ]
    - || if [ condition1 ] || [ condition2 ]
    - < or -lt 
    - > or -gt
    - <= or -le
    - >= or -ge

```sh
#! /bin/bash

echo -n "yes or no:"

read answer
echo $answer
if  [[ "$answer" == "yes" ]] # necessary spaces around the operator and the braces
then
    echo "You agree"
elif [[ "$answer" = "no" ]] # use == or  simply =
then
    echo "You disagree"
else
echo "Unkown answer($answer)"
fi
```


    
### Arithmetic calculations

- Expressions:
    - $((value1 operator value2))
    - $(($var operator $var2))
    - Examples
    ```sh
    echo ((3+3))
    a=45
    b=58
    echo $(($a + $b))
    c=$(($a + $b))
    echo $c
    ```
- Operators list
    - \+ addition
    - \- subtraction
    - \* multiplication
    - / integer division
    - % modulo
    


```sh
#! /bin/bash

echo -m "Enter two entegers:"
read a
read b
sum=$((a+b))
product=$((a*b))
echo "$a+$b=$sum"
echo "$a*$b=$product"

if [[ $sum == $product ]] # or simply =
then
    echo "Sum equal to product"
elif [[ $sum -gt $product ]]
then
    echo "Sum greater than product"

elif [[ $sum -lt $product ]]
then
    echo "Sum less than product"
fi
```

### Arrays
- Array creation and initialization

my_array=(1 2 "three" "four" 5)

- Print the array

Try to print the array
echo $my_array

This prints just the first item of the array, and not the entire array.

To print the entire array, use

echo ${my_array[@]}

- Acess item ie array indexing

Use indexes to access an item of the array

${my_array[n]} Acess the item at index n
Note that array indexes range from 0 to N-1 where N is the number of items i the array

Ex 

\${my_array[0]} Acess the item at index  0, ie the first item

\${my_array[1]} Acess the item at index  1, ie the second item

Access is for read or modification
echo ${my_array[0]}

To modify an item, use
my_array[1]="new value"
echo ${my_array[@]}

- Get the  size of the array
echo ${#my_array[@]}

- Get the indexes of the array

echo ${!my_array[@]}
- Append item to an array

my_array+=(100)
echo ${my_array[@]}

You can add more than one item at once
my_array+=(200 300 "last")
echo ${my_array[@]}


### for loops
- 2 syntaxes:
    - Syntax one:
    ```sh
    N=6
    for (( i=0; i<=$N; i++ )) ; do
    echo $i
    done
    ```
    - Syntax 2: Browse an array 
        - Browse array  elements
        ```sh
        for item in ${my_array[@]} ; do
        echo $item
        done
        ```
        - Browse array indexes
        ```sh
        for i in ${!my_array[@]} ; do
        echo ${my_array[$i]}
        done
        ```


## Scheduling Jobs using Cron

- System admins, data engineers or even developers may need to schedule jobs that run automatically at certain times
    - Examples: Schedule
        - a load script that runs at midnight every night
        - a backup script to run every sunday at 2 AM
- Cron allows to automate such tasks (on Linux and Unix-line OSs)
- Cron is a service that runs scheduled jobs consiting of shell commands or shell scripts
- Crond is a daemon/service that
    - interprets 'crontab file' every minute
    - submit the corresponding job to Cron at scheduled times 
- Crontab:
    - short for Cron table
    - A file containing jobs and schedule data
    - is also  a command that invokes a text editor to allow you to edit crontab files

    crontab -e open an editor

![alt text](image-2.png)

crontab -l list all cron jobs and their schedules (just print the content of the file)

crontab -l | tail -6  list the fist 6 cron jobs

![alt text](image-3.png)

crontab -r  remove all your cron jobs


### Cheat Sheet: Introduction to Shell Scripting
[Module 3 Cheat Sheet - Introduction to Shell Scripting
](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTS1MWDAxMTdFTi1Ta2lsbHNOZXR3b3JrL2xhYnMvdjRfbmV3X2NvbnRlbnQvbGFicy9yZWFkaW5ncy9NM19DaGVhdF9TaGVldF9JbnRyb190b19TaGVsbF9TY3JpcHRpbmcubWQiLCJ0b29sX3R5cGUiOiJpbnN0cnVjdGlvbmFsLWxhYiIsImFkbWluIjpmYWxzZSwiaWF0IjoxNzExNjM4NjQxfQ.a5rAy3qDmGekAMX0CfgHEIBiX3QDzC9e4UuP9s2idzg)