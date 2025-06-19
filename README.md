# ros2_ws_tools

Various handy scripts for managing your ros2 ws. I add a symbolic link to this from a ros2 workspace and use it that way.

## Usage

- run_tests.py: 
  - run all tests: execute from workspace directory
  - run only package tests: run_tests.py --package <my_package>
  - notes:
    - add unittest.main(verbosity=2) to you unittests for a nice cleanup of test output
    - this approach does not require that the ROS2 package builds a python package. IMHO, thats one too many packages!
  
