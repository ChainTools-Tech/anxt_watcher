import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from tabulate import tabulate
from tqdm import tqdm
from anxt_watcher.logger import configure_logging
from anxt_watcher.fetcher import fetch_data
from anxt_watcher.parser import parse_data
from anxt_watcher.utils import read_hosts, sort_data
from anxt_watcher.cli import get_cli_args


def main():
    # Configure logging
    configure_logging()

    # Parse command-line arguments
    args = get_cli_args()

    # Read host file
    hosts = read_hosts(args.file)
    all_data = []

    logging.info(f"Total hosts to query: {len(hosts)}")

    # Fetch data from hosts
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fetch_data, host): host for host in hosts}

        # Use tqdm for progress bar
        with tqdm(total=len(hosts), desc="Processing hosts") as pbar:
            for future in as_completed(futures):
                host = futures[future]
                data = future.result()
                parsed_data = parse_data(host, data)
                all_data.append(parsed_data)
                pbar.update(1)

    # Sort and display the data
    all_data_sorted = sort_data(all_data)

    if all_data_sorted:
        table = tabulate(all_data_sorted, headers="keys", tablefmt="grid")
        print(table)
    else:
        logging.warning("No data available from any host")


if __name__ == "__main__":
    main()
