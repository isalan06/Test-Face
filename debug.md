pip3 install opencv-python
Collecting opencv-python
  Downloading https://files.pythonhosted.org/packages/ac/71/25c98e634b6bdeca4727c7f6d6927b056080668c5008ad3c8fc9e7f8f6ec/opencv-python-4.12.0.88.tar.gz (95.4MB)
    100% |████████████████████████████████| 95.4MB 3.5kB/s 
    Complete output from command python setup.py egg_info:
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/tmp/pip-build-q1ogzyex/opencv-python/setup.py", line 10, in <module>
        from skbuild import cmaker, setup
    ModuleNotFoundError: No module named 'skbuild'
    
    ----------------------------------------
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-q1ogzyex/opencv-python/



pip3 install opencv-python
WARNING: pip is being invoked by an old script wrapper. This will fail in a future version of pip.
Please see https://github.com/pypa/pip/issues/5599 for advice on fixing the underlying issue.
To avoid this problem you can invoke Python with '-m pip' instead of running pip directly.
Defaulting to user installation because normal site-packages is not writeable
Collecting opencv-python
  Using cached opencv-python-4.12.0.88.tar.gz (95.4 MB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: numpy<2.0 in /usr/lib/python3/dist-packages (from opencv-python) (1.13.3)
Building wheels for collected packages: opencv-python
  Building wheel for opencv-python (pyproject.toml) ... error
  ERROR: Command errored out with exit status -4:
   command: /usr/bin/python3 /home/nexaiot/.local/lib/python3.6/site-packages/pip/_vendor/pep517/in_process/_in_process.py build_wheel /tmp/tmp98076j2i
       cwd: /tmp/pip-install-z5b62vgg/opencv-python_3a8ed60ea157406fad829a2e46fafe1c
  Complete output (77 lines):
  
  
  --------------------------------------------------------------------------------
  -- Trying 'Ninja' generator
  --------------------------------
  ---------------------------
  ----------------------
  -----------------
  ------------
  -------
  --
  CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
    Compatibility with CMake < 3.5 will be removed from a future version of
    CMake.
  
    Update the VERSION argument <min> value or use a ...<max> suffix to tell
    CMake that the project does not need compatibility with older versions.
  
  Not searching for unused variables given on the command line.
  
  CMake Error: CMake was unable to find a build program corresponding to "Ninja".  CMAKE_MAKE_PROGRAM is not set.  You probably need to select a different build tool.
  -- Configuring incomplete, errors occurred!
  --
  -------
  ------------
  -----------------
  ----------------------
  ---------------------------
  --------------------------------
  -- Trying 'Ninja' generator - failure
  --------------------------------------------------------------------------------
  
  
  
  --------------------------------------------------------------------------------
  -- Trying 'Unix Makefiles' generator
  --------------------------------
  ---------------------------
  ----------------------
  -----------------
  ------------
  -------
  --
  CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
    Compatibility with CMake < 3.5 will be removed from a future version of
    CMake.
  
    Update the VERSION argument <min> value or use a ...<max> suffix to tell
    CMake that the project does not need compatibility with older versions.
  
  Not searching for unused variables given on the command line.
  
  -- The C compiler identification is GNU 11.4.0
  -- Detecting C compiler ABI info
  -- Detecting C compiler ABI info - done
  -- Check for working C compiler: /usr/bin/cc - skipped
  -- Detecting C compile features
  -- Detecting C compile features - done
  -- The CXX compiler identification is GNU 11.4.0
  -- Detecting CXX compiler ABI info
  -- Detecting CXX compiler ABI info - done
  -- Check for working CXX compiler: /usr/bin/c++ - skipped
  -- Detecting CXX compile features
  -- Detecting CXX compile features - done
  -- Configuring done (2.0s)
  -- Generating done (0.0s)
  -- Build files have been written to: /tmp/pip-install-z5b62vgg/opencv-python_3a8ed60ea157406fad829a2e46fafe1c/_cmake_test_compile/build
  --
  -------
  ------------
  -----------------
  ----------------------
  ---------------------------
  --------------------------------
  -- Trying 'Unix Makefiles' generator - success
  --------------------------------------------------------------------------------
  
  ----------------------------------------
  ERROR: Failed building wheel for opencv-python
Failed to build opencv-python
ERROR: Could not build wheels for opencv-python, which is required to install pyproject.toml-based projects

