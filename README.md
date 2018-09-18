# Linux Path Traversal

Linux path traversal is tool to create unix like virtual file system and roam around in this structure.

  - Supports all basic unix commands
  - Keeps directories in memory
  - Logs out result on console as well as in file


### Usage

Tool requires python 2.7 to run.
```sh
$ git clone .
$ cd linux-path-traversal
```

### Instructions
> Run following commands to create log folder.
> Log configuration can be changed from *logging_config.yaml* file.
> */var/log/traversal/debug.log*  
> */var/log/traversal/warn.log*  
> */var/log/traversal/all.log*
```sh
sudo mkdir -p /var/log/traversal
sudo chown username:username /var/log/traversal
```

### Running
```sh
python traversal
```
Above command gives an interface to run commands in session. User CTRL+C to kill session.
*Note* that application keeps data in memory and killing sessionwill delete all data stored in memory.

### Example
- *mkdir India*  
SUCC: REACHED
- *mkdir Delhi*  
SUCC: CREATED
- *mkdir Mumbai*  
SUCC: CREATED
- *ls*  
DIRS: Delhi Mumbai
- *pwd*  
PATH: /India/Delhi
- *cd /India*  
SUCC: REACHED
- *rm Delhi*  
SUCC: DELETED
- *rm /India/Mumbai*  
SUCC: DELETED
- *cd /*  
SUCC: REACHED
- *ls*  
DIRS: India
- *session clear*  
SUCC: RESET TO HOME!
- *^C*  
Good bye!

# To add new commands
If you want to add more commands to this tool, create a file name under *traversal/cmds* folder with command name. Create a class with filename <Command name in CAPS>Command in it. and you are ready to go!

### Todos
 - Add support of keeping files as well.
 -  Persist data this on disk to avoid failover.
 - Store timezone-aware time in created_at field.
 - Show directory created datetime on *ls* command.
 - Currently subdirectories are stored in a list which makes fetching directory by name *expensive* - **O(N)** time complexity. Use a dictionary/Hash map to store subdirectories.


**Free Software**
