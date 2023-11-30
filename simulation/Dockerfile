# Use a ROS 2 Humble base image for arm64 architecture
FROM osrf/ros:humble-desktop

# Set the maintainer label
LABEL maintainer="Zhenpeng Ge <zhenpeng.ge@qq.com>"

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ignition-fortress \
    libignition-cmake2-dev \
    ros-humble-ros-gz \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies if there are any (not provided in the info but just in case)
# RUN pip3 install <python-package-name>

# Set up ROS2 workspace
RUN mkdir -p /simulator_ws/src

WORKDIR /simulator_ws/src

# Clone necessary repositories
RUN git clone https://github.com/robomaster-oss/rmoss_gazebo.git -b humble
RUN git clone https://github.com/robomaster-oss/rmoss_interfaces.git -b humble
RUN git clone https://github.com/robomaster-oss/rmoss_core.git -b humble
RUN git clone https://github.com/robomaster-oss/rmoss_gz_resources.git -b humble --depth=1
RUN git clone https://github.com/robomaster-oss/rmua19_gazebo_simulator.git -b humble
# Install ROS dependencies


WORKDIR /simulator_ws
RUN rosdep update

# Install the missing camera_info_manager package
RUN apt-get update && apt-get install -y ros-humble-camera-info-manager

# Build the workspace
RUN echo "source /simulator_ws/install/setup.bash" >> ~/.bashrc

RUN /bin/bash -c '. /opt/ros/humble/setup.bash; colcon build --symlink-install'

# RUN source /simulator_ws/install/setup.bash && colcon build --symlink-install

# Source setup script for the workspace in bashrc so it gets sourced on container start
# RUN echo "source /simulator_ws/install/setup.bash" >> ~/.bashrc

RUN colcon list
# Expose container's graphical interface to the host
# ENV DISPLAY=:0
RUN pip install xmacro



# Default command to keep the container running without exiting
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY entrypoint2.sh /entrypoint2.sh
RUN chmod +x /entrypoint2.sh

COPY entrypoint3.sh /entrypoint3.sh
RUN chmod +x /entrypoint3.sh

COPY newpub.py /simulator_ws/newpub.py
COPY pub_for_shooting.py /simulator_ws/pub_for_shooting.py



COPY entrypoint4.sh /entrypoint4.sh
RUN chmod +x /entrypoint4.sh

COPY newpub2.py /simulator_ws/newpub2.py
COPY pub_for_shooting2.py /simulator_ws/pub_for_shooting2.py

COPY entrypoint6.sh /entrypoint6.sh
RUN chmod +x /entrypoint6.sh
COPY entrypoint5.sh /entrypoint5.sh
RUN chmod +x /entrypoint5.sh

COPY entrypoint7.sh /entrypoint7.sh
RUN chmod +x /entrypoint7.sh

COPY entrypoint8.sh /entrypoint8.sh
RUN chmod +x /entrypoint8.sh