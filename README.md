# ros2_ws_tools

Various handy scripts for managing your ros2 ws. I add a symbolic link to this from a ros2 workspace and use it that way.

## run_tests.py

### Usage
  - run all tests: execute from ROS2 workspace directory
  - run only package tests: run_tests.py --package <my_package> from ROS2 workspace directory

### Notes
  - Add unittest.main(verbosity=2) to your unittests for a nice cleanup of test output
  - run_tests.py does not require that the ROS2 package builds a python package (of the python part of the package). IMHO, that's one too many packages!
  - Authored by GPT-4o, after I made my constraints (no python package) clear
