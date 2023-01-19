# hw1-scripting

![Task](https://img.shields.io/badge/task-Scripting-blue.svg)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/ConnorS1110/hw1-scripting/tests.yml?label=Tests&logo=github)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language](https://img.shields.io/github/languages/top/ConnorS1110/hw1-scripting.svg)](https://github.com/ConnorS1110/hw1-scripting)
[![DOI](https://zenodo.org/badge/588966418.svg)](https://zenodo.org/badge/latestdoi/588966418)
![GitHub contributors](https://img.shields.io/github/contributors/ConnorS1110/hw1-scripting?label=Contributors&logo=github)

This program is an argument parser that interprets command-line arguments, and outputs information depending on the flags that are set. A series of pre-made examples are run that run nested functions for each example and determines whether the output of those nested functions is `True` or `False`. Depending on the flags that are set, you can see the output of these test results in the terminal window.

## Instructions

The examples are run from `main.py` in the src directory. To run the code, at the root directory, run the following command in a terminal window:

```
python src/main.py [FLAG] [VALUE]
```

For example, to see the results of all the test cases run:

```
python src/main.py -g all
```

To display help, run:

```
python src/main -h True
python src/main -h HELP
```

## Team Members

- Connor Smith (Unity ID: cpsmith6)
- Ashvin Gaonkar (Unity ID: agaonka2)
- Liwen "Cynthia" Du (Unity ID: ldu2)
