#!/bin/bash


echo "Building packages..."
colcon build --symlink-install

echo "Sourcing setup files..."
source /simulator_ws/install/setup.bash
source /opt/ros/humble/setup.bash


# Run your ROS 2 launch file or command to start the simulation
# ros2 launch rmua19_gazebo_simulator standard_robot_a_test.launch.py
ros2 launch rmua19_gazebo_simulator simple_competition_1v1.launch.py
