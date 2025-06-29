# HostileHosting
"simple" file hosting alternative to services like nextcloud - PoC





## What should be possible with this software (TODO)

- [X] share a folder with files inside it
    - [ ] download the whole directory inside a .zip file
    - [ ] share it with a password auth
- [X] upload a file
    - [ ] only up to a size
    - [ ] with password auth
- [X] both options together
- [X] serve routes independently 
- [X] routes are available behind hashed values to obfuscate paths
- [X] for now, only through .json config file
- [ ] protect for
    - [X] path traversal with ../../../
    - [ ] symbolic links downloads (link pointing to /home/user/.ssh/id_rsa)
    
