# IA_Team_Project

## This project is created as part of M.Sc. in AI for the University of Essex as a Team project

The objective of this project is to watch a source directory and move files based on [SEARCH] criteria given in the ini file that is created as bot.ini when the main program bot_setup.py is executed.

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
criteria1 = *.*<br/>
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

### 2. When the bot is setup as a SERVER, it will move files based on the criteria provided in the the bot.ini file. Here the criteria can be combinations of word search + file type, word search only or file type only. Each criteria must be unique accompanied with a destination directory where it needs to be moved
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
criteria2 = , file_type2, /path/to/destination_directory2<br/>
criteria3 = search_word3, file_type3, /path/to/destination_directory3<br/>
<br/>
[PROCESSES]<br/>
num_processes = 2<br/>
num_processes_scaling_factor = 0.8<br/>
min_processes = 2<br/>
<br/>
[FLAGS]<br/>
stop_flag = False<br/>
