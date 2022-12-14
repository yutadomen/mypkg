# SPDX-FileCopyrightText: 2022 Yuta Domen
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener():
    def __init__(self):
        self.pub = node.create_subscription(Int16, "countup", cb, 10)

def cb(msg):
    node.get_logger().info("Listen: %s" % msg.data)

rclpy.init()
node = Node("listener")
listener = Listener()
rclpy.spin(node)
