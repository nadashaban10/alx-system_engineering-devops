the goal if this challenge to move ur images "screenshots of cmd challenge" from ur local machine "ur pc" to remote machine  using SFTP 

first of all ... go to CMD challenge and solve all the questions with the correct answer , then take screenshot after each 9 questions 

once you finished!

1- make a directory named  "command_line_for_the_win" in ur old repo named "alx-system_engineering-devops" 

2- go to open your windows-terminal and put ur SFTP and PASSWORD.

3- using this command to go to ur new directory 

 cd /root/alx-system_engineering-devops/command_line_for_the_win/

4- lets move ur images! by using put command + ur file path 

example : put "C:\Users\TS\Desktop\0-first_9_tasks.png"

5- finalllyyyyyy! push all ur edits and go to your GitHub to see it






WHAT IS SFTP ?

sftp is a file transfer program, similar to ftp(1), which performs all operations over an encrypted ssh(1) transport. It may also use many features of ssh, such as public key authentication and compression.

The destination may be specified either as [user@]host[:path] or as a URI in the form sftp://[user@]host[:port][/path].

If the destination includes a path and it is not a directory, sftp will retrieve files automatically if a non-interactive authentication method is used; otherwise it will do so after successful interactive authentication.

If no path is specified, or if the path is a directory, sftp will log in to the specified host and enter interactive command mode, changing to the remote directory if one was specified. An optional trailing slash can be used to force the path to be interpreted as a directory.

Since the destination formats use colon characters to delimit host names from path names or port numbers, IPv6 addresses must be enclosed in square brackets to avoid ambiguity. 
