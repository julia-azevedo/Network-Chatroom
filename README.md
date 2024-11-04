# Network Chat-Room
Python-based Chat Room project utilizing sockets, threads and a GUI interface with PySimpleGUI.

## Getting Started
Instructions on how to set up and run the application.

### Server
To start the server, ensure that:
- **Python 3** is installed.

Run the following command in your terminal to start the server:
- `python server.py`
  or
- `python3 server.py`

Once executed, the server will be running and awaiting client connections.

**Note**: The server script is set to allow a maximum of 4 client connections. This limit can be modified by adjusting the `MAX_CLIENTS` constant in the `server.py` script.

### Clients
To join the chat room, each client needs to run the client script. Ensure that:
- **Python 3** is installed;
- **PySimpleGUI** is installed.

To install PySimpleGUI, you may need to use a Python virtual environment. Instructions for setting up a virtual environment are available [here](https://docs.python.org/3/library/venv.html).

With your virtual environment active, install PySimpleGUI using:
- `pip install pysimplegui`
  or
- `pip3 install pysimplegui`

To launch the client, simply run:
- `python client.py`
  or
- `python3 client.py`

Choose a nickname to use in the chat (no spaces allowed), and you’re ready to connect to the chat room!