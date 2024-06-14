# # tests.sh: This script will execute the unit tests using Python's unittest framework. It will also run the ETL pipeline and check for the existence of the output file (the SQLite database).


#!/bin/bash

# Set variables
OUTPUT_DB="../data/etl_data.db"
OUTPUT_DB_TEST="../data/test_etl_data.db"
TABLE_NAME="etl_table"
LOG_FILE="etl_pipeline.log"

# Function to display an error message and exit
error_exit() {
    echo "$1" 1>&2
    exit 1
}

Install_Libraries() {
    pip3 install -r requirements.txt
    echo "--------------------------------------------------------------------------"
    echo "Libraries installed successfully"
    echo "--------------------------------------------------------------------------"
}

Checking_KaggleAPI() {
    # Check if Kaggle package is installed
    if pip3 show kaggle >/dev/null 2>&1; then
        echo "Verifying Kaggle API..."
        echo "Kaggle API is installed."
        echo "--------------------------------------------------------------------------"
    else
        echo "Kaggle API is not installed. Please install it using 'pip install kaggle' or visit my github issue: https://github.com/ZeeshanAhmed13/made-template-23432274/issues/7."
        exit 1
    fi
  
}

# Function to clean up before starting 
cleanup() {
    echo "Cleaning up previous artifacts..."
    [ -f "$OUTPUT_DB" ] && rm "$OUTPUT_DB" && echo "Removed existing database: $OUTPUT_DB"
    [ -f "$OUTPUT_DB_TEST" ] && rm "$OUTPUT_DB_TEST" && echo "Removed existing test_database: $OUTPUT_DB_TEST"
    [ -f "$LOG_FILE" ] && rm "$LOG_FILE" && echo "Removed existing log file: $LOG_FILE"
    echo "-------------------------------------------------------------------------"
}

# Function to run unit tests
run_unit_tests() {
    echo "Unit tests are running..."
    python3 -m unittest discover -s . -p 'unit_test.py' || error_exit "Unit tests failed."
}

# Function to run the ETL pipeline
run_etl_pipeline() {
    echo "--------------------------------------------------------------------------"
    echo "Executing the complete ETL pipeline..."
    python3 -c "
from ETL_Pipeline import ETLPipeline
etl = ETLPipeline()
etl.run('../data/etl_data.db', 'etl_table')
" || error_exit "ETL pipeline execution failed."
    [ -f "$OUTPUT_DB_TEST" ] && rm "$OUTPUT_DB_TEST"
}

# Function to validate the output database
validate_output_db() {
    echo "--------------------------------------------------------------------------"
    echo "Validating output database..."
    if [ -f "$OUTPUT_DB" ]; then
        echo "Output file successfully created: $OUTPUT_DB"
        echo "--------------------------------------------------------------------------"
    else
        error_exit "Output file not found: $OUTPUT_DB"
    fi
}

# Function to display logs if they exist
display_logs() {
    if [ -f "$LOG_FILE" ]; then
        echo "Displaying log file:"
        cat "$LOG_FILE"
    fi
}

# Main script execution
main() {
    #Install_Libraries
    Checking_KaggleAPI
    cleanup
    run_unit_tests
    run_etl_pipeline
    validate_output_db
    display_logs
    echo "All tests passed successfully."
}

# Execute the main function
main
