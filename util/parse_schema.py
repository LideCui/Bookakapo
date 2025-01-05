#!/usr/bin/env python3

import argparse
import re

# Function to parse the SQL schema and convert to Markdown
def sql_to_markdown(sql):
    # Regex to capture table name and columns
    table_re = re.compile(r"CREATE TABLE\s+`?(\w+)`?\s*\(([^;]+)\);", re.IGNORECASE | re.DOTALL)
    column_re = re.compile(r"`?(\w+)`?\s+(\w+\([0-9,]+\)|\w+)(?:\s+(NOT NULL|NULL))?", re.IGNORECASE)

    markdown_tables = []
    
    # Iterate over each table found in the SQL schema
    for table_match in table_re.finditer(sql):
        table_name = table_match.group(1)
        columns_part = table_match.group(2)
        
        # Create a Markdown table header
        markdown = f"### Table: `{table_name}`\n\n"
        markdown += "| Column Name | Data Type | Nullable |\n"
        markdown += "|-------------|-----------|----------|\n"

        # Process each column in the table
        for column_match in column_re.finditer(columns_part):
            column_name = column_match.group(1)
            data_type = column_match.group(2)
            nullable = column_match.group(3) or "NULL"
            
            # Add each column to the Markdown table
            markdown += f"| {column_name} | {data_type} | {nullable} |\n"
        
        markdown_tables.append(markdown)
    
    return "\n".join(markdown_tables)

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description="Convert SQL schema to Markdown tables.")
    parser.add_argument("input", help="Input SQL file")
    parser.add_argument("-o", "--output", help="Output Markdown file", default=None)
    
    args = parser.parse_args()
    
    # Read the input SQL file
    with open(args.input, 'r') as sql_file:
        sql_content = sql_file.read()
    
    # Convert SQL to Markdown
    markdown_output = sql_to_markdown(sql_content)
    
    # Write output to a file or print it
    if args.output:
        with open(args.output, 'w') as md_file:
            md_file.write(markdown_output)
        print(f"Markdown table written to {args.output}")
    else:
        print(markdown_output)

# Entry point of the script
if __name__ == "__main__":
    main()
