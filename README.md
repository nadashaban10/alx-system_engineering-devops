Postmortem: Apache 504 Error Incident

Summary: On April 15th, 2024, at midnight (PST), the server experienced a 504 error

Timeline:

00:00 PST: 500 error observed for website access.
00:05 PST: Confirmed Apache and MySQL status.
00:10 PST: Website not loading correctly despite server and database functioning.
00:12 PST: Apache server restart resulted in successful curl test (status 200 OK).
00:18 PST: Error logs reviewed for insights.
00:25 PST: Identified premature shutdown of Apache in /var/log without PHP error logs.
00:30 PST: Enabled PHP error logging in php.ini.
00:32 PST: Restarted Apache and reviewed PHP error logs.
00:36 PST: Discovered mistyped file name in wp-settings.php.
00:38 PST: Fixed file name and restarted Apache.
00:40 PST: Server and website resumed normal operation.
Root Cause and Resolution:
The root cause was a misspelled file name referenced in wp-settings.php, triggering a 500 error. Initial investigation found PHP error logging disabled, hindering error identification. Enabling PHP error logging and reviewing logs revealed the misspelling issue. A Puppet script was deployed to correct the file name across servers, resolving the issue.

Corrective and Preventive Measures:

Enable error logging on all servers and sites for easier error identification.
Conduct local testing before multi-server deployment to catch and correct errors early, reducing downtime risk.
