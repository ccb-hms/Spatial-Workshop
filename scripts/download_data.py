#!/usr/bin/env python
"""Download and extract workshop data."""
import os
import zipfile
import sys

def main():
    """Download and extract spatial workshop data."""
    file_id = "1WGIxjywr3azsdGG4gSKRhlEKKhWPePG5"
    zip_filename = "spatial-workshop-data.zip"
    
    print("Downloading workshop data...")
    # Use gdown to download
    import gdown
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, zip_filename, quiet=False)
    
    print(f"Extracting {zip_filename}...")
    # Extract the zip file to the current directory
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall('.')
    
    print(f"Removing {zip_filename}...")
    # Clean up the zip file
    os.remove(zip_filename)
    
    print("Data download and extraction complete!")

if __name__ == "__main__":
    main()

