import socket
import psutil
from threading import Thread
import netifaces as ni
from collections import defaultdict

# ---------------------------------------------------------------------------


def send_and_receive_data(ifname):
    # 假设我们想要绑定到'eth0'这个网络接口
    # interface_name = "WLAN"

    # 获取该接口的所有地址信息
    iface_addrs = ni.ifaddresses(ifname)

    # 提取IPv4地址（如果有）
    ipv4_addr = iface_addrs[ni.AF_INET][0]["addr"]

    # 选择一个未使用的端口
    port = 12345

    # 创建TCP套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 将套接字绑定到该接口的IP地址和选定的端口
    server_socket.bind((ipv4_addr, port))

    print(f"Server socket bound to {ipv4_addr}:{port}")

    # 开始监听传入连接
    server_socket.listen(5)
    print("Server is listening for incoming connections...")

    # 处理连接（示例代码，通常会放入循环中处理多个连接）
    client_socket, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # 接收数据并发送响应
    data = client_socket.recv(1024)
    print(f"Received data: {data.decode()}")

    client_socket.sendall(b"Hello from server!")

    # 关闭客户端和服务器套接字
    client_socket.close()
    server_socket.close()


def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f"Received request: {request.decode()}")
    client_socket.sendall(b"ACK!")
    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))  # 绑定到所有可用的网络接口
    server.listen(5)
    print("Server started, waiting for connections...")

    while True:
        client, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = Thread(target=handle_client, args=(client,))
        client_handler.start()


def get_active_network_interfaces():
    interfaces = psutil.net_if_addrs()
    active_interfaces = defaultdict(list)

    for interface_name, interface_addresses in interfaces.items():
        # 获取对应接口的状态
        interface_status = psutil.net_if_stats().get(interface_name).isup

        if interface_status:
            for address in interface_addresses:
                # 我们这里只关心IPv4地址
                if address.family == socket.AF_INET:
                    active_interfaces[interface_name].append(address.address)
                if address.family == socket.AF_INET6:
                    active_interfaces[interface_name].append(address.address)

    return active_interfaces

    # net_if_stats = psutil.net_if_stats()

    # for interface_name, stats in net_if_stats.items():
    #     print(f"网卡名称: {interface_name}")
    #     print(f"  是否启动: {stats.isup}")
    #     print(f"  MTU: {stats.mtu}")
    #     print(f"  接收速率: {stats.speed}")
    #     print(f" 双工模式: {stats.duplex}")


if __name__ == "__main__":
    active_interfaces = get_active_network_interfaces()
    print(active_interfaces)
    # send_and_receive_data("WLAN")
    # start_server()
