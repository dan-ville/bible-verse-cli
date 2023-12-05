#!/usr/bin/env python3
import argparse
from services.esv_api_service import ESVService

def main():
    parser = argparse.ArgumentParser(description="Retrieve Bible verses from the ESV API.")
    parser.add_argument('-r', '--reference', type=str, help="Bible verse reference (e.g., John 11:35)", default=None)

    args = parser.parse_args()

    esv_service = ESVService()
    
    if args.reference:
        # Get the verse via the reference
        verse = esv_service.get_bible_verse(args.reference)
        print(verse)
    else:
        # Handle the case where no reference is provided
        print("No reference provided. Please provide a Bible verse reference.")

if __name__ == "__main__":
    main()
