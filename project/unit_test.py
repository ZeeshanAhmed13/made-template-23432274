# unit_test.py: This Python file will contain unit tests for each stage of the ETL pipeline (extraction, transformation, and loading) and a system test to validate that the output SQLite database file is created.

import unittest
import pandas as pd
import sqlite3
import os
from project.ETL_Pipeline import ETLPipeline

class TestETLPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # Run once for all tests
        self.etl = ETLPipeline()
        self.test_db_name = './data/test_etl_data.db'
        self.test_table_name = 'test_etl_table'

    def test_extraction(self):
        # Test the extraction step
        try:
            crop_df, temperature_df = self.etl.extract()
            # Validate the extracted data
            self.assertIsInstance(crop_df, list, "Crop data should be a list of DataFrames.")
            self.assertTrue(all(isinstance(df, pd.DataFrame) for df in crop_df), "All elements in crop_df should be DataFrames.")
            self.assertIsInstance(temperature_df, pd.DataFrame, "Temperature data should be a DataFrame.")
        except Exception as e:
            self.fail(f"Extraction test failed: {e}")

    def test_transformation(self):
        # Test the transformation step
        try:
            crop_df, temperature_df = self.etl.extract()
            transformed_df = self.etl.transform(crop_df, temperature_df)
            # Validate the transformed data
            self.assertIsInstance(transformed_df, pd.DataFrame, "Transformed data should be a DataFrame.")
            
            # checking the required columns names
            required_columns = ['Country Name', 'Item', 'Element', 'Unit_x', 'Change ', 'Unit_y'] + ["Y" + str(i) for i in range(1970, 2020)] + [str(i) for i in range(1970, 2020)]
            for column in required_columns:
                self.assertIn(column, transformed_df.columns, f"Transformed data should have '{column}' column.")
            
            # Check the data types of specific columns
            col_dtypes = {'Country Name': 'string', 'Item': 'string', 'Element': 'string', 'Change ': 'string'}
            years_dictY_dtype = {f"Y{i}": 'float64' for i in range(1970, 2020)}
            years_dict_dtype = {f"{i}": 'float64' for i in range(1970, 2020)}
            # Merging dictionaries
            expected_dtypes = {**col_dtypes, **years_dictY_dtype, **years_dict_dtype}
            # checking datatypes
            for column, expected_dtype in expected_dtypes.items():
                actual_dtype = str(transformed_df[column].dtype)
                self.assertEqual(actual_dtype, expected_dtype, f"Column '{column}' should be of type '{expected_dtype}', but got '{actual_dtype}'.")

        except Exception as e:
            self.fail(f"Transformation test failed: {e}")

    def test_loading(self):
        # Test the loading step
        try:
            crop_df, temperature_df = self.etl.extract()
            transformed_df = self.etl.transform(crop_df, temperature_df)
            db_name, table_name = self.etl.load(transformed_df, self.test_db_name, self.test_table_name)
            # Validate the loading
            self.assertTrue(os.path.exists(db_name), "Database file should exist.")
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()
            cursor.execute(f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='{table_name}'")
            table_exists = cursor.fetchone()[0] == 1
            conn.close()
            self.assertTrue(table_exists, f"Table '{table_name}' should exist in the database.")
        except Exception as e:
            self.fail(f"Loading test failed: {e}")

    def test_system(self):
        # Test the full ETL pipeline
        if os.path.exists(self.test_db_name):
            os.remove(self.test_db_name)
        transformed_data, db_name, table_name = self.etl.run(self.test_db_name, self.test_table_name)
        # Validate the system test
        self.assertTrue(os.path.exists(db_name), "Database file should be created by the ETL pipeline.")
        self.assertIsInstance(transformed_data, pd.DataFrame, "Transformed data should be a DataFrame.")
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        table_exists = cursor.fetchone()[0] == 1
        conn.close()
        self.assertTrue(table_exists, f"Table '{table_name}' should exist in the database.")

if __name__ == '__main__':
    unittest.main()
