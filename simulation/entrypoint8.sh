#!/bin/bash


echo "Building packages..."
colcon build --symlink-install

echo "Sourcing setup files..."
source /simulator_ws/install/setup.bash
source /opt/ros/humble/setup.bash


# Wait for user input


# Run your ROS 2 launch file or command to start the simulatio

# ros2 run rmoss_gz_base test_chassis_cmd.py --ros-args -r __ns:=/red_standard_robot1/robot_base -p v:=0.5 -p w:=0.5
sleep 5

rviz2