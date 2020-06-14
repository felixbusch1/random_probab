# random_probab

This script visualizes the number of "ones" within randomly generated binary strings.
So it counts in which of the random generated strings are no 1s, one 1, two 1s etc...
For every value of possible number of 1s in a string we count the appearance. 
The result is plottet in a graph.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip3 install matplotlib numpy
```

## Usage

With default settings (length (l) = 8, number of strings (n) = 128)
```bash
python3 random_probab.py 
```
With non-default settings for example
```bash
python3 random_probab.py -l 8 -n 64
```
