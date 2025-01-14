import socket
import struct
import netifaces as ni


def get_local_ip():
    """获取本机IP地址"""
    try:
        # 通过访问一个外部服务器（如8.8.8.8，这是Google的公共DNS服务器）的方式获取本地IP
        # 创建一个UDP空包到外部服务器的任意端口，并获取其源地址（即本地IP）
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))  # 这里使用的地址是Google的公共DNS服务器地址
        local_ip = sock.getsockname()[0]
        sock.close()
        return local_ip
    except Exception as e:
        print(f"Error occurred: {e}")
        return "127.0.0.1"  # 如果出现错误，默认返回回环地址


if __name__ == "__main__":
    # 获取本机IP地址
    LOCAL_IP = get_local_ip()
    print(f"Local IP address: {LOCAL_IP}")
    LOCAL_PORT = 42557
    unicast, multicast, broadcast = (False, True, False)

    # --------------------------------------------------------------------------------------
    if unicast:
        # 单播目标地址和端口
        UNICAST_IP = "192.168.1.100"  # 替换为实际的目标IP地址
        UNICAST_PORT = 54321

        # 创建UDP套接字
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((LOCAL_IP, LOCAL_PORT))

        # 发送数据到单播地址
        message = b"Hello, Unicast!"
        sock.sendto(message, (UNICAST_IP, UNICAST_PORT))

        print(f"Sent message: {message.decode()} to {UNICAST_IP}:{UNICAST_PORT}")

        # 关闭套接字
        sock.close()

    # ------------------------------------------------------------------------------
    if multicast:
        # 组播地址和端口
        MCAST_GRP = "224.1.1.1"
        MCAST_PORT = 5007

        # 创建UDP套接字
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

        # 设置TTL（生存时间）
        ttl = struct.pack("b", 2)  # 设置TTL为1，表示数据包最多可以经过1个路由器
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
        sock.bind((LOCAL_IP, LOCAL_PORT))

        # 发送数据到组播地址
        message = b"Hello, Multicast!"
        sock.sendto(message, (MCAST_GRP, MCAST_PORT))

        print(
            f"Sent message: {message.decode()} to {MCAST_GRP}:{MCAST_PORT} with TTL=2"
        )

        # 关闭套接字
        sock.close()

    # -----------------------------------------------------------------------------------
    if broadcast:
        # 广播地址和端口
        BROADCAST_IP = "<broadcast>"  # 使用'<broadcast>'特殊字符串或具体的广播地址如'192.168.1.255'
        BROADCAST_PORT = 34567

        # 创建UDP套接字并设置允许广播
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.bind((LOCAL_IP, LOCAL_PORT))

        # 发送数据到广播地址
        message = b"Hello, Broadcast!"
        sock.sendto(message, (BROADCAST_IP, BROADCAST_PORT))

        print(f"Sent message: {message.decode()} to {BROADCAST_IP}:{BROADCAST_PORT}")

        # 关闭套接字
        sock.close()
