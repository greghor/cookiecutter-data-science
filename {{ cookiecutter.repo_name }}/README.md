{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
  ------------

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
    ├── references
    ├── requirements.txt
    ├── setup.py
    ├── src
    │   ├── assets
    │   ├── data             <- Data pipelines, merging and preparation and feature engineering scripts
    │   ├── environement     <- Environment directory contains docker containers used to create either r or python sandbox environments, anaconda environments, R environment (R version and package versions).
    │   ├── explore          <- Notebooks/scripts used in the initial exploration and discovery phase
    │   ├── main             <- Scripts that spawn other scripts such as data prep, model training and interference and testing
    │   ├── model            <- Model training, hyper parameter tuning, evaluation and prediction scripts
    │   ├── test             <- Test scripts used to run through scenarios to ensure scripts are fit for purpose
    │   └── utils            <- Scripts that don't fit into the other categories
    ├── test_environment.py
    └── tox.ini

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
