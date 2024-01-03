#COMMANDS
1-to dissplays the PID >> echo "$$" 
-------------------------------------------------
2-to displays a list of currently running processes. >> ps -auxf
    -a	All processes
    -u	User-oriented information
    -x	Processes not attached to a terminal
    -f	Full format of process information
    ------------------------------------------------
3-
  >>  ps -aux | grep bash 
ps -aux: This part of the command displays information about all processes (-a), including those owned by other users (-u), and in a user-oriented format (-x).

|: The pipe symbol sends the output of the previous command (ps -aux) as input to the next command.

grep bash: This part uses the grep command to filter the output from ps -aux and only display lines that contain the word "bash."
----------------------------------------------------
5-Key Differences between (grep) and (pgrep):

Target: grep operates on text, while pgrep operates on processes.
Input: grep handles text patterns and files, while pgrep takes patterns and process-related options.
Output: grep displays matching lines, while pgrep prints PIDs.
Applications: grep is used for analyzing textual data, while pgrep is mainly used for managing processes.
-----------------------------------------------------
