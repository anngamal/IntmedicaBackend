# Project Summary

### What I Learned

- Don't create an `__init__.py` file randomly; it will override where `instance/` is created when running Flask database commands with SQLAlchemy. 
    - Specifically, the presence of `__init__.py` inside of the `server/` subdirectory caused `instance/` to be created _outside_ of `server/` instead of inside the folder.