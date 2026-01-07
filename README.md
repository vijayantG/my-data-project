Python Data Automation Framework

This project is a Python application used to run automated data jobs using configuration files.
It shows how real data pipelines are built and executed in a simple and practical way.

## What This Project Does

* Runs data jobs using YAML configuration
* Reads data from CSV files
* Validates and processes the data
* Writes logs for tracking execution
* Sends alerts when a job fails
* Runs from the command line
* Can be executed using Docker

## Project Structure

* `config/` – Job configuration files
* `data/` – Sample input data
* `src/` – Python source code
* `.github/workflows/` – GitHub Actions CI pipeline
* `Dockerfile` – Docker setup
* `requirements.txt` – Python dependencies

## Technologies Used

* Python
* pandas
* argparse
* PyYAML
* logging
* Docker
* GitHub Actions

## How to Run
bash command -  python src/main.py --config config/config.yaml

The job will load data, validate it, process it, and log the results.



