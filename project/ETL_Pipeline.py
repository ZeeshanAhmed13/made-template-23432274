import pandas as pd
import sqlite3
import kaggle
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ETLPipeline:
    def __init__(self):
        self.urls = [
            'https://query.data.world/s/3ibkgfh656yrydhmsg4uboxxm7hysr?dws=00000',
            'https://query.data.world/s/2x6uq5jmauvfnmfhc5ud4jv5amq4p6?dws=00000',
            'https://query.data.world/s/nc25wfakg22iva2tmkx4icgfnufggx?dws=00000',
            'https://query.data.world/s/fglgedqxdxc2giqvqgvbjxsqic2tuw?dws=00000',
            'https://query.data.world/s/wva7g5yxspu3bninh4ucn7xrp4h6sc?dws=00000'
        ]
        self.columns_to_string = ['Area', 'Item', 'Element', 'Unit']
        self.columns_to_string1 = ['Country Name', 'Change ', 'Unit']
        self.columns_to_drop = ['Area Code', 'Item Code', 'Element Code'] + [f'Y{i}F' for i in range(1961, 2020)] + [f'Y{i}' for i in range(1961, 1970)]
        self.columns_to_drop1 = ['ObjectId', '2020', '2021']
        self.dataset_kaggle = "mdazizulkabirlovlu/all-countries-temperature-statistics-1970-2021"
        self.csv_file_name = "all countries global temperature.csv"

    def extract(self):
        try:
            # ----------------------------------------------------------------------------------------
            # Extraction --> DataSource-1: Crop Production
            # ----------------------------------------------------------------------------------------
            crop_df = []
            print('---------------------------------------------------------------------------')
            for n, url in enumerate(self.urls):
                try:
                    df = pd.read_csv(url, encoding='latin-1')
                    # append 5 dataframes in total for crop production dataset
                    crop_df.append(df)
                    if n+1 == 5:
                        logging.info(f"Successfully extracted 'Crop Production' data")
                    else:
                        continue
                except Exception as e:
                    logging.error(f"Failed to extract data from {url}: {e}")

            # ----------------------------------------------------------------------------------------
            # Extraction --> DataSource-2: All Countries Temperature Statistics 1970-2021
            # ----------------------------------------------------------------------------------------
            
            # Download the dataset from Kaggle
            kaggle.api.dataset_download_files(self.dataset_kaggle, path='.', unzip=True)
            
            # Check if the file was downloaded and extracted correctly
            if os.path.exists(self.csv_file_name):
                temperature_df = pd.read_csv(self.csv_file_name)
                # Remove the csv file
                os.remove(self.csv_file_name)
                logging.info(f"Successfully extracted 'Temperature Data'")
                print('---------------------------------------------------------------------------')
                
            else:
                raise FileNotFoundError(f"File {self.csv_file_name} not found.")
            
            return crop_df, temperature_df
        
        except Exception as e:
            logging.error(f"An error occurred during extraction: {e}")
            raise

    def transform(self, crop_df, temperature_df):
        try:
            
            # ----------------------------------------------------------------------------------------
            # Transformation --> DataSource-1: Crop Production
            # ----------------------------------------------------------------------------------------

            # list of years            
            Y_years = ["Y" + str(i) for i in range(1970, 2020)]
            crop_dataframes = []

            for df in crop_df:
                try:
                    # Convert specified columns to string type
                    df[self.columns_to_string] = df[self.columns_to_string].astype('string')
                    # Drop unnecessary columns
                    df.drop(columns=self.columns_to_drop, inplace=True)
                    # linear interpolate columns with numeric missing values
                    df[Y_years] = df[Y_years].interpolate(method='linear')
                    crop_dataframes.append(df)
                except Exception as e:
                    logging.error(f"Failed to transform 'Crop Production' data: {e}")
            
            concatenated_df = pd.concat(crop_dataframes, axis=0, ignore_index=True)
            crop_concatenated_df = concatenated_df.rename(columns={'Area': 'Country Name'})
            
            # ----------------------------------------------------------------------------------------
            # Transformation --> DataSource-2: All Countries Temperature Statistics 1970-2021
            # ----------------------------------------------------------------------------------------

            # list of years            
            years = [str(i) for i in range(1970, 2020)]
            # Drop unnecessary columns from temperature_df
            temperature_df.drop(columns=self.columns_to_drop1, inplace=True)
            # Convert specified columns to string type
            temperature_df[self.columns_to_string1] = temperature_df[self.columns_to_string1].astype('string')
            # linear interpolate columns with numeric missing values
            temperature_df[years] = temperature_df[years].interpolate(method='linear')

            # ----------------------------------------------------------------------------------------
            
            # Transformation --> Merging DataSource-2 & DataSource-2
            transformed_df = pd.merge(crop_concatenated_df, temperature_df, on='Country Name', how='inner')
            # Forward filling with remaining missing values
            transformed_df = transformed_df.interpolate(method='ffill')
            # Filtered crops of interest
            transformed_df = transformed_df[(transformed_df['Item'].isin(['Maize', 'Wheat', 'Rice, paddy','Sugar cane','Potatoes','Coconuts','Grapes', 'Dates']))].reset_index()


            return transformed_df
        
        except Exception as e:
            logging.error(f"An error occurred during transformation: {e}")
            raise

    def load(self, dataframe, db_name, table_name):
        try:
            # Connect to SQLite database
            conn = sqlite3.connect(db_name)
            # Store the dataframe in the specified table
            dataframe.to_sql(table_name, conn, if_exists='replace', index=False)
            logging.info(f"Loading completed, data saved to database '{db_name}' in table '{table_name}'.")
        except Exception as e:
            logging.error(f"An error occurred during loading: {e}")
            raise
        finally:
            # Close the connection
            conn.close()
        return db_name, table_name            
            
        
    def run(self, db_name, table_name):
        try:
            crop_df, temperature_df = self.extract()
            logging.info("Extraction completed.")
            
            transformed_data = self.transform(crop_df, temperature_df)
            logging.info("Transformation completed.")
            
            db_name, table_name = self.load(transformed_data, db_name, table_name)
            logging.info("ETL process completed successfully.")
            
        except Exception as e:
            logging.error(f"An error occurred during the ETL process: {e}")
                         
        return transformed_data, db_name, table_name


# Running the ETL pipeline
etl = ETLPipeline()
transformed_data, db_name, table_name = etl.run('../data/etl_data.db', 'etl_table')

'''
from etl_pipeline import ETLPipeline

# Running the ETL pipeline
etl = ETLPipeline()
transformed_data, db_name, table_name = etl.run('etl_data.db', 'etl_table')
''' 