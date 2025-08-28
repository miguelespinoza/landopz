#!/usr/bin/env python3
"""
Filter out records with excluded keywords in Owner Name(s) column
"""

import pandas as pd
import os
import sys

# Keywords to exclude from Owner Name(s) column
EXCLUDE_KEYWORDS = [
    'LLC', 'INC', 'CORP', 'LTD', 'LP', 'COMPANY', 'ENTERPRISES', 'HOLDINGS',
    'INVESTMENTS', 'DEVELOPMENT', 'VENTURES', 'CHURCH', 'BAPTIST', 'METHODIST',
    'CATHOLIC', 'TEMPLE', 'SYNAGOGUE', 'MOSQUE', 'MINISTRY', 'PARISH',
    'CONGREGATION', 'DIOCESE', 'COUNTY', 'CITY', 'STATE', 'FEDERAL',
    'GOVERNMENT', 'MUNICIPAL', 'SCHOOL DISTRICT', 'WATER AUTHORITY',
    'HOUSING AUTHORITY', 'ELECTRIC', 'POWER', 'UTILITY', 'PIPELINE',
    'TELECOM', 'CABLE', 'TRANSMISSION', 'SUBSTATION', 'TIMBER', 'FORESTRY',
    'LUMBER', 'PULP', 'PAPER COMPANY', 'REAL ESTATE', 'REALTY', 'REALTOR',
    'BROKER', 'PROPERTY MANAGEMENT', 'LAND COMPANY', 'YMCA', 'PARTNERSHIP',
    'TOWN OF', 'TEXTILE', 'INVESTMENT', 'FAMILY TRUST'
]

def filter_owner_names(input_file, output_dir):
    """
    Filter CSV file to remove records with excluded keywords in Owner Name(s) column
    """
    # Read CSV file
    print(f"Reading {input_file}...")
    df = pd.read_csv(input_file)
    
    print(f"Total records before filtering: {len(df)}")
    
    # Check if Owner Name(s) column exists
    owner_col = None
    for col in df.columns:
        if 'owner' in col.lower() and 'name' in col.lower():
            owner_col = col
            break
    
    if not owner_col:
        print("Error: Could not find Owner Name(s) column")
        print(f"Available columns: {list(df.columns)}")
        return
    
    print(f"Using column: {owner_col}")
    
    # Create mask to exclude records with keywords
    mask = pd.Series([True] * len(df))
    excluded_records = []
    
    for keyword in EXCLUDE_KEYWORDS:
        # Case-insensitive search for keyword
        keyword_mask = df[owner_col].str.contains(keyword, case=False, na=False)
        excluded_count = keyword_mask.sum()
        if excluded_count > 0:
            print(f"Excluding {excluded_count} records containing '{keyword}'")
            excluded_records.extend(df[keyword_mask][owner_col].tolist())
        mask = mask & ~keyword_mask
    
    # Apply filter
    filtered_df = df[mask]
    
    print(f"Records after filtering: {len(filtered_df)}")
    print(f"Records removed: {len(df) - len(filtered_df)}")
    
    # Create output filename
    input_filename = os.path.basename(input_file)
    output_filename = input_filename.replace('.csv', '-scrubbed.csv')
    output_path = os.path.join(output_dir, output_filename)
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Delete existing scrubbed file if it exists
    if os.path.exists(output_path):
        os.remove(output_path)
        print(f"Deleted existing file: {output_path}")
    
    # Save filtered data
    filtered_df.to_csv(output_path, index=False)
    print(f"Filtered data saved to: {output_path}")
    
    # Save excluded records for review
    if excluded_records:
        excluded_filename = input_filename.replace('.csv', '-excluded.txt')
        excluded_path = os.path.join(output_dir, excluded_filename)
        with open(excluded_path, 'w') as f:
            f.write("Excluded Owner Names:\n")
            f.write("=" * 50 + "\n")
            for name in set(excluded_records):  # Remove duplicates
                f.write(f"{name}\n")
        print(f"Excluded names saved to: {excluded_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python filter-owner-names.py <input_csv_file>")
        print("Example: python filter-owner-names.py ../data/gaston-county-nc-land-insights-aug-28-2025.csv")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Check if file exists
    if not os.path.exists(input_file):
        print(f"Error: File not found: {input_file}")
        sys.exit(1)
    
    # Output directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    output_dir = os.path.join(project_root, 'data', 'scrubbed')
    
    filter_owner_names(input_file, output_dir)

if __name__ == "__main__":
    main()