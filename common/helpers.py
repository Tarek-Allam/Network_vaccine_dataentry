from socket import gethostname, gethostbyname


def get_local_ip() -> str:
    host_name = gethostname()
    local_ip = gethostbyname(host_name)
    return local_ip
