<!-- omit in toc -->
# Python: for PHP Developers

Supplementary repo for my "Python for PHP Developers: Deep Dive" series of articles, which explore Python in depth, but from a PHP developer's perspective:

- [Python for PHP Developers: Deep Dive Part 1](https://billmartin.io/blog/python-for-php-developers-part-1)
- [Python for PHP Developers: Deep Dive Part 2](https://billmartin.io/blog/python-for-php-developers-part-2)
- Python for PHP Developers: Deep Dive Part 3 (pending)
- Python for PHP Developers: Deep Dive Part 4 (pending)

This repo may prove useful for tinkering with the same Python code examples used in these articles.

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

