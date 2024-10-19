def parse_data(host, data):
    if data:
        return {
            "Host": host,
            "Application": data.get("application", "N/A"),
            "Version": data.get("version", "N/A"),
            "Blockchain State": data.get("blockchainState", "N/A"),
            "Number of Blocks": data.get("numberOfBlocks", "N/A"),
            "Is Offline": data.get("isOffline", "N/A"),
            "Services": ", ".join(data.get("services", [])),
            "Max Memory": data.get("maxMemory", "N/A"),
            "Free Memory": data.get("freeMemory", "N/A"),
            "Is Testnet": data.get("isTestnet", "N/A"),
            "Is Light Client": data.get("isLightClient", "N/A"),
            "Is Downloading": data.get("isDownloading", "N/A"),
            "Is Scanning": data.get("isScanning", "N/A"),
            "Number of Connected Peers": data.get("numberOfConnectedPeers", "N/A"),
        }
    else:
        return {
            "Host": host,
            "Application": "ERROR",
            "Version": "ERROR",
            "Blockchain State": "ERROR",
            "Number of Blocks": "ERROR",
            "Is Offline": "ERROR",
            "Services": "ERROR",
            "Max Memory": "ERROR",
            "Free Memory": "ERROR",
            "Is Testnet": "ERROR",
            "Is Light Client": "ERROR",
            "Is Downloading": "ERROR",
            "Is Scanning": "ERROR",
            "Number of Connected Peers": "ERROR",
        }
