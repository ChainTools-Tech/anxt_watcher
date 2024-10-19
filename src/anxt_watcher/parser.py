import colorama
from colorama import Fore, Style

# Initialize colorama for cross-platform support (Windows, macOS, Linux)
colorama.init(autoreset=True)

def parse_data(host, data):
    """Parse the fetched data and add color based on the blockchain state."""
    if data:
        blockchain_state = data.get("blockchainState", "N/A")

        # Apply color based on the state of the blockchain
        if blockchain_state == "UP_TO_DATE":
            colored_state = f"{Fore.GREEN}{blockchain_state}{Style.RESET_ALL}"
        elif blockchain_state == "DOWNLOADING":
            colored_state = f"{Fore.YELLOW}{blockchain_state}{Style.RESET_ALL}"
        else:
            colored_state = f"{Fore.RED}{blockchain_state}{Style.RESET_ALL}"

        return {
            "Host": host,
            "Application": data.get("application", "N/A"),
            "Version": data.get("version", "N/A"),
            "Blockchain State": colored_state,  # Add the colored blockchain state
            "Number of Blocks": data.get("numberOfBlocks", "N/A"),
            "Is Offline": data.get("isOffline", "N/A"),
            "Services": ", ".join(data.get("services", [])),
            # "Max Memory": data.get("maxMemory", "N/A"),
            # "Free Memory": data.get("freeMemory", "N/A"),
            # "Is Testnet": data.get("isTestnet", "N/A"),
            # "Is Light Client": data.get("isLightClient", "N/A"),
            # "Is Downloading": data.get("isDownloading", "N/A"),
            # "Is Scanning": data.get("isScanning", "N/A"),
            "Number of Connected Peers": data.get("numberOfConnectedPeers", "N/A"),
        }
    else:
        return {
            "Host": host,
            "Application": "ERROR",
            "Version": "ERROR",
            "Blockchain State": f"{Fore.RED}ERROR{Style.RESET_ALL}",  # Color the error state red
            "Number of Blocks": "ERROR",
            "Is Offline": "ERROR",
            "Services": "ERROR",
            # "Max Memory": "ERROR",
            # "Free Memory": "ERROR",
            # "Is Testnet": "ERROR",
            # "Is Light Client": "ERROR",
            # "Is Downloading": "ERROR",
            # "Is Scanning": "ERROR",
            "Number of Connected Peers": "ERROR",
        }
