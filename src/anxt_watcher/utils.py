def read_hosts(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def sort_data(data):
    return sorted(data, key=lambda x: x["Host"])
