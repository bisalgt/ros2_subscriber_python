

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from sensor_msgs.msg import PointCloud2
from sensor_msgs_py import point_cloud2
import numpy as np
# import rosbag
# import ros_numpy
# import sensor_msgs




class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            PointCloud2,
            '/carla/ego_vehicle/lidar',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.i = 0

    def listener_callback(self, msg):
        
        # self.get_logger().info('I heard: "%s"' % msg.data)
        self.get_logger().info(f'Loop : {self.i}')
        self.get_logger().info('I heard data')
        # print(dir(msg.data))
        print("00000000000000000000000000")
        print(type(msg.data))
        print(type(msg))

        pcd_data = point_cloud2.read_points(msg, skip_nans=True)
        points = np.array(list(pcd_data))
        print(type(points[0]))

        

        # pcd_data = point_cloud2.read_points(msg.data)

        # saving a file working using numpy
        # points = np.array(msg.data)
        np.savetxt(f"lidar_data/frame_{self.i}.csv", points, delimiter=",")

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


if __name__ == '__main__':
    main()
