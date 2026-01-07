import logging
import argparse
import os
from config_loader import load_config
from data_loader import load_csv
from validator import validate_columns
from notifier import send_alert
from transformer import normalize_salary

def setup_logger(log_file, level):
    log_dir = os.path.dirname(log_file) 
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    logging.basicConfig(
        filename=log_file,
        level=getattr(logging, level),
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def main():
    # 1. Setup Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    try:
        # 2. Load Configuration
        config = load_config(args.config)
        
        # 3. Setup Logging
        setup_logger(config["logging"]["file"], config["logging"]["level"])
        logging.info("Application started")

        # 4. Core Logic Block
        df = load_csv(config["data_source"]["path"])
        
        # Validation
        validate_columns(df, config["validation"]["required_columns"])
        logging.info("Validation successful.")

        # Transformation
        df = normalize_salary(df)
        logging.info("Transformation completed: Salary data normalized.")
        print("Data cleaned successfully.")

        # 5. Success!
        logging.info("Process completed successfully.")

    except FileNotFoundError as e:
        error_msg = f"File missing: {e}"
        logging.error(error_msg)
        send_alert(error_msg)
        
    except ValueError as e:
        error_msg = f"Data validation error: {e}"
        logging.error(error_msg)
        send_alert(error_msg)

    except Exception as e:
        # THE GLOBAL CATCH-ALL
        error_msg = f"UNEXPECTED CRASH: {str(e)}"
        logging.error(error_msg)
        send_alert(error_msg)

if __name__ == "__main__":
    main()