import os
import pandas as pd
import xarray as xr
from sqlalchemy import create_engine

# --- Database Configuration ---
# This will create a single database file named 'netcdf_database.db'
DB_FILE = "netcdf_database.db"
DATABASE_URL = f"sqlite:///{DB_FILE}"
engine = create_engine(DATABASE_URL)

def load_nc_to_db(nc_filepath: str, table_name: str, db_engine):
    """
    Reads a NetCDF file, flattens its multi-dimensional data into a 2D DataFrame,
    and loads it into a new SQL table.
    """
    try:
        print(f"Reading NetCDF file: {nc_filepath}...")
        # Open the dataset using xarray
        with xr.open_dataset(nc_filepath) as ds:
            # The key step: convert the multi-dimensional dataset to a flat pandas DataFrame
            # This turns coordinates (time, depth, lat, lon) into columns
            df = ds.to_dataframe().reset_index()
            
            # Optional: Drop rows where the main variables have no data (NaN)
            # Add or remove variables from this list based on your file
            main_vars = [var for var in ds.data_vars if var not in ds.coords]
            df.dropna(subset=main_vars, how='all', inplace=True)

            print(f"Loading flattened NetCDF data into table '{table_name}'...")
            df.to_sql(table_name, db_engine, if_exists='replace', index=False, chunksize=10000)
            
            print(f"✅ Successfully loaded {len(df)} rows into '{table_name}'.")
    except FileNotFoundError:
        print(f"❌ Error: The file was not found at {nc_filepath}")
        print("Please ensure the path is correct and the file is in that location.")
    except Exception as e:
        print(f"❌ An error occurred while processing the NetCDF file: {e}")

if __name__ == "__main__":
    # --- The path to your NetCDF file is set here ---
    # Using a raw string (r"...") is important for Windows paths
    nc_file = r"C:\Users\apran\Videos\Cin\LIBRARY\SQL Agent for Sensor Data\cmems_mod_glo_phy_anfc_0.083deg_PT1H-m_1756878552683.nc"
    
    # --- The desired name for the table that will hold the ocean data ---
    nc_table_name = 'ocean_data'
    
    if os.path.exists(DB_FILE):
        print(f"Database '{DB_FILE}' already exists. To rebuild it, please delete the file first.")
    else:
        print(f"Creating new database '{DB_FILE}'...")
        load_nc_to_db(nc_filepath=nc_file, table_name=nc_table_name, db_engine=engine)
        print("\nDatabase setup is complete!")