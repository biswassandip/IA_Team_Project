# IA_Team_Project

## This project is created as part of M.Sc. in AI for the University of Essex as a Team project

The objective of this project is to watch a source directory and move files based on [SEARCH] criteria given in the ini file that is created as bot.ini when the main program bot_setup.py is executed.

## Python 3.10.2

## Dependencies

### Package Version<br/>

-------<br/>
altgraph 0.17.3<br/>
bcrypt 4.0.1<br/>
cffi 1.15.1<br/>
colorama 0.4.6<br/>
cryptography 41.0.1<br/>
importlib-metadata 6.7.0<br/>
jaraco.classes 3.2.3<br/>
keyring 24.2.0<br/>
macholib 1.16.2<br/>
more-itertools 9.1.0<br/>
paramiko 3.2.0<br/>
pip 23.1.2<br/>
pycparser 2.21<br/>
pyinstaller 5.13.0<br/>
pyinstaller-hooks-contrib 2023.5<br/>
PyNaCl 1.5.0<br/>
setuptools 58.1.0<br/>
watchdog 3.0.0<br/>
zipp 3.15.0<br/>
<br/>

## How the bot works?

### 1. When the bot is setup as a CLIENT, it will sftp the files to a staging server based on the provided criteria of file types in the bot.ini file

[GENERAL]<br/>
ini_file_path = /abc/def/IA_BOT/bot.ini<br/>
source_dir = /dd<br/>
log_file = /abc/def/IA_BOT/log/bot_log.log<br/>
error_dir = /abc/def/IA_Team_Project/IA_BOT/error<br/>
unmatched_dir = /abc/def/IA_BOT/unmatched<br/>
rotate_logs = True<br/>
rotation_size = 1000000<br/>
<br/>
[CLIENT]<br/>
criteria1 = _._<br/>
<br/>
[SFTP]<br/>
sftp_ip = 22.22.22.22<br/>
sftp_port = 3444<br/>
sftp_path = /dd/<br/>
keystore_service_name = IA_BOT<br/>
keystore_pem_name = PEM_IA_BOT<br/>
private_key_path = /abc/def/IA_BOT/private_key.pem<br/>
<br/>
[FLAGS]<br/>
stop_flag = False<br/>

### 2. When the bot is setup as a SERVER, it will move files based on the criteria provided in the bot.ini file. Here the criteria can be combinations of word search + file type, word search only or file type only. Each criteria must be unique and accompanied with a destination directory where it needs to be moved

<br/>
[GENERAL]<br/>
ini_file_path = /abc/def/IA_BOT/bot.ini<br/>
source_dir = /dd<br/>
log_file = /abc/def/IA_BOT/log/bot_log.log<br/>
error_dir = /abc/def/IA_BOT/error<br/>
unmatched_dir = /abc/def/IA_BOT/unmatched<br/>
rotate_logs = True<br/>
rotation_size = 1000000<br/>
<br/>
[SERVER]<br/>
criteria1 = search_word1, , /path/to/destination_directory1<br/>
criteria2 = , *.pdf, /path/to/destination_directory2<br/>
criteria3 = search_word3, *.txt, /path/to/destination_directory3<br/>
<br/>
[PROCESSES]<br/>
num_processes = 2<br/>
num_processes_scaling_factor = 0.8<br/>
min_processes = 2<br/>
<br/>
[FLAGS]<br/>
stop_flag = False<br/>
<br/>
### 3. To avoid dependencies, the executable in the /dist folder can also be executed and follow the process
<br/>

## How to execute?

Execute the main program <b>bot_setup.py</b>. This will give you the below menu:

=================================================<br/>
BOT SETUP MENU<br/>
=================================================<br/>

1. Client BOT setup<br/>
2. Server BOT setup<br/>
   <br/>
3. Start process<br/>
   <br/>
4. Stop process<br/>
   <br/>
5. Quit<br/>
   <br/>
   Enter your options between 1-5: <br/>
   <br/>
   <br/>
   Option 1 - would create the ini file and required setup for Client setup. After this review the bot.ini file and update it as required.<br/><br/>
   Option 2 - would create the ini file and required setup for Server setup. After this review the bot.ini file and update it as required.<br/><br/>
   Option 3 - now you can start the process and it will start based on the bot.ini configuration. Please note that any update in the ini file after starting processing would require to stop the process by updating <b>stop_flag=True</b> in the bot.ini file.<br/><br/>
   Option 4 - execute the bot_setup.py and when this option is selected then the process will be stopped. Alternatively, to stop the process by updating <b>stop_flag=True</b> in the bot.ini file.<br/><br/>
   Option 5 - will quit the options.<br/><br/>
   <br/>
