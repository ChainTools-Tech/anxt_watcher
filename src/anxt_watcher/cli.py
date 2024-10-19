import argparse

def get_cli_args():
    """Handles command-line arguments."""
    parser = argparse.ArgumentParser(description="Check the status of Jelurida nodes (Ardor and NXT).")
    parser.add_argument('--file', required=True, help="Path to the file containing the list of hosts")
    return parser.parse_args()
