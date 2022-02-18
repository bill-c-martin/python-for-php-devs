

## Instal Python and friends

```bash
sudo apt update
sudo apt -y upgrade
python3 -V
sudo apt install -y python3-pip
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
sudo apt install -y python3-venv
```

## Boot Up Virtual Environment

`python3 -m venv my_env` was used to create virtual environment in `environments/my_env/`.

So run:

```bash
source environments/my_env/bin/activate
```

To exit virtual env:

```bash
deactivate
```

## Begin

[here](https://www.learnpython.org/)
