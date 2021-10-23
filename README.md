# Docker Example

This is an example for setting up a python script with Docker.  This includes Selenium and Headless Chrome.

## Commands

You can build this docker instance with the following command:

```
docker run -it buyer-resist run.py
```

You can run the script using:

```
docker run --rm -it -v "$(pwd):/usr/src/app" buyer-resist run.py
```
