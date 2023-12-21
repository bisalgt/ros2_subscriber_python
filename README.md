# Subscriber of ros topic for saving lidar sensor


- Resource ros2 (foxy) setup file in current terminal `source /opt/ros/foxy/setup.bash`

- On the root of pkg, check if dependencies are all meet using rosdep `rosdep install -i --from-path src --rosdistro foxy -y`

- Everytime changes are made, ros2 package must be rebuild using `colcon build --packages-select py_subscriber` (Need to source ros2 environment )

- Need to resource the created pkg setup file in a new terminal before being able to run the package. `source path_to_pkg_root/install/setup.bash`

- pkg can run using `ros2 run py_subscriber listener`

- Data will be saved to lidar_data folder in csv format. Contains all data from lidar [x, y, z, intensity in our case.]




## System Setup

- Os - Ubuntu 20.04

- carla 0.9.13 (packaged version)

- ros2 foxy for ubuntu 20.04

- carla-ros-bridge (build from source and sourcing as `source ~/carla-ros-bridge/install/setup.bash`). We need to source everytime in a terminal if we use carla_ros_bridge

- Running an ego vehicle on the terminal where ros-bridge was sourced using `ros2 launch carla_ros_bridge carla_ros_bridge_with_example_ego_vehicle.launch.py`

- By default lidar sensor is attached to the vehicle, the lidar sensor publishes data to ros2 topic `/carla/ego_vehicle/lidar` . We can view in Rviz using `ros2 run rviz2 rviz2` and subscribing to the appropriate topic. [Need to fix the Fixed Frame issue in Rviz by subscribing to appropriate topic `ego_vehicle/lidar` so that we can visualize the current lidar data and not a fixed place data]

- The data can be visualized from the lidar sensor, which can be view using ros2 command `ros2 topic echo /carla/ego_vehicle/lidar`. Can also use `rqt_graph` on the terminal to visualize the node.