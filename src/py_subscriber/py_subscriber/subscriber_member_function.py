

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from sensor_msgs.msg import PointCloud2
from sensor_msgs_py import point_cloud2
import numpy as np
# import rosbag
# import ros_numpy
# import sensor_msgs
import sys
import argparse



class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        args = get_args_from_cli()
        self.ros_topic = args.ros_topic
        self.file_prefix = args.save_fileprefix
        self.file_format = args.outputfile_format
        self.subscription = self.create_subscription(
            PointCloud2,
            self.ros_topic,
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.i = 0

    def listener_callback(self, msg):
        
        # self.get_logger().info('I heard: "%s"' % msg.data)
        self.get_logger().info(f'Loop : {self.i}')
        self.get_logger().info('I heard data')
        # print(msg)
        # print(dir(msg))
        # print(msg._fields)
        # print("-------------------------------------------")
        # print(msg.fields)
        # print(dir(msg.fields[0]))
        fields = [field.name for field in msg.fields]
        print(fields)
        fields_str = ','.join(fields)
        # print("-------------------------------------------")


        pcd_data = point_cloud2.read_points(msg, skip_nans=True, field_names=fields)
        points = np.array(list(pcd_data))

        # pcd_data = point_cloud2.read_points(msg.data)

        # saving a file working using numpy
        # points = np.array(msg.data)
        np.savetxt(f"lidar_data/{self.file_prefix}{self.i}.{self.file_format}", points, delimiter=",", header=fields_str)

        # When directly using like this, it gives a different data type so using point_cloud2 is preferable
        # points2 = np.array(msg.data)
        # np.savetxt(f"lidar_data/frame_original_{self.i}.csv", points2, delimiter=",")


        self.get_logger().info("Done Saving to file!")
        self.i += 1
        


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)


    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


def get_args_from_cli():
    parser = argparse.ArgumentParser(
        prog="Listener function to subscribe to topic and save the file",
        description="python program subscribes to a ros2 topic and then saves the file in a csv format",
    )
    parser.add_argument('-t', '--ros-topic', default="/carla/ego_vehicle/lidar")
    parser.add_argument('-s', '--save-fileprefix', default="frame_")
    parser.add_argument('-f', '--outputfile-format', default='csv')
    args = parser.parse_args()
    return args



if __name__ == '__main__':
    main()
