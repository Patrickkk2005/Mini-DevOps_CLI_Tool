**MINI-DEVOPS-CLI**

A command-line tool for common DevOps tasks — system monitoring, Docker management,
log reading, file backups, and task automation.

**INSTALLATION**

(bash) <br>
git clone https://github.com/Patrickkk2005/Mini-DevOps_CLI_Tool <br>
cd mini-devops-cli <br>
pip install .

**FEATURES**

-   System monitoring — CPU, memory, disk usage
-   Docker management — list, start, stop containers
-   Log reader — read and filter log files
-   File manager — copy, backup, and organise files
-   Scheduler — automate recurring DevOps tasks


**USAGE**

devops monitor                # Show CPU, memory, disk usage <br> 
devops monitor --watch 5      # Refresh every 5 seconds

devops docker ps              # List containers <br>
devops docker start <name>    # Start a container <br>
devops docker stop <name>     # Stop a container

devops logs read /var/log/app.log            # Show last 20 lines <br>
devops logs read /var/log/app.log --lines 50 # Show last 50 lines <br>
devops logs filter /var/log/app.log ERROR    # Show only ERROR lines <br>
devops logs filter /var/log/app.log error -i # Case-insensitive filter <br>
devops logs watch /var/log/app.log           # "tail" live (Ctrl+C to stop)

devops files copy src.txt dst.txt     # Copy a file <br>
devops files copy my_folder/ backup/  # Copy a directory <br>
devops files backup app.log           # Create timestamped backup <br>
devops files find /var/log "*.log"    # Find files matching pattern

devops schedule once "echo hello"                    # Run a command once <br>
devops schedule once "echo hello" --delay 10         # Run after 10s delay <br>
devops schedule run "echo hi" --every 5 --times 3    # Run 3 times, every 5s

p.s. to run tests install the pytest library and run: <br>
python -m pytest tests/ -v