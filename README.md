# ANXT Watcher

ANXT Watcher is a command-line tool designed to monitor **Jelurida nodes** running on the **Ardor** and **NXT** blockchains. It collects real-time information about the status of nodes, including their application version, blockchain state, number of blocks, and other critical metrics.

## Features

- Monitor multiple Ardor and NXT nodes via HTTP/HTTPS.
- Automatically detect node availability and fall back to HTTPS if HTTP fails.
- Color-coded status for quick visual insights into the node's blockchain state.
- Support for displaying key metrics, including application type, node version, memory usage, and connected peers.
- Multithreaded architecture for fast and efficient data fetching from multiple nodes.

## Color-Coded Blockchain State

The tool provides a color-coded **Blockchain State** for easier status monitoring:

- **Green**: `UP_TO_DATE` (Node is up to date with the latest block).
- **Yellow**: `DOWNLOADING` (Node is currently downloading blocks).
- **Red**: `ERROR` (Node is not responding or an error occurred).

## Installation

ANXT Watcher is available as a Python package. It requires Python 3.6 or higher.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/anxt_watcher.git
cd anxt_watcher
```

2. Set Up a Virtual Environment (Optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the Package

```bash
pip install .
```

**Usage**

Once installed, you can use the anxtwatch command to monitor your nodes. You will need to provide a file with a list of node hosts (one host per line).
Example Host File (hosts.txt)

```
node1.example.com
node2.example.com
node3.example.com
```

**Running ANXT Watcher**

```bash
anxtwatch --file hosts.txt
```

This will fetch the status of all nodes listed in hosts.txt and display the results in a table format.
Example Output

```
+-------------------+-------------+---------+-------------------+------------------+-------------+---------------------+--------------+--------------+-------------+----------------+-----------------+--------------+--------------------------+
| Host              | Application | Version | Blockchain State   | Number of Blocks | Is Offline  | Services            | Max Memory   | Free Memory  | Is Testnet  | Is Light Client| Is Downloading  | Is Scanning  | Number of Connected Peers |
+-------------------+-------------+---------+-------------------+------------------+-------------+---------------------+--------------+--------------+-------------+----------------+-----------------+--------------+--------------------------+
| node1.example.com | Ardor       | 2.5.0   | UP_TO_DATE         | 3637445          | False       | PRUNABLE, API, CORS | 8386510848   | 3522470416   | False       | False          | False           | False        | 14                       |
| node2.example.com | ERROR       | ERROR   | ERROR              | ERROR            | ERROR       | ERROR               | ERROR        | ERROR        | ERROR       | ERROR          | ERROR           | ERROR        | ERROR                    |
| node3.example.com | NXT         | 1.12.0  | DOWNLOADING        | 2000000          | False       | API, CORS           | 4193255424   | 1000000000   | False       | False          | True            | False        | 10                       |
+-------------------+-------------+---------+-------------------+------------------+-------------+---------------------+--------------+--------------+-------------+----------------+-----------------+--------------+--------------------------+
```

**Configuration**

Hosts File: The tool accepts a list of node hostnames or IP addresses in a file. Each host should be listed on a new line.

Supported Protocols: The tool first attempts to connect via HTTP. If the connection fails, it falls back to HTTPS.

**License**

ANXT Watcher is licensed under the MIT License. See the LICENSE file for more details.


---
Internal tag: 001
