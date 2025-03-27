[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
# Motion-planning-algorithms

# Dependencies
-   Python
-   Opencv 
-   Numpy

# Environment 
<img src="Resources/map.jpg" width="500" alt="Alt text" title="Environment">


## Installing OpenCV for C++
```
sudo apt-get update $ sudo apt-get upgrade
sudo apt-get install build-essential 
sudo apt-get install cmake 
sudo apt-get install git 
sudo apt-get install unzip 
sudo apt-get install pkg-config
sudo apt-get install libjpeg-dev 
sudo apt-get install libpng-dev 
sudo apt-get install libtiff-dev


# Install minimal prerequisites (Ubuntu 18.04 as reference)
sudo apt update && sudo apt install -y cmake g++ wget unzip

# Download and unpack sources
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.x.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.x.zip
unzip opencv.zip
unzip opencv_contrib.zip

# Create build directory and switch into it
mkdir -p build && cd build

# Configure
cmake -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-4.x/modules ../opencv-4.x

# Build
cmake --build .

#To install openCV headers
sudo apt install libopencv-dev

```
## Install compiler
```
sudo apt install -y g++
```
