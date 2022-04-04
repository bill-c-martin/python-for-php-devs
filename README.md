<!-- omit in toc -->
# Python: for PHP Developers

Supplementary repo for my "Python for PHP Developers: Deep Dive" series of articles, which provide a in-depth review of Python from a PHP developer's prespective:

- [Python for PHP Developers: Deep Dive Part 1](https://billmartin.io/blog/python-for-php-developers-part-1)
- [Python for PHP Developers: Deep Dive Part 2](https://billmartin.io/blog/python-for-php-developers-part-2)

This repo is useful to tinker with the same code examples used in these articles.

## Install Python and Friends

In Ubuntu:

```bash
sudo apt update
sudo apt -y upgrade

# Confirm python 3.* is installed, else install it
python3 -V

# Get le friends too
sudo apt install -y python3-pip
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
```

### Setup Virtual Environment

Install `venv`:

```bash
sudo apt install -y python3-venv
```

Clone this repo, and in the root directory, setup a virtual environment:

```bash
python3 -m venv env
```

Activate the virtual environment:
```bash
source env/bin/activate
```

Test run one of the `.py` files in this repo:

```bash
python3 code/01-hello.py
```

To exit the virtual environment:

```bash
deactivate
```

