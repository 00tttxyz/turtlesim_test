### turtlesim小乌龟跟踪

![fig: run.png](docs/imgs/run.png "效果")

#### ROS安装

```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo sh -c '. /etc/lsb-release && echo "deb http://mirrors.tuna.tsinghua.edu.cn/ros/ubuntu/ `lsb_release -cs` main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt install curl
wget http://packages.ros.org/ros.key
sudo apt-key add ros.key

sudo apt update
sudo apt install ros-noetic-desktop-full

echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```



#### 下载

```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
catkin_init_workspace
git clone https://github.com/00tttxyz/turtlesim_test.git
cd ..
catkin_make
```

#### 运行

```
roslaunch turtlesim_test test.launch
```
