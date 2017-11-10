Udacity Logs Analysis Project
========================


The task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database

----------


Requirements and Setup
-------------
To execute the Logs Analysis application successfully requires a virtual machine to be setup, using Virtualbox and Vagrant. The commands needs to also be executed from within a Shell Terminal such as Git Bash or Cmder.

#### <i class="icon-hdd"></i>  Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. You can [download it from virtualbox.org, here][1]. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

Currently (October 2017), the supported version of VirtualBox to install is version 5.1. Newer versions do not work with the current release of Vagrant.

Ubuntu users: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need 
#### <i class="icon-hdd"></i>  Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. [Download it from vagrantup.com][2]. Install the version for your operating system.

> **Windows users:**  The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.



#### <i class="icon-upload"></i> Start the Virtual Machine

From your terminal, inside the `LogsAnalysis_Udacity` directory , run the command `vagrant up`. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM.

> **Windows users:**  if running 'vagrant up' hangs indefinitely, you may have to upgrade 'Windows Powershell'. Executing the 'vagrant up' command has minimum requirement of Windows  Powershell Version 3.0 </


#### <i class="icon-file"></i> Poplulate Database 

 1. Extract newsdata.zip (newsdata.sql) into working directory
 2. After extraction run `psql newsdata`
 3.  To populate the database with data from newsdata.sql you can either:
- Paste each statement in to psql **OR**
    - Use the command `\i newsdata.sql` to import the whole file into psql at once

#### <i class="icon-file"></i> Create Views

You can create the views in 3 ways:
 1. From within psql terminal run command `\i createviews.sql`**OR**
 2. Run command `python createviews.py` inside terminal but outside of psql (to exit psql run command `\q`)
 3.  Copy and paste data from createviews.sql into psql terminal.
 

#### <i class="icon-folder-open"></i> Running the Application

1. Inside the terminal run the command `python newsdata.py`
2. After running the command a new file called `logoutput.txt` should be created within working directory answering the 3 questions Required from the analysis, namely:

> **Questions:**

> 1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
> 2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top
> 3. On which days did more than 1% of requests lead to errors?

[1]: https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
[2]: https://www.vagrantup.com/downloads.html


