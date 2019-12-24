# Cookiecutter Data Science

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._

Adapted from https://github.com/drivendata/cookiecutter-data-science

### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter https://github.com/drivendata/cookiecutter-data-science.git

### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile             <- Contains instructions for command line execution
├── README.md
├── data                 <- Base data directory, no data will be directly held under this folder
│   ├── archive          <- Archived data that is not in use, out of date or no longer needed.
│   ├── interim          <- Intermediate data that has been transformed, this could be data that is undergoing staging but is not yet ready for models or to be cut for presentations
│   ├── processed        <- Final data ready for training models, or scoring models, doing data cuts
│   └── raw              <- Original data from clients and/or third party, this data is raw form and could include dictionaries
├── docs                 <- A default Sphinx project; see sphinx-doc.org for details
│   ├── Makefile
│   ├── commands.rst
│   ├── conf.py
│   ├── getting-started.rst
│   ├── index.rst
│   └── make.bat
├── model                <- If only one tool is used then files can be stored directly under folder
│   ├── llamasoft        <- For Llamasoft models this is self-contained file that holds code and data.
│   ├── python
│   ├── r
│   └── spss
├── output
│   ├── log              <- Log files if scripts have developed to capture error messaging that might occur
│   └── results          <- Model output, could include model output such as coefficient values, t-tests, variable importance, accuracy statistics etc
│       ├── predict      <- Sub folder for capturing predictions
│       └── visuals
│           ├── figures  <- Sub folder for figures created as part of the model development and evaluation, might be diagnostic plots or variable importance plots
│           └── tableau  <- Dashboards created show insights on models
├── requirements.txt
├── setup.py
├── src
│   ├── assets           <- Store here data dictionaries, modalities mapping, etc...
│   ├── data             <- Data pipelines, merging and preparation and feature engineering scripts
│   ├── environement     <- Environment directory contains docker containers used to create either r or python sandbox environments, anaconda environments, R environment (R version and package versions).
│   ├── explore          <- Notebooks/scripts used in the initial exploration and discovery phase
│   ├── main             <- Scripts that spawn other scripts such as data prep, model training and interference and testing
│   ├── model            <- Model training, hyper parameter tuning, evaluation and prediction scripts
│   ├── test             <- Test scripts used to run through scenarios to ensure scripts are fit for purpose
│   └── utils            <- Scripts that don't fit into the other categories
├── test_environment.py
└── tox.ini
```

## Contributing

We welcome contributions! [See the docs for guidelines](https://drivendata.github.io/cookiecutter-data-science/#contributing).

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
