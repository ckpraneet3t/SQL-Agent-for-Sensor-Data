import xarray as xr

try:
    nc_path = r'C:\Users\apran\Videos\Cin\LIBRARY\SQL Agent for Sensor Data\cmems_mod_glo_phy_anfc_0.083deg_PT1H-m_1756878552683.nc'
    csv_path = r'ocean_data.csv'

    print("Opening NetCDF file...")
    with xr.open_dataset(nc_path) as ds:
        print("Converting to DataFrame... This might take a while for large files.")
        df = ds.to_dataframe()
    
    df.reset_index(inplace=True)
    
    print(f"Saving DataFrame to {csv_path}...")
    df.to_csv(csv_path, index=False)
    
    print("\nConversion complete.")
    print(f"CSV file saved at: {csv_path}")

except FileNotFoundError:
    print(f"Error: The file was not found at the specified path:\n{nc_path}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")