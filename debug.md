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




python3 -m pip install --user opencv-python==4.3.0.38
Collecting opencv-python==4.3.0.38
  Downloading opencv-python-4.3.0.38.tar.gz (88.0 MB)
     |████████████████████████████████| 88.0 MB 53 kB/s             
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: numpy>=1.13.3 in /usr/lib/python3/dist-packages (from opencv-python==4.3.0.38) (1.13.3)
Building wheels for collected packages: opencv-python
  Building wheel for opencv-python (pyproject.toml) ... error
  ERROR: Command errored out with exit status 1:
   command: /usr/bin/python3 /home/nexaiot/.local/lib/python3.6/site-packages/pip/_vendor/pep517/in_process/_in_process.py build_wheel /tmp/tmpvxjk254b
       cwd: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d
  Complete output (2438 lines):
  
  
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
  -- Configuring done (1.7s)
  -- Generating done (0.0s)
  -- Build files have been written to: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_cmake_test_compile/build
  --
  -------
  ------------
  -----------------
  ----------------------
  ---------------------------
  --------------------------------
  -- Trying 'Unix Makefiles' generator - success
  --------------------------------------------------------------------------------
  
  Configuring Project
    Working directory:
      /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-build
    Command:
      /tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/cmake/data/bin/cmake /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv -G 'Unix Makefiles' -DCMAKE_INSTALL_PREFIX:PATH=/tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install -DPYTHON_VERSION_STRING:STRING=3.6.9 -DSKBUILD:INTERNAL=TRUE -DCMAKE_MODULE_PATH:PATH=/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/skbuild/resources/cmake -DPYTHON_EXECUTABLE:PATH=/usr/bin/python3 -DPYTHON_INCLUDE_DIR:PATH=/usr/include/python3.6m -DPYTHON_LIBRARY:PATH=/usr/lib/aarch64-linux-gnu/libpython3.6m.so -DPython_EXECUTABLE:PATH=/usr/bin/python3 -DPython_ROOT_DIR:PATH=/usr -DPython_INCLUDE_DIR:PATH=/usr/include/python3.6m -DPython_FIND_REGISTRY:STRING=NEVER -DPython_NumPy_INCLUDE_DIRS:PATH=/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/numpy/core/include -DPython3_EXECUTABLE:PATH=/usr/bin/python3 -DPython3_ROOT_DIR:PATH=/usr -DPython3_INCLUDE_DIR:PATH=/usr/include/python3.6m -DPython3_FIND_REGISTRY:STRING=NEVER -DPython3_NumPy_INCLUDE_DIRS:PATH=/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/numpy/core/include -DPYTHON3_EXECUTABLE=/usr/bin/python3 -DPYTHON3_INCLUDE_DIR=/usr/include/python3.6m -DPYTHON3_LIBRARY=/usr/lib/aarch64-linux-gnu/libpython3.6m.so -DBUILD_opencv_python3=ON -DBUILD_opencv_python2=OFF -DBUILD_opencv_java=OFF -DOPENCV_SKIP_PYTHON_LOADER=ON -DOPENCV_PYTHON3_INSTALL_PATH=python -DINSTALL_CREATE_DISTRIB=ON -DBUILD_opencv_apps=OFF -DBUILD_SHARED_LIBS=OFF -DBUILD_TESTS=OFF -DBUILD_PERF_TESTS=OFF -DBUILD_DOCS=OFF -DCMAKE_BUILD_TYPE:STRING=Release
  
  -- The CXX compiler identification is GNU 11.4.0
  -- The C compiler identification is GNU 11.4.0
  -- Detecting CXX compiler ABI info
  -- Detecting CXX compiler ABI info - done
  -- Check for working CXX compiler: /usr/bin/c++ - skipped
  -- Detecting CXX compile features
  -- Detecting CXX compile features - done
  -- Detecting C compiler ABI info
  -- Detecting C compiler ABI info - done
  -- Check for working C compiler: /usr/bin/cc - skipped
  -- Detecting C compile features
  -- Detecting C compile features - done
  -- Detected processor: aarch64
  CMake Warning (dev) at cmake/OpenCVUtils.cmake:131 (find_package):
    Policy CMP0148 is not set: The FindPythonInterp and FindPythonLibs modules
    are removed.  Run "cmake --help-policy CMP0148" for policy details.  Use
    the cmake_policy command to set the policy and suppress this warning.
  
  Call Stack (most recent call first):
    cmake/OpenCVDetectPython.cmake:64 (find_host_package)
    cmake/OpenCVDetectPython.cmake:271 (find_python)
    CMakeLists.txt:598 (include)
  This warning is for project developers.  Use -Wno-dev to suppress it.
  
  -- Found PythonInterp: /usr/bin/python3 (found suitable version "3.6.9", minimum required is "2.7")
  CMake Warning at cmake/OpenCVDetectPython.cmake:81 (message):
    CMake's 'find_host_package(PythonInterp 2.7)' found wrong Python version:
  
    PYTHON_EXECUTABLE=/usr/bin/python3
  
    PYTHON_VERSION_STRING=3.6.9
  
    Consider providing the 'PYTHON2_EXECUTABLE' variable via CMake command line
    or environment variables
  
  Call Stack (most recent call first):
    cmake/OpenCVDetectPython.cmake:271 (find_python)
    CMakeLists.txt:598 (include)
  
  
  -- Found Python2: /usr/bin/python2.7 (found version "2.7.17") found components: Interpreter
  CMake Warning (dev) at cmake/OpenCVUtils.cmake:131 (find_package):
    Policy CMP0148 is not set: The FindPythonInterp and FindPythonLibs modules
    are removed.  Run "cmake --help-policy CMP0148" for policy details.  Use
    the cmake_policy command to set the policy and suppress this warning.
  
  Call Stack (most recent call first):
    cmake/OpenCVDetectPython.cmake:96 (find_host_package)
    cmake/OpenCVDetectPython.cmake:271 (find_python)
    CMakeLists.txt:598 (include)
  This warning is for project developers.  Use -Wno-dev to suppress it.
  
  -- Found PythonInterp: /usr/bin/python2.7 (found version "2.7.17")
  CMake Warning (dev) at cmake/OpenCVDetectPython.cmake:140 (find_package):
    Policy CMP0148 is not set: The FindPythonInterp and FindPythonLibs modules
    are removed.  Run "cmake --help-policy CMP0148" for policy details.  Use
    the cmake_policy command to set the policy and suppress this warning.
  
  Call Stack (most recent call first):
    cmake/OpenCVDetectPython.cmake:271 (find_python)
    CMakeLists.txt:598 (include)
  This warning is for project developers.  Use -Wno-dev to suppress it.
  
  -- Could NOT find PythonLibs: Found unsuitable version "3.6.9", but required is exact version "2.7.17" (found /usr/lib/aarch64-linux-gnu/libpython3.6m.so)
  Traceback (most recent call last):
    File "<string>", line 1, in <module>
    File "/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/numpy/__init__.py", line 142, in <module>
      from . import add_newdocs
    File "/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/numpy/add_newdocs.py", line 13, in <module>
      from numpy.lib import add_newdoc
    File "/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/numpy/lib/__init__.py", line 8, in <module>
      from .type_check import *
    File "/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/numpy/lib/type_check.py", line 11, in <module>
      import numpy.core.numeric as _nx
    File "/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/numpy/core/__init__.py", line 26, in <module>
      raise ImportError(msg)
  ImportError:
  Importing the multiarray numpy extension module failed.  Most
  likely you are trying to import a failed build of numpy.
  If you're working with a numpy git repo, try `git clean -xdf` (removes all
  files not under version control).  Otherwise reinstall numpy.
  
  Original error was: cannot import name multiarray
  
  CMake Warning (dev) at cmake/OpenCVUtils.cmake:131 (find_package):
    Policy CMP0148 is not set: The FindPythonInterp and FindPythonLibs modules
    are removed.  Run "cmake --help-policy CMP0148" for policy details.  Use
    the cmake_policy command to set the policy and suppress this warning.
  
  Call Stack (most recent call first):
    cmake/OpenCVDetectPython.cmake:64 (find_host_package)
    cmake/OpenCVDetectPython.cmake:280 (find_python)
    CMakeLists.txt:598 (include)
  This warning is for project developers.  Use -Wno-dev to suppress it.
  
  -- Found PythonInterp: /usr/bin/python3 (found suitable version "3.6.9", minimum required is "3.2")
  CMake Warning (dev) at cmake/OpenCVDetectPython.cmake:140 (find_package):
    Policy CMP0148 is not set: The FindPythonInterp and FindPythonLibs modules
    are removed.  Run "cmake --help-policy CMP0148" for policy details.  Use
    the cmake_policy command to set the policy and suppress this warning.
  
  Call Stack (most recent call first):
    cmake/OpenCVDetectPython.cmake:280 (find_python)
    CMakeLists.txt:598 (include)
  This warning is for project developers.  Use -Wno-dev to suppress it.
  
  -- Found PythonLibs: /usr/lib/aarch64-linux-gnu/libpython3.6m.so (found suitable exact version "3.6.9")
  -- Looking for ccache - not found
  -- Performing Test HAVE_CXX_FSIGNED_CHAR
  -- Performing Test HAVE_CXX_FSIGNED_CHAR - Success
  -- Performing Test HAVE_C_FSIGNED_CHAR
  -- Performing Test HAVE_C_FSIGNED_CHAR - Success
  -- Performing Test HAVE_CXX_W
  -- Performing Test HAVE_CXX_W - Success
  -- Performing Test HAVE_C_W
  -- Performing Test HAVE_C_W - Success
  -- Performing Test HAVE_CXX_WALL
  -- Performing Test HAVE_CXX_WALL - Success
  -- Performing Test HAVE_C_WALL
  -- Performing Test HAVE_C_WALL - Success
  -- Performing Test HAVE_CXX_WERROR_RETURN_TYPE
  -- Performing Test HAVE_CXX_WERROR_RETURN_TYPE - Success
  -- Performing Test HAVE_C_WERROR_RETURN_TYPE
  -- Performing Test HAVE_C_WERROR_RETURN_TYPE - Success
  -- Performing Test HAVE_CXX_WERROR_NON_VIRTUAL_DTOR
  -- Performing Test HAVE_CXX_WERROR_NON_VIRTUAL_DTOR - Success
  -- Performing Test HAVE_C_WERROR_NON_VIRTUAL_DTOR
  -- Performing Test HAVE_C_WERROR_NON_VIRTUAL_DTOR - Failed
  -- Performing Test HAVE_CXX_WERROR_ADDRESS
  -- Performing Test HAVE_CXX_WERROR_ADDRESS - Success
  -- Performing Test HAVE_C_WERROR_ADDRESS
  -- Performing Test HAVE_C_WERROR_ADDRESS - Success
  -- Performing Test HAVE_CXX_WERROR_SEQUENCE_POINT
  -- Performing Test HAVE_CXX_WERROR_SEQUENCE_POINT - Success
  -- Performing Test HAVE_C_WERROR_SEQUENCE_POINT
  -- Performing Test HAVE_C_WERROR_SEQUENCE_POINT - Success
  -- Performing Test HAVE_CXX_WFORMAT
  -- Performing Test HAVE_CXX_WFORMAT - Success
  -- Performing Test HAVE_C_WFORMAT
  -- Performing Test HAVE_C_WFORMAT - Success
  -- Performing Test HAVE_CXX_WERROR_FORMAT_SECURITY
  -- Performing Test HAVE_CXX_WERROR_FORMAT_SECURITY - Success
  -- Performing Test HAVE_C_WERROR_FORMAT_SECURITY
  -- Performing Test HAVE_C_WERROR_FORMAT_SECURITY - Success
  -- Performing Test HAVE_CXX_WMISSING_DECLARATIONS
  -- Performing Test HAVE_CXX_WMISSING_DECLARATIONS - Success
  -- Performing Test HAVE_C_WMISSING_DECLARATIONS
  -- Performing Test HAVE_C_WMISSING_DECLARATIONS - Success
  -- Performing Test HAVE_CXX_WMISSING_PROTOTYPES
  -- Performing Test HAVE_CXX_WMISSING_PROTOTYPES - Failed
  -- Performing Test HAVE_C_WMISSING_PROTOTYPES
  -- Performing Test HAVE_C_WMISSING_PROTOTYPES - Success
  -- Performing Test HAVE_CXX_WSTRICT_PROTOTYPES
  -- Performing Test HAVE_CXX_WSTRICT_PROTOTYPES - Failed
  -- Performing Test HAVE_C_WSTRICT_PROTOTYPES
  -- Performing Test HAVE_C_WSTRICT_PROTOTYPES - Success
  -- Performing Test HAVE_CXX_WUNDEF
  -- Performing Test HAVE_CXX_WUNDEF - Success
  -- Performing Test HAVE_C_WUNDEF
  -- Performing Test HAVE_C_WUNDEF - Success
  -- Performing Test HAVE_CXX_WINIT_SELF
  -- Performing Test HAVE_CXX_WINIT_SELF - Success
  -- Performing Test HAVE_C_WINIT_SELF
  -- Performing Test HAVE_C_WINIT_SELF - Success
  -- Performing Test HAVE_CXX_WPOINTER_ARITH
  -- Performing Test HAVE_CXX_WPOINTER_ARITH - Success
  -- Performing Test HAVE_C_WPOINTER_ARITH
  -- Performing Test HAVE_C_WPOINTER_ARITH - Success
  -- Performing Test HAVE_CXX_WSHADOW
  -- Performing Test HAVE_CXX_WSHADOW - Success
  -- Performing Test HAVE_C_WSHADOW
  -- Performing Test HAVE_C_WSHADOW - Success
  -- Performing Test HAVE_CXX_WSIGN_PROMO
  -- Performing Test HAVE_CXX_WSIGN_PROMO - Success
  -- Performing Test HAVE_C_WSIGN_PROMO
  -- Performing Test HAVE_C_WSIGN_PROMO - Failed
  -- Performing Test HAVE_CXX_WUNINITIALIZED
  -- Performing Test HAVE_CXX_WUNINITIALIZED - Success
  -- Performing Test HAVE_C_WUNINITIALIZED
  -- Performing Test HAVE_C_WUNINITIALIZED - Success
  -- Performing Test HAVE_CXX_WSUGGEST_OVERRIDE
  -- Performing Test HAVE_CXX_WSUGGEST_OVERRIDE - Success
  -- Performing Test HAVE_C_WSUGGEST_OVERRIDE
  -- Performing Test HAVE_C_WSUGGEST_OVERRIDE - Failed
  -- Performing Test HAVE_CXX_WNO_DELETE_NON_VIRTUAL_DTOR
  -- Performing Test HAVE_CXX_WNO_DELETE_NON_VIRTUAL_DTOR - Success
  -- Performing Test HAVE_C_WNO_DELETE_NON_VIRTUAL_DTOR
  -- Performing Test HAVE_C_WNO_DELETE_NON_VIRTUAL_DTOR - Failed
  -- Performing Test HAVE_CXX_WNO_UNNAMED_TYPE_TEMPLATE_ARGS
  -- Performing Test HAVE_CXX_WNO_UNNAMED_TYPE_TEMPLATE_ARGS - Failed
  -- Performing Test HAVE_C_WNO_UNNAMED_TYPE_TEMPLATE_ARGS
  -- Performing Test HAVE_C_WNO_UNNAMED_TYPE_TEMPLATE_ARGS - Failed
  -- Performing Test HAVE_CXX_WNO_COMMENT
  -- Performing Test HAVE_CXX_WNO_COMMENT - Success
  -- Performing Test HAVE_C_WNO_COMMENT
  -- Performing Test HAVE_C_WNO_COMMENT - Success
  -- Performing Test HAVE_CXX_WIMPLICIT_FALLTHROUGH_3
  -- Performing Test HAVE_CXX_WIMPLICIT_FALLTHROUGH_3 - Success
  -- Performing Test HAVE_C_WIMPLICIT_FALLTHROUGH_3
  -- Performing Test HAVE_C_WIMPLICIT_FALLTHROUGH_3 - Success
  -- Performing Test HAVE_CXX_WNO_STRICT_OVERFLOW
  -- Performing Test HAVE_CXX_WNO_STRICT_OVERFLOW - Success
  -- Performing Test HAVE_C_WNO_STRICT_OVERFLOW
  -- Performing Test HAVE_C_WNO_STRICT_OVERFLOW - Success
  -- Performing Test HAVE_CXX_FDIAGNOSTICS_SHOW_OPTION
  -- Performing Test HAVE_CXX_FDIAGNOSTICS_SHOW_OPTION - Success
  -- Performing Test HAVE_C_FDIAGNOSTICS_SHOW_OPTION
  -- Performing Test HAVE_C_FDIAGNOSTICS_SHOW_OPTION - Success
  -- Performing Test HAVE_CXX_PTHREAD
  -- Performing Test HAVE_CXX_PTHREAD - Success
  -- Performing Test HAVE_C_PTHREAD
  -- Performing Test HAVE_C_PTHREAD - Success
  -- Performing Test HAVE_CXX_FOMIT_FRAME_POINTER
  -- Performing Test HAVE_CXX_FOMIT_FRAME_POINTER - Success
  -- Performing Test HAVE_C_FOMIT_FRAME_POINTER
  -- Performing Test HAVE_C_FOMIT_FRAME_POINTER - Success
  -- Performing Test HAVE_CXX_FFUNCTION_SECTIONS
  -- Performing Test HAVE_CXX_FFUNCTION_SECTIONS - Success
  -- Performing Test HAVE_C_FFUNCTION_SECTIONS
  -- Performing Test HAVE_C_FFUNCTION_SECTIONS - Success
  -- Performing Test HAVE_CXX_FDATA_SECTIONS
  -- Performing Test HAVE_CXX_FDATA_SECTIONS - Success
  -- Performing Test HAVE_C_FDATA_SECTIONS
  -- Performing Test HAVE_C_FDATA_SECTIONS - Success
  -- Performing Test HAVE_CPU_NEON_SUPPORT (check file: cmake/checks/cpu_neon.cpp)
  -- Performing Test HAVE_CPU_NEON_SUPPORT - Success
  -- Performing Test HAVE_CPU_FP16_SUPPORT (check file: cmake/checks/cpu_fp16.cpp)
  -- Performing Test HAVE_CPU_FP16_SUPPORT - Success
  -- Performing Test HAVE_CPU_BASELINE_FLAGS
  -- Performing Test HAVE_CPU_BASELINE_FLAGS - Success
  -- Performing Test HAVE_CXX_FVISIBILITY_HIDDEN
  -- Performing Test HAVE_CXX_FVISIBILITY_HIDDEN - Success
  -- Performing Test HAVE_C_FVISIBILITY_HIDDEN
  -- Performing Test HAVE_C_FVISIBILITY_HIDDEN - Success
  -- Performing Test HAVE_CXX_FVISIBILITY_INLINES_HIDDEN
  -- Performing Test HAVE_CXX_FVISIBILITY_INLINES_HIDDEN - Success
  -- Performing Test HAVE_C_FVISIBILITY_INLINES_HIDDEN
  -- Performing Test HAVE_C_FVISIBILITY_INLINES_HIDDEN - Failed
  -- Performing Test HAVE_LINK_AS_NEEDED
  -- Performing Test HAVE_LINK_AS_NEEDED - Success
  -- Looking for pthread.h
  -- Looking for pthread.h - found
  -- Looking for posix_memalign
  -- Looking for posix_memalign - found
  -- Looking for malloc.h
  -- Looking for malloc.h - found
  -- Looking for memalign
  -- Looking for memalign - found
  -- Found ZLIB: /usr/lib/aarch64-linux-gnu/libz.so (found suitable version "1.2.11", minimum required is "1.2.3")
  -- Could NOT find JPEG (missing: JPEG_LIBRARY JPEG_INCLUDE_DIR)
  -- Performing Test HAVE_C_WNO_UNUSED_PARAMETER
  -- Performing Test HAVE_C_WNO_UNUSED_PARAMETER - Success
  -- Performing Test HAVE_C_WNO_SIGN_COMPARE
  -- Performing Test HAVE_C_WNO_SIGN_COMPARE - Success
  -- Performing Test HAVE_C_WNO_SHORTEN_64_TO_32
  -- Performing Test HAVE_C_WNO_SHORTEN_64_TO_32 - Failed
  -- Performing Test HAVE_C_WNO_IMPLICIT_FALLTHROUGH
  -- Performing Test HAVE_C_WNO_IMPLICIT_FALLTHROUGH - Success
  -- libjpeg-turbo: VERSION = 2.0.4, BUILD = opencv-4.3.0-libjpeg-turbo
  -- Looking for sys/types.h
  -- Looking for sys/types.h - found
  -- Looking for stdint.h
  -- Looking for stdint.h - found
  -- Looking for stddef.h
  -- Looking for stddef.h - found
  -- Check size of size_t
  -- Check size of size_t - done
  -- Check size of unsigned long
  -- Check size of unsigned long - done
  -- Performing Test HAVE_BUILTIN_CTZL
  -- Performing Test HAVE_BUILTIN_CTZL - Success
  -- Looking for include file locale.h
  -- Looking for include file locale.h - found
  -- Looking for include file stdlib.h
  -- Looking for include file stdlib.h - found
  -- Looking for include file sys/types.h
  -- Looking for include file sys/types.h - found
  -- Could NOT find TIFF (missing: TIFF_LIBRARY TIFF_INCLUDE_DIR)
  -- Looking for assert.h
  -- Looking for assert.h - found
  -- Looking for dlfcn.h
  -- Looking for dlfcn.h - found
  -- Looking for fcntl.h
  -- Looking for fcntl.h - found
  -- Looking for inttypes.h
  -- Looking for inttypes.h - found
  -- Looking for io.h
  -- Looking for io.h - not found
  -- Looking for limits.h
  -- Looking for limits.h - found
  -- Looking for memory.h
  -- Looking for memory.h - found
  -- Looking for search.h
  -- Looking for search.h - found
  -- Looking for string.h
  -- Looking for string.h - found
  -- Looking for strings.h
  -- Looking for strings.h - found
  -- Looking for sys/time.h
  -- Looking for sys/time.h - found
  -- Looking for unistd.h
  -- Looking for unistd.h - found
  -- Performing Test C_HAS_inline
  -- Performing Test C_HAS_inline - Success
  -- Check size of signed short
  -- Check size of signed short - done
  -- Check size of unsigned short
  -- Check size of unsigned short - done
  -- Check size of signed int
  -- Check size of signed int - done
  -- Check size of unsigned int
  -- Check size of unsigned int - done
  -- Check size of signed long
  -- Check size of signed long - done
  -- Check size of signed long long
  -- Check size of signed long long - done
  -- Check size of unsigned long long
  -- Check size of unsigned long long - done
  -- Check size of unsigned char *
  -- Check size of unsigned char * - done
  -- Check size of ptrdiff_t
  -- Check size of ptrdiff_t - done
  -- Check size of INT8
  -- Check size of INT8 - failed
  -- Check size of INT16
  -- Check size of INT16 - failed
  -- Check size of INT32
  -- Check size of INT32 - failed
  -- Looking for floor
  -- Looking for floor - found
  -- Looking for pow
  -- Looking for pow - found
  -- Looking for sqrt
  -- Looking for sqrt - found
  -- Looking for isascii
  -- Looking for isascii - found
  -- Looking for memset
  -- Looking for memset - found
  -- Looking for mmap
  -- Looking for mmap - found
  -- Looking for getopt
  -- Looking for getopt - found
  -- Looking for memmove
  -- Looking for memmove - found
  -- Looking for setmode
  -- Looking for setmode - not found
  -- Looking for strcasecmp
  -- Looking for strcasecmp - found
  -- Looking for strchr
  -- Looking for strchr - found
  -- Looking for strrchr
  -- Looking for strrchr - found
  -- Looking for strstr
  -- Looking for strstr - found
  -- Looking for strtol
  -- Looking for strtol - found
  -- Looking for strtol
  -- Looking for strtol - found
  -- Looking for strtoull
  -- Looking for strtoull - found
  -- Looking for lfind
  -- Looking for lfind - found
  -- Performing Test HAVE_SNPRINTF
  -- Performing Test HAVE_SNPRINTF - Success
  -- Performing Test HAVE_C_WNO_UNUSED_BUT_SET_VARIABLE
  -- Performing Test HAVE_C_WNO_UNUSED_BUT_SET_VARIABLE - Success
  -- Performing Test HAVE_C_WNO_MISSING_PROTOTYPES
  -- Performing Test HAVE_C_WNO_MISSING_PROTOTYPES - Success
  -- Performing Test HAVE_C_WNO_MISSING_DECLARATIONS
  -- Performing Test HAVE_C_WNO_MISSING_DECLARATIONS - Success
  -- Performing Test HAVE_C_WNO_UNDEF
  -- Performing Test HAVE_C_WNO_UNDEF - Success
  -- Performing Test HAVE_C_WNO_UNUSED
  -- Performing Test HAVE_C_WNO_UNUSED - Success
  -- Performing Test HAVE_C_WNO_CAST_ALIGN
  -- Performing Test HAVE_C_WNO_CAST_ALIGN - Success
  -- Performing Test HAVE_C_WNO_SHADOW
  -- Performing Test HAVE_C_WNO_SHADOW - Success
  -- Performing Test HAVE_C_WNO_MAYBE_UNINITIALIZED
  -- Performing Test HAVE_C_WNO_MAYBE_UNINITIALIZED - Success
  -- Performing Test HAVE_C_WNO_POINTER_TO_INT_CAST
  -- Performing Test HAVE_C_WNO_POINTER_TO_INT_CAST - Success
  -- Performing Test HAVE_C_WNO_INT_TO_POINTER_CAST
  -- Performing Test HAVE_C_WNO_INT_TO_POINTER_CAST - Success
  -- Performing Test HAVE_C_WNO_MISLEADING_INDENTATION
  -- Performing Test HAVE_C_WNO_MISLEADING_INDENTATION - Success
  -- Performing Test HAVE_CXX_WNO_MISSING_DECLARATIONS
  -- Performing Test HAVE_CXX_WNO_MISSING_DECLARATIONS - Success
  -- Performing Test HAVE_CXX_WNO_UNUSED_PARAMETER
  -- Performing Test HAVE_CXX_WNO_UNUSED_PARAMETER - Success
  -- Performing Test HAVE_CXX_WNO_MISSING_PROTOTYPES
  -- Performing Test HAVE_CXX_WNO_MISSING_PROTOTYPES - Failed
  -- Performing Test HAVE_CXX_WNO_UNDEF
  -- Performing Test HAVE_CXX_WNO_UNDEF - Success
  -- Performing Test HAVE_C_STD_C99
  -- Performing Test HAVE_C_STD_C99 - Success
  -- Performing Test HAVE_C_WNO_UNUSED_VARIABLE
  -- Performing Test HAVE_C_WNO_UNUSED_VARIABLE - Success
  -- Performing Test HAVE_C_WNO_UNUSED_FUNCTION
  -- Performing Test HAVE_C_WNO_UNUSED_FUNCTION - Success
  -- Could NOT find OpenJPEG (minimal suitable version: 2.0, recommended version >= 2.3.1)
  -- Found JPEG: libjpeg-turbo
  -- Could NOT find Jasper (missing: JASPER_LIBRARIES JASPER_INCLUDE_DIR)
  -- Performing Test HAVE_C_WNO_IMPLICIT_FUNCTION_DECLARATION
  -- Performing Test HAVE_C_WNO_IMPLICIT_FUNCTION_DECLARATION - Success
  -- Performing Test HAVE_C_WNO_UNINITIALIZED
  -- Performing Test HAVE_C_WNO_UNINITIALIZED - Success
  -- Performing Test HAVE_C_WNO_UNUSED_BUT_SET_PARAMETER
  -- Performing Test HAVE_C_WNO_UNUSED_BUT_SET_PARAMETER - Success
  -- Performing Test HAVE_C_WNO_POINTER_COMPARE
  -- Performing Test HAVE_C_WNO_POINTER_COMPARE - Success
  -- Performing Test HAVE_C_WNO_ABSOLUTE_VALUE
  -- Performing Test HAVE_C_WNO_ABSOLUTE_VALUE - Success
  -- Performing Test HAVE_C_WNO_STRICT_PROTOTYPES
  -- Performing Test HAVE_C_WNO_STRICT_PROTOTYPES - Success
  -- Found ZLIB: /usr/lib/aarch64-linux-gnu/libz.so (found version "1.2.11")
  -- Could NOT find PNG (missing: PNG_LIBRARY PNG_PNG_INCLUDE_DIR)
  -- The ASM compiler identification is GNU
  -- Found assembler: /usr/bin/cc
  -- Looking for semaphore.h
  -- Looking for semaphore.h - found
  -- Performing Test HAVE_CXX_WNO_SHADOW
  -- Performing Test HAVE_CXX_WNO_SHADOW - Success
  -- Performing Test HAVE_CXX_WNO_UNUSED
  -- Performing Test HAVE_CXX_WNO_UNUSED - Success
  -- Performing Test HAVE_CXX_WNO_SIGN_COMPARE
  -- Performing Test HAVE_CXX_WNO_SIGN_COMPARE - Success
  -- Performing Test HAVE_CXX_WNO_UNINITIALIZED
  -- Performing Test HAVE_CXX_WNO_UNINITIALIZED - Success
  -- Performing Test HAVE_CXX_WNO_SWITCH
  -- Performing Test HAVE_CXX_WNO_SWITCH - Success
  -- Performing Test HAVE_CXX_WNO_PARENTHESES
  -- Performing Test HAVE_CXX_WNO_PARENTHESES - Success
  -- Performing Test HAVE_CXX_WNO_ARRAY_BOUNDS
  -- Performing Test HAVE_CXX_WNO_ARRAY_BOUNDS - Success
  -- Performing Test HAVE_CXX_WNO_EXTRA
  -- Performing Test HAVE_CXX_WNO_EXTRA - Success
  -- Performing Test HAVE_CXX_WNO_DEPRECATED_DECLARATIONS
  -- Performing Test HAVE_CXX_WNO_DEPRECATED_DECLARATIONS - Success
  -- Performing Test HAVE_CXX_WNO_MISLEADING_INDENTATION
  -- Performing Test HAVE_CXX_WNO_MISLEADING_INDENTATION - Success
  -- Performing Test HAVE_CXX_WNO_DEPRECATED
  -- Performing Test HAVE_CXX_WNO_DEPRECATED - Success
  -- Performing Test HAVE_CXX_WNO_SUGGEST_OVERRIDE
  -- Performing Test HAVE_CXX_WNO_SUGGEST_OVERRIDE - Success
  -- Performing Test HAVE_CXX_WNO_INCONSISTENT_MISSING_OVERRIDE
  -- Performing Test HAVE_CXX_WNO_INCONSISTENT_MISSING_OVERRIDE - Failed
  -- Performing Test HAVE_CXX_WNO_IMPLICIT_FALLTHROUGH
  -- Performing Test HAVE_CXX_WNO_IMPLICIT_FALLTHROUGH - Success
  -- Performing Test HAVE_CXX_WNO_TAUTOLOGICAL_COMPARE
  -- Performing Test HAVE_CXX_WNO_TAUTOLOGICAL_COMPARE - Success
  -- Performing Test HAVE_CXX_WNO_REORDER
  -- Performing Test HAVE_CXX_WNO_REORDER - Success
  -- Performing Test HAVE_CXX_WNO_UNUSED_RESULT
  -- Performing Test HAVE_CXX_WNO_UNUSED_RESULT - Success
  -- Performing Test HAVE_CXX_WNO_CLASS_MEMACCESS
  -- Performing Test HAVE_CXX_WNO_CLASS_MEMACCESS - Success
  -- Checking for module 'gtk+-3.0'
  --   No package 'gtk+-3.0' found
  -- Checking for module 'gtk+-2.0'
  --   No package 'gtk+-2.0' found
  -- Checking for module 'gthread-2.0'
  --   Found gthread-2.0, version 2.56.4
  -- Could not find OpenBLAS include. Turning OpenBLAS_FOUND off
  -- Could not find OpenBLAS lib. Turning OpenBLAS_FOUND off
  -- Could NOT find Atlas (missing: Atlas_CBLAS_INCLUDE_DIR Atlas_CLAPACK_INCLUDE_DIR Atlas_CBLAS_LIBRARY Atlas_BLAS_LIBRARY Atlas_LAPACK_LIBRARY)
  -- Looking for sgemm_
  -- Looking for sgemm_ - not found
  -- Performing Test CMAKE_HAVE_LIBC_PTHREAD
  -- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
  -- Found Threads: TRUE
  -- Could NOT find BLAS (missing: BLAS_LIBRARIES)
  -- Could NOT find LAPACK (missing: LAPACK_LIBRARIES)
      Reason given by package: LAPACK could not be found because dependency BLAS could not be found.
  
  -- Performing Test HAVE_CXX_WNO_UNUSED_LOCAL_TYPEDEFS
  -- Performing Test HAVE_CXX_WNO_UNUSED_LOCAL_TYPEDEFS - Success
  -- Performing Test HAVE_CXX_WNO_SIGN_PROMO
  -- Performing Test HAVE_CXX_WNO_SIGN_PROMO - Success
  -- Performing Test HAVE_CXX_WNO_TAUTOLOGICAL_UNDEFINED_COMPARE
  -- Performing Test HAVE_CXX_WNO_TAUTOLOGICAL_UNDEFINED_COMPARE - Failed
  -- Performing Test HAVE_CXX_WNO_IGNORED_QUALIFIERS
  -- Performing Test HAVE_CXX_WNO_IGNORED_QUALIFIERS - Success
  -- Performing Test HAVE_CXX_WNO_UNUSED_FUNCTION
  -- Performing Test HAVE_CXX_WNO_UNUSED_FUNCTION - Success
  -- Performing Test HAVE_CXX_WNO_UNUSED_CONST_VARIABLE
  -- Performing Test HAVE_CXX_WNO_UNUSED_CONST_VARIABLE - Success
  -- Performing Test HAVE_CXX_WNO_SHORTEN_64_TO_32
  -- Performing Test HAVE_CXX_WNO_SHORTEN_64_TO_32 - Failed
  -- Performing Test HAVE_CXX_WNO_INVALID_OFFSETOF
  -- Performing Test HAVE_CXX_WNO_INVALID_OFFSETOF - Success
  -- Performing Test HAVE_CXX_WNO_ENUM_COMPARE_SWITCH
  -- Performing Test HAVE_CXX_WNO_ENUM_COMPARE_SWITCH - Failed
  -- Could NOT find JNI (missing: JAVA_INCLUDE_PATH JAVA_INCLUDE_PATH2 AWT JVM)
  -- VTK is not found. Please set -DVTK_DIR in CMake to VTK build directory, or to VTK install subdirectory with VTKConfig.cmake file
  CMake Deprecation Warning at 3rdparty/carotene/hal/CMakeLists.txt:1 (cmake_minimum_required):
    Compatibility with CMake < 3.5 will be removed from a future version of
    CMake.
  
    Update the VERSION argument <min> value or use a ...<max> suffix to tell
    CMake that the project does not need compatibility with older versions.
  
  
  CMake Deprecation Warning at 3rdparty/carotene/CMakeLists.txt:1 (cmake_minimum_required):
    Compatibility with CMake < 3.5 will be removed from a future version of
    CMake.
  
    Update the VERSION argument <min> value or use a ...<max> suffix to tell
    CMake that the project does not need compatibility with older versions.
  
  
  -- Looking for dlerror in dl
  -- Looking for dlerror in dl - found
  -- ADE: Download: v0.1.1f.zip
  -- Checking for modules 'libavcodec;libavformat;libavutil;libswscale'
  --   No package 'libavcodec' found
  --   No package 'libavformat' found
  --   No package 'libavutil' found
  --   No package 'libswscale' found
  -- Checking for module 'gstreamer-base-1.0'
  --   No package 'gstreamer-base-1.0' found
  -- Checking for module 'gstreamer-app-1.0'
  --   No package 'gstreamer-app-1.0' found
  -- Checking for module 'gstreamer-riff-1.0'
  --   No package 'gstreamer-riff-1.0' found
  -- Checking for module 'gstreamer-pbutils-1.0'
  --   No package 'gstreamer-pbutils-1.0' found
  -- Checking for module 'libdc1394-2'
  --   No package 'libdc1394-2' found
  -- Allocator metrics storage type: 'int'
  -- Excluding from source files list: modules/imgproc/src/corner.avx.cpp
  -- Excluding from source files list: modules/imgproc/src/imgwarp.avx2.cpp
  -- Excluding from source files list: modules/imgproc/src/imgwarp.sse4_1.cpp
  -- Excluding from source files list: modules/imgproc/src/resize.avx2.cpp
  -- Excluding from source files list: modules/imgproc/src/resize.sse4_1.cpp
  -- Registering hook 'INIT_MODULE_SOURCES_opencv_dnn': /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/dnn/cmake/hooks/INIT_MODULE_SOURCES_opencv_dnn.cmake
  -- opencv_dnn: filter out cuda4dnn source code
  -- Excluding from source files list: <BUILD>/modules/dnn/layers/layers_common.avx.cpp
  -- Excluding from source files list: <BUILD>/modules/dnn/layers/layers_common.avx2.cpp
  -- Excluding from source files list: <BUILD>/modules/dnn/layers/layers_common.avx512_skx.cpp
  -- Excluding from source files list: modules/features2d/src/fast.avx2.cpp
  -- Performing Test HAVE_CXX_WNO_OVERLOADED_VIRTUAL
  -- Performing Test HAVE_CXX_WNO_OVERLOADED_VIRTUAL - Success
  -- Performing Test HAVE_CXX_WNO_UNUSED_PRIVATE_FIELD
  -- Performing Test HAVE_CXX_WNO_UNUSED_PRIVATE_FIELD - Failed
  --
  -- General configuration for OpenCV 4.3.0 =====================================
  --   Version control:               unknown
  --
  --   Platform:
  --     Timestamp:                   2026-05-12T03:14:45Z
  --     Host:                        Linux 4.9.140-tegra aarch64
  --     CMake:                       3.28.4
  --     CMake generator:             Unix Makefiles
  --     CMake build tool:            /usr/bin/make
  --     Configuration:               Release
  --
  --   CPU/HW features:
  --     Baseline:                    NEON FP16
  --       required:                  NEON
  --       disabled:                  VFPV3
  --
  --   C/C++:
  --     Built as dynamic libs?:      NO
  --     C++ standard:                11
  --     C++ Compiler:                /usr/bin/c++  (ver 11.4.0)
  --     C++ flags (Release):         -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wsuggest-override -Wno-delete-non-virtual-dtor -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections    -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG
  --     C++ flags (Debug):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wsuggest-override -Wno-delete-non-virtual-dtor -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections    -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG
  --     C Compiler:                  /usr/bin/cc
  --     C flags (Release):           -fsigned-char -W -Wall -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Winit-self -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections    -fvisibility=hidden -O3 -DNDEBUG  -DNDEBUG
  --     C flags (Debug):             -fsigned-char -W -Wall -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Winit-self -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections    -fvisibility=hidden -g  -O0 -DDEBUG -D_DEBUG
  --     Linker flags (Release):      -Wl,--gc-sections -Wl,--as-needed
  --     Linker flags (Debug):        -Wl,--gc-sections -Wl,--as-needed
  --     ccache:                      NO
  --     Precompiled headers:         NO
  --     Extra dependencies:          ade /usr/lib/aarch64-linux-gnu/libgthread-2.0.so /usr/lib/aarch64-linux-gnu/libglib-2.0.so /usr/lib/aarch64-linux-gnu/libz.so dl m pthread rt
  --     3rdparty dependencies:       ittnotify libprotobuf libjpeg-turbo libwebp libpng libtiff libjasper IlmImf quirc tegra_hal
  --
  --   OpenCV modules:
  --     To be built:                 calib3d core dnn features2d flann gapi highgui imgcodecs imgproc ml objdetect photo python3 stitching video videoio
  --     Disabled:                    world
  --     Disabled by dependency:      -
  --     Unavailable:                 java js python2 ts
  --     Applications:                -
  --     Documentation:               NO
  --     Non-free algorithms:         NO
  --
  --   GUI:
  --     GTK+:                        NO
  --     VTK support:                 NO
  --
  --   Media I/O:
  --     ZLib:                        /usr/lib/aarch64-linux-gnu/libz.so (ver 1.2.11)
  --     JPEG:                        libjpeg-turbo (ver 2.0.4-62)
  --     WEBP:                        build (ver encoder: 0x020f)
  --     PNG:                         build (ver 1.6.37)
  --     TIFF:                        build (ver 42 - 4.0.10)
  --     JPEG 2000:                   build Jasper (ver 1.900.1)
  --     OpenEXR:                     build (ver 2.3.0)
  --     HDR:                         YES
  --     SUNRASTER:                   YES
  --     PXM:                         YES
  --     PFM:                         YES
  --
  --   Video I/O:
  --     DC1394:                      NO
  --     FFMPEG:                      NO
  --       avcodec:                   NO
  --       avformat:                  NO
  --       avutil:                    NO
  --       swscale:                   NO
  --       avresample:                NO
  --     GStreamer:                   NO
  --     v4l/v4l2:                    YES (linux/videodev2.h)
  --
  --   Parallel framework:            pthreads
  --
  --   Trace:                         YES (with Intel ITT)
  --
  --   Other third-party libraries:
  --     Lapack:                      NO
  --     Eigen:                       NO
  --     Custom HAL:                  YES (carotene (ver 0.0.1))
  --     Protobuf:                    build (3.5.1)
  --
  --   OpenCL:                        YES (no extra features)
  --     Include path:                /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/include/opencl/1.2
  --     Link libraries:              Dynamic load
  --
  --   Python 3:
  --     Interpreter:                 /usr/bin/python3 (ver 3.6.9)
  --     Libraries:                   /usr/lib/aarch64-linux-gnu/libpython3.6m.so (ver 3.6.9)
  --     numpy:                       /tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/numpy/core/include (ver 1.13.3)
  --     install path:                python
  --
  --   Python (for build):            /usr/bin/python2.7
  --
  --   Java:
  --     ant:                         NO
  --     JNI:                         NO
  --     Java wrappers:               NO
  --     Java tests:                  NO
  --
  --   Install to:                    /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install
  -- -----------------------------------------------------------------
  --
  -- Configuring done (78.9s)
  -- Generating done (1.7s)
  -- Build files have been written to: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-build
  [  0%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcapimin.c.o
  [  0%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcapistd.c.o
  [  1%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jccoefct.c.o
  [  1%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jccolor.c.o
  [  1%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcdctmgr.c.o
  [  1%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jchuff.c.o
  [  1%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcicc.c.o
  [  1%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcinit.c.o
  [  1%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcmainct.c.o
  [  1%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcmarker.c.o
  [  1%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcmaster.c.o
  [  1%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcomapi.c.o
  [  2%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcparam.c.o
  [  2%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcphuff.c.o
  [  2%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcprepct.c.o
  [  2%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcsample.c.o
  [  2%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jctrans.c.o
  [  2%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdapimin.c.o
  [  2%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdapistd.c.o
  [  2%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdatadst.c.o
  [  2%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdatasrc.c.o
  [  2%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdcoefct.c.o
  [  3%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdcolor.c.o
  [  3%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jddctmgr.c.o
  [  3%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdhuff.c.o
  [  3%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdicc.c.o
  [  3%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdinput.c.o
  [  3%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdmainct.c.o
  [  3%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdmarker.c.o
  [  3%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdmaster.c.o
  [  3%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdmerge.c.o
  [  3%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdphuff.c.o
  [  4%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdpostct.c.o
  [  4%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdsample.c.o
  [  4%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdtrans.c.o
  [  4%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jerror.c.o
  [  4%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jfdctflt.c.o
  [  4%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jfdctfst.c.o
  [  4%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jfdctint.c.o
  [  4%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jidctflt.c.o
  [  4%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jidctfst.c.o
  [  4%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jidctint.c.o
  [  5%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jidctred.c.o
  [  5%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jquant1.c.o
  [  5%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jquant2.c.o
  [  5%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jutils.c.o
  [  5%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jmemmgr.c.o
  [  5%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jmemnobs.c.o
  [  5%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jaricom.c.o
  [  5%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcarith.c.o
  [  5%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdarith.c.o
  [  5%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jsimd_none.c.o
  [  6%] Linking C static library ../lib/liblibjpeg-turbo.a
  [  6%] Built target libjpeg-turbo
  [  6%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_aux.c.o
  [  6%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_close.c.o
  [  6%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_codec.c.o
  [  6%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_color.c.o
  [  6%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_compress.c.o
  [  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_dir.c.o
  [  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_dirinfo.c.o
  [  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_dirread.c.o
  [  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_dirwrite.c.o
  [  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_dumpmode.c.o
  [  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_error.c.o
  [  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_extension.c.o
  [  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_fax3.c.o
  [  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_fax3sm.c.o
  [  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_flush.c.o
  [  8%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_getimage.c.o
  [  8%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_jbig.c.o
  [  8%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_jpeg_12.c.o
  [  8%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_jpeg.c.o
  [  8%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_luv.c.o
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:822:18: warning: argument 1 of type ‘float[3]’ with mismatched bound [-Warray-parameter=]
    822 | XYZtoRGB24(float xyz[3], uint8 rgb[3])
        |            ~~~~~~^~~~~~
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffiop.h:64,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:25:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffio.h:497:24: note: previously declared as ‘float *’
    497 | extern void XYZtoRGB24(float*, uint8*);
        |                        ^~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:822:32: warning: argument 2 of type ‘uint8[3]’ {aka ‘unsigned char[3]’} with mismatched bound [-Warray-parameter=]
    822 | XYZtoRGB24(float xyz[3], uint8 rgb[3])
        |                          ~~~~~~^~~~~~
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffiop.h:64,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:25:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffio.h:497:32: note: previously declared as ‘uint8 *’ {aka ‘unsigned char *’}
    497 | extern void XYZtoRGB24(float*, uint8*);
        |                                ^~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:976:31: warning: argument 2 of type ‘float[3]’ with mismatched bound [-Warray-parameter=]
    976 | LogLuv24toXYZ(uint32 p, float XYZ[3])
        |                         ~~~~~~^~~~~~
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffiop.h:64,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:25:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffio.h:499:35: note: previously declared as ‘float *’
    499 | extern void LogLuv24toXYZ(uint32, float*);
        |                                   ^~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:1004:23: warning: argument 1 of type ‘float[3]’ with mismatched bound [-Warray-parameter=]
   1004 | LogLuv24fromXYZ(float XYZ[3], int em)
        |                 ~~~~~~^~~~~~
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffiop.h:64,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:25:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffio.h:511:31: note: previously declared as ‘float *’
    511 | extern uint32 LogLuv24fromXYZ(float*, int);
        |                               ^~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:1117:31: warning: argument 2 of type ‘float[3]’ with mismatched bound [-Warray-parameter=]
   1117 | LogLuv32toXYZ(uint32 p, float XYZ[3])
        |                         ~~~~~~^~~~~~
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffiop.h:64,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:25:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffio.h:500:35: note: previously declared as ‘float *’
    500 | extern void LogLuv32toXYZ(uint32, float*);
        |                                   ^~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:1142:23: warning: argument 1 of type ‘float[3]’ with mismatched bound [-Warray-parameter=]
   1142 | LogLuv32fromXYZ(float XYZ[3], int em)
        |                 ~~~~~~^~~~~~
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffiop.h:64,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:25:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffio.h:512:31: note: previously declared as ‘float *’
    512 | extern uint32 LogLuv32fromXYZ(float*, int);
        |                               ^~~~~~
  [  8%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_lzma.c.o
  [  8%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_lzw.c.o
  [  8%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_next.c.o
  [  8%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_ojpeg.c.o
  [  8%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_open.c.o
  [  9%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_packbits.c.o
  [  9%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_pixarlog.c.o
  [  9%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_predict.c.o
  [  9%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_print.c.o
  [  9%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_read.c.o
  [  9%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_strip.c.o
  [  9%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_swab.c.o
  [  9%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_thunder.c.o
  [  9%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_tile.c.o
  [  9%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_version.c.o
  [ 10%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_warning.c.o
  [ 10%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_webp.c.o
  [ 10%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_write.c.o
  [ 10%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_zip.c.o
  [ 10%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_zstd.c.o
  [ 10%] Building CXX object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_stream.cxx.o
  [ 10%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_unix.c.o
  [ 10%] Linking CXX static library ../lib/liblibtiff.a
  [ 10%] Built target libtiff
  [ 10%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dec/alpha_dec.c.o
  [ 10%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dec/buffer_dec.c.o
  [ 11%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dec/frame_dec.c.o
  [ 11%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dec/idec_dec.c.o
  [ 11%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dec/io_dec.c.o
  [ 11%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dec/quant_dec.c.o
  [ 11%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dec/tree_dec.c.o
  [ 11%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dec/vp8_dec.c.o
  [ 11%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dec/vp8l_dec.c.o
  [ 11%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dec/webp_dec.c.o
  [ 11%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/demux/anim_decode.c.o
  [ 11%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/demux/demux.c.o
  [ 12%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/alpha_processing.c.o
  [ 12%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/alpha_processing_mips_dsp_r2.c.o
  [ 12%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/alpha_processing_neon.c.o
  [ 12%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/alpha_processing_sse2.c.o
  [ 12%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/alpha_processing_sse41.c.o
  [ 12%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/cost.c.o
  [ 12%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/cost_mips32.c.o
  [ 12%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/cost_mips_dsp_r2.c.o
  [ 12%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/cost_neon.c.o
  [ 12%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/cost_sse2.c.o
  [ 13%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/cpu.c.o
  [ 13%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/dec.c.o
  [ 13%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/dec_clip_tables.c.o
  [ 13%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/dec_mips32.c.o
  [ 13%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/dec_mips_dsp_r2.c.o
  [ 13%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/dec_msa.c.o
  [ 13%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/dec_neon.c.o
  [ 13%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/dec_sse2.c.o
  [ 13%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/dec_sse41.c.o
  [ 13%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/enc.c.o
  [ 14%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/enc_mips32.c.o
  [ 14%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/enc_mips_dsp_r2.c.o
  [ 14%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/enc_msa.c.o
  [ 14%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/enc_neon.c.o
  [ 14%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/enc_sse2.c.o
  [ 14%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/enc_sse41.c.o
  [ 14%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/filters.c.o
  [ 14%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/filters_mips_dsp_r2.c.o
  [ 14%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/filters_msa.c.o
  [ 14%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/filters_neon.c.o
  [ 15%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/filters_sse2.c.o
  [ 15%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless.c.o
  [ 15%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_enc.c.o
  [ 15%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_enc_mips32.c.o
  [ 15%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_enc_mips_dsp_r2.c.o
  [ 15%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_enc_msa.c.o
  [ 15%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_enc_neon.c.o
  [ 15%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_enc_sse2.c.o
  [ 15%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_enc_sse41.c.o
  [ 15%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_mips_dsp_r2.c.o
  [ 16%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_msa.c.o
  [ 16%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_neon.c.o
  [ 16%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_sse2.c.o
  [ 16%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/rescaler.c.o
  [ 16%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/rescaler_mips32.c.o
  [ 16%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/rescaler_mips_dsp_r2.c.o
  [ 16%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/rescaler_msa.c.o
  [ 16%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/rescaler_neon.c.o
  [ 16%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/rescaler_sse2.c.o
  [ 16%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/ssim.c.o
  [ 17%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/ssim_sse2.c.o
  [ 17%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/upsampling.c.o
  [ 17%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/upsampling_mips_dsp_r2.c.o
  [ 17%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/upsampling_msa.c.o
  [ 17%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/upsampling_neon.c.o
  [ 17%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/upsampling_sse2.c.o
  [ 17%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/upsampling_sse41.c.o
  [ 17%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/yuv.c.o
  [ 17%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/yuv_mips32.c.o
  [ 17%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/yuv_mips_dsp_r2.c.o
  [ 18%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/yuv_neon.c.o
  [ 18%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/yuv_sse2.c.o
  [ 18%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/yuv_sse41.c.o
  [ 18%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/alpha_enc.c.o
  [ 18%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/analysis_enc.c.o
  [ 18%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/backward_references_cost_enc.c.o
  [ 18%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/backward_references_enc.c.o
  [ 18%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/config_enc.c.o
  [ 18%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/cost_enc.c.o
  [ 18%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/filter_enc.c.o
  [ 19%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/frame_enc.c.o
  [ 19%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/histogram_enc.c.o
  [ 19%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/iterator_enc.c.o
  [ 19%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/near_lossless_enc.c.o
  [ 19%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/picture_csp_enc.c.o
  [ 19%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/picture_enc.c.o
  [ 19%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/picture_psnr_enc.c.o
  [ 19%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/picture_rescale_enc.c.o
  [ 19%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/picture_tools_enc.c.o
  [ 19%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/predictor_enc.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/quant_enc.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/syntax_enc.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/token_enc.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/tree_enc.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/vp8l_enc.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/webp_enc.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/mux/anim_encode.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/mux/muxedit.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/mux/muxinternal.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/mux/muxread.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/bit_reader_utils.c.o
  [ 21%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/bit_writer_utils.c.o
  [ 21%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/color_cache_utils.c.o
  [ 21%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/filters_utils.c.o
  [ 21%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/huffman_encode_utils.c.o
  [ 21%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/huffman_utils.c.o
  [ 21%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/quant_levels_dec_utils.c.o
  [ 21%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/quant_levels_utils.c.o
  [ 21%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/random_utils.c.o
  [ 21%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/rescaler_utils.c.o
  [ 21%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/thread_utils.c.o
  [ 22%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/utils.c.o
  [ 22%] Linking C static library ../lib/liblibwebp.a
  [ 22%] Built target libwebp
  [ 22%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_cm.c.o
  In function ‘jas_cmprof_createsycc’,
      inlined from ‘jas_cmprof_createfromclrspc’ at /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libjasper/jas_cm.c:153:22,
      inlined from ‘jas_cmprof_createfromclrspc’ at /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libjasper/jas_cm.c:144:15:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libjasper/jas_cm.c:219:5: warning: ‘jas_cmshapmat_invmat’ accessing 96 bytes in a region of size 32 [-Wstringop-overflow=]
    219 |     jas_cmshapmat_invmat(revshapmat->mat, fwdshapmat->mat);
        |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libjasper/jas_cm.c: In function ‘jas_cmprof_createfromclrspc’:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libjasper/jas_cm.c:219:5: note: referencing argument 2 of type ‘jas_cmreal_t (*)[4]’ {aka ‘double (*)[4]’}
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libjasper/jas_cm.c:1001:12: note: in a call to function ‘jas_cmshapmat_invmat’
   1001 | static int jas_cmshapmat_invmat(jas_cmreal_t out[3][4], jas_cmreal_t in[3][4])
        |            ^~~~~~~~~~~~~~~~~~~~
  [ 22%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_debug.c.o
  [ 22%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_getopt.c.o
  [ 22%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_icc.c.o
  [ 22%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_iccdata.c.o
  [ 22%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_image.c.o
  [ 22%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_init.c.o
  [ 22%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_malloc.c.o
  [ 22%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_seq.c.o
  [ 23%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_stream.c.o
  [ 23%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_string.c.o
  [ 23%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_tmr.c.o
  [ 23%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_tvp.c.o
  [ 23%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_version.c.o
  [ 23%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jp2_cod.c.o
  [ 23%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jp2_dec.c.o
  [ 23%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jp2_enc.c.o
  [ 23%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_bs.c.o
  [ 23%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_cs.c.o
  [ 24%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_dec.c.o
  [ 24%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_enc.c.o
  [ 24%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_math.c.o
  [ 24%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_mct.c.o
  [ 24%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_mqcod.c.o
  [ 24%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_mqdec.c.o
  [ 24%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_mqenc.c.o
  [ 24%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_qmfb.c.o
  [ 24%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_t1cod.c.o
  [ 24%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_t1dec.c.o
  [ 25%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_t1enc.c.o
  [ 25%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_t2cod.c.o
  [ 25%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_t2dec.c.o
  [ 25%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_t2enc.c.o
  [ 25%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_tagtree.c.o
  [ 25%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_tsfb.c.o
  [ 25%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_util.c.o
  [ 25%] Linking C static library ../lib/liblibjasper.a
  [ 25%] Built target libjasper
  [ 25%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/png.c.o
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c: In function ‘png_convert_to_rfc1123_buffer’:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/pngpriv.h:1749:4: warning: ‘number_buf’ may be used uninitialized [-Wmaybe-uninitialized]
   1749 |    png_format_number(buffer, buffer + (sizeof buffer), format, number)
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:757:69: note: in definition of macro ‘APPEND_STRING’
    757 | #     define APPEND_STRING(string) pos = png_safecat(out, 29, pos, (string))
        |                                                                     ^~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:759:24: note: in expansion of macro ‘PNG_FORMAT_NUMBER’
    759 |          APPEND_STRING(PNG_FORMAT_NUMBER(number_buf, format, (value)))
        |                        ^~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:762:7: note: in expansion of macro ‘APPEND_NUMBER’
    762 |       APPEND_NUMBER(PNG_NUMBER_FORMAT_u, (unsigned)ptime->day);
        |       ^~~~~~~~~~~~~
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.h:335,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/pngpriv.h:386,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:14:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/pngpriv.h:1744:33: note: by argument 1 of type ‘png_const_charp’ {aka ‘const char *’} to ‘png_format_number’ declared here
   1744 | PNG_INTERNAL_FUNCTION(png_charp,png_format_number,(png_const_charp start,
        |                                 ^~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/pngconf.h:287:70: note: in definition of macro ‘PNG_FUNCTION’
    287 | #  define PNG_FUNCTION(type, name, args, attributes) attributes type name args
        |                                                                      ^~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/pngpriv.h:1744:1: note: in expansion of macro ‘PNG_INTERNAL_FUNCTION’
   1744 | PNG_INTERNAL_FUNCTION(png_charp,png_format_number,(png_const_charp start,
        | ^~~~~~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:755:12: note: ‘number_buf’ declared here
    755 |       char number_buf[5]; /* enough for a four-digit year */
        |            ^~~~~~~~~~
  In function ‘png_convert_to_rfc1123_buffer’,
      inlined from ‘png_convert_to_rfc1123’ at /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:796:11:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/pngpriv.h:1749:4: warning: ‘number_buf’ may be used uninitialized [-Wmaybe-uninitialized]
   1749 |    png_format_number(buffer, buffer + (sizeof buffer), format, number)
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:757:69: note: in definition of macro ‘APPEND_STRING’
    757 | #     define APPEND_STRING(string) pos = png_safecat(out, 29, pos, (string))
        |                                                                     ^~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:759:24: note: in expansion of macro ‘PNG_FORMAT_NUMBER’
    759 |          APPEND_STRING(PNG_FORMAT_NUMBER(number_buf, format, (value)))
        |                        ^~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:762:7: note: in expansion of macro ‘APPEND_NUMBER’
    762 |       APPEND_NUMBER(PNG_NUMBER_FORMAT_u, (unsigned)ptime->day);
        |       ^~~~~~~~~~~~~
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.h:335,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/pngpriv.h:386,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:14:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c: In function ‘png_convert_to_rfc1123’:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/pngpriv.h:1744:33: note: by argument 1 of type ‘png_const_charp’ {aka ‘const char *’} to ‘png_format_number’ declared here
   1744 | PNG_INTERNAL_FUNCTION(png_charp,png_format_number,(png_const_charp start,
        |                                 ^~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/pngconf.h:287:70: note: in definition of macro ‘PNG_FUNCTION’
    287 | #  define PNG_FUNCTION(type, name, args, attributes) attributes type name args
        |                                                                      ^~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/pngpriv.h:1744:1: note: in expansion of macro ‘PNG_INTERNAL_FUNCTION’
   1744 | PNG_INTERNAL_FUNCTION(png_charp,png_format_number,(png_const_charp start,
        | ^~~~~~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:755:12: note: ‘number_buf’ declared here
    755 |       char number_buf[5]; /* enough for a four-digit year */
        |            ^~~~~~~~~~
  [ 25%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngerror.c.o
  [ 25%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngget.c.o
  [ 25%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngmem.c.o
  [ 25%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngpread.c.o
  [ 25%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngread.c.o
  [ 25%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngrio.c.o
  [ 25%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngrtran.c.o
  [ 25%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngrutil.c.o
  [ 26%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngset.c.o
  [ 26%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngtrans.c.o
  [ 26%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngwio.c.o
  [ 26%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngwrite.c.o
  [ 26%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngwtran.c.o
  [ 26%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngwutil.c.o
  [ 26%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/arm/arm_init.c.o
  [ 26%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/arm/filter_neon_intrinsics.c.o
  [ 26%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/arm/palette_neon_intrinsics.c.o
  [ 26%] Linking C static library ../lib/liblibpng.a
  [ 26%] Built target libpng
  [ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Half/half.cpp.o
  [ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Iex/IexBaseExc.cpp.o
  [ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Iex/IexThrowErrnoExc.cpp.o
  [ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfAcesFile.cpp.o
  [ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfAttribute.cpp.o
  [ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfB44Compressor.cpp.o
  [ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfBoxAttribute.cpp.o
  [ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfCRgbaFile.cpp.o
  [ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfChannelList.cpp.o
  [ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfChannelListAttribute.cpp.o
  [ 27%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfChromaticities.cpp.o
  [ 27%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfChromaticitiesAttribute.cpp.o
  [ 27%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfCompositeDeepScanLine.cpp.o
  [ 27%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfCompressionAttribute.cpp.o
  [ 27%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfCompressor.cpp.o
  [ 27%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfConvert.cpp.o
  [ 27%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepCompositing.cpp.o
  [ 27%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepFrameBuffer.cpp.o
  [ 27%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepImageStateAttribute.cpp.o
  [ 27%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepScanLineInputFile.cpp.o
  [ 28%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepScanLineInputPart.cpp.o
  [ 28%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepScanLineOutputFile.cpp.o
  [ 28%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepScanLineOutputPart.cpp.o
  [ 28%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepTiledInputFile.cpp.o
  [ 28%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepTiledInputPart.cpp.o
  [ 28%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepTiledOutputFile.cpp.o
  [ 28%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepTiledOutputPart.cpp.o
  [ 28%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDoubleAttribute.cpp.o
  [ 28%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDwaCompressor.cpp.o
  [ 28%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfEnvmap.cpp.o
  [ 29%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfEnvmapAttribute.cpp.o
  [ 29%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfFastHuf.cpp.o
  [ 29%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfFloatAttribute.cpp.o
  [ 29%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfFloatVectorAttribute.cpp.o
  [ 29%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfFrameBuffer.cpp.o
  [ 29%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfFramesPerSecond.cpp.o
  [ 29%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfGenericInputFile.cpp.o
  [ 29%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfGenericOutputFile.cpp.o
  [ 29%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfHeader.cpp.o
  [ 29%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfHuf.cpp.o
  [ 30%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfIO.cpp.o
  [ 30%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfInputFile.cpp.o
  [ 30%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfInputPart.cpp.o
  [ 30%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfInputPartData.cpp.o
  [ 30%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfIntAttribute.cpp.o
  [ 30%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfKeyCode.cpp.o
  [ 30%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfKeyCodeAttribute.cpp.o
  [ 30%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfLineOrderAttribute.cpp.o
  [ 30%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfLut.cpp.o
  [ 30%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfMatrixAttribute.cpp.o
  [ 31%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfMisc.cpp.o
  [ 31%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfMultiPartInputFile.cpp.o
  [ 31%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfMultiPartOutputFile.cpp.o
  [ 31%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfMultiView.cpp.o
  [ 31%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfOpaqueAttribute.cpp.o
  [ 31%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfOutputFile.cpp.o
  [ 31%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfOutputPart.cpp.o
  [ 31%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfOutputPartData.cpp.o
  [ 31%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfPartType.cpp.o
  [ 31%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfPizCompressor.cpp.o
  [ 32%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfPreviewImage.cpp.o
  [ 32%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfPreviewImageAttribute.cpp.o
  [ 32%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfPxr24Compressor.cpp.o
  [ 32%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfRational.cpp.o
  [ 32%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfRationalAttribute.cpp.o
  [ 32%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfRgbaFile.cpp.o
  [ 32%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfRgbaYca.cpp.o
  [ 32%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfRle.cpp.o
  [ 32%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfRleCompressor.cpp.o
  [ 32%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfScanLineInputFile.cpp.o
  [ 33%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfStandardAttributes.cpp.o
  [ 33%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfStdIO.cpp.o
  [ 33%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfStringAttribute.cpp.o
  [ 33%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfStringVectorAttribute.cpp.o
  [ 33%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfSystemSpecific.cpp.o
  [ 33%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTestFile.cpp.o
  [ 33%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfThreading.cpp.o
  [ 33%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTileDescriptionAttribute.cpp.o
  [ 33%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTileOffsets.cpp.o
  [ 33%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTiledInputFile.cpp.o
  [ 34%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTiledInputPart.cpp.o
  [ 34%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTiledMisc.cpp.o
  [ 34%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTiledOutputFile.cpp.o
  [ 34%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTiledOutputPart.cpp.o
  [ 34%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTiledRgbaFile.cpp.o
  [ 34%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTimeCode.cpp.o
  [ 34%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTimeCodeAttribute.cpp.o
  [ 34%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfVecAttribute.cpp.o
  [ 34%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfVersion.cpp.o
  [ 34%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfWav.cpp.o
  [ 35%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfZip.cpp.o
  [ 35%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfZipCompressor.cpp.o
  [ 35%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/dwaLookups.cpp.o
  [ 35%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThread.cpp.o
  [ 35%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThreadMutex.cpp.o
  [ 35%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThreadMutexPosix.cpp.o
  [ 35%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThreadPool.cpp.o
  [ 35%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThreadPosix.cpp.o
  [ 35%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThreadSemaphore.cpp.o
  [ 35%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThreadSemaphorePosix.cpp.o
  [ 36%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThreadSemaphorePosixCompat.cpp.o
  [ 36%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Imath/ImathBox.cpp.o
  [ 36%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Imath/ImathColorAlgo.cpp.o
  [ 36%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Imath/ImathFun.cpp.o
  [ 36%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Imath/ImathMatrixAlgo.cpp.o
  [ 36%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Imath/ImathRandom.cpp.o
  [ 36%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Imath/ImathShear.cpp.o
  [ 36%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Imath/ImathVec.cpp.o
  [ 36%] Linking CXX static library ../lib/libIlmImf.a
  [ 36%] Built target IlmImf
  [ 37%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/arena.cc.o
  [ 37%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/arenastring.cc.o
  [ 37%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/extension_set.cc.o
  [ 37%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/generated_message_table_driven_lite.cc.o
  [ 37%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/generated_message_util.cc.o
  [ 37%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/coded_stream.cc.o
  [ 37%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/zero_copy_stream.cc.o
  [ 37%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/zero_copy_stream_impl_lite.cc.o
  [ 37%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/message_lite.cc.o
  [ 37%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/repeated_field.cc.o
  [ 38%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/atomicops_internals_x86_gcc.cc.o
  [ 38%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/bytestream.cc.o
  [ 38%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/common.cc.o
  [ 38%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/int128.cc.o
  [ 38%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/io_win32.cc.o
  [ 38%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/once.cc.o
  [ 38%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/status.cc.o
  [ 38%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/statusor.cc.o
  [ 38%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/stringpiece.cc.o
  [ 38%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/stringprintf.cc.o
  [ 39%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/structurally_valid.cc.o
  [ 39%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/strutil.cc.o
  [ 39%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/time.cc.o
  [ 39%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/wire_format_lite.cc.o
  [ 39%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/any.cc.o
  [ 39%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/any.pb.cc.o
  [ 39%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/api.pb.cc.o
  [ 39%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/descriptor.cc.o
  [ 39%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/descriptor.pb.cc.o
  [ 39%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/descriptor_database.cc.o
  [ 40%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/duration.pb.cc.o
  [ 40%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/dynamic_message.cc.o
  [ 40%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/empty.pb.cc.o
  [ 40%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/extension_set_heavy.cc.o
  [ 40%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/field_mask.pb.cc.o
  [ 40%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/generated_message_reflection.cc.o
  [ 40%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/generated_message_table_driven.cc.o
  [ 40%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/gzip_stream.cc.o
  [ 40%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/printer.cc.o
  [ 40%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/strtod.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/tokenizer.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/zero_copy_stream_impl.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/map_field.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/message.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/reflection_ops.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/service.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/source_context.pb.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/struct.pb.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/mathlimits.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/substitute.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/text_format.cc.o
  [ 42%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/timestamp.pb.cc.o
  [ 42%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/type.pb.cc.o
  [ 42%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/unknown_field_set.cc.o
  [ 42%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/delimited_message_util.cc.o
  [ 42%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/field_comparator.cc.o
  [ 42%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/field_mask_util.cc.o
  [ 42%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/datapiece.cc.o
  [ 42%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/default_value_objectwriter.cc.o
  [ 42%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/field_mask_utility.cc.o
  [ 42%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/json_escaping.cc.o
  [ 43%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/json_objectwriter.cc.o
  [ 43%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/json_stream_parser.cc.o
  [ 43%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/object_writer.cc.o
  [ 43%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/proto_writer.cc.o
  [ 43%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/protostream_objectsource.cc.o
  [ 43%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/protostream_objectwriter.cc.o
  [ 43%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/type_info.cc.o
  [ 43%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/utility.cc.o
  [ 43%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/json_util.cc.o
  [ 43%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/message_differencer.cc.o
  [ 44%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/time_util.cc.o
  [ 44%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/type_resolver_util.cc.o
  [ 44%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/wire_format.cc.o
  [ 44%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/wrappers.pb.cc.o
  [ 44%] Linking CXX static library ../lib/liblibprotobuf.a
  [ 44%] Built target libprotobuf
  [ 44%] Building C object 3rdparty/quirc/CMakeFiles/quirc.dir/src/decode.c.o
  [ 44%] Building C object 3rdparty/quirc/CMakeFiles/quirc.dir/src/quirc.c.o
  [ 44%] Building C object 3rdparty/quirc/CMakeFiles/quirc.dir/src/version_db.c.o
  [ 44%] Linking C static library ../lib/libquirc.a
  [ 44%] Built target quirc
  [ 44%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/absdiff.cpp.o
  [ 44%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/accumulate.cpp.o
  [ 45%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/add.cpp.o
  [ 45%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/add_weighted.cpp.o
  [ 45%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/bitwise.cpp.o
  [ 45%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/blur.cpp.o
  [ 45%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/canny.cpp.o
  [ 45%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/channel_extract.cpp.o
  [ 45%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/channels_combine.cpp.o
  [ 45%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/cmp.cpp.o
  [ 45%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/colorconvert.cpp.o
  [ 45%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/common.cpp.o
  [ 46%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/convert.cpp.o
  [ 46%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/convert_depth.cpp.o
  [ 46%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/convert_scale.cpp.o
  [ 46%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/convolution.cpp.o
  [ 46%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/count_nonzero.cpp.o
  [ 46%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/div.cpp.o
  [ 46%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/dot_product.cpp.o
  [ 46%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/fast.cpp.o
  [ 46%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/fill_minmaxloc.cpp.o
  [ 46%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/flip.cpp.o
  [ 47%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/gaussian_blur.cpp.o
  [ 47%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/in_range.cpp.o
  [ 47%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/integral.cpp.o
  [ 47%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/laplacian.cpp.o
  [ 47%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/magnitude.cpp.o
  [ 47%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/meanstddev.cpp.o
  [ 47%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/median_filter.cpp.o
  [ 47%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/min_max.cpp.o
  [ 47%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/minmaxloc.cpp.o
  [ 47%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/morph.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/mul.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/norm.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/opticalflow.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/phase.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/pyramid.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/reduce.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/remap.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/resize.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/scharr.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/separable_filter.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/sobel.cpp.o
  [ 49%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/sub.cpp.o
  [ 49%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/sum.cpp.o
  [ 49%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/template_matching.cpp.o
  [ 49%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/threshold.cpp.o
  [ 49%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/warp_affine.cpp.o
  [ 49%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/warp_perspective.cpp.o
  [ 49%] Built target carotene_objs
  [ 50%] Linking CXX static library ../../lib/libtegra_hal.a
  [ 50%] Built target tegra_hal
  [ 50%] Building C object 3rdparty/ittnotify/CMakeFiles/ittnotify.dir/src/ittnotify/ittnotify_static.c.o
  [ 50%] Building C object 3rdparty/ittnotify/CMakeFiles/ittnotify.dir/src/ittnotify/jitprofiling.c.o
  [ 51%] Linking C static library ../lib/libittnotify.a
  [ 51%] Built target ittnotify
  [ 51%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/alloc.cpp.o
  [ 52%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/assert.cpp.o
  [ 52%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/check_cycles.cpp.o
  [ 52%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/edge.cpp.o
  [ 52%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/execution_engine.cpp.o
  [ 52%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/graph.cpp.o
  [ 52%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/memory_accessor.cpp.o
  [ 52%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/memory_descriptor.cpp.o
  [ 52%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/memory_descriptor_ref.cpp.o
  [ 52%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/memory_descriptor_view.cpp.o
  [ 52%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/metadata.cpp.o
  [ 53%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/metatypes.cpp.o
  [ 53%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/node.cpp.o
  [ 53%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/passes/communications.cpp.o
  [ 53%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/search.cpp.o
  [ 53%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/subgraphs.cpp.o
  [ 53%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/topological_sort.cpp.o
  [ 53%] Linking CXX static library ../lib/libade.a
  [ 53%] Built target ade
  [ 53%] Built target opencv_videoio_plugins
  [ 53%] Processing OpenCL kernels (core)
  [ 53%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/algorithm.cpp.o
  [ 53%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/alloc.cpp.o
  [ 53%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/arithm.cpp.o
  [ 53%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/arithm.dispatch.cpp.o
  [ 53%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/array.cpp.o
  [ 54%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/async.cpp.o
  [ 54%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/batch_distance.cpp.o
  [ 54%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/bindings_utils.cpp.o
  [ 54%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/buffer_area.cpp.o
  [ 54%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/channels.cpp.o
  [ 54%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/check.cpp.o
  [ 54%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/command_line_parser.cpp.o
  [ 54%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/conjugate_gradient.cpp.o
  [ 54%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/convert.dispatch.cpp.o
  [ 54%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/convert_c.cpp.o
  [ 55%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/convert_scale.dispatch.cpp.o
  [ 55%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/copy.cpp.o
  [ 55%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/count_non_zero.dispatch.cpp.o
  [ 55%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/cuda_gpu_mat.cpp.o
  [ 55%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/cuda_host_mem.cpp.o
  [ 55%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/cuda_info.cpp.o
  [ 55%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/cuda_stream.cpp.o
  [ 55%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/datastructs.cpp.o
  [ 55%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/directx.cpp.o
  [ 55%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/downhill_simplex.cpp.o
  [ 56%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/dxt.cpp.o
  [ 56%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/gl_core_3_1.cpp.o
  [ 56%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/glob.cpp.o
  [ 56%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/hal_internal.cpp.o
  [ 56%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/kmeans.cpp.o
  [ 56%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/lapack.cpp.o
  [ 56%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/lda.cpp.o
  [ 56%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/logger.cpp.o
  [ 56%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/lpsolver.cpp.o
  [ 56%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/lut.cpp.o
  [ 57%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/mathfuncs.cpp.o
  [ 57%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/mathfuncs_core.dispatch.cpp.o
  [ 57%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matmul.dispatch.cpp.o
  [ 57%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matrix.cpp.o
  [ 57%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matrix_c.cpp.o
  [ 57%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matrix_decomp.cpp.o
  [ 57%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matrix_expressions.cpp.o
  [ 57%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matrix_iterator.cpp.o
  [ 57%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matrix_operations.cpp.o
  [ 57%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matrix_sparse.cpp.o
  [ 58%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matrix_wrap.cpp.o
  [ 58%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/mean.dispatch.cpp.o
  [ 58%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/merge.dispatch.cpp.o
  [ 58%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/minmax.cpp.o
  [ 58%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/norm.cpp.o
  [ 58%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/ocl.cpp.o
  [ 58%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/opencl/runtime/opencl_clamdblas.cpp.o
  [ 58%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/opencl/runtime/opencl_clamdfft.cpp.o
  [ 58%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/opencl/runtime/opencl_core.cpp.o
  [ 58%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/opengl.cpp.o
  [ 59%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/out.cpp.o
  [ 59%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/ovx.cpp.o
  [ 59%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/parallel.cpp.o
  [ 59%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/parallel_impl.cpp.o
  [ 59%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/pca.cpp.o
  [ 59%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/persistence.cpp.o
  [ 59%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/persistence_json.cpp.o
  [ 59%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/persistence_types.cpp.o
  [ 59%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/persistence_xml.cpp.o
  [ 59%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/persistence_yml.cpp.o
  [ 60%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/rand.cpp.o
  [ 60%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/softfloat.cpp.o
  [ 60%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/split.dispatch.cpp.o
  [ 60%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/stat.dispatch.cpp.o
  [ 60%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/stat_c.cpp.o
  [ 60%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/stl.cpp.o
  [ 60%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/sum.dispatch.cpp.o
  [ 60%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/system.cpp.o
  [ 60%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/tables.cpp.o
  [ 60%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/trace.cpp.o
  [ 61%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/types.cpp.o
  [ 61%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/umatrix.cpp.o
  [ 61%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/utils/datafile.cpp.o
  [ 61%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/utils/filesystem.cpp.o
  [ 61%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/utils/logtagconfigparser.cpp.o
  [ 61%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/utils/logtagmanager.cpp.o
  [ 61%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/utils/samples.cpp.o
  [ 61%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/va_intel.cpp.o
  [ 61%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/opencl_kernels_core.cpp.o
  [ 61%] Linking CXX static library ../../lib/libopencv_core.a
  [ 61%] Built target opencv_core
  [ 61%] Building CXX object modules/flann/CMakeFiles/opencv_flann.dir/src/flann.cpp.o
  [ 61%] Building CXX object modules/flann/CMakeFiles/opencv_flann.dir/src/miniflann.cpp.o
  [ 61%] Linking CXX static library ../../lib/libopencv_flann.a
  [ 61%] Built target opencv_flann
  [ 61%] Processing OpenCL kernels (imgproc)
  [ 61%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/accum.cpp.o
  [ 61%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/accum.dispatch.cpp.o
  [ 61%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/approx.cpp.o
  [ 61%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/bilateral_filter.dispatch.cpp.o
  [ 61%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/blend.cpp.o
  [ 61%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/box_filter.dispatch.cpp.o
  [ 61%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/canny.cpp.o
  [ 62%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/clahe.cpp.o
  [ 62%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/color.cpp.o
  [ 62%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/color_hsv.dispatch.cpp.o
  [ 62%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/color_lab.cpp.o
  [ 62%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/color_rgb.dispatch.cpp.o
  [ 62%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/color_yuv.dispatch.cpp.o
  [ 62%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/colormap.cpp.o
  [ 62%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/connectedcomponents.cpp.o
  [ 62%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/contours.cpp.o
  [ 62%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/convhull.cpp.o
  [ 63%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/corner.cpp.o
  [ 63%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/cornersubpix.cpp.o
  [ 63%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/demosaicing.cpp.o
  [ 63%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/deriv.cpp.o
  [ 63%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/distransform.cpp.o
  [ 63%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/drawing.cpp.o
  [ 63%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/emd.cpp.o
  [ 63%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/featureselect.cpp.o
  [ 63%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/filter.dispatch.cpp.o
  [ 63%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/floodfill.cpp.o
  [ 64%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/gabor.cpp.o
  [ 64%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/generalized_hough.cpp.o
  [ 64%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/geometry.cpp.o
  [ 64%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/grabcut.cpp.o
  [ 64%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/hershey_fonts.cpp.o
  [ 64%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/histogram.cpp.o
  [ 64%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/hough.cpp.o
  [ 64%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/imgwarp.cpp.o
  [ 64%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/intersection.cpp.o
  [ 64%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/linefit.cpp.o
  [ 65%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/lsd.cpp.o
  [ 65%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/main.cpp.o
  [ 65%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/matchcontours.cpp.o
  [ 65%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/median_blur.dispatch.cpp.o
  [ 65%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/min_enclosing_triangle.cpp.o
  [ 65%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/moments.cpp.o
  [ 65%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/morph.dispatch.cpp.o
  [ 65%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/phasecorr.cpp.o
  [ 65%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/pyramids.cpp.o
  [ 65%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/resize.cpp.o
  [ 66%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/rotcalipers.cpp.o
  [ 66%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/samplers.cpp.o
  [ 66%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/segmentation.cpp.o
  [ 66%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/shapedescr.cpp.o
  [ 66%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/smooth.dispatch.cpp.o
  [ 66%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/spatialgradient.cpp.o
  [ 66%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/subdivision2d.cpp.o
  [ 66%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/sumpixels.dispatch.cpp.o
  [ 66%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/tables.cpp.o
  [ 66%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/templmatch.cpp.o
  [ 67%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/thresh.cpp.o
  [ 67%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/utils.cpp.o
  [ 67%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/opencl_kernels_imgproc.cpp.o
  [ 67%] Linking CXX static library ../../lib/libopencv_imgproc.a
  [ 67%] Built target opencv_imgproc
  [ 67%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/ann_mlp.cpp.o
  [ 67%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/boost.cpp.o
  [ 67%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/data.cpp.o
  [ 67%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/em.cpp.o
  [ 67%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/gbt.cpp.o
  [ 67%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/inner_functions.cpp.o
  [ 68%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/kdtree.cpp.o
  [ 68%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/knearest.cpp.o
  [ 68%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/lr.cpp.o
  [ 68%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/nbayes.cpp.o
  [ 68%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/rtrees.cpp.o
  [ 68%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/svm.cpp.o
  [ 68%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/svmsgd.cpp.o
  [ 68%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/testset.cpp.o
  [ 68%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/tree.cpp.o
  [ 68%] Linking CXX static library ../../lib/libopencv_ml.a
  [ 68%] Built target opencv_ml
  [ 68%] Processing OpenCL kernels (photo)
  [ 69%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/align.cpp.o
  [ 69%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/calibrate.cpp.o
  [ 69%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/contrast_preserve.cpp.o
  [ 69%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/denoise_tvl1.cpp.o
  [ 69%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/denoising.cpp.o
  [ 69%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/denoising.cuda.cpp.o
  [ 69%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/hdr_common.cpp.o
  [ 69%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/inpaint.cpp.o
  [ 69%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/merge.cpp.o
  [ 69%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/npr.cpp.o
  [ 70%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/seamless_cloning.cpp.o
  [ 70%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/seamless_cloning_impl.cpp.o
  [ 70%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/tonemap.cpp.o
  [ 70%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/opencl_kernels_photo.cpp.o
  [ 70%] Linking CXX static library ../../lib/libopencv_photo.a
  [ 70%] Built target opencv_photo
  [ 71%] Processing OpenCL kernels (dnn)
  [ 71%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/caffe/opencv-caffe.pb.cc.o
  [ 71%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/onnx/opencv-onnx.pb.cc.o
  [ 71%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/attr_value.pb.cc.o
  [ 71%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/function.pb.cc.o
  [ 71%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/graph.pb.cc.o
  [ 71%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/op_def.pb.cc.o
  [ 71%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/tensor.pb.cc.o
  [ 71%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/tensor_shape.pb.cc.o
  [ 71%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/types.pb.cc.o
  [ 72%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/versions.pb.cc.o
  [ 72%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/caffe/caffe_importer.cpp.o
  [ 72%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/caffe/caffe_io.cpp.o
  [ 72%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/caffe/caffe_shrinker.cpp.o
  [ 72%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/darknet/darknet_importer.cpp.o
  [ 72%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/darknet/darknet_io.cpp.o
  [ 72%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/dnn.cpp.o
  [ 72%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/graph_simplifier.cpp.o
  [ 72%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/halide_scheduler.cpp.o
  [ 72%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/ie_ngraph.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/init.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/batch_norm_layer.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/blank_layer.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/concat_layer.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/const_layer.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/convolution_layer.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/crop_and_resize_layer.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/detection_output_layer.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/elementwise_layers.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/eltwise_layer.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/flatten_layer.cpp.o
  [ 74%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/fully_connected_layer.cpp.o
  [ 74%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/layers_common.cpp.o
  [ 74%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/lrn_layer.cpp.o
  [ 74%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/max_unpooling_layer.cpp.o
  [ 74%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/mvn_layer.cpp.o
  [ 74%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/normalize_bbox_layer.cpp.o
  [ 74%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/padding_layer.cpp.o
  [ 74%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/permute_layer.cpp.o
  [ 74%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/pooling_layer.cpp.o
  [ 74%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/prior_box_layer.cpp.o
  [ 75%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/proposal_layer.cpp.o
  [ 75%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/recurrent_layers.cpp.o
  [ 75%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/region_layer.cpp.o
  [ 75%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/reorg_layer.cpp.o
  [ 75%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/reshape_layer.cpp.o
  [ 75%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/resize_layer.cpp.o
  [ 75%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/scale_layer.cpp.o
  [ 75%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/shuffle_channel_layer.cpp.o
  [ 75%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/slice_layer.cpp.o
  [ 75%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/softmax_layer.cpp.o
  [ 76%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/split_layer.cpp.o
  [ 76%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/model.cpp.o
  [ 76%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/nms.cpp.o
  [ 76%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/ocl4dnn/src/common.cpp.o
  [ 76%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/ocl4dnn/src/math_functions.cpp.o
  [ 76%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/ocl4dnn/src/ocl4dnn_conv_spatial.cpp.o
  [ 76%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/ocl4dnn/src/ocl4dnn_inner_product.cpp.o
  [ 76%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/ocl4dnn/src/ocl4dnn_lrn.cpp.o
  [ 76%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/ocl4dnn/src/ocl4dnn_pool.cpp.o
  [ 76%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/ocl4dnn/src/ocl4dnn_softmax.cpp.o
  [ 77%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/onnx/onnx_graph_simplifier.cpp.o
  [ 77%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/onnx/onnx_importer.cpp.o
  [ 77%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/op_halide.cpp.o
  [ 77%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/op_inf_engine.cpp.o
  [ 77%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/op_vkcom.cpp.o
  [ 77%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/tengine4dnn/src/tengine_graph_convolution.cpp.o
  [ 77%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/tensorflow/tf_graph_simplifier.cpp.o
  [ 77%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/tensorflow/tf_importer.cpp.o
  [ 77%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/tensorflow/tf_io.cpp.o
  [ 77%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/torch/THDiskFile.cpp.o
  [ 78%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/torch/THFile.cpp.o
  [ 78%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/torch/THGeneral.cpp.o
  [ 78%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/torch/torch_importer.cpp.o
  [ 78%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/avg_pool_spv.cpp.o
  [ 78%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/concat_spv.cpp.o
  [ 78%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/conv48_spv.cpp.o
  [ 78%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/conv_spv.cpp.o
  [ 78%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/dw_conv_spv.cpp.o
  [ 78%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/lrn_spv.cpp.o
  [ 78%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/max_pool_spv.cpp.o
  [ 79%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/permute_spv.cpp.o
  [ 79%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/prior_box_spv.cpp.o
  [ 79%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/relu_spv.cpp.o
  [ 79%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/softmax_spv.cpp.o
  [ 79%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/buffer.cpp.o
  [ 79%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/context.cpp.o
  [ 79%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/internal.cpp.o
  [ 79%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/op_base.cpp.o
  [ 79%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/op_concat.cpp.o
  [ 79%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/op_conv.cpp.o
  [ 80%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/op_lrn.cpp.o
  [ 80%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/op_permute.cpp.o
  [ 80%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/op_pool.cpp.o
  [ 80%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/op_prior_box.cpp.o
  [ 80%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/op_relu.cpp.o
  [ 80%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/op_softmax.cpp.o
  [ 80%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/tensor.cpp.o
  [ 80%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/vulkan/vk_functions.cpp.o
  [ 80%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/vulkan/vk_loader.cpp.o
  [ 80%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/opencl_kernels_dnn.cpp.o
  [ 81%] Linking CXX static library ../../lib/libopencv_dnn.a
  [ 81%] Built target opencv_dnn
  [ 81%] Processing OpenCL kernels (features2d)
  [ 81%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/agast.cpp.o
  [ 81%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/agast_score.cpp.o
  [ 81%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/akaze.cpp.o
  [ 81%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/bagofwords.cpp.o
  [ 81%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/blobdetector.cpp.o
  [ 81%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/brisk.cpp.o
  [ 81%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/draw.cpp.o
  [ 81%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/dynamic.cpp.o
  [ 82%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/evaluation.cpp.o
  [ 82%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/fast.cpp.o
  [ 82%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/fast_score.cpp.o
  [ 82%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/feature2d.cpp.o
  [ 82%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/gftt.cpp.o
  [ 82%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/kaze.cpp.o
  [ 82%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/kaze/AKAZEFeatures.cpp.o
  [ 82%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/kaze/KAZEFeatures.cpp.o
  [ 82%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/kaze/fed.cpp.o
  [ 82%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/kaze/nldiffusion_functions.cpp.o
  [ 83%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/keypoint.cpp.o
  [ 83%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/main.cpp.o
  [ 83%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/matchers.cpp.o
  [ 83%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/mser.cpp.o
  [ 83%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/orb.cpp.o
  [ 83%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/opencl_kernels_features2d.cpp.o
  [ 83%] Linking CXX static library ../../lib/libopencv_features2d.a
  [ 83%] Built target opencv_features2d
  [ 84%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/gorigin.cpp.o
  [ 84%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/gmat.cpp.o
  [ 84%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/garray.cpp.o
  [ 84%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/gopaque.cpp.o
  [ 84%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/gscalar.cpp.o
  [ 84%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/gkernel.cpp.o
  [ 84%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/gbackend.cpp.o
  [ 84%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/gproto.cpp.o
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/optional.hpp:11,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/gscalar.hpp:16,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/core.hpp:18,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/precomp.hpp:14,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:8:
  In function ‘bool cv::util::operator==(const cv::util::variant<Ts ...>&, const cv::util::variant<Ts ...>&) [with Us = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’,
      inlined from ‘bool cv::can_describe(const GMetaArg&, const GRunArgP&)’ at /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:160:68:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:369:34: warning: ‘<anonymous>’ may be used uninitialized [-Wmaybe-uninitialized]
    369 |         return (eqs[lhs.index()])(lhs.memory, rhs.memory);
        |                ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp: In function ‘bool cv::can_describe(const GMetaArg&, const GRunArgP&)’:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:120:25: note: by argument 2 of type ‘const std::aligned_storage<48, 8>::type*’ to ‘static bool cv::util::variant<Ts>::equal_h<T>::help(const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*, const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*) [with T = cv::GScalarDesc; Ts = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’ declared here
    120 |             static bool help(const Memory lhs, const Memory rhs) {
        |                         ^~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:160:119: note: ‘<anonymous>’ declared here
    160 |     case GRunArgP::index_of<cv::Scalar*>():            return meta == GMetaArg(descr_of(*util::get<cv::Scalar*>(argp)));
        |                                                                                                                       ^
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/optional.hpp:11,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/gscalar.hpp:16,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/core.hpp:18,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/precomp.hpp:14,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:8:
  In function ‘bool cv::util::operator==(const cv::util::variant<Ts ...>&, const cv::util::variant<Ts ...>&) [with Us = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’,
      inlined from ‘bool cv::can_describe(const GMetaArg&, const GRunArgP&)’ at /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:161:68:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:369:34: warning: ‘<anonymous>’ may be used uninitialized [-Wmaybe-uninitialized]
    369 |         return (eqs[lhs.index()])(lhs.memory, rhs.memory);
        |                ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp: In function ‘bool cv::can_describe(const GMetaArg&, const GRunArgP&)’:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:120:25: note: by argument 2 of type ‘const std::aligned_storage<48, 8>::type*’ to ‘static bool cv::util::variant<Ts>::equal_h<T>::help(const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*, const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*) [with T = cv::GArrayDesc; Ts = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’ declared here
    120 |             static bool help(const Memory lhs, const Memory rhs) {
        |                         ^~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:161:129: note: ‘<anonymous>’ declared here
    161 |     case GRunArgP::index_of<cv::detail::VectorRef>():  return meta == GMetaArg(util::get<cv::detail::VectorRef>(argp).descr_of());
        |                                                                                                                                 ^
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/optional.hpp:11,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/gscalar.hpp:16,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/core.hpp:18,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/precomp.hpp:14,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:8:
  In function ‘bool cv::util::operator==(const cv::util::variant<Ts ...>&, const cv::util::variant<Ts ...>&) [with Us = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’,
      inlined from ‘bool cv::can_describe(const GMetaArg&, const GRunArgP&)’ at /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:162:68:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:369:34: warning: ‘<anonymous>’ may be used uninitialized [-Wmaybe-uninitialized]
    369 |         return (eqs[lhs.index()])(lhs.memory, rhs.memory);
        |                ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp: In function ‘bool cv::can_describe(const GMetaArg&, const GRunArgP&)’:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:120:25: note: by argument 2 of type ‘const std::aligned_storage<48, 8>::type*’ to ‘static bool cv::util::variant<Ts>::equal_h<T>::help(const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*, const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*) [with T = cv::GOpaqueDesc; Ts = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’ declared here
    120 |             static bool help(const Memory lhs, const Memory rhs) {
        |                         ^~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:162:129: note: ‘<anonymous>’ declared here
    162 |     case GRunArgP::index_of<cv::detail::OpaqueRef>():  return meta == GMetaArg(util::get<cv::detail::OpaqueRef>(argp).descr_of());
        |                                                                                                                                 ^
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/optional.hpp:11,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/gscalar.hpp:16,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/core.hpp:18,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/precomp.hpp:14,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:8:
  In function ‘bool cv::util::operator==(const cv::util::variant<Ts ...>&, const cv::util::variant<Ts ...>&) [with Us = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’,
      inlined from ‘bool cv::can_describe(const GMetaArg&, const GRunArg&)’ at /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:178:66:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:369:34: warning: ‘<anonymous>’ may be used uninitialized [-Wmaybe-uninitialized]
    369 |         return (eqs[lhs.index()])(lhs.memory, rhs.memory);
        |                ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp: In function ‘bool cv::can_describe(const GMetaArg&, const GRunArg&)’:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:120:25: note: by argument 2 of type ‘const std::aligned_storage<48, 8>::type*’ to ‘static bool cv::util::variant<Ts>::equal_h<T>::help(const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*, const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*) [with T = cv::GScalarDesc; Ts = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’ declared here
    120 |             static bool help(const Memory lhs, const Memory rhs) {
        |                         ^~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:178:118: note: ‘<anonymous>’ declared here
    178 |     case GRunArg::index_of<cv::Scalar>():            return meta == cv::GMetaArg(descr_of(util::get<cv::Scalar>(arg)));
        |                                                                                                                      ^
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/optional.hpp:11,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/gscalar.hpp:16,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/core.hpp:18,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/precomp.hpp:14,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:8:
  In function ‘bool cv::util::operator==(const cv::util::variant<Ts ...>&, const cv::util::variant<Ts ...>&) [with Us = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’,
      inlined from ‘bool cv::can_describe(const GMetaArg&, const GRunArg&)’ at /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:179:66:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:369:34: warning: ‘<anonymous>’ may be used uninitialized [-Wmaybe-uninitialized]
    369 |         return (eqs[lhs.index()])(lhs.memory, rhs.memory);
        |                ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp: In function ‘bool cv::can_describe(const GMetaArg&, const GRunArg&)’:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:120:25: note: by argument 2 of type ‘const std::aligned_storage<48, 8>::type*’ to ‘static bool cv::util::variant<Ts>::equal_h<T>::help(const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*, const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*) [with T = cv::GArrayDesc; Ts = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’ declared here
    120 |             static bool help(const Memory lhs, const Memory rhs) {
        |                         ^~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:179:130: note: ‘<anonymous>’ declared here
    179 |     case GRunArg::index_of<cv::detail::VectorRef>(): return meta == cv::GMetaArg(util::get<cv::detail::VectorRef>(arg).descr_of());
        |                                                                                                                                  ^
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/optional.hpp:11,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/gscalar.hpp:16,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/core.hpp:18,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/precomp.hpp:14,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:8:
  In function ‘bool cv::util::operator==(const cv::util::variant<Ts ...>&, const cv::util::variant<Ts ...>&) [with Us = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’,
      inlined from ‘bool cv::can_describe(const GMetaArg&, const GRunArg&)’ at /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:180:66:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:369:34: warning: ‘<anonymous>’ may be used uninitialized [-Wmaybe-uninitialized]
    369 |         return (eqs[lhs.index()])(lhs.memory, rhs.memory);
        |                ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp: In function ‘bool cv::can_describe(const GMetaArg&, const GRunArg&)’:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:120:25: note: by argument 2 of type ‘const std::aligned_storage<48, 8>::type*’ to ‘static bool cv::util::variant<Ts>::equal_h<T>::help(const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*, const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*) [with T = cv::GOpaqueDesc; Ts = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’ declared here
    120 |             static bool help(const Memory lhs, const Memory rhs) {
        |                         ^~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:180:130: note: ‘<anonymous>’ declared here
    180 |     case GRunArg::index_of<cv::detail::OpaqueRef>(): return meta == cv::GMetaArg(util::get<cv::detail::OpaqueRef>(arg).descr_of());
        |                                                                                                                                  ^
  [ 84%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/gnode.cpp.o
  [ 84%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/gcall.cpp.o
  [ 85%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/gcomputation.cpp.o
  [ 85%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/operators.cpp.o
  [ 85%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/kernels_core.cpp.o
  [ 85%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/kernels_imgproc.cpp.o
  [ 85%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/render.cpp.o
  [ 85%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/render_ocv.cpp.o
  [ 85%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/ginfer.cpp.o
  [ 85%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/ft_render.cpp.o
  [ 85%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/gmodel.cpp.o
  [ 85%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/gmodelbuilder.cpp.o
  [ 86%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/gislandmodel.cpp.o
  [ 86%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/gcompiler.cpp.o
  [ 86%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/gcompiled.cpp.o
  [ 86%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/gstreaming.cpp.o
  [ 86%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/passes/helpers.cpp.o
  [ 86%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/passes/dump_dot.cpp.o
  [ 86%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/passes/islands.cpp.o
  [ 86%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/passes/meta.cpp.o
  [ 86%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/passes/kernels.cpp.o
  [ 86%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/passes/exec.cpp.o
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/compiler/passes/exec.cpp: In function ‘void cv::gimpl::{anonymous}::fuseTrivial(cv::gimpl::GIslandModel::Graph&, const ade::Graph&)’:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/compiler/passes/exec.cpp:74:25: warning: loop variable ‘nh’ creates a copy from type ‘const ade::Handle<ade::Node>’ [-Wrange-loop-construct]
     74 |         for (const auto nh : proto.in_nhs)
        |                         ^~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/compiler/passes/exec.cpp:74:25: note: use reference type to prevent copying
     74 |         for (const auto nh : proto.in_nhs)
        |                         ^~
        |                         &
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/compiler/passes/exec.cpp:79:25: warning: loop variable ‘nh’ creates a copy from type ‘const ade::Handle<ade::Node>’ [-Wrange-loop-construct]
     79 |         for (const auto nh : proto.out_nhs)
        |                         ^~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/compiler/passes/exec.cpp:79:25: note: use reference type to prevent copying
     79 |         for (const auto nh : proto.out_nhs)
        |                         ^~
        |                         &
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/compiler/passes/exec.cpp:93:25: warning: loop variable ‘nh’ creates a copy from type ‘const ade::Handle<ade::Node>’ [-Wrange-loop-construct]
     93 |         for (const auto nh : proto.in_nhs)
        |                         ^~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/compiler/passes/exec.cpp:93:25: note: use reference type to prevent copying
     93 |         for (const auto nh : proto.in_nhs)
        |                         ^~
        |                         &
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/compiler/passes/exec.cpp:98:25: warning: loop variable ‘nh’ creates a copy from type ‘const ade::Handle<ade::Node>’ [-Wrange-loop-construct]
     98 |         for (const auto nh : proto.out_nhs)
        |                         ^~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/compiler/passes/exec.cpp:98:25: note: use reference type to prevent copying
     98 |         for (const auto nh : proto.out_nhs)
        |                         ^~
        |                         &
  [ 87%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/passes/transformations.cpp.o
  [ 87%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/passes/pattern_matching.cpp.o
  [ 87%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/passes/perform_substitution.cpp.o
  [ 87%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/passes/streaming.cpp.o
  [ 87%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/executor/gexecutor.cpp.o
  [ 87%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/executor/gstreamingexecutor.cpp.o
  [ 87%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/executor/gasync.cpp.o
  [ 87%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/cpu/gcpubackend.cpp.o
  [ 87%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/cpu/gcpukernel.cpp.o
  [ 87%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/cpu/gcpuimgproc.cpp.o
  [ 88%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/cpu/gcpucore.cpp.o
  [ 88%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/fluid/gfluidbuffer.cpp.o
  [ 88%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/fluid/gfluidbackend.cpp.o
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/backends/fluid/gfluidbackend.cpp: In lambda function:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/backends/fluid/gfluidbackend.cpp:1464:37: warning: loop variable ‘node’ creates a copy from type ‘const ade::Handle<ade::Node>’ [-Wrange-loop-construct]
   1464 |                     for (const auto node : isl->contents())
        |                                     ^~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/backends/fluid/gfluidbackend.cpp:1464:37: note: use reference type to prevent copying
   1464 |                     for (const auto node : isl->contents())
        |                                     ^~~~
        |                                     &
  [ 88%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/fluid/gfluidimgproc.cpp.o
  [ 88%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/fluid/gfluidimgproc_func.dispatch.cpp.o
  [ 88%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/fluid/gfluidcore.cpp.o
  [ 88%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/ocl/goclbackend.cpp.o
  [ 88%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/ocl/goclkernel.cpp.o
  [ 88%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/ocl/goclimgproc.cpp.o
  [ 88%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/ocl/goclcore.cpp.o
  [ 89%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/ie/giebackend.cpp.o
  [ 89%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/render/grenderocvbackend.cpp.o
  [ 89%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/render/grenderocv.cpp.o
  [ 89%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/plaidml/gplaidmlcore.cpp.o
  [ 89%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/plaidml/gplaidmlbackend.cpp.o
  [ 89%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/common/gcompoundbackend.cpp.o
  [ 89%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/common/gcompoundkernel.cpp.o
  [ 89%] Linking CXX static library ../../lib/libopencv_gapi.a
  [ 89%] Built target opencv_gapi
  [ 89%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/loadsave.cpp.o
  [ 89%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/utils.cpp.o
  [ 89%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_base.cpp.o
  [ 89%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_bmp.cpp.o
  [ 89%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_exr.cpp.o
  [ 89%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_gdal.cpp.o
  [ 89%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_gdcm.cpp.o
  [ 89%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_hdr.cpp.o
  [ 89%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_jpeg.cpp.o
  [ 89%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_jpeg2000.cpp.o
  [ 90%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_jpeg2000_openjpeg.cpp.o
  [ 90%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_pam.cpp.o
  [ 90%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_pfm.cpp.o
  [ 90%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_png.cpp.o
  [ 90%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_pxm.cpp.o
  [ 90%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_sunras.cpp.o
  [ 90%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_tiff.cpp.o
  [ 90%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_webp.cpp.o
  [ 90%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/bitstrm.cpp.o
  [ 90%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/rgbe.cpp.o
  [ 91%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/exif.cpp.o
  [ 91%] Linking CXX static library ../../lib/libopencv_imgcodecs.a
  [ 91%] Built target opencv_imgcodecs
  [ 91%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/videoio_registry.cpp.o
  [ 91%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/videoio_c.cpp.o
  [ 91%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/cap.cpp.o
  [ 91%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/cap_images.cpp.o
  [ 91%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/cap_mjpeg_encoder.cpp.o
  [ 92%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/cap_mjpeg_decoder.cpp.o
  [ 92%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/backend_plugin.cpp.o
  [ 92%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/backend_static.cpp.o
  [ 92%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/container_avi.cpp.o
  [ 92%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/cap_v4l.cpp.o
  [ 92%] Linking CXX static library ../../lib/libopencv_videoio.a
  [ 92%] Built target opencv_videoio
  [ 92%] Processing OpenCL kernels (calib3d)
  [ 92%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/ap3p.cpp.o
  [ 92%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/calibinit.cpp.o
  [ 92%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/calibration.cpp.o
  [ 92%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/calibration_handeye.cpp.o
  [ 92%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/checkchessboard.cpp.o
  [ 92%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/chessboard.cpp.o
  [ 92%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/circlesgrid.cpp.o
  [ 93%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/compat_ptsetreg.cpp.o
  [ 93%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/dls.cpp.o
  [ 93%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/epnp.cpp.o
  [ 93%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/fisheye.cpp.o
  [ 93%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/five-point.cpp.o
  [ 93%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/fundam.cpp.o
  [ 93%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/homography_decomp.cpp.o
  [ 93%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/ippe.cpp.o
  [ 93%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/levmarq.cpp.o
  [ 93%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/main.cpp.o
  [ 94%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/p3p.cpp.o
  [ 94%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/polynom_solver.cpp.o
  [ 94%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/posit.cpp.o
  [ 94%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/ptsetreg.cpp.o
  [ 94%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/quadsubpix.cpp.o
  [ 94%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/rho.cpp.o
  [ 94%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/solvepnp.cpp.o
  [ 94%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/stereobm.cpp.o
  [ 94%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/stereosgbm.cpp.o
  [ 94%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/triangulate.cpp.o
  [ 95%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/undistort.dispatch.cpp.o
  [ 95%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/upnp.cpp.o
  [ 95%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/opencl_kernels_calib3d.cpp.o
  [ 95%] Linking CXX static library ../../lib/libopencv_calib3d.a
  [ 95%] Built target opencv_calib3d
  [ 95%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/window.cpp.o
  [ 95%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/roiSelector.cpp.o
  [ 96%] Linking CXX static library ../../lib/libopencv_highgui.a
  [ 96%] Built target opencv_highgui
  [ 97%] Processing OpenCL kernels (objdetect)
  [ 97%] Building CXX object modules/objdetect/CMakeFiles/opencv_objdetect.dir/src/cascadedetect.cpp.o
  [ 97%] Building CXX object modules/objdetect/CMakeFiles/opencv_objdetect.dir/src/cascadedetect_convert.cpp.o
  [ 97%] Building CXX object modules/objdetect/CMakeFiles/opencv_objdetect.dir/src/detection_based_tracker.cpp.o
  [ 97%] Building CXX object modules/objdetect/CMakeFiles/opencv_objdetect.dir/src/hog.cpp.o
  [ 97%] Building CXX object modules/objdetect/CMakeFiles/opencv_objdetect.dir/src/main.cpp.o
  [ 97%] Building CXX object modules/objdetect/CMakeFiles/opencv_objdetect.dir/src/qrcode.cpp.o
  [ 97%] Building CXX object modules/objdetect/CMakeFiles/opencv_objdetect.dir/opencl_kernels_objdetect.cpp.o
  [ 97%] Linking CXX static library ../../lib/libopencv_objdetect.a
  [ 97%] Built target opencv_objdetect
  [ 97%] Processing OpenCL kernels (stitching)
  [ 97%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/autocalib.cpp.o
  [ 97%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/blenders.cpp.o
  [ 98%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/camera.cpp.o
  [ 98%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/exposure_compensate.cpp.o
  [ 98%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/matchers.cpp.o
  [ 98%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/motion_estimators.cpp.o
  [ 98%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/seam_finders.cpp.o
  [ 98%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/stitcher.cpp.o
  [ 98%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/timelapsers.cpp.o
  [ 98%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/util.cpp.o
  [ 98%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/warpers.cpp.o
  [ 98%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/warpers_cuda.cpp.o
  [ 99%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/opencl_kernels_stitching.cpp.o
  [ 99%] Linking CXX static library ../../lib/libopencv_stitching.a
  [ 99%] Built target opencv_stitching
  [ 99%] Processing OpenCL kernels (video)
  [ 99%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/bgfg_KNN.cpp.o
  [ 99%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/bgfg_gaussmix2.cpp.o
  [ 99%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/camshift.cpp.o
  [ 99%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/dis_flow.cpp.o
  [ 99%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/ecc.cpp.o
  [ 99%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/kalman.cpp.o
  [ 99%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/lkpyramid.cpp.o
  [100%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/optflowgf.cpp.o
  [100%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/optical_flow_io.cpp.o
  [100%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/variational_refinement.cpp.o
  [100%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/opencl_kernels_video.cpp.o
  [100%] Linking CXX static library ../../lib/libopencv_video.a
  [100%] Built target opencv_video
  [100%] Generate files for Python bindings and documentation
  Note: Class Feature2D has more than 1 base class (not supported by Python C extensions)
        Bases:  cv::Algorithm, cv::class, cv::Feature2D, cv::Algorithm
        Only the first base class will be used
  Note: Class detail_GraphCutSeamFinder has more than 1 base class (not supported by Python C extensions)
        Bases:  cv::detail::GraphCutSeamFinderBase, cv::detail::SeamFinder
        Only the first base class will be used
  [100%] Built target gen_opencv_python_source
  [100%] Building CXX object modules/python3/CMakeFiles/opencv_python3.dir/__/src2/cv2.cpp.o
  [100%] Linking CXX shared module ../../lib/python3/cv2.cpython-36m-aarch64-linux-gnu.so
  [100%] Built target opencv_python3
  Install the project...
  -- Install configuration: "Release"
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/opencl-headers-LICENSE.txt
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/cvconfig.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/opencv_modules.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/cmake/opencv4/OpenCVModules.cmake
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/cmake/opencv4/OpenCVModules-release.cmake
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/cmake/opencv4/OpenCVConfig-version.cmake
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/cmake/opencv4/OpenCVConfig.cmake
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/bin/setup_vars_opencv4.sh
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/valgrind.supp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/valgrind_3rdparty.supp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/liblibjpeg-turbo.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/libjpeg-turbo-README.md
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/libjpeg-turbo-LICENSE.md
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/libjpeg-turbo-README.ijg
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/liblibtiff.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/libtiff-COPYRIGHT
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/liblibwebp.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/liblibjasper.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/jasper-LICENSE
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/jasper-README
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/jasper-copyright
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/liblibpng.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/libpng-LICENSE
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/libpng-README
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/libIlmImf.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/openexr-LICENSE
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/openexr-AUTHORS.ilmbase
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/openexr-AUTHORS.openexr
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/liblibprotobuf.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/protobuf-LICENSE
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/protobuf-README.md
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/libquirc.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/quirc-LICENSE
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/libtegra_hal.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/libittnotify.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/ittnotify-LICENSE.BSD
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/ittnotify-LICENSE.GPL
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/opencv.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/libade.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/ade-LICENSE
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_core.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/ocl_defs.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/opencl_info.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/opencl_svm.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/autogenerated/opencl_clamdblas.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/autogenerated/opencl_clamdfft.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/autogenerated/opencl_core.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/autogenerated/opencl_core_wrappers.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/autogenerated/opencl_gl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/autogenerated/opencl_gl_wrappers.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/opencl_clamdblas.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/opencl_clamdfft.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/opencl_core.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/opencl_core_wrappers.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/opencl_gl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/opencl_gl_wrappers.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/opencl_svm_20.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/opencl_svm_definitions.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/opencl_svm_hsa_extension.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/block.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/border_interpolate.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/color.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/common.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/datamov_utils.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/dynamic_smem.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/emulation.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/filters.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/funcattrib.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/functional.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/limits.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/reduce.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/saturate_cast.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/scan.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/simd_functions.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/transform.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/type_traits.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/utility.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/vec_distance.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/vec_math.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/vec_traits.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/warp.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/warp_reduce.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/warp_shuffle.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/detail/color_detail.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/detail/reduce.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/detail/reduce_key_val.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/detail/transform_detail.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/detail/type_traits_detail.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/detail/vec_distance_detail.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/affine.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/async.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/base.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/bindings_utils.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/bufferpool.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/check.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/core.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/core_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda.inl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda_stream_accessor.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda_types.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cv_cpu_dispatch.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cv_cpu_helper.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cvdef.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cvstd.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cvstd.inl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cvstd_wrapper.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/directx.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/eigen.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/fast_math.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/hal.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/interface.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin_avx.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin_avx512.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin_cpp.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin_forward.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin_msa.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin_neon.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin_sse.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin_sse_em.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin_vsx.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin_wasm.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/msa_macros.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/simd_utils.impl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/mat.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/mat.inl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/matx.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/neon_utils.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/ocl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/ocl_genbase.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opengl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/operations.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/optim.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/ovx.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/persistence.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/saturate.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/simd_intrinsics.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/softfloat.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/sse_utils.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/traits.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/types.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/types_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/utility.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/utils/allocator_stats.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/utils/allocator_stats.impl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/utils/filesystem.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/utils/instrumentation.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/utils/logger.defines.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/utils/logger.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/utils/logtag.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/utils/tls.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/utils/trace.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/va_intel.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/version.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/vsx_utils.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/detail/async_promise.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/detail/exception_ptr.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/SoftFloat-COPYING.txt
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_flann.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/all_indices.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/allocator.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/any.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/autotuned_index.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/composite_index.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/config.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/defines.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/dist.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/dummy.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/dynamic_bitset.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/flann.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/flann_base.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/general.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/ground_truth.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/hdf5.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/heap.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/hierarchical_clustering_index.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/index_testing.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/kdtree_index.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/kdtree_single_index.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/kmeans_index.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/linear_index.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/logger.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/lsh_index.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/lsh_table.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/matrix.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/miniflann.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/nn_index.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/object_factory.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/params.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/random.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/result_set.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/sampling.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/saving.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/simplex_downhill.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/timer.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_imgproc.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgproc.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgproc/hal/hal.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgproc/hal/interface.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgproc/imgproc.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgproc/imgproc_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgproc/types_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgproc/detail/gcgraph.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_ml.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/ml.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/ml/ml.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/ml/ml.inl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_photo.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/photo.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/photo/cuda.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/photo/legacy/constants_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/photo/photo.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_dnn.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/dnn.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/dnn/all_layers.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/dnn/dict.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/dnn/dnn.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/dnn/dnn.inl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/dnn/layer.details.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/dnn/layer.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/dnn/shape_utils.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/dnn/utils/inference_engine.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/dnn/version.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_features2d.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/features2d.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/features2d/features2d.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/features2d/hal/interface.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_gapi.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/core.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/cpu/core.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/cpu/gcpukernel.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/cpu/imgproc.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/fluid/core.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/fluid/gfluidbuffer.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/fluid/gfluidkernel.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/fluid/imgproc.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/garg.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/garray.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gasync_context.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gcall.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gcommon.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gcompiled.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gcompiled_async.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gcompoundkernel.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gcomputation.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gcomputation_async.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gkernel.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gmat.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gmetaarg.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gopaque.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gproto.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gpu/core.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gpu/ggpukernel.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gpu/imgproc.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gscalar.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gstreaming.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gtransform.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gtype_traits.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gtyped.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/imgproc.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/infer.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/infer/ie.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/ocl/core.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/ocl/goclkernel.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/ocl/imgproc.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/opencv_includes.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/operators.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/own/assert.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/own/convert.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/own/cvdefs.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/own/exports.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/own/mat.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/own/saturate.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/own/scalar.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/own/types.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/plaidml/core.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/plaidml/gplaidmlkernel.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/plaidml/plaidml.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/render.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/render/render.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/streaming/cap.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/streaming/source.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/util/any.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/util/compiler_hints.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/util/optional.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/util/throw.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/util/util.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/util/variant.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_imgcodecs.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgcodecs.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgcodecs/imgcodecs.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgcodecs/imgcodecs_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgcodecs/ios.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgcodecs/legacy/constants_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_videoio.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/videoio.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/videoio/cap_ios.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/videoio/legacy/constants_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/videoio/registry.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/videoio/videoio.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/videoio/videoio_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_calib3d.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/calib3d.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/calib3d/calib3d.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/calib3d/calib3d_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_highgui.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/highgui.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/highgui/highgui.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/highgui/highgui_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_objdetect.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/objdetect.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/objdetect/detection_based_tracker.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/objdetect/objdetect.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_stitching.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/warpers.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/autocalib.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/blenders.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/camera.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/exposure_compensate.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/matchers.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/motion_estimators.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/seam_finders.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/timelapsers.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/util.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/util_inl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/warpers.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/warpers_inl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_video.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/video.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/video/background_segm.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/video/legacy/constants_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/video/tracking.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/video/video.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/python/cv2.cpython-36m-aarch64-linux-gnu.so
  -- Set non-toolchain portion of runtime path of "/tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/python/cv2.cpython-36m-aarch64-linux-gnu.so" to "/tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib"
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_eye.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_eye_tree_eyeglasses.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalcatface.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalcatface_extended.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalface_alt.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalface_alt2.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalface_alt_tree.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalface_default.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_fullbody.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_lefteye_2splits.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_licence_plate_rus_16stages.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_lowerbody.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_profileface.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_righteye_2splits.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_russian_plate_number.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_smile.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_upperbody.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/lbpcascades/lbpcascade_frontalcatface.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/lbpcascades/lbpcascade_frontalface.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/lbpcascades/lbpcascade_frontalface_improved.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/lbpcascades/lbpcascade_profileface.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/lbpcascades/lbpcascade_silverware.xml
  Copying files from CMake output
  creating directory _skbuild/linux-aarch64-3.6/cmake-install/cv2
  copying _skbuild/linux-aarch64-3.6/cmake-install/python/cv2.cpython-36m-aarch64-linux-gnu.so -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/cv2.cpython-36m-aarch64-linux-gnu.so
  creating directory _skbuild/linux-aarch64-3.6/cmake-install/cv2/data
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_eye.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_eye.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_eye_tree_eyeglasses.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_eye_tree_eyeglasses.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalcatface.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_frontalcatface.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalcatface_extended.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_frontalcatface_extended.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalface_alt.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_frontalface_alt.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalface_alt2.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_frontalface_alt2.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalface_alt_tree.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_frontalface_alt_tree.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalface_default.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_frontalface_default.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_fullbody.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_fullbody.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_lefteye_2splits.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_lefteye_2splits.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_licence_plate_rus_16stages.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_licence_plate_rus_16stages.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_lowerbody.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_lowerbody.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_profileface.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_profileface.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_righteye_2splits.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_righteye_2splits.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_russian_plate_number.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_russian_plate_number.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_smile.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_smile.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_upperbody.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_upperbody.xml
  Copying files from non-default sourcetree locations
  copying LICENSE.txt -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/LICENSE.txt
  copying LICENSE-3RD-PARTY.txt -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/LICENSE-3RD-PARTY.txt
  Traceback (most recent call last):
    File "/home/nexaiot/.local/lib/python3.6/site-packages/pip/_vendor/pep517/in_process/_in_process.py", line 363, in <module>
      main()
    File "/home/nexaiot/.local/lib/python3.6/site-packages/pip/_vendor/pep517/in_process/_in_process.py", line 345, in main
      json_out['return_val'] = hook(**hook_input['kwargs'])
    File "/home/nexaiot/.local/lib/python3.6/site-packages/pip/_vendor/pep517/in_process/_in_process.py", line 262, in build_wheel
      metadata_directory)
    File "/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/setuptools/build_meta.py", line 231, in build_wheel
      wheel_directory, config_settings)
    File "/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/setuptools/build_meta.py", line 215, in _build_with_temp_dir
      self.run_setup()
    File "/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/setuptools/build_meta.py", line 268, in run_setup
      self).run_setup(setup_script=setup_script)
python3 -m pip install --user opencv-python==4.3.0.38
Collecting opencv-python==4.3.0.38
  Downloading opencv-python-4.3.0.38.tar.gz (88.0 MB)
     |████████████████████████████████| 88.0 MB 53 kB/s             
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: numpy>=1.13.3 in /usr/lib/python3/dist-packages (from opencv-python==4.3.0.38) (1.13.3)
Building wheels for collected packages: opencv-python
  Building wheel for opencv-python (pyproject.toml) ... error
  ERROR: Command errored out with exit status 1:
   command: /usr/bin/python3 /home/nexaiot/.local/lib/python3.6/site-packages/pip/_vendor/pep517/in_process/_in_process.py build_wheel /tmp/tmpvxjk254b
       cwd: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d
  Complete output (2438 lines):
  
  
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
  -- Configuring done (1.7s)
  -- Generating done (0.0s)
  -- Build files have been written to: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_cmake_test_compile/build
  --
  -------
  ------------
  -----------------
  ----------------------
  ---------------------------
  --------------------------------
  -- Trying 'Unix Makefiles' generator - success
  --------------------------------------------------------------------------------
  
  Configuring Project
    Working directory:
      /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-build
    Command:
      /tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/cmake/data/bin/cmake /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv -G 'Unix Makefiles' -DCMAKE_INSTALL_PREFIX:PATH=/tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install -DPYTHON_VERSION_STRING:STRING=3.6.9 -DSKBUILD:INTERNAL=TRUE -DCMAKE_MODULE_PATH:PATH=/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/skbuild/resources/cmake -DPYTHON_EXECUTABLE:PATH=/usr/bin/python3 -DPYTHON_INCLUDE_DIR:PATH=/usr/include/python3.6m -DPYTHON_LIBRARY:PATH=/usr/lib/aarch64-linux-gnu/libpython3.6m.so -DPython_EXECUTABLE:PATH=/usr/bin/python3 -DPython_ROOT_DIR:PATH=/usr -DPython_INCLUDE_DIR:PATH=/usr/include/python3.6m -DPython_FIND_REGISTRY:STRING=NEVER -DPython_NumPy_INCLUDE_DIRS:PATH=/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/numpy/core/include -DPython3_EXECUTABLE:PATH=/usr/bin/python3 -DPython3_ROOT_DIR:PATH=/usr -DPython3_INCLUDE_DIR:PATH=/usr/include/python3.6m -DPython3_FIND_REGISTRY:STRING=NEVER -DPython3_NumPy_INCLUDE_DIRS:PATH=/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/numpy/core/include -DPYTHON3_EXECUTABLE=/usr/bin/python3 -DPYTHON3_INCLUDE_DIR=/usr/include/python3.6m -DPYTHON3_LIBRARY=/usr/lib/aarch64-linux-gnu/libpython3.6m.so -DBUILD_opencv_python3=ON -DBUILD_opencv_python2=OFF -DBUILD_opencv_java=OFF -DOPENCV_SKIP_PYTHON_LOADER=ON -DOPENCV_PYTHON3_INSTALL_PATH=python -DINSTALL_CREATE_DISTRIB=ON -DBUILD_opencv_apps=OFF -DBUILD_SHARED_LIBS=OFF -DBUILD_TESTS=OFF -DBUILD_PERF_TESTS=OFF -DBUILD_DOCS=OFF -DCMAKE_BUILD_TYPE:STRING=Release
  
  -- The CXX compiler identification is GNU 11.4.0
  -- The C compiler identification is GNU 11.4.0
  -- Detecting CXX compiler ABI info
  -- Detecting CXX compiler ABI info - done
  -- Check for working CXX compiler: /usr/bin/c++ - skipped
  -- Detecting CXX compile features
  -- Detecting CXX compile features - done
  -- Detecting C compiler ABI info
  -- Detecting C compiler ABI info - done
  -- Check for working C compiler: /usr/bin/cc - skipped
  -- Detecting C compile features
  -- Detecting C compile features - done
  -- Detected processor: aarch64
  CMake Warning (dev) at cmake/OpenCVUtils.cmake:131 (find_package):
    Policy CMP0148 is not set: The FindPythonInterp and FindPythonLibs modules
    are removed.  Run "cmake --help-policy CMP0148" for policy details.  Use
    the cmake_policy command to set the policy and suppress this warning.
  
  Call Stack (most recent call first):
    cmake/OpenCVDetectPython.cmake:64 (find_host_package)
    cmake/OpenCVDetectPython.cmake:271 (find_python)
    CMakeLists.txt:598 (include)
  This warning is for project developers.  Use -Wno-dev to suppress it.
  
  -- Found PythonInterp: /usr/bin/python3 (found suitable version "3.6.9", minimum required is "2.7")
  CMake Warning at cmake/OpenCVDetectPython.cmake:81 (message):
    CMake's 'find_host_package(PythonInterp 2.7)' found wrong Python version:
  
    PYTHON_EXECUTABLE=/usr/bin/python3
  
    PYTHON_VERSION_STRING=3.6.9
  
    Consider providing the 'PYTHON2_EXECUTABLE' variable via CMake command line
    or environment variables
  
  Call Stack (most recent call first):
    cmake/OpenCVDetectPython.cmake:271 (find_python)
    CMakeLists.txt:598 (include)
  
  
  -- Found Python2: /usr/bin/python2.7 (found version "2.7.17") found components: Interpreter
  CMake Warning (dev) at cmake/OpenCVUtils.cmake:131 (find_package):
    Policy CMP0148 is not set: The FindPythonInterp and FindPythonLibs modules
    are removed.  Run "cmake --help-policy CMP0148" for policy details.  Use
    the cmake_policy command to set the policy and suppress this warning.
  
  Call Stack (most recent call first):
    cmake/OpenCVDetectPython.cmake:96 (find_host_package)
    cmake/OpenCVDetectPython.cmake:271 (find_python)
    CMakeLists.txt:598 (include)
  This warning is for project developers.  Use -Wno-dev to suppress it.
  
  -- Found PythonInterp: /usr/bin/python2.7 (found version "2.7.17")
  CMake Warning (dev) at cmake/OpenCVDetectPython.cmake:140 (find_package):
    Policy CMP0148 is not set: The FindPythonInterp and FindPythonLibs modules
    are removed.  Run "cmake --help-policy CMP0148" for policy details.  Use
    the cmake_policy command to set the policy and suppress this warning.
  
  Call Stack (most recent call first):
    cmake/OpenCVDetectPython.cmake:271 (find_python)
    CMakeLists.txt:598 (include)
  This warning is for project developers.  Use -Wno-dev to suppress it.
  
  -- Could NOT find PythonLibs: Found unsuitable version "3.6.9", but required is exact version "2.7.17" (found /usr/lib/aarch64-linux-gnu/libpython3.6m.so)
  Traceback (most recent call last):
    File "<string>", line 1, in <module>
    File "/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/numpy/__init__.py", line 142, in <module>
      from . import add_newdocs
    File "/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/numpy/add_newdocs.py", line 13, in <module>
      from numpy.lib import add_newdoc
    File "/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/numpy/lib/__init__.py", line 8, in <module>
      from .type_check import *
    File "/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/numpy/lib/type_check.py", line 11, in <module>
      import numpy.core.numeric as _nx
    File "/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/numpy/core/__init__.py", line 26, in <module>
      raise ImportError(msg)
  ImportError:
  Importing the multiarray numpy extension module failed.  Most
  likely you are trying to import a failed build of numpy.
  If you're working with a numpy git repo, try `git clean -xdf` (removes all
  files not under version control).  Otherwise reinstall numpy.
  
  Original error was: cannot import name multiarray
  
  CMake Warning (dev) at cmake/OpenCVUtils.cmake:131 (find_package):
    Policy CMP0148 is not set: The FindPythonInterp and FindPythonLibs modules
    are removed.  Run "cmake --help-policy CMP0148" for policy details.  Use
    the cmake_policy command to set the policy and suppress this warning.
  
  Call Stack (most recent call first):
    cmake/OpenCVDetectPython.cmake:64 (find_host_package)
    cmake/OpenCVDetectPython.cmake:280 (find_python)
    CMakeLists.txt:598 (include)
  This warning is for project developers.  Use -Wno-dev to suppress it.
  
  -- Found PythonInterp: /usr/bin/python3 (found suitable version "3.6.9", minimum required is "3.2")
  CMake Warning (dev) at cmake/OpenCVDetectPython.cmake:140 (find_package):
    Policy CMP0148 is not set: The FindPythonInterp and FindPythonLibs modules
    are removed.  Run "cmake --help-policy CMP0148" for policy details.  Use
    the cmake_policy command to set the policy and suppress this warning.
  
  Call Stack (most recent call first):
    cmake/OpenCVDetectPython.cmake:280 (find_python)
    CMakeLists.txt:598 (include)
  This warning is for project developers.  Use -Wno-dev to suppress it.
  
  -- Found PythonLibs: /usr/lib/aarch64-linux-gnu/libpython3.6m.so (found suitable exact version "3.6.9")
  -- Looking for ccache - not found
  -- Performing Test HAVE_CXX_FSIGNED_CHAR
  -- Performing Test HAVE_CXX_FSIGNED_CHAR - Success
  -- Performing Test HAVE_C_FSIGNED_CHAR
  -- Performing Test HAVE_C_FSIGNED_CHAR - Success
  -- Performing Test HAVE_CXX_W
  -- Performing Test HAVE_CXX_W - Success
  -- Performing Test HAVE_C_W
  -- Performing Test HAVE_C_W - Success
  -- Performing Test HAVE_CXX_WALL
  -- Performing Test HAVE_CXX_WALL - Success
  -- Performing Test HAVE_C_WALL
  -- Performing Test HAVE_C_WALL - Success
  -- Performing Test HAVE_CXX_WERROR_RETURN_TYPE
  -- Performing Test HAVE_CXX_WERROR_RETURN_TYPE - Success
  -- Performing Test HAVE_C_WERROR_RETURN_TYPE
  -- Performing Test HAVE_C_WERROR_RETURN_TYPE - Success
  -- Performing Test HAVE_CXX_WERROR_NON_VIRTUAL_DTOR
  -- Performing Test HAVE_CXX_WERROR_NON_VIRTUAL_DTOR - Success
  -- Performing Test HAVE_C_WERROR_NON_VIRTUAL_DTOR
  -- Performing Test HAVE_C_WERROR_NON_VIRTUAL_DTOR - Failed
  -- Performing Test HAVE_CXX_WERROR_ADDRESS
  -- Performing Test HAVE_CXX_WERROR_ADDRESS - Success
  -- Performing Test HAVE_C_WERROR_ADDRESS
  -- Performing Test HAVE_C_WERROR_ADDRESS - Success
  -- Performing Test HAVE_CXX_WERROR_SEQUENCE_POINT
  -- Performing Test HAVE_CXX_WERROR_SEQUENCE_POINT - Success
  -- Performing Test HAVE_C_WERROR_SEQUENCE_POINT
  -- Performing Test HAVE_C_WERROR_SEQUENCE_POINT - Success
  -- Performing Test HAVE_CXX_WFORMAT
  -- Performing Test HAVE_CXX_WFORMAT - Success
  -- Performing Test HAVE_C_WFORMAT
  -- Performing Test HAVE_C_WFORMAT - Success
  -- Performing Test HAVE_CXX_WERROR_FORMAT_SECURITY
  -- Performing Test HAVE_CXX_WERROR_FORMAT_SECURITY - Success
  -- Performing Test HAVE_C_WERROR_FORMAT_SECURITY
  -- Performing Test HAVE_C_WERROR_FORMAT_SECURITY - Success
  -- Performing Test HAVE_CXX_WMISSING_DECLARATIONS
  -- Performing Test HAVE_CXX_WMISSING_DECLARATIONS - Success
  -- Performing Test HAVE_C_WMISSING_DECLARATIONS
  -- Performing Test HAVE_C_WMISSING_DECLARATIONS - Success
  -- Performing Test HAVE_CXX_WMISSING_PROTOTYPES
  -- Performing Test HAVE_CXX_WMISSING_PROTOTYPES - Failed
  -- Performing Test HAVE_C_WMISSING_PROTOTYPES
  -- Performing Test HAVE_C_WMISSING_PROTOTYPES - Success
  -- Performing Test HAVE_CXX_WSTRICT_PROTOTYPES
  -- Performing Test HAVE_CXX_WSTRICT_PROTOTYPES - Failed
  -- Performing Test HAVE_C_WSTRICT_PROTOTYPES
  -- Performing Test HAVE_C_WSTRICT_PROTOTYPES - Success
  -- Performing Test HAVE_CXX_WUNDEF
  -- Performing Test HAVE_CXX_WUNDEF - Success
  -- Performing Test HAVE_C_WUNDEF
  -- Performing Test HAVE_C_WUNDEF - Success
  -- Performing Test HAVE_CXX_WINIT_SELF
  -- Performing Test HAVE_CXX_WINIT_SELF - Success
  -- Performing Test HAVE_C_WINIT_SELF
  -- Performing Test HAVE_C_WINIT_SELF - Success
  -- Performing Test HAVE_CXX_WPOINTER_ARITH
  -- Performing Test HAVE_CXX_WPOINTER_ARITH - Success
  -- Performing Test HAVE_C_WPOINTER_ARITH
  -- Performing Test HAVE_C_WPOINTER_ARITH - Success
  -- Performing Test HAVE_CXX_WSHADOW
  -- Performing Test HAVE_CXX_WSHADOW - Success
  -- Performing Test HAVE_C_WSHADOW
  -- Performing Test HAVE_C_WSHADOW - Success
  -- Performing Test HAVE_CXX_WSIGN_PROMO
  -- Performing Test HAVE_CXX_WSIGN_PROMO - Success
  -- Performing Test HAVE_C_WSIGN_PROMO
  -- Performing Test HAVE_C_WSIGN_PROMO - Failed
  -- Performing Test HAVE_CXX_WUNINITIALIZED
  -- Performing Test HAVE_CXX_WUNINITIALIZED - Success
  -- Performing Test HAVE_C_WUNINITIALIZED
  -- Performing Test HAVE_C_WUNINITIALIZED - Success
  -- Performing Test HAVE_CXX_WSUGGEST_OVERRIDE
  -- Performing Test HAVE_CXX_WSUGGEST_OVERRIDE - Success
  -- Performing Test HAVE_C_WSUGGEST_OVERRIDE
  -- Performing Test HAVE_C_WSUGGEST_OVERRIDE - Failed
  -- Performing Test HAVE_CXX_WNO_DELETE_NON_VIRTUAL_DTOR
  -- Performing Test HAVE_CXX_WNO_DELETE_NON_VIRTUAL_DTOR - Success
  -- Performing Test HAVE_C_WNO_DELETE_NON_VIRTUAL_DTOR
  -- Performing Test HAVE_C_WNO_DELETE_NON_VIRTUAL_DTOR - Failed
  -- Performing Test HAVE_CXX_WNO_UNNAMED_TYPE_TEMPLATE_ARGS
  -- Performing Test HAVE_CXX_WNO_UNNAMED_TYPE_TEMPLATE_ARGS - Failed
  -- Performing Test HAVE_C_WNO_UNNAMED_TYPE_TEMPLATE_ARGS
  -- Performing Test HAVE_C_WNO_UNNAMED_TYPE_TEMPLATE_ARGS - Failed
  -- Performing Test HAVE_CXX_WNO_COMMENT
  -- Performing Test HAVE_CXX_WNO_COMMENT - Success
  -- Performing Test HAVE_C_WNO_COMMENT
  -- Performing Test HAVE_C_WNO_COMMENT - Success
  -- Performing Test HAVE_CXX_WIMPLICIT_FALLTHROUGH_3
  -- Performing Test HAVE_CXX_WIMPLICIT_FALLTHROUGH_3 - Success
  -- Performing Test HAVE_C_WIMPLICIT_FALLTHROUGH_3
  -- Performing Test HAVE_C_WIMPLICIT_FALLTHROUGH_3 - Success
  -- Performing Test HAVE_CXX_WNO_STRICT_OVERFLOW
  -- Performing Test HAVE_CXX_WNO_STRICT_OVERFLOW - Success
  -- Performing Test HAVE_C_WNO_STRICT_OVERFLOW
  -- Performing Test HAVE_C_WNO_STRICT_OVERFLOW - Success
  -- Performing Test HAVE_CXX_FDIAGNOSTICS_SHOW_OPTION
  -- Performing Test HAVE_CXX_FDIAGNOSTICS_SHOW_OPTION - Success
  -- Performing Test HAVE_C_FDIAGNOSTICS_SHOW_OPTION
  -- Performing Test HAVE_C_FDIAGNOSTICS_SHOW_OPTION - Success
  -- Performing Test HAVE_CXX_PTHREAD
  -- Performing Test HAVE_CXX_PTHREAD - Success
  -- Performing Test HAVE_C_PTHREAD
  -- Performing Test HAVE_C_PTHREAD - Success
  -- Performing Test HAVE_CXX_FOMIT_FRAME_POINTER
  -- Performing Test HAVE_CXX_FOMIT_FRAME_POINTER - Success
  -- Performing Test HAVE_C_FOMIT_FRAME_POINTER
  -- Performing Test HAVE_C_FOMIT_FRAME_POINTER - Success
  -- Performing Test HAVE_CXX_FFUNCTION_SECTIONS
  -- Performing Test HAVE_CXX_FFUNCTION_SECTIONS - Success
  -- Performing Test HAVE_C_FFUNCTION_SECTIONS
  -- Performing Test HAVE_C_FFUNCTION_SECTIONS - Success
  -- Performing Test HAVE_CXX_FDATA_SECTIONS
  -- Performing Test HAVE_CXX_FDATA_SECTIONS - Success
  -- Performing Test HAVE_C_FDATA_SECTIONS
  -- Performing Test HAVE_C_FDATA_SECTIONS - Success
  -- Performing Test HAVE_CPU_NEON_SUPPORT (check file: cmake/checks/cpu_neon.cpp)
  -- Performing Test HAVE_CPU_NEON_SUPPORT - Success
  -- Performing Test HAVE_CPU_FP16_SUPPORT (check file: cmake/checks/cpu_fp16.cpp)
  -- Performing Test HAVE_CPU_FP16_SUPPORT - Success
  -- Performing Test HAVE_CPU_BASELINE_FLAGS
  -- Performing Test HAVE_CPU_BASELINE_FLAGS - Success
  -- Performing Test HAVE_CXX_FVISIBILITY_HIDDEN
  -- Performing Test HAVE_CXX_FVISIBILITY_HIDDEN - Success
  -- Performing Test HAVE_C_FVISIBILITY_HIDDEN
  -- Performing Test HAVE_C_FVISIBILITY_HIDDEN - Success
  -- Performing Test HAVE_CXX_FVISIBILITY_INLINES_HIDDEN
  -- Performing Test HAVE_CXX_FVISIBILITY_INLINES_HIDDEN - Success
  -- Performing Test HAVE_C_FVISIBILITY_INLINES_HIDDEN
  -- Performing Test HAVE_C_FVISIBILITY_INLINES_HIDDEN - Failed
  -- Performing Test HAVE_LINK_AS_NEEDED
  -- Performing Test HAVE_LINK_AS_NEEDED - Success
  -- Looking for pthread.h
  -- Looking for pthread.h - found
  -- Looking for posix_memalign
  -- Looking for posix_memalign - found
  -- Looking for malloc.h
  -- Looking for malloc.h - found
  -- Looking for memalign
  -- Looking for memalign - found
  -- Found ZLIB: /usr/lib/aarch64-linux-gnu/libz.so (found suitable version "1.2.11", minimum required is "1.2.3")
  -- Could NOT find JPEG (missing: JPEG_LIBRARY JPEG_INCLUDE_DIR)
  -- Performing Test HAVE_C_WNO_UNUSED_PARAMETER
  -- Performing Test HAVE_C_WNO_UNUSED_PARAMETER - Success
  -- Performing Test HAVE_C_WNO_SIGN_COMPARE
  -- Performing Test HAVE_C_WNO_SIGN_COMPARE - Success
  -- Performing Test HAVE_C_WNO_SHORTEN_64_TO_32
  -- Performing Test HAVE_C_WNO_SHORTEN_64_TO_32 - Failed
  -- Performing Test HAVE_C_WNO_IMPLICIT_FALLTHROUGH
  -- Performing Test HAVE_C_WNO_IMPLICIT_FALLTHROUGH - Success
  -- libjpeg-turbo: VERSION = 2.0.4, BUILD = opencv-4.3.0-libjpeg-turbo
  -- Looking for sys/types.h
  -- Looking for sys/types.h - found
  -- Looking for stdint.h
  -- Looking for stdint.h - found
  -- Looking for stddef.h
  -- Looking for stddef.h - found
  -- Check size of size_t
  -- Check size of size_t - done
  -- Check size of unsigned long
  -- Check size of unsigned long - done
  -- Performing Test HAVE_BUILTIN_CTZL
  -- Performing Test HAVE_BUILTIN_CTZL - Success
  -- Looking for include file locale.h
  -- Looking for include file locale.h - found
  -- Looking for include file stdlib.h
  -- Looking for include file stdlib.h - found
  -- Looking for include file sys/types.h
  -- Looking for include file sys/types.h - found
  -- Could NOT find TIFF (missing: TIFF_LIBRARY TIFF_INCLUDE_DIR)
  -- Looking for assert.h
  -- Looking for assert.h - found
  -- Looking for dlfcn.h
  -- Looking for dlfcn.h - found
  -- Looking for fcntl.h
  -- Looking for fcntl.h - found
  -- Looking for inttypes.h
  -- Looking for inttypes.h - found
  -- Looking for io.h
  -- Looking for io.h - not found
  -- Looking for limits.h
  -- Looking for limits.h - found
  -- Looking for memory.h
  -- Looking for memory.h - found
  -- Looking for search.h
  -- Looking for search.h - found
  -- Looking for string.h
  -- Looking for string.h - found
  -- Looking for strings.h
  -- Looking for strings.h - found
  -- Looking for sys/time.h
  -- Looking for sys/time.h - found
  -- Looking for unistd.h
  -- Looking for unistd.h - found
  -- Performing Test C_HAS_inline
  -- Performing Test C_HAS_inline - Success
  -- Check size of signed short
  -- Check size of signed short - done
  -- Check size of unsigned short
  -- Check size of unsigned short - done
  -- Check size of signed int
  -- Check size of signed int - done
  -- Check size of unsigned int
  -- Check size of unsigned int - done
  -- Check size of signed long
  -- Check size of signed long - done
  -- Check size of signed long long
  -- Check size of signed long long - done
  -- Check size of unsigned long long
  -- Check size of unsigned long long - done
  -- Check size of unsigned char *
  -- Check size of unsigned char * - done
  -- Check size of ptrdiff_t
  -- Check size of ptrdiff_t - done
  -- Check size of INT8
  -- Check size of INT8 - failed
  -- Check size of INT16
  -- Check size of INT16 - failed
  -- Check size of INT32
  -- Check size of INT32 - failed
  -- Looking for floor
  -- Looking for floor - found
  -- Looking for pow
  -- Looking for pow - found
  -- Looking for sqrt
  -- Looking for sqrt - found
  -- Looking for isascii
  -- Looking for isascii - found
  -- Looking for memset
  -- Looking for memset - found
  -- Looking for mmap
  -- Looking for mmap - found
  -- Looking for getopt
  -- Looking for getopt - found
  -- Looking for memmove
  -- Looking for memmove - found
  -- Looking for setmode
  -- Looking for setmode - not found
  -- Looking for strcasecmp
  -- Looking for strcasecmp - found
  -- Looking for strchr
  -- Looking for strchr - found
  -- Looking for strrchr
  -- Looking for strrchr - found
  -- Looking for strstr
  -- Looking for strstr - found
  -- Looking for strtol
  -- Looking for strtol - found
  -- Looking for strtol
  -- Looking for strtol - found
  -- Looking for strtoull
  -- Looking for strtoull - found
  -- Looking for lfind
  -- Looking for lfind - found
  -- Performing Test HAVE_SNPRINTF
  -- Performing Test HAVE_SNPRINTF - Success
  -- Performing Test HAVE_C_WNO_UNUSED_BUT_SET_VARIABLE
  -- Performing Test HAVE_C_WNO_UNUSED_BUT_SET_VARIABLE - Success
  -- Performing Test HAVE_C_WNO_MISSING_PROTOTYPES
  -- Performing Test HAVE_C_WNO_MISSING_PROTOTYPES - Success
  -- Performing Test HAVE_C_WNO_MISSING_DECLARATIONS
  -- Performing Test HAVE_C_WNO_MISSING_DECLARATIONS - Success
  -- Performing Test HAVE_C_WNO_UNDEF
  -- Performing Test HAVE_C_WNO_UNDEF - Success
  -- Performing Test HAVE_C_WNO_UNUSED
  -- Performing Test HAVE_C_WNO_UNUSED - Success
  -- Performing Test HAVE_C_WNO_CAST_ALIGN
  -- Performing Test HAVE_C_WNO_CAST_ALIGN - Success
  -- Performing Test HAVE_C_WNO_SHADOW
  -- Performing Test HAVE_C_WNO_SHADOW - Success
  -- Performing Test HAVE_C_WNO_MAYBE_UNINITIALIZED
  -- Performing Test HAVE_C_WNO_MAYBE_UNINITIALIZED - Success
  -- Performing Test HAVE_C_WNO_POINTER_TO_INT_CAST
  -- Performing Test HAVE_C_WNO_POINTER_TO_INT_CAST - Success
  -- Performing Test HAVE_C_WNO_INT_TO_POINTER_CAST
  -- Performing Test HAVE_C_WNO_INT_TO_POINTER_CAST - Success
  -- Performing Test HAVE_C_WNO_MISLEADING_INDENTATION
  -- Performing Test HAVE_C_WNO_MISLEADING_INDENTATION - Success
  -- Performing Test HAVE_CXX_WNO_MISSING_DECLARATIONS
  -- Performing Test HAVE_CXX_WNO_MISSING_DECLARATIONS - Success
  -- Performing Test HAVE_CXX_WNO_UNUSED_PARAMETER
  -- Performing Test HAVE_CXX_WNO_UNUSED_PARAMETER - Success
  -- Performing Test HAVE_CXX_WNO_MISSING_PROTOTYPES
  -- Performing Test HAVE_CXX_WNO_MISSING_PROTOTYPES - Failed
  -- Performing Test HAVE_CXX_WNO_UNDEF
  -- Performing Test HAVE_CXX_WNO_UNDEF - Success
  -- Performing Test HAVE_C_STD_C99
  -- Performing Test HAVE_C_STD_C99 - Success
  -- Performing Test HAVE_C_WNO_UNUSED_VARIABLE
  -- Performing Test HAVE_C_WNO_UNUSED_VARIABLE - Success
  -- Performing Test HAVE_C_WNO_UNUSED_FUNCTION
  -- Performing Test HAVE_C_WNO_UNUSED_FUNCTION - Success
  -- Could NOT find OpenJPEG (minimal suitable version: 2.0, recommended version >= 2.3.1)
  -- Found JPEG: libjpeg-turbo
  -- Could NOT find Jasper (missing: JASPER_LIBRARIES JASPER_INCLUDE_DIR)
  -- Performing Test HAVE_C_WNO_IMPLICIT_FUNCTION_DECLARATION
  -- Performing Test HAVE_C_WNO_IMPLICIT_FUNCTION_DECLARATION - Success
  -- Performing Test HAVE_C_WNO_UNINITIALIZED
  -- Performing Test HAVE_C_WNO_UNINITIALIZED - Success
  -- Performing Test HAVE_C_WNO_UNUSED_BUT_SET_PARAMETER
  -- Performing Test HAVE_C_WNO_UNUSED_BUT_SET_PARAMETER - Success
  -- Performing Test HAVE_C_WNO_POINTER_COMPARE
  -- Performing Test HAVE_C_WNO_POINTER_COMPARE - Success
  -- Performing Test HAVE_C_WNO_ABSOLUTE_VALUE
  -- Performing Test HAVE_C_WNO_ABSOLUTE_VALUE - Success
  -- Performing Test HAVE_C_WNO_STRICT_PROTOTYPES
  -- Performing Test HAVE_C_WNO_STRICT_PROTOTYPES - Success
  -- Found ZLIB: /usr/lib/aarch64-linux-gnu/libz.so (found version "1.2.11")
  -- Could NOT find PNG (missing: PNG_LIBRARY PNG_PNG_INCLUDE_DIR)
  -- The ASM compiler identification is GNU
  -- Found assembler: /usr/bin/cc
  -- Looking for semaphore.h
  -- Looking for semaphore.h - found
  -- Performing Test HAVE_CXX_WNO_SHADOW
  -- Performing Test HAVE_CXX_WNO_SHADOW - Success
  -- Performing Test HAVE_CXX_WNO_UNUSED
  -- Performing Test HAVE_CXX_WNO_UNUSED - Success
  -- Performing Test HAVE_CXX_WNO_SIGN_COMPARE
  -- Performing Test HAVE_CXX_WNO_SIGN_COMPARE - Success
  -- Performing Test HAVE_CXX_WNO_UNINITIALIZED
  -- Performing Test HAVE_CXX_WNO_UNINITIALIZED - Success
  -- Performing Test HAVE_CXX_WNO_SWITCH
  -- Performing Test HAVE_CXX_WNO_SWITCH - Success
  -- Performing Test HAVE_CXX_WNO_PARENTHESES
  -- Performing Test HAVE_CXX_WNO_PARENTHESES - Success
  -- Performing Test HAVE_CXX_WNO_ARRAY_BOUNDS
  -- Performing Test HAVE_CXX_WNO_ARRAY_BOUNDS - Success
  -- Performing Test HAVE_CXX_WNO_EXTRA
  -- Performing Test HAVE_CXX_WNO_EXTRA - Success
  -- Performing Test HAVE_CXX_WNO_DEPRECATED_DECLARATIONS
  -- Performing Test HAVE_CXX_WNO_DEPRECATED_DECLARATIONS - Success
  -- Performing Test HAVE_CXX_WNO_MISLEADING_INDENTATION
  -- Performing Test HAVE_CXX_WNO_MISLEADING_INDENTATION - Success
  -- Performing Test HAVE_CXX_WNO_DEPRECATED
  -- Performing Test HAVE_CXX_WNO_DEPRECATED - Success
  -- Performing Test HAVE_CXX_WNO_SUGGEST_OVERRIDE
  -- Performing Test HAVE_CXX_WNO_SUGGEST_OVERRIDE - Success
  -- Performing Test HAVE_CXX_WNO_INCONSISTENT_MISSING_OVERRIDE
  -- Performing Test HAVE_CXX_WNO_INCONSISTENT_MISSING_OVERRIDE - Failed
  -- Performing Test HAVE_CXX_WNO_IMPLICIT_FALLTHROUGH
  -- Performing Test HAVE_CXX_WNO_IMPLICIT_FALLTHROUGH - Success
  -- Performing Test HAVE_CXX_WNO_TAUTOLOGICAL_COMPARE
  -- Performing Test HAVE_CXX_WNO_TAUTOLOGICAL_COMPARE - Success
  -- Performing Test HAVE_CXX_WNO_REORDER
  -- Performing Test HAVE_CXX_WNO_REORDER - Success
  -- Performing Test HAVE_CXX_WNO_UNUSED_RESULT
  -- Performing Test HAVE_CXX_WNO_UNUSED_RESULT - Success
  -- Performing Test HAVE_CXX_WNO_CLASS_MEMACCESS
  -- Performing Test HAVE_CXX_WNO_CLASS_MEMACCESS - Success
  -- Checking for module 'gtk+-3.0'
  --   No package 'gtk+-3.0' found
  -- Checking for module 'gtk+-2.0'
  --   No package 'gtk+-2.0' found
  -- Checking for module 'gthread-2.0'
  --   Found gthread-2.0, version 2.56.4
  -- Could not find OpenBLAS include. Turning OpenBLAS_FOUND off
  -- Could not find OpenBLAS lib. Turning OpenBLAS_FOUND off
  -- Could NOT find Atlas (missing: Atlas_CBLAS_INCLUDE_DIR Atlas_CLAPACK_INCLUDE_DIR Atlas_CBLAS_LIBRARY Atlas_BLAS_LIBRARY Atlas_LAPACK_LIBRARY)
  -- Looking for sgemm_
  -- Looking for sgemm_ - not found
  -- Performing Test CMAKE_HAVE_LIBC_PTHREAD
  -- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
  -- Found Threads: TRUE
  -- Could NOT find BLAS (missing: BLAS_LIBRARIES)
  -- Could NOT find LAPACK (missing: LAPACK_LIBRARIES)
      Reason given by package: LAPACK could not be found because dependency BLAS could not be found.
  
  -- Performing Test HAVE_CXX_WNO_UNUSED_LOCAL_TYPEDEFS
  -- Performing Test HAVE_CXX_WNO_UNUSED_LOCAL_TYPEDEFS - Success
  -- Performing Test HAVE_CXX_WNO_SIGN_PROMO
  -- Performing Test HAVE_CXX_WNO_SIGN_PROMO - Success
  -- Performing Test HAVE_CXX_WNO_TAUTOLOGICAL_UNDEFINED_COMPARE
  -- Performing Test HAVE_CXX_WNO_TAUTOLOGICAL_UNDEFINED_COMPARE - Failed
  -- Performing Test HAVE_CXX_WNO_IGNORED_QUALIFIERS
  -- Performing Test HAVE_CXX_WNO_IGNORED_QUALIFIERS - Success
  -- Performing Test HAVE_CXX_WNO_UNUSED_FUNCTION
  -- Performing Test HAVE_CXX_WNO_UNUSED_FUNCTION - Success
  -- Performing Test HAVE_CXX_WNO_UNUSED_CONST_VARIABLE
  -- Performing Test HAVE_CXX_WNO_UNUSED_CONST_VARIABLE - Success
  -- Performing Test HAVE_CXX_WNO_SHORTEN_64_TO_32
  -- Performing Test HAVE_CXX_WNO_SHORTEN_64_TO_32 - Failed
  -- Performing Test HAVE_CXX_WNO_INVALID_OFFSETOF
  -- Performing Test HAVE_CXX_WNO_INVALID_OFFSETOF - Success
  -- Performing Test HAVE_CXX_WNO_ENUM_COMPARE_SWITCH
  -- Performing Test HAVE_CXX_WNO_ENUM_COMPARE_SWITCH - Failed
  -- Could NOT find JNI (missing: JAVA_INCLUDE_PATH JAVA_INCLUDE_PATH2 AWT JVM)
  -- VTK is not found. Please set -DVTK_DIR in CMake to VTK build directory, or to VTK install subdirectory with VTKConfig.cmake file
  CMake Deprecation Warning at 3rdparty/carotene/hal/CMakeLists.txt:1 (cmake_minimum_required):
    Compatibility with CMake < 3.5 will be removed from a future version of
    CMake.
  
    Update the VERSION argument <min> value or use a ...<max> suffix to tell
    CMake that the project does not need compatibility with older versions.
  
  
  CMake Deprecation Warning at 3rdparty/carotene/CMakeLists.txt:1 (cmake_minimum_required):
    Compatibility with CMake < 3.5 will be removed from a future version of
    CMake.
  
    Update the VERSION argument <min> value or use a ...<max> suffix to tell
    CMake that the project does not need compatibility with older versions.
  
  
  -- Looking for dlerror in dl
  -- Looking for dlerror in dl - found
  -- ADE: Download: v0.1.1f.zip
  -- Checking for modules 'libavcodec;libavformat;libavutil;libswscale'
  --   No package 'libavcodec' found
  --   No package 'libavformat' found
  --   No package 'libavutil' found
  --   No package 'libswscale' found
  -- Checking for module 'gstreamer-base-1.0'
  --   No package 'gstreamer-base-1.0' found
  -- Checking for module 'gstreamer-app-1.0'
  --   No package 'gstreamer-app-1.0' found
  -- Checking for module 'gstreamer-riff-1.0'
  --   No package 'gstreamer-riff-1.0' found
  -- Checking for module 'gstreamer-pbutils-1.0'
  --   No package 'gstreamer-pbutils-1.0' found
  -- Checking for module 'libdc1394-2'
  --   No package 'libdc1394-2' found
  -- Allocator metrics storage type: 'int'
  -- Excluding from source files list: modules/imgproc/src/corner.avx.cpp
  -- Excluding from source files list: modules/imgproc/src/imgwarp.avx2.cpp
  -- Excluding from source files list: modules/imgproc/src/imgwarp.sse4_1.cpp
  -- Excluding from source files list: modules/imgproc/src/resize.avx2.cpp
  -- Excluding from source files list: modules/imgproc/src/resize.sse4_1.cpp
  -- Registering hook 'INIT_MODULE_SOURCES_opencv_dnn': /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/dnn/cmake/hooks/INIT_MODULE_SOURCES_opencv_dnn.cmake
  -- opencv_dnn: filter out cuda4dnn source code
  -- Excluding from source files list: <BUILD>/modules/dnn/layers/layers_common.avx.cpp
  -- Excluding from source files list: <BUILD>/modules/dnn/layers/layers_common.avx2.cpp
  -- Excluding from source files list: <BUILD>/modules/dnn/layers/layers_common.avx512_skx.cpp
  -- Excluding from source files list: modules/features2d/src/fast.avx2.cpp
  -- Performing Test HAVE_CXX_WNO_OVERLOADED_VIRTUAL
  -- Performing Test HAVE_CXX_WNO_OVERLOADED_VIRTUAL - Success
  -- Performing Test HAVE_CXX_WNO_UNUSED_PRIVATE_FIELD
  -- Performing Test HAVE_CXX_WNO_UNUSED_PRIVATE_FIELD - Failed
  --
  -- General configuration for OpenCV 4.3.0 =====================================
  --   Version control:               unknown
  --
  --   Platform:
  --     Timestamp:                   2026-05-12T03:14:45Z
  --     Host:                        Linux 4.9.140-tegra aarch64
  --     CMake:                       3.28.4
  --     CMake generator:             Unix Makefiles
  --     CMake build tool:            /usr/bin/make
  --     Configuration:               Release
  --
  --   CPU/HW features:
  --     Baseline:                    NEON FP16
  --       required:                  NEON
  --       disabled:                  VFPV3
  --
  --   C/C++:
  --     Built as dynamic libs?:      NO
  --     C++ standard:                11
  --     C++ Compiler:                /usr/bin/c++  (ver 11.4.0)
  --     C++ flags (Release):         -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wsuggest-override -Wno-delete-non-virtual-dtor -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections    -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG
  --     C++ flags (Debug):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wsuggest-override -Wno-delete-non-virtual-dtor -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections    -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG
  --     C Compiler:                  /usr/bin/cc
  --     C flags (Release):           -fsigned-char -W -Wall -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Winit-self -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections    -fvisibility=hidden -O3 -DNDEBUG  -DNDEBUG
  --     C flags (Debug):             -fsigned-char -W -Wall -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Winit-self -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections    -fvisibility=hidden -g  -O0 -DDEBUG -D_DEBUG
  --     Linker flags (Release):      -Wl,--gc-sections -Wl,--as-needed
  --     Linker flags (Debug):        -Wl,--gc-sections -Wl,--as-needed
  --     ccache:                      NO
  --     Precompiled headers:         NO
  --     Extra dependencies:          ade /usr/lib/aarch64-linux-gnu/libgthread-2.0.so /usr/lib/aarch64-linux-gnu/libglib-2.0.so /usr/lib/aarch64-linux-gnu/libz.so dl m pthread rt
  --     3rdparty dependencies:       ittnotify libprotobuf libjpeg-turbo libwebp libpng libtiff libjasper IlmImf quirc tegra_hal
  --
  --   OpenCV modules:
  --     To be built:                 calib3d core dnn features2d flann gapi highgui imgcodecs imgproc ml objdetect photo python3 stitching video videoio
  --     Disabled:                    world
  --     Disabled by dependency:      -
  --     Unavailable:                 java js python2 ts
  --     Applications:                -
  --     Documentation:               NO
  --     Non-free algorithms:         NO
  --
  --   GUI:
  --     GTK+:                        NO
  --     VTK support:                 NO
  --
  --   Media I/O:
  --     ZLib:                        /usr/lib/aarch64-linux-gnu/libz.so (ver 1.2.11)
  --     JPEG:                        libjpeg-turbo (ver 2.0.4-62)
  --     WEBP:                        build (ver encoder: 0x020f)
  --     PNG:                         build (ver 1.6.37)
  --     TIFF:                        build (ver 42 - 4.0.10)
  --     JPEG 2000:                   build Jasper (ver 1.900.1)
  --     OpenEXR:                     build (ver 2.3.0)
  --     HDR:                         YES
  --     SUNRASTER:                   YES
  --     PXM:                         YES
  --     PFM:                         YES
  --
  --   Video I/O:
  --     DC1394:                      NO
  --     FFMPEG:                      NO
  --       avcodec:                   NO
  --       avformat:                  NO
  --       avutil:                    NO
  --       swscale:                   NO
  --       avresample:                NO
  --     GStreamer:                   NO
  --     v4l/v4l2:                    YES (linux/videodev2.h)
  --
  --   Parallel framework:            pthreads
  --
  --   Trace:                         YES (with Intel ITT)
  --
  --   Other third-party libraries:
  --     Lapack:                      NO
  --     Eigen:                       NO
  --     Custom HAL:                  YES (carotene (ver 0.0.1))
  --     Protobuf:                    build (3.5.1)
  --
  --   OpenCL:                        YES (no extra features)
  --     Include path:                /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/include/opencl/1.2
  --     Link libraries:              Dynamic load
  --
  --   Python 3:
  --     Interpreter:                 /usr/bin/python3 (ver 3.6.9)
  --     Libraries:                   /usr/lib/aarch64-linux-gnu/libpython3.6m.so (ver 3.6.9)
  --     numpy:                       /tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/numpy/core/include (ver 1.13.3)
  --     install path:                python
  --
  --   Python (for build):            /usr/bin/python2.7
  --
  --   Java:
  --     ant:                         NO
  --     JNI:                         NO
  --     Java wrappers:               NO
  --     Java tests:                  NO
  --
  --   Install to:                    /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install
  -- -----------------------------------------------------------------
  --
  -- Configuring done (78.9s)
  -- Generating done (1.7s)
  -- Build files have been written to: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-build
  [  0%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcapimin.c.o
  [  0%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcapistd.c.o
  [  1%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jccoefct.c.o
  [  1%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jccolor.c.o
  [  1%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcdctmgr.c.o
  [  1%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jchuff.c.o
  [  1%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcicc.c.o
  [  1%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcinit.c.o
  [  1%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcmainct.c.o
  [  1%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcmarker.c.o
  [  1%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcmaster.c.o
  [  1%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcomapi.c.o
  [  2%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcparam.c.o
  [  2%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcphuff.c.o
  [  2%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcprepct.c.o
  [  2%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcsample.c.o
  [  2%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jctrans.c.o
  [  2%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdapimin.c.o
  [  2%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdapistd.c.o
  [  2%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdatadst.c.o
  [  2%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdatasrc.c.o
  [  2%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdcoefct.c.o
  [  3%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdcolor.c.o
  [  3%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jddctmgr.c.o
  [  3%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdhuff.c.o
  [  3%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdicc.c.o
  [  3%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdinput.c.o
  [  3%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdmainct.c.o
  [  3%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdmarker.c.o
  [  3%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdmaster.c.o
  [  3%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdmerge.c.o
  [  3%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdphuff.c.o
  [  4%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdpostct.c.o
  [  4%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdsample.c.o
  [  4%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdtrans.c.o
  [  4%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jerror.c.o
  [  4%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jfdctflt.c.o
  [  4%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jfdctfst.c.o
  [  4%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jfdctint.c.o
  [  4%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jidctflt.c.o
  [  4%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jidctfst.c.o
  [  4%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jidctint.c.o
  [  5%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jidctred.c.o
  [  5%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jquant1.c.o
  [  5%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jquant2.c.o
  [  5%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jutils.c.o
  [  5%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jmemmgr.c.o
  [  5%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jmemnobs.c.o
  [  5%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jaricom.c.o
  [  5%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jcarith.c.o
  [  5%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jdarith.c.o
  [  5%] Building C object 3rdparty/libjpeg-turbo/CMakeFiles/libjpeg-turbo.dir/src/jsimd_none.c.o
  [  6%] Linking C static library ../lib/liblibjpeg-turbo.a
  [  6%] Built target libjpeg-turbo
  [  6%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_aux.c.o
  [  6%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_close.c.o
  [  6%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_codec.c.o
  [  6%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_color.c.o
  [  6%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_compress.c.o
  [  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_dir.c.o
  [  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_dirinfo.c.o
  [  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_dirread.c.o
  [  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_dirwrite.c.o
  [  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_dumpmode.c.o
  [  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_error.c.o
  [  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_extension.c.o
  [  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_fax3.c.o
  [  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_fax3sm.c.o
  [  7%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_flush.c.o
  [  8%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_getimage.c.o
  [  8%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_jbig.c.o
  [  8%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_jpeg_12.c.o
  [  8%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_jpeg.c.o
  [  8%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_luv.c.o
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:822:18: warning: argument 1 of type ‘float[3]’ with mismatched bound [-Warray-parameter=]
    822 | XYZtoRGB24(float xyz[3], uint8 rgb[3])
        |            ~~~~~~^~~~~~
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffiop.h:64,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:25:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffio.h:497:24: note: previously declared as ‘float *’
    497 | extern void XYZtoRGB24(float*, uint8*);
        |                        ^~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:822:32: warning: argument 2 of type ‘uint8[3]’ {aka ‘unsigned char[3]’} with mismatched bound [-Warray-parameter=]
    822 | XYZtoRGB24(float xyz[3], uint8 rgb[3])
        |                          ~~~~~~^~~~~~
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffiop.h:64,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:25:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffio.h:497:32: note: previously declared as ‘uint8 *’ {aka ‘unsigned char *’}
    497 | extern void XYZtoRGB24(float*, uint8*);
        |                                ^~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:976:31: warning: argument 2 of type ‘float[3]’ with mismatched bound [-Warray-parameter=]
    976 | LogLuv24toXYZ(uint32 p, float XYZ[3])
        |                         ~~~~~~^~~~~~
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffiop.h:64,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:25:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffio.h:499:35: note: previously declared as ‘float *’
    499 | extern void LogLuv24toXYZ(uint32, float*);
        |                                   ^~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:1004:23: warning: argument 1 of type ‘float[3]’ with mismatched bound [-Warray-parameter=]
   1004 | LogLuv24fromXYZ(float XYZ[3], int em)
        |                 ~~~~~~^~~~~~
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffiop.h:64,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:25:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffio.h:511:31: note: previously declared as ‘float *’
    511 | extern uint32 LogLuv24fromXYZ(float*, int);
        |                               ^~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:1117:31: warning: argument 2 of type ‘float[3]’ with mismatched bound [-Warray-parameter=]
   1117 | LogLuv32toXYZ(uint32 p, float XYZ[3])
        |                         ~~~~~~^~~~~~
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffiop.h:64,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:25:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffio.h:500:35: note: previously declared as ‘float *’
    500 | extern void LogLuv32toXYZ(uint32, float*);
        |                                   ^~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:1142:23: warning: argument 1 of type ‘float[3]’ with mismatched bound [-Warray-parameter=]
   1142 | LogLuv32fromXYZ(float XYZ[3], int em)
        |                 ~~~~~~^~~~~~
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffiop.h:64,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tif_luv.c:25:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libtiff/tiffio.h:512:31: note: previously declared as ‘float *’
    512 | extern uint32 LogLuv32fromXYZ(float*, int);
        |                               ^~~~~~
  [  8%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_lzma.c.o
  [  8%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_lzw.c.o
  [  8%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_next.c.o
  [  8%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_ojpeg.c.o
  [  8%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_open.c.o
  [  9%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_packbits.c.o
  [  9%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_pixarlog.c.o
  [  9%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_predict.c.o
  [  9%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_print.c.o
  [  9%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_read.c.o
  [  9%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_strip.c.o
  [  9%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_swab.c.o
  [  9%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_thunder.c.o
  [  9%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_tile.c.o
  [  9%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_version.c.o
  [ 10%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_warning.c.o
  [ 10%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_webp.c.o
  [ 10%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_write.c.o
  [ 10%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_zip.c.o
  [ 10%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_zstd.c.o
  [ 10%] Building CXX object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_stream.cxx.o
  [ 10%] Building C object 3rdparty/libtiff/CMakeFiles/libtiff.dir/tif_unix.c.o
  [ 10%] Linking CXX static library ../lib/liblibtiff.a
  [ 10%] Built target libtiff
  [ 10%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dec/alpha_dec.c.o
  [ 10%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dec/buffer_dec.c.o
  [ 11%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dec/frame_dec.c.o
  [ 11%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dec/idec_dec.c.o
  [ 11%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dec/io_dec.c.o
  [ 11%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dec/quant_dec.c.o
  [ 11%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dec/tree_dec.c.o
  [ 11%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dec/vp8_dec.c.o
  [ 11%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dec/vp8l_dec.c.o
  [ 11%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dec/webp_dec.c.o
  [ 11%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/demux/anim_decode.c.o
  [ 11%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/demux/demux.c.o
  [ 12%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/alpha_processing.c.o
  [ 12%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/alpha_processing_mips_dsp_r2.c.o
  [ 12%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/alpha_processing_neon.c.o
  [ 12%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/alpha_processing_sse2.c.o
  [ 12%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/alpha_processing_sse41.c.o
  [ 12%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/cost.c.o
  [ 12%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/cost_mips32.c.o
  [ 12%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/cost_mips_dsp_r2.c.o
  [ 12%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/cost_neon.c.o
  [ 12%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/cost_sse2.c.o
  [ 13%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/cpu.c.o
  [ 13%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/dec.c.o
  [ 13%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/dec_clip_tables.c.o
  [ 13%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/dec_mips32.c.o
  [ 13%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/dec_mips_dsp_r2.c.o
  [ 13%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/dec_msa.c.o
  [ 13%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/dec_neon.c.o
  [ 13%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/dec_sse2.c.o
  [ 13%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/dec_sse41.c.o
  [ 13%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/enc.c.o
  [ 14%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/enc_mips32.c.o
  [ 14%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/enc_mips_dsp_r2.c.o
  [ 14%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/enc_msa.c.o
  [ 14%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/enc_neon.c.o
  [ 14%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/enc_sse2.c.o
  [ 14%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/enc_sse41.c.o
  [ 14%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/filters.c.o
  [ 14%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/filters_mips_dsp_r2.c.o
  [ 14%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/filters_msa.c.o
  [ 14%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/filters_neon.c.o
  [ 15%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/filters_sse2.c.o
  [ 15%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless.c.o
  [ 15%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_enc.c.o
  [ 15%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_enc_mips32.c.o
  [ 15%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_enc_mips_dsp_r2.c.o
  [ 15%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_enc_msa.c.o
  [ 15%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_enc_neon.c.o
  [ 15%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_enc_sse2.c.o
  [ 15%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_enc_sse41.c.o
  [ 15%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_mips_dsp_r2.c.o
  [ 16%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_msa.c.o
  [ 16%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_neon.c.o
  [ 16%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/lossless_sse2.c.o
  [ 16%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/rescaler.c.o
  [ 16%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/rescaler_mips32.c.o
  [ 16%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/rescaler_mips_dsp_r2.c.o
  [ 16%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/rescaler_msa.c.o
  [ 16%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/rescaler_neon.c.o
  [ 16%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/rescaler_sse2.c.o
  [ 16%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/ssim.c.o
  [ 17%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/ssim_sse2.c.o
  [ 17%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/upsampling.c.o
  [ 17%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/upsampling_mips_dsp_r2.c.o
  [ 17%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/upsampling_msa.c.o
  [ 17%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/upsampling_neon.c.o
  [ 17%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/upsampling_sse2.c.o
  [ 17%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/upsampling_sse41.c.o
  [ 17%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/yuv.c.o
  [ 17%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/yuv_mips32.c.o
  [ 17%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/yuv_mips_dsp_r2.c.o
  [ 18%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/yuv_neon.c.o
  [ 18%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/yuv_sse2.c.o
  [ 18%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/dsp/yuv_sse41.c.o
  [ 18%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/alpha_enc.c.o
  [ 18%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/analysis_enc.c.o
  [ 18%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/backward_references_cost_enc.c.o
  [ 18%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/backward_references_enc.c.o
  [ 18%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/config_enc.c.o
  [ 18%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/cost_enc.c.o
  [ 18%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/filter_enc.c.o
  [ 19%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/frame_enc.c.o
  [ 19%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/histogram_enc.c.o
  [ 19%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/iterator_enc.c.o
  [ 19%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/near_lossless_enc.c.o
  [ 19%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/picture_csp_enc.c.o
  [ 19%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/picture_enc.c.o
  [ 19%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/picture_psnr_enc.c.o
  [ 19%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/picture_rescale_enc.c.o
  [ 19%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/picture_tools_enc.c.o
  [ 19%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/predictor_enc.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/quant_enc.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/syntax_enc.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/token_enc.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/tree_enc.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/vp8l_enc.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/enc/webp_enc.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/mux/anim_encode.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/mux/muxedit.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/mux/muxinternal.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/mux/muxread.c.o
  [ 20%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/bit_reader_utils.c.o
  [ 21%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/bit_writer_utils.c.o
  [ 21%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/color_cache_utils.c.o
  [ 21%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/filters_utils.c.o
  [ 21%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/huffman_encode_utils.c.o
  [ 21%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/huffman_utils.c.o
  [ 21%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/quant_levels_dec_utils.c.o
  [ 21%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/quant_levels_utils.c.o
  [ 21%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/random_utils.c.o
  [ 21%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/rescaler_utils.c.o
  [ 21%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/thread_utils.c.o
  [ 22%] Building C object 3rdparty/libwebp/CMakeFiles/libwebp.dir/src/utils/utils.c.o
  [ 22%] Linking C static library ../lib/liblibwebp.a
  [ 22%] Built target libwebp
  [ 22%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_cm.c.o
  In function ‘jas_cmprof_createsycc’,
      inlined from ‘jas_cmprof_createfromclrspc’ at /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libjasper/jas_cm.c:153:22,
      inlined from ‘jas_cmprof_createfromclrspc’ at /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libjasper/jas_cm.c:144:15:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libjasper/jas_cm.c:219:5: warning: ‘jas_cmshapmat_invmat’ accessing 96 bytes in a region of size 32 [-Wstringop-overflow=]
    219 |     jas_cmshapmat_invmat(revshapmat->mat, fwdshapmat->mat);
        |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libjasper/jas_cm.c: In function ‘jas_cmprof_createfromclrspc’:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libjasper/jas_cm.c:219:5: note: referencing argument 2 of type ‘jas_cmreal_t (*)[4]’ {aka ‘double (*)[4]’}
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libjasper/jas_cm.c:1001:12: note: in a call to function ‘jas_cmshapmat_invmat’
   1001 | static int jas_cmshapmat_invmat(jas_cmreal_t out[3][4], jas_cmreal_t in[3][4])
        |            ^~~~~~~~~~~~~~~~~~~~
  [ 22%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_debug.c.o
  [ 22%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_getopt.c.o
  [ 22%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_icc.c.o
  [ 22%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_iccdata.c.o
  [ 22%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_image.c.o
  [ 22%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_init.c.o
  [ 22%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_malloc.c.o
  [ 22%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_seq.c.o
  [ 23%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_stream.c.o
  [ 23%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_string.c.o
  [ 23%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_tmr.c.o
  [ 23%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_tvp.c.o
  [ 23%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jas_version.c.o
  [ 23%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jp2_cod.c.o
  [ 23%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jp2_dec.c.o
  [ 23%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jp2_enc.c.o
  [ 23%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_bs.c.o
  [ 23%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_cs.c.o
  [ 24%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_dec.c.o
  [ 24%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_enc.c.o
  [ 24%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_math.c.o
  [ 24%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_mct.c.o
  [ 24%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_mqcod.c.o
  [ 24%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_mqdec.c.o
  [ 24%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_mqenc.c.o
  [ 24%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_qmfb.c.o
  [ 24%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_t1cod.c.o
  [ 24%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_t1dec.c.o
  [ 25%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_t1enc.c.o
  [ 25%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_t2cod.c.o
  [ 25%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_t2dec.c.o
  [ 25%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_t2enc.c.o
  [ 25%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_tagtree.c.o
  [ 25%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_tsfb.c.o
  [ 25%] Building C object 3rdparty/libjasper/CMakeFiles/libjasper.dir/jpc_util.c.o
  [ 25%] Linking C static library ../lib/liblibjasper.a
  [ 25%] Built target libjasper
  [ 25%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/png.c.o
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c: In function ‘png_convert_to_rfc1123_buffer’:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/pngpriv.h:1749:4: warning: ‘number_buf’ may be used uninitialized [-Wmaybe-uninitialized]
   1749 |    png_format_number(buffer, buffer + (sizeof buffer), format, number)
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:757:69: note: in definition of macro ‘APPEND_STRING’
    757 | #     define APPEND_STRING(string) pos = png_safecat(out, 29, pos, (string))
        |                                                                     ^~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:759:24: note: in expansion of macro ‘PNG_FORMAT_NUMBER’
    759 |          APPEND_STRING(PNG_FORMAT_NUMBER(number_buf, format, (value)))
        |                        ^~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:762:7: note: in expansion of macro ‘APPEND_NUMBER’
    762 |       APPEND_NUMBER(PNG_NUMBER_FORMAT_u, (unsigned)ptime->day);
        |       ^~~~~~~~~~~~~
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.h:335,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/pngpriv.h:386,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:14:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/pngpriv.h:1744:33: note: by argument 1 of type ‘png_const_charp’ {aka ‘const char *’} to ‘png_format_number’ declared here
   1744 | PNG_INTERNAL_FUNCTION(png_charp,png_format_number,(png_const_charp start,
        |                                 ^~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/pngconf.h:287:70: note: in definition of macro ‘PNG_FUNCTION’
    287 | #  define PNG_FUNCTION(type, name, args, attributes) attributes type name args
        |                                                                      ^~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/pngpriv.h:1744:1: note: in expansion of macro ‘PNG_INTERNAL_FUNCTION’
   1744 | PNG_INTERNAL_FUNCTION(png_charp,png_format_number,(png_const_charp start,
        | ^~~~~~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:755:12: note: ‘number_buf’ declared here
    755 |       char number_buf[5]; /* enough for a four-digit year */
        |            ^~~~~~~~~~
  In function ‘png_convert_to_rfc1123_buffer’,
      inlined from ‘png_convert_to_rfc1123’ at /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:796:11:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/pngpriv.h:1749:4: warning: ‘number_buf’ may be used uninitialized [-Wmaybe-uninitialized]
   1749 |    png_format_number(buffer, buffer + (sizeof buffer), format, number)
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:757:69: note: in definition of macro ‘APPEND_STRING’
    757 | #     define APPEND_STRING(string) pos = png_safecat(out, 29, pos, (string))
        |                                                                     ^~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:759:24: note: in expansion of macro ‘PNG_FORMAT_NUMBER’
    759 |          APPEND_STRING(PNG_FORMAT_NUMBER(number_buf, format, (value)))
        |                        ^~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:762:7: note: in expansion of macro ‘APPEND_NUMBER’
    762 |       APPEND_NUMBER(PNG_NUMBER_FORMAT_u, (unsigned)ptime->day);
        |       ^~~~~~~~~~~~~
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.h:335,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/pngpriv.h:386,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:14:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c: In function ‘png_convert_to_rfc1123’:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/pngpriv.h:1744:33: note: by argument 1 of type ‘png_const_charp’ {aka ‘const char *’} to ‘png_format_number’ declared here
   1744 | PNG_INTERNAL_FUNCTION(png_charp,png_format_number,(png_const_charp start,
        |                                 ^~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/pngconf.h:287:70: note: in definition of macro ‘PNG_FUNCTION’
    287 | #  define PNG_FUNCTION(type, name, args, attributes) attributes type name args
        |                                                                      ^~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/pngpriv.h:1744:1: note: in expansion of macro ‘PNG_INTERNAL_FUNCTION’
   1744 | PNG_INTERNAL_FUNCTION(png_charp,png_format_number,(png_const_charp start,
        | ^~~~~~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/3rdparty/libpng/png.c:755:12: note: ‘number_buf’ declared here
    755 |       char number_buf[5]; /* enough for a four-digit year */
        |            ^~~~~~~~~~
  [ 25%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngerror.c.o
  [ 25%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngget.c.o
  [ 25%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngmem.c.o
  [ 25%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngpread.c.o
  [ 25%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngread.c.o
  [ 25%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngrio.c.o
  [ 25%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngrtran.c.o
  [ 25%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngrutil.c.o
  [ 26%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngset.c.o
  [ 26%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngtrans.c.o
  [ 26%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngwio.c.o
  [ 26%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngwrite.c.o
  [ 26%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngwtran.c.o
  [ 26%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/pngwutil.c.o
  [ 26%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/arm/arm_init.c.o
  [ 26%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/arm/filter_neon_intrinsics.c.o
  [ 26%] Building C object 3rdparty/libpng/CMakeFiles/libpng.dir/arm/palette_neon_intrinsics.c.o
  [ 26%] Linking C static library ../lib/liblibpng.a
  [ 26%] Built target libpng
  [ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Half/half.cpp.o
  [ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Iex/IexBaseExc.cpp.o
  [ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Iex/IexThrowErrnoExc.cpp.o
  [ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfAcesFile.cpp.o
  [ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfAttribute.cpp.o
  [ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfB44Compressor.cpp.o
  [ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfBoxAttribute.cpp.o
  [ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfCRgbaFile.cpp.o
  [ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfChannelList.cpp.o
  [ 26%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfChannelListAttribute.cpp.o
  [ 27%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfChromaticities.cpp.o
  [ 27%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfChromaticitiesAttribute.cpp.o
  [ 27%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfCompositeDeepScanLine.cpp.o
  [ 27%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfCompressionAttribute.cpp.o
  [ 27%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfCompressor.cpp.o
  [ 27%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfConvert.cpp.o
  [ 27%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepCompositing.cpp.o
  [ 27%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepFrameBuffer.cpp.o
  [ 27%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepImageStateAttribute.cpp.o
  [ 27%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepScanLineInputFile.cpp.o
  [ 28%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepScanLineInputPart.cpp.o
  [ 28%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepScanLineOutputFile.cpp.o
  [ 28%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepScanLineOutputPart.cpp.o
  [ 28%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepTiledInputFile.cpp.o
  [ 28%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepTiledInputPart.cpp.o
  [ 28%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepTiledOutputFile.cpp.o
  [ 28%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDeepTiledOutputPart.cpp.o
  [ 28%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDoubleAttribute.cpp.o
  [ 28%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfDwaCompressor.cpp.o
  [ 28%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfEnvmap.cpp.o
  [ 29%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfEnvmapAttribute.cpp.o
  [ 29%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfFastHuf.cpp.o
  [ 29%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfFloatAttribute.cpp.o
  [ 29%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfFloatVectorAttribute.cpp.o
  [ 29%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfFrameBuffer.cpp.o
  [ 29%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfFramesPerSecond.cpp.o
  [ 29%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfGenericInputFile.cpp.o
  [ 29%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfGenericOutputFile.cpp.o
  [ 29%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfHeader.cpp.o
  [ 29%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfHuf.cpp.o
  [ 30%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfIO.cpp.o
  [ 30%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfInputFile.cpp.o
  [ 30%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfInputPart.cpp.o
  [ 30%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfInputPartData.cpp.o
  [ 30%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfIntAttribute.cpp.o
  [ 30%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfKeyCode.cpp.o
  [ 30%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfKeyCodeAttribute.cpp.o
  [ 30%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfLineOrderAttribute.cpp.o
  [ 30%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfLut.cpp.o
  [ 30%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfMatrixAttribute.cpp.o
  [ 31%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfMisc.cpp.o
  [ 31%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfMultiPartInputFile.cpp.o
  [ 31%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfMultiPartOutputFile.cpp.o
  [ 31%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfMultiView.cpp.o
  [ 31%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfOpaqueAttribute.cpp.o
  [ 31%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfOutputFile.cpp.o
  [ 31%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfOutputPart.cpp.o
  [ 31%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfOutputPartData.cpp.o
  [ 31%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfPartType.cpp.o
  [ 31%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfPizCompressor.cpp.o
  [ 32%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfPreviewImage.cpp.o
  [ 32%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfPreviewImageAttribute.cpp.o
  [ 32%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfPxr24Compressor.cpp.o
  [ 32%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfRational.cpp.o
  [ 32%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfRationalAttribute.cpp.o
  [ 32%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfRgbaFile.cpp.o
  [ 32%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfRgbaYca.cpp.o
  [ 32%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfRle.cpp.o
  [ 32%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfRleCompressor.cpp.o
  [ 32%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfScanLineInputFile.cpp.o
  [ 33%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfStandardAttributes.cpp.o
  [ 33%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfStdIO.cpp.o
  [ 33%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfStringAttribute.cpp.o
  [ 33%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfStringVectorAttribute.cpp.o
  [ 33%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfSystemSpecific.cpp.o
  [ 33%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTestFile.cpp.o
  [ 33%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfThreading.cpp.o
  [ 33%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTileDescriptionAttribute.cpp.o
  [ 33%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTileOffsets.cpp.o
  [ 33%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTiledInputFile.cpp.o
  [ 34%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTiledInputPart.cpp.o
  [ 34%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTiledMisc.cpp.o
  [ 34%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTiledOutputFile.cpp.o
  [ 34%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTiledOutputPart.cpp.o
  [ 34%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTiledRgbaFile.cpp.o
  [ 34%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTimeCode.cpp.o
  [ 34%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfTimeCodeAttribute.cpp.o
  [ 34%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfVecAttribute.cpp.o
  [ 34%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfVersion.cpp.o
  [ 34%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfWav.cpp.o
  [ 35%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfZip.cpp.o
  [ 35%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/ImfZipCompressor.cpp.o
  [ 35%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmImf/dwaLookups.cpp.o
  [ 35%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThread.cpp.o
  [ 35%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThreadMutex.cpp.o
  [ 35%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThreadMutexPosix.cpp.o
  [ 35%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThreadPool.cpp.o
  [ 35%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThreadPosix.cpp.o
  [ 35%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThreadSemaphore.cpp.o
  [ 35%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThreadSemaphorePosix.cpp.o
  [ 36%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/IlmThread/IlmThreadSemaphorePosixCompat.cpp.o
  [ 36%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Imath/ImathBox.cpp.o
  [ 36%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Imath/ImathColorAlgo.cpp.o
  [ 36%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Imath/ImathFun.cpp.o
  [ 36%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Imath/ImathMatrixAlgo.cpp.o
  [ 36%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Imath/ImathRandom.cpp.o
  [ 36%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Imath/ImathShear.cpp.o
  [ 36%] Building CXX object 3rdparty/openexr/CMakeFiles/IlmImf.dir/Imath/ImathVec.cpp.o
  [ 36%] Linking CXX static library ../lib/libIlmImf.a
  [ 36%] Built target IlmImf
  [ 37%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/arena.cc.o
  [ 37%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/arenastring.cc.o
  [ 37%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/extension_set.cc.o
  [ 37%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/generated_message_table_driven_lite.cc.o
  [ 37%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/generated_message_util.cc.o
  [ 37%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/coded_stream.cc.o
  [ 37%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/zero_copy_stream.cc.o
  [ 37%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/zero_copy_stream_impl_lite.cc.o
  [ 37%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/message_lite.cc.o
  [ 37%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/repeated_field.cc.o
  [ 38%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/atomicops_internals_x86_gcc.cc.o
  [ 38%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/bytestream.cc.o
  [ 38%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/common.cc.o
  [ 38%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/int128.cc.o
  [ 38%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/io_win32.cc.o
  [ 38%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/once.cc.o
  [ 38%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/status.cc.o
  [ 38%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/statusor.cc.o
  [ 38%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/stringpiece.cc.o
  [ 38%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/stringprintf.cc.o
  [ 39%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/structurally_valid.cc.o
  [ 39%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/strutil.cc.o
  [ 39%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/time.cc.o
  [ 39%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/wire_format_lite.cc.o
  [ 39%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/any.cc.o
  [ 39%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/any.pb.cc.o
  [ 39%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/api.pb.cc.o
  [ 39%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/descriptor.cc.o
  [ 39%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/descriptor.pb.cc.o
  [ 39%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/descriptor_database.cc.o
  [ 40%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/duration.pb.cc.o
  [ 40%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/dynamic_message.cc.o
  [ 40%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/empty.pb.cc.o
  [ 40%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/extension_set_heavy.cc.o
  [ 40%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/field_mask.pb.cc.o
  [ 40%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/generated_message_reflection.cc.o
  [ 40%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/generated_message_table_driven.cc.o
  [ 40%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/gzip_stream.cc.o
  [ 40%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/printer.cc.o
  [ 40%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/strtod.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/tokenizer.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/io/zero_copy_stream_impl.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/map_field.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/message.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/reflection_ops.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/service.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/source_context.pb.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/struct.pb.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/mathlimits.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/stubs/substitute.cc.o
  [ 41%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/text_format.cc.o
  [ 42%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/timestamp.pb.cc.o
  [ 42%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/type.pb.cc.o
  [ 42%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/unknown_field_set.cc.o
  [ 42%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/delimited_message_util.cc.o
  [ 42%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/field_comparator.cc.o
  [ 42%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/field_mask_util.cc.o
  [ 42%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/datapiece.cc.o
  [ 42%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/default_value_objectwriter.cc.o
  [ 42%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/field_mask_utility.cc.o
  [ 42%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/json_escaping.cc.o
  [ 43%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/json_objectwriter.cc.o
  [ 43%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/json_stream_parser.cc.o
  [ 43%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/object_writer.cc.o
  [ 43%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/proto_writer.cc.o
  [ 43%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/protostream_objectsource.cc.o
  [ 43%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/protostream_objectwriter.cc.o
  [ 43%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/type_info.cc.o
  [ 43%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/internal/utility.cc.o
  [ 43%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/json_util.cc.o
  [ 43%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/message_differencer.cc.o
  [ 44%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/time_util.cc.o
  [ 44%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/util/type_resolver_util.cc.o
  [ 44%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/wire_format.cc.o
  [ 44%] Building CXX object 3rdparty/protobuf/CMakeFiles/libprotobuf.dir/src/google/protobuf/wrappers.pb.cc.o
  [ 44%] Linking CXX static library ../lib/liblibprotobuf.a
  [ 44%] Built target libprotobuf
  [ 44%] Building C object 3rdparty/quirc/CMakeFiles/quirc.dir/src/decode.c.o
  [ 44%] Building C object 3rdparty/quirc/CMakeFiles/quirc.dir/src/quirc.c.o
  [ 44%] Building C object 3rdparty/quirc/CMakeFiles/quirc.dir/src/version_db.c.o
  [ 44%] Linking C static library ../lib/libquirc.a
  [ 44%] Built target quirc
  [ 44%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/absdiff.cpp.o
  [ 44%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/accumulate.cpp.o
  [ 45%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/add.cpp.o
  [ 45%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/add_weighted.cpp.o
  [ 45%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/bitwise.cpp.o
  [ 45%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/blur.cpp.o
  [ 45%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/canny.cpp.o
  [ 45%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/channel_extract.cpp.o
  [ 45%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/channels_combine.cpp.o
  [ 45%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/cmp.cpp.o
  [ 45%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/colorconvert.cpp.o
  [ 45%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/common.cpp.o
  [ 46%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/convert.cpp.o
  [ 46%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/convert_depth.cpp.o
  [ 46%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/convert_scale.cpp.o
  [ 46%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/convolution.cpp.o
  [ 46%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/count_nonzero.cpp.o
  [ 46%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/div.cpp.o
  [ 46%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/dot_product.cpp.o
  [ 46%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/fast.cpp.o
  [ 46%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/fill_minmaxloc.cpp.o
  [ 46%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/flip.cpp.o
  [ 47%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/gaussian_blur.cpp.o
  [ 47%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/in_range.cpp.o
  [ 47%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/integral.cpp.o
  [ 47%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/laplacian.cpp.o
  [ 47%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/magnitude.cpp.o
  [ 47%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/meanstddev.cpp.o
  [ 47%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/median_filter.cpp.o
  [ 47%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/min_max.cpp.o
  [ 47%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/minmaxloc.cpp.o
  [ 47%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/morph.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/mul.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/norm.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/opticalflow.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/phase.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/pyramid.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/reduce.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/remap.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/resize.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/scharr.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/separable_filter.cpp.o
  [ 48%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/sobel.cpp.o
  [ 49%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/sub.cpp.o
  [ 49%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/sum.cpp.o
  [ 49%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/template_matching.cpp.o
  [ 49%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/threshold.cpp.o
  [ 49%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/warp_affine.cpp.o
  [ 49%] Building CXX object 3rdparty/carotene/hal/carotene/CMakeFiles/carotene_objs.dir/src/warp_perspective.cpp.o
  [ 49%] Built target carotene_objs
  [ 50%] Linking CXX static library ../../lib/libtegra_hal.a
  [ 50%] Built target tegra_hal
  [ 50%] Building C object 3rdparty/ittnotify/CMakeFiles/ittnotify.dir/src/ittnotify/ittnotify_static.c.o
  [ 50%] Building C object 3rdparty/ittnotify/CMakeFiles/ittnotify.dir/src/ittnotify/jitprofiling.c.o
  [ 51%] Linking C static library ../lib/libittnotify.a
  [ 51%] Built target ittnotify
  [ 51%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/alloc.cpp.o
  [ 52%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/assert.cpp.o
  [ 52%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/check_cycles.cpp.o
  [ 52%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/edge.cpp.o
  [ 52%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/execution_engine.cpp.o
  [ 52%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/graph.cpp.o
  [ 52%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/memory_accessor.cpp.o
  [ 52%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/memory_descriptor.cpp.o
  [ 52%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/memory_descriptor_ref.cpp.o
  [ 52%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/memory_descriptor_view.cpp.o
  [ 52%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/metadata.cpp.o
  [ 53%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/metatypes.cpp.o
  [ 53%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/node.cpp.o
  [ 53%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/passes/communications.cpp.o
  [ 53%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/search.cpp.o
  [ 53%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/subgraphs.cpp.o
  [ 53%] Building CXX object modules/CMakeFiles/ade.dir/__/3rdparty/ade/ade-0.1.1f/sources/ade/source/topological_sort.cpp.o
  [ 53%] Linking CXX static library ../lib/libade.a
  [ 53%] Built target ade
  [ 53%] Built target opencv_videoio_plugins
  [ 53%] Processing OpenCL kernels (core)
  [ 53%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/algorithm.cpp.o
  [ 53%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/alloc.cpp.o
  [ 53%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/arithm.cpp.o
  [ 53%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/arithm.dispatch.cpp.o
  [ 53%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/array.cpp.o
  [ 54%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/async.cpp.o
  [ 54%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/batch_distance.cpp.o
  [ 54%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/bindings_utils.cpp.o
  [ 54%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/buffer_area.cpp.o
  [ 54%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/channels.cpp.o
  [ 54%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/check.cpp.o
  [ 54%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/command_line_parser.cpp.o
  [ 54%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/conjugate_gradient.cpp.o
  [ 54%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/convert.dispatch.cpp.o
  [ 54%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/convert_c.cpp.o
  [ 55%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/convert_scale.dispatch.cpp.o
  [ 55%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/copy.cpp.o
  [ 55%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/count_non_zero.dispatch.cpp.o
  [ 55%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/cuda_gpu_mat.cpp.o
  [ 55%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/cuda_host_mem.cpp.o
  [ 55%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/cuda_info.cpp.o
  [ 55%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/cuda_stream.cpp.o
  [ 55%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/datastructs.cpp.o
  [ 55%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/directx.cpp.o
  [ 55%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/downhill_simplex.cpp.o
  [ 56%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/dxt.cpp.o
  [ 56%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/gl_core_3_1.cpp.o
  [ 56%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/glob.cpp.o
  [ 56%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/hal_internal.cpp.o
  [ 56%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/kmeans.cpp.o
  [ 56%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/lapack.cpp.o
  [ 56%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/lda.cpp.o
  [ 56%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/logger.cpp.o
  [ 56%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/lpsolver.cpp.o
  [ 56%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/lut.cpp.o
  [ 57%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/mathfuncs.cpp.o
  [ 57%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/mathfuncs_core.dispatch.cpp.o
  [ 57%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matmul.dispatch.cpp.o
  [ 57%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matrix.cpp.o
  [ 57%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matrix_c.cpp.o
  [ 57%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matrix_decomp.cpp.o
  [ 57%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matrix_expressions.cpp.o
  [ 57%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matrix_iterator.cpp.o
  [ 57%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matrix_operations.cpp.o
  [ 57%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matrix_sparse.cpp.o
  [ 58%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/matrix_wrap.cpp.o
  [ 58%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/mean.dispatch.cpp.o
  [ 58%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/merge.dispatch.cpp.o
  [ 58%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/minmax.cpp.o
  [ 58%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/norm.cpp.o
  [ 58%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/ocl.cpp.o
  [ 58%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/opencl/runtime/opencl_clamdblas.cpp.o
  [ 58%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/opencl/runtime/opencl_clamdfft.cpp.o
  [ 58%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/opencl/runtime/opencl_core.cpp.o
  [ 58%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/opengl.cpp.o
  [ 59%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/out.cpp.o
  [ 59%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/ovx.cpp.o
  [ 59%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/parallel.cpp.o
  [ 59%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/parallel_impl.cpp.o
  [ 59%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/pca.cpp.o
  [ 59%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/persistence.cpp.o
  [ 59%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/persistence_json.cpp.o
  [ 59%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/persistence_types.cpp.o
  [ 59%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/persistence_xml.cpp.o
  [ 59%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/persistence_yml.cpp.o
  [ 60%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/rand.cpp.o
  [ 60%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/softfloat.cpp.o
  [ 60%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/split.dispatch.cpp.o
  [ 60%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/stat.dispatch.cpp.o
  [ 60%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/stat_c.cpp.o
  [ 60%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/stl.cpp.o
  [ 60%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/sum.dispatch.cpp.o
  [ 60%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/system.cpp.o
  [ 60%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/tables.cpp.o
  [ 60%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/trace.cpp.o
  [ 61%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/types.cpp.o
  [ 61%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/umatrix.cpp.o
  [ 61%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/utils/datafile.cpp.o
  [ 61%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/utils/filesystem.cpp.o
  [ 61%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/utils/logtagconfigparser.cpp.o
  [ 61%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/utils/logtagmanager.cpp.o
  [ 61%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/utils/samples.cpp.o
  [ 61%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/src/va_intel.cpp.o
  [ 61%] Building CXX object modules/core/CMakeFiles/opencv_core.dir/opencl_kernels_core.cpp.o
  [ 61%] Linking CXX static library ../../lib/libopencv_core.a
  [ 61%] Built target opencv_core
  [ 61%] Building CXX object modules/flann/CMakeFiles/opencv_flann.dir/src/flann.cpp.o
  [ 61%] Building CXX object modules/flann/CMakeFiles/opencv_flann.dir/src/miniflann.cpp.o
  [ 61%] Linking CXX static library ../../lib/libopencv_flann.a
  [ 61%] Built target opencv_flann
  [ 61%] Processing OpenCL kernels (imgproc)
  [ 61%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/accum.cpp.o
  [ 61%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/accum.dispatch.cpp.o
  [ 61%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/approx.cpp.o
  [ 61%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/bilateral_filter.dispatch.cpp.o
  [ 61%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/blend.cpp.o
  [ 61%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/box_filter.dispatch.cpp.o
  [ 61%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/canny.cpp.o
  [ 62%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/clahe.cpp.o
  [ 62%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/color.cpp.o
  [ 62%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/color_hsv.dispatch.cpp.o
  [ 62%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/color_lab.cpp.o
  [ 62%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/color_rgb.dispatch.cpp.o
  [ 62%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/color_yuv.dispatch.cpp.o
  [ 62%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/colormap.cpp.o
  [ 62%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/connectedcomponents.cpp.o
  [ 62%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/contours.cpp.o
  [ 62%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/convhull.cpp.o
  [ 63%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/corner.cpp.o
  [ 63%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/cornersubpix.cpp.o
  [ 63%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/demosaicing.cpp.o
  [ 63%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/deriv.cpp.o
  [ 63%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/distransform.cpp.o
  [ 63%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/drawing.cpp.o
  [ 63%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/emd.cpp.o
  [ 63%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/featureselect.cpp.o
  [ 63%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/filter.dispatch.cpp.o
  [ 63%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/floodfill.cpp.o
  [ 64%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/gabor.cpp.o
  [ 64%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/generalized_hough.cpp.o
  [ 64%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/geometry.cpp.o
  [ 64%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/grabcut.cpp.o
  [ 64%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/hershey_fonts.cpp.o
  [ 64%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/histogram.cpp.o
  [ 64%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/hough.cpp.o
  [ 64%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/imgwarp.cpp.o
  [ 64%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/intersection.cpp.o
  [ 64%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/linefit.cpp.o
  [ 65%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/lsd.cpp.o
  [ 65%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/main.cpp.o
  [ 65%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/matchcontours.cpp.o
  [ 65%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/median_blur.dispatch.cpp.o
  [ 65%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/min_enclosing_triangle.cpp.o
  [ 65%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/moments.cpp.o
  [ 65%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/morph.dispatch.cpp.o
  [ 65%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/phasecorr.cpp.o
  [ 65%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/pyramids.cpp.o
  [ 65%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/resize.cpp.o
  [ 66%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/rotcalipers.cpp.o
  [ 66%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/samplers.cpp.o
  [ 66%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/segmentation.cpp.o
  [ 66%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/shapedescr.cpp.o
  [ 66%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/smooth.dispatch.cpp.o
  [ 66%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/spatialgradient.cpp.o
  [ 66%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/subdivision2d.cpp.o
  [ 66%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/sumpixels.dispatch.cpp.o
  [ 66%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/tables.cpp.o
  [ 66%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/templmatch.cpp.o
  [ 67%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/thresh.cpp.o
  [ 67%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/src/utils.cpp.o
  [ 67%] Building CXX object modules/imgproc/CMakeFiles/opencv_imgproc.dir/opencl_kernels_imgproc.cpp.o
  [ 67%] Linking CXX static library ../../lib/libopencv_imgproc.a
  [ 67%] Built target opencv_imgproc
  [ 67%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/ann_mlp.cpp.o
  [ 67%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/boost.cpp.o
  [ 67%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/data.cpp.o
  [ 67%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/em.cpp.o
  [ 67%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/gbt.cpp.o
  [ 67%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/inner_functions.cpp.o
  [ 68%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/kdtree.cpp.o
  [ 68%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/knearest.cpp.o
  [ 68%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/lr.cpp.o
  [ 68%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/nbayes.cpp.o
  [ 68%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/rtrees.cpp.o
  [ 68%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/svm.cpp.o
  [ 68%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/svmsgd.cpp.o
  [ 68%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/testset.cpp.o
  [ 68%] Building CXX object modules/ml/CMakeFiles/opencv_ml.dir/src/tree.cpp.o
  [ 68%] Linking CXX static library ../../lib/libopencv_ml.a
  [ 68%] Built target opencv_ml
  [ 68%] Processing OpenCL kernels (photo)
  [ 69%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/align.cpp.o
  [ 69%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/calibrate.cpp.o
  [ 69%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/contrast_preserve.cpp.o
  [ 69%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/denoise_tvl1.cpp.o
  [ 69%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/denoising.cpp.o
  [ 69%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/denoising.cuda.cpp.o
  [ 69%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/hdr_common.cpp.o
  [ 69%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/inpaint.cpp.o
  [ 69%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/merge.cpp.o
  [ 69%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/npr.cpp.o
  [ 70%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/seamless_cloning.cpp.o
  [ 70%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/seamless_cloning_impl.cpp.o
  [ 70%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/src/tonemap.cpp.o
  [ 70%] Building CXX object modules/photo/CMakeFiles/opencv_photo.dir/opencl_kernels_photo.cpp.o
  [ 70%] Linking CXX static library ../../lib/libopencv_photo.a
  [ 70%] Built target opencv_photo
  [ 71%] Processing OpenCL kernels (dnn)
  [ 71%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/caffe/opencv-caffe.pb.cc.o
  [ 71%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/onnx/opencv-onnx.pb.cc.o
  [ 71%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/attr_value.pb.cc.o
  [ 71%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/function.pb.cc.o
  [ 71%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/graph.pb.cc.o
  [ 71%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/op_def.pb.cc.o
  [ 71%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/tensor.pb.cc.o
  [ 71%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/tensor_shape.pb.cc.o
  [ 71%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/types.pb.cc.o
  [ 72%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/misc/tensorflow/versions.pb.cc.o
  [ 72%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/caffe/caffe_importer.cpp.o
  [ 72%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/caffe/caffe_io.cpp.o
  [ 72%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/caffe/caffe_shrinker.cpp.o
  [ 72%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/darknet/darknet_importer.cpp.o
  [ 72%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/darknet/darknet_io.cpp.o
  [ 72%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/dnn.cpp.o
  [ 72%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/graph_simplifier.cpp.o
  [ 72%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/halide_scheduler.cpp.o
  [ 72%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/ie_ngraph.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/init.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/batch_norm_layer.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/blank_layer.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/concat_layer.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/const_layer.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/convolution_layer.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/crop_and_resize_layer.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/detection_output_layer.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/elementwise_layers.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/eltwise_layer.cpp.o
  [ 73%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/flatten_layer.cpp.o
  [ 74%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/fully_connected_layer.cpp.o
  [ 74%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/layers_common.cpp.o
  [ 74%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/lrn_layer.cpp.o
  [ 74%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/max_unpooling_layer.cpp.o
  [ 74%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/mvn_layer.cpp.o
  [ 74%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/normalize_bbox_layer.cpp.o
  [ 74%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/padding_layer.cpp.o
  [ 74%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/permute_layer.cpp.o
  [ 74%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/pooling_layer.cpp.o
  [ 74%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/prior_box_layer.cpp.o
  [ 75%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/proposal_layer.cpp.o
  [ 75%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/recurrent_layers.cpp.o
  [ 75%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/region_layer.cpp.o
  [ 75%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/reorg_layer.cpp.o
  [ 75%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/reshape_layer.cpp.o
  [ 75%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/resize_layer.cpp.o
  [ 75%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/scale_layer.cpp.o
  [ 75%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/shuffle_channel_layer.cpp.o
  [ 75%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/slice_layer.cpp.o
  [ 75%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/softmax_layer.cpp.o
  [ 76%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/layers/split_layer.cpp.o
  [ 76%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/model.cpp.o
  [ 76%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/nms.cpp.o
  [ 76%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/ocl4dnn/src/common.cpp.o
  [ 76%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/ocl4dnn/src/math_functions.cpp.o
  [ 76%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/ocl4dnn/src/ocl4dnn_conv_spatial.cpp.o
  [ 76%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/ocl4dnn/src/ocl4dnn_inner_product.cpp.o
  [ 76%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/ocl4dnn/src/ocl4dnn_lrn.cpp.o
  [ 76%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/ocl4dnn/src/ocl4dnn_pool.cpp.o
  [ 76%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/ocl4dnn/src/ocl4dnn_softmax.cpp.o
  [ 77%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/onnx/onnx_graph_simplifier.cpp.o
  [ 77%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/onnx/onnx_importer.cpp.o
  [ 77%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/op_halide.cpp.o
  [ 77%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/op_inf_engine.cpp.o
  [ 77%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/op_vkcom.cpp.o
  [ 77%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/tengine4dnn/src/tengine_graph_convolution.cpp.o
  [ 77%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/tensorflow/tf_graph_simplifier.cpp.o
  [ 77%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/tensorflow/tf_importer.cpp.o
  [ 77%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/tensorflow/tf_io.cpp.o
  [ 77%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/torch/THDiskFile.cpp.o
  [ 78%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/torch/THFile.cpp.o
  [ 78%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/torch/THGeneral.cpp.o
  [ 78%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/torch/torch_importer.cpp.o
  [ 78%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/avg_pool_spv.cpp.o
  [ 78%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/concat_spv.cpp.o
  [ 78%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/conv48_spv.cpp.o
  [ 78%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/conv_spv.cpp.o
  [ 78%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/dw_conv_spv.cpp.o
  [ 78%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/lrn_spv.cpp.o
  [ 78%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/max_pool_spv.cpp.o
  [ 79%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/permute_spv.cpp.o
  [ 79%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/prior_box_spv.cpp.o
  [ 79%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/relu_spv.cpp.o
  [ 79%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/shader/softmax_spv.cpp.o
  [ 79%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/buffer.cpp.o
  [ 79%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/context.cpp.o
  [ 79%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/internal.cpp.o
  [ 79%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/op_base.cpp.o
  [ 79%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/op_concat.cpp.o
  [ 79%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/op_conv.cpp.o
  [ 80%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/op_lrn.cpp.o
  [ 80%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/op_permute.cpp.o
  [ 80%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/op_pool.cpp.o
  [ 80%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/op_prior_box.cpp.o
  [ 80%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/op_relu.cpp.o
  [ 80%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/op_softmax.cpp.o
  [ 80%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/src/tensor.cpp.o
  [ 80%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/vulkan/vk_functions.cpp.o
  [ 80%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/src/vkcom/vulkan/vk_loader.cpp.o
  [ 80%] Building CXX object modules/dnn/CMakeFiles/opencv_dnn.dir/opencl_kernels_dnn.cpp.o
  [ 81%] Linking CXX static library ../../lib/libopencv_dnn.a
  [ 81%] Built target opencv_dnn
  [ 81%] Processing OpenCL kernels (features2d)
  [ 81%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/agast.cpp.o
  [ 81%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/agast_score.cpp.o
  [ 81%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/akaze.cpp.o
  [ 81%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/bagofwords.cpp.o
  [ 81%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/blobdetector.cpp.o
  [ 81%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/brisk.cpp.o
  [ 81%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/draw.cpp.o
  [ 81%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/dynamic.cpp.o
  [ 82%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/evaluation.cpp.o
  [ 82%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/fast.cpp.o
  [ 82%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/fast_score.cpp.o
  [ 82%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/feature2d.cpp.o
  [ 82%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/gftt.cpp.o
  [ 82%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/kaze.cpp.o
  [ 82%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/kaze/AKAZEFeatures.cpp.o
  [ 82%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/kaze/KAZEFeatures.cpp.o
  [ 82%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/kaze/fed.cpp.o
  [ 82%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/kaze/nldiffusion_functions.cpp.o
  [ 83%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/keypoint.cpp.o
  [ 83%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/main.cpp.o
  [ 83%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/matchers.cpp.o
  [ 83%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/mser.cpp.o
  [ 83%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/src/orb.cpp.o
  [ 83%] Building CXX object modules/features2d/CMakeFiles/opencv_features2d.dir/opencl_kernels_features2d.cpp.o
  [ 83%] Linking CXX static library ../../lib/libopencv_features2d.a
  [ 83%] Built target opencv_features2d
  [ 84%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/gorigin.cpp.o
  [ 84%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/gmat.cpp.o
  [ 84%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/garray.cpp.o
  [ 84%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/gopaque.cpp.o
  [ 84%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/gscalar.cpp.o
  [ 84%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/gkernel.cpp.o
  [ 84%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/gbackend.cpp.o
  [ 84%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/gproto.cpp.o
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/optional.hpp:11,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/gscalar.hpp:16,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/core.hpp:18,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/precomp.hpp:14,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:8:
  In function ‘bool cv::util::operator==(const cv::util::variant<Ts ...>&, const cv::util::variant<Ts ...>&) [with Us = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’,
      inlined from ‘bool cv::can_describe(const GMetaArg&, const GRunArgP&)’ at /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:160:68:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:369:34: warning: ‘<anonymous>’ may be used uninitialized [-Wmaybe-uninitialized]
    369 |         return (eqs[lhs.index()])(lhs.memory, rhs.memory);
        |                ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp: In function ‘bool cv::can_describe(const GMetaArg&, const GRunArgP&)’:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:120:25: note: by argument 2 of type ‘const std::aligned_storage<48, 8>::type*’ to ‘static bool cv::util::variant<Ts>::equal_h<T>::help(const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*, const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*) [with T = cv::GScalarDesc; Ts = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’ declared here
    120 |             static bool help(const Memory lhs, const Memory rhs) {
        |                         ^~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:160:119: note: ‘<anonymous>’ declared here
    160 |     case GRunArgP::index_of<cv::Scalar*>():            return meta == GMetaArg(descr_of(*util::get<cv::Scalar*>(argp)));
        |                                                                                                                       ^
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/optional.hpp:11,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/gscalar.hpp:16,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/core.hpp:18,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/precomp.hpp:14,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:8:
  In function ‘bool cv::util::operator==(const cv::util::variant<Ts ...>&, const cv::util::variant<Ts ...>&) [with Us = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’,
      inlined from ‘bool cv::can_describe(const GMetaArg&, const GRunArgP&)’ at /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:161:68:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:369:34: warning: ‘<anonymous>’ may be used uninitialized [-Wmaybe-uninitialized]
    369 |         return (eqs[lhs.index()])(lhs.memory, rhs.memory);
        |                ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp: In function ‘bool cv::can_describe(const GMetaArg&, const GRunArgP&)’:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:120:25: note: by argument 2 of type ‘const std::aligned_storage<48, 8>::type*’ to ‘static bool cv::util::variant<Ts>::equal_h<T>::help(const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*, const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*) [with T = cv::GArrayDesc; Ts = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’ declared here
    120 |             static bool help(const Memory lhs, const Memory rhs) {
        |                         ^~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:161:129: note: ‘<anonymous>’ declared here
    161 |     case GRunArgP::index_of<cv::detail::VectorRef>():  return meta == GMetaArg(util::get<cv::detail::VectorRef>(argp).descr_of());
        |                                                                                                                                 ^
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/optional.hpp:11,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/gscalar.hpp:16,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/core.hpp:18,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/precomp.hpp:14,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:8:
  In function ‘bool cv::util::operator==(const cv::util::variant<Ts ...>&, const cv::util::variant<Ts ...>&) [with Us = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’,
      inlined from ‘bool cv::can_describe(const GMetaArg&, const GRunArgP&)’ at /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:162:68:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:369:34: warning: ‘<anonymous>’ may be used uninitialized [-Wmaybe-uninitialized]
    369 |         return (eqs[lhs.index()])(lhs.memory, rhs.memory);
        |                ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp: In function ‘bool cv::can_describe(const GMetaArg&, const GRunArgP&)’:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:120:25: note: by argument 2 of type ‘const std::aligned_storage<48, 8>::type*’ to ‘static bool cv::util::variant<Ts>::equal_h<T>::help(const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*, const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*) [with T = cv::GOpaqueDesc; Ts = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’ declared here
    120 |             static bool help(const Memory lhs, const Memory rhs) {
        |                         ^~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:162:129: note: ‘<anonymous>’ declared here
    162 |     case GRunArgP::index_of<cv::detail::OpaqueRef>():  return meta == GMetaArg(util::get<cv::detail::OpaqueRef>(argp).descr_of());
        |                                                                                                                                 ^
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/optional.hpp:11,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/gscalar.hpp:16,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/core.hpp:18,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/precomp.hpp:14,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:8:
  In function ‘bool cv::util::operator==(const cv::util::variant<Ts ...>&, const cv::util::variant<Ts ...>&) [with Us = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’,
      inlined from ‘bool cv::can_describe(const GMetaArg&, const GRunArg&)’ at /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:178:66:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:369:34: warning: ‘<anonymous>’ may be used uninitialized [-Wmaybe-uninitialized]
    369 |         return (eqs[lhs.index()])(lhs.memory, rhs.memory);
        |                ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp: In function ‘bool cv::can_describe(const GMetaArg&, const GRunArg&)’:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:120:25: note: by argument 2 of type ‘const std::aligned_storage<48, 8>::type*’ to ‘static bool cv::util::variant<Ts>::equal_h<T>::help(const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*, const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*) [with T = cv::GScalarDesc; Ts = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’ declared here
    120 |             static bool help(const Memory lhs, const Memory rhs) {
        |                         ^~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:178:118: note: ‘<anonymous>’ declared here
    178 |     case GRunArg::index_of<cv::Scalar>():            return meta == cv::GMetaArg(descr_of(util::get<cv::Scalar>(arg)));
        |                                                                                                                      ^
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/optional.hpp:11,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/gscalar.hpp:16,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/core.hpp:18,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/precomp.hpp:14,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:8:
  In function ‘bool cv::util::operator==(const cv::util::variant<Ts ...>&, const cv::util::variant<Ts ...>&) [with Us = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’,
      inlined from ‘bool cv::can_describe(const GMetaArg&, const GRunArg&)’ at /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:179:66:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:369:34: warning: ‘<anonymous>’ may be used uninitialized [-Wmaybe-uninitialized]
    369 |         return (eqs[lhs.index()])(lhs.memory, rhs.memory);
        |                ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp: In function ‘bool cv::can_describe(const GMetaArg&, const GRunArg&)’:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:120:25: note: by argument 2 of type ‘const std::aligned_storage<48, 8>::type*’ to ‘static bool cv::util::variant<Ts>::equal_h<T>::help(const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*, const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*) [with T = cv::GArrayDesc; Ts = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’ declared here
    120 |             static bool help(const Memory lhs, const Memory rhs) {
        |                         ^~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:179:130: note: ‘<anonymous>’ declared here
    179 |     case GRunArg::index_of<cv::detail::VectorRef>(): return meta == cv::GMetaArg(util::get<cv::detail::VectorRef>(arg).descr_of());
        |                                                                                                                                  ^
  In file included from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/optional.hpp:11,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/gscalar.hpp:16,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/core.hpp:18,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/precomp.hpp:14,
                   from /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:8:
  In function ‘bool cv::util::operator==(const cv::util::variant<Ts ...>&, const cv::util::variant<Ts ...>&) [with Us = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’,
      inlined from ‘bool cv::can_describe(const GMetaArg&, const GRunArg&)’ at /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:180:66:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:369:34: warning: ‘<anonymous>’ may be used uninitialized [-Wmaybe-uninitialized]
    369 |         return (eqs[lhs.index()])(lhs.memory, rhs.memory);
        |                ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp: In function ‘bool cv::can_describe(const GMetaArg&, const GRunArg&)’:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/include/opencv2/gapi/util/variant.hpp:120:25: note: by argument 2 of type ‘const std::aligned_storage<48, 8>::type*’ to ‘static bool cv::util::variant<Ts>::equal_h<T>::help(const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*, const typename std::aligned_storage<cv::util::variant<Ts>::S, cv::util::variant<Ts>::A>::type*) [with T = cv::GOpaqueDesc; Ts = {cv::util::monostate, cv::GMatDesc, cv::GScalarDesc, cv::GArrayDesc, cv::GOpaqueDesc}]’ declared here
    120 |             static bool help(const Memory lhs, const Memory rhs) {
        |                         ^~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/api/gproto.cpp:180:130: note: ‘<anonymous>’ declared here
    180 |     case GRunArg::index_of<cv::detail::OpaqueRef>(): return meta == cv::GMetaArg(util::get<cv::detail::OpaqueRef>(arg).descr_of());
        |                                                                                                                                  ^
  [ 84%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/gnode.cpp.o
  [ 84%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/gcall.cpp.o
  [ 85%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/gcomputation.cpp.o
  [ 85%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/operators.cpp.o
  [ 85%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/kernels_core.cpp.o
  [ 85%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/kernels_imgproc.cpp.o
  [ 85%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/render.cpp.o
  [ 85%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/render_ocv.cpp.o
  [ 85%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/ginfer.cpp.o
  [ 85%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/api/ft_render.cpp.o
  [ 85%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/gmodel.cpp.o
  [ 85%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/gmodelbuilder.cpp.o
  [ 86%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/gislandmodel.cpp.o
  [ 86%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/gcompiler.cpp.o
  [ 86%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/gcompiled.cpp.o
  [ 86%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/gstreaming.cpp.o
  [ 86%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/passes/helpers.cpp.o
  [ 86%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/passes/dump_dot.cpp.o
  [ 86%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/passes/islands.cpp.o
  [ 86%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/passes/meta.cpp.o
  [ 86%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/passes/kernels.cpp.o
  [ 86%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/passes/exec.cpp.o
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/compiler/passes/exec.cpp: In function ‘void cv::gimpl::{anonymous}::fuseTrivial(cv::gimpl::GIslandModel::Graph&, const ade::Graph&)’:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/compiler/passes/exec.cpp:74:25: warning: loop variable ‘nh’ creates a copy from type ‘const ade::Handle<ade::Node>’ [-Wrange-loop-construct]
     74 |         for (const auto nh : proto.in_nhs)
        |                         ^~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/compiler/passes/exec.cpp:74:25: note: use reference type to prevent copying
     74 |         for (const auto nh : proto.in_nhs)
        |                         ^~
        |                         &
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/compiler/passes/exec.cpp:79:25: warning: loop variable ‘nh’ creates a copy from type ‘const ade::Handle<ade::Node>’ [-Wrange-loop-construct]
     79 |         for (const auto nh : proto.out_nhs)
        |                         ^~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/compiler/passes/exec.cpp:79:25: note: use reference type to prevent copying
     79 |         for (const auto nh : proto.out_nhs)
        |                         ^~
        |                         &
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/compiler/passes/exec.cpp:93:25: warning: loop variable ‘nh’ creates a copy from type ‘const ade::Handle<ade::Node>’ [-Wrange-loop-construct]
     93 |         for (const auto nh : proto.in_nhs)
        |                         ^~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/compiler/passes/exec.cpp:93:25: note: use reference type to prevent copying
     93 |         for (const auto nh : proto.in_nhs)
        |                         ^~
        |                         &
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/compiler/passes/exec.cpp:98:25: warning: loop variable ‘nh’ creates a copy from type ‘const ade::Handle<ade::Node>’ [-Wrange-loop-construct]
     98 |         for (const auto nh : proto.out_nhs)
        |                         ^~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/compiler/passes/exec.cpp:98:25: note: use reference type to prevent copying
     98 |         for (const auto nh : proto.out_nhs)
        |                         ^~
        |                         &
  [ 87%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/passes/transformations.cpp.o
  [ 87%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/passes/pattern_matching.cpp.o
  [ 87%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/passes/perform_substitution.cpp.o
  [ 87%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/compiler/passes/streaming.cpp.o
  [ 87%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/executor/gexecutor.cpp.o
  [ 87%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/executor/gstreamingexecutor.cpp.o
  [ 87%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/executor/gasync.cpp.o
  [ 87%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/cpu/gcpubackend.cpp.o
  [ 87%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/cpu/gcpukernel.cpp.o
  [ 87%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/cpu/gcpuimgproc.cpp.o
  [ 88%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/cpu/gcpucore.cpp.o
  [ 88%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/fluid/gfluidbuffer.cpp.o
  [ 88%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/fluid/gfluidbackend.cpp.o
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/backends/fluid/gfluidbackend.cpp: In lambda function:
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/backends/fluid/gfluidbackend.cpp:1464:37: warning: loop variable ‘node’ creates a copy from type ‘const ade::Handle<ade::Node>’ [-Wrange-loop-construct]
   1464 |                     for (const auto node : isl->contents())
        |                                     ^~~~
  /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/opencv/modules/gapi/src/backends/fluid/gfluidbackend.cpp:1464:37: note: use reference type to prevent copying
   1464 |                     for (const auto node : isl->contents())
        |                                     ^~~~
        |                                     &
  [ 88%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/fluid/gfluidimgproc.cpp.o
  [ 88%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/fluid/gfluidimgproc_func.dispatch.cpp.o
  [ 88%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/fluid/gfluidcore.cpp.o
  [ 88%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/ocl/goclbackend.cpp.o
  [ 88%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/ocl/goclkernel.cpp.o
  [ 88%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/ocl/goclimgproc.cpp.o
  [ 88%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/ocl/goclcore.cpp.o
  [ 89%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/ie/giebackend.cpp.o
  [ 89%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/render/grenderocvbackend.cpp.o
  [ 89%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/render/grenderocv.cpp.o
  [ 89%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/plaidml/gplaidmlcore.cpp.o
  [ 89%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/plaidml/gplaidmlbackend.cpp.o
  [ 89%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/common/gcompoundbackend.cpp.o
  [ 89%] Building CXX object modules/gapi/CMakeFiles/opencv_gapi.dir/src/backends/common/gcompoundkernel.cpp.o
  [ 89%] Linking CXX static library ../../lib/libopencv_gapi.a
  [ 89%] Built target opencv_gapi
  [ 89%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/loadsave.cpp.o
  [ 89%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/utils.cpp.o
  [ 89%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_base.cpp.o
  [ 89%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_bmp.cpp.o
  [ 89%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_exr.cpp.o
  [ 89%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_gdal.cpp.o
  [ 89%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_gdcm.cpp.o
  [ 89%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_hdr.cpp.o
  [ 89%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_jpeg.cpp.o
  [ 89%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_jpeg2000.cpp.o
  [ 90%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_jpeg2000_openjpeg.cpp.o
  [ 90%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_pam.cpp.o
  [ 90%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_pfm.cpp.o
  [ 90%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_png.cpp.o
  [ 90%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_pxm.cpp.o
  [ 90%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_sunras.cpp.o
  [ 90%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_tiff.cpp.o
  [ 90%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/grfmt_webp.cpp.o
  [ 90%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/bitstrm.cpp.o
  [ 90%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/rgbe.cpp.o
  [ 91%] Building CXX object modules/imgcodecs/CMakeFiles/opencv_imgcodecs.dir/src/exif.cpp.o
  [ 91%] Linking CXX static library ../../lib/libopencv_imgcodecs.a
  [ 91%] Built target opencv_imgcodecs
  [ 91%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/videoio_registry.cpp.o
  [ 91%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/videoio_c.cpp.o
  [ 91%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/cap.cpp.o
  [ 91%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/cap_images.cpp.o
  [ 91%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/cap_mjpeg_encoder.cpp.o
  [ 92%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/cap_mjpeg_decoder.cpp.o
  [ 92%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/backend_plugin.cpp.o
  [ 92%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/backend_static.cpp.o
  [ 92%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/container_avi.cpp.o
  [ 92%] Building CXX object modules/videoio/CMakeFiles/opencv_videoio.dir/src/cap_v4l.cpp.o
  [ 92%] Linking CXX static library ../../lib/libopencv_videoio.a
  [ 92%] Built target opencv_videoio
  [ 92%] Processing OpenCL kernels (calib3d)
  [ 92%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/ap3p.cpp.o
  [ 92%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/calibinit.cpp.o
  [ 92%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/calibration.cpp.o
  [ 92%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/calibration_handeye.cpp.o
  [ 92%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/checkchessboard.cpp.o
  [ 92%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/chessboard.cpp.o
  [ 92%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/circlesgrid.cpp.o
  [ 93%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/compat_ptsetreg.cpp.o
  [ 93%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/dls.cpp.o
  [ 93%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/epnp.cpp.o
  [ 93%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/fisheye.cpp.o
  [ 93%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/five-point.cpp.o
  [ 93%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/fundam.cpp.o
  [ 93%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/homography_decomp.cpp.o
  [ 93%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/ippe.cpp.o
  [ 93%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/levmarq.cpp.o
  [ 93%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/main.cpp.o
  [ 94%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/p3p.cpp.o
  [ 94%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/polynom_solver.cpp.o
  [ 94%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/posit.cpp.o
  [ 94%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/ptsetreg.cpp.o
  [ 94%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/quadsubpix.cpp.o
  [ 94%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/rho.cpp.o
  [ 94%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/solvepnp.cpp.o
  [ 94%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/stereobm.cpp.o
  [ 94%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/stereosgbm.cpp.o
  [ 94%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/triangulate.cpp.o
  [ 95%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/undistort.dispatch.cpp.o
  [ 95%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/src/upnp.cpp.o
  [ 95%] Building CXX object modules/calib3d/CMakeFiles/opencv_calib3d.dir/opencl_kernels_calib3d.cpp.o
  [ 95%] Linking CXX static library ../../lib/libopencv_calib3d.a
  [ 95%] Built target opencv_calib3d
  [ 95%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/window.cpp.o
  [ 95%] Building CXX object modules/highgui/CMakeFiles/opencv_highgui.dir/src/roiSelector.cpp.o
  [ 96%] Linking CXX static library ../../lib/libopencv_highgui.a
  [ 96%] Built target opencv_highgui
  [ 97%] Processing OpenCL kernels (objdetect)
  [ 97%] Building CXX object modules/objdetect/CMakeFiles/opencv_objdetect.dir/src/cascadedetect.cpp.o
  [ 97%] Building CXX object modules/objdetect/CMakeFiles/opencv_objdetect.dir/src/cascadedetect_convert.cpp.o
  [ 97%] Building CXX object modules/objdetect/CMakeFiles/opencv_objdetect.dir/src/detection_based_tracker.cpp.o
  [ 97%] Building CXX object modules/objdetect/CMakeFiles/opencv_objdetect.dir/src/hog.cpp.o
  [ 97%] Building CXX object modules/objdetect/CMakeFiles/opencv_objdetect.dir/src/main.cpp.o
  [ 97%] Building CXX object modules/objdetect/CMakeFiles/opencv_objdetect.dir/src/qrcode.cpp.o
  [ 97%] Building CXX object modules/objdetect/CMakeFiles/opencv_objdetect.dir/opencl_kernels_objdetect.cpp.o
  [ 97%] Linking CXX static library ../../lib/libopencv_objdetect.a
  [ 97%] Built target opencv_objdetect
  [ 97%] Processing OpenCL kernels (stitching)
  [ 97%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/autocalib.cpp.o
  [ 97%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/blenders.cpp.o
  [ 98%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/camera.cpp.o
  [ 98%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/exposure_compensate.cpp.o
  [ 98%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/matchers.cpp.o
  [ 98%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/motion_estimators.cpp.o
  [ 98%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/seam_finders.cpp.o
  [ 98%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/stitcher.cpp.o
  [ 98%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/timelapsers.cpp.o
  [ 98%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/util.cpp.o
  [ 98%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/warpers.cpp.o
  [ 98%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/src/warpers_cuda.cpp.o
  [ 99%] Building CXX object modules/stitching/CMakeFiles/opencv_stitching.dir/opencl_kernels_stitching.cpp.o
  [ 99%] Linking CXX static library ../../lib/libopencv_stitching.a
  [ 99%] Built target opencv_stitching
  [ 99%] Processing OpenCL kernels (video)
  [ 99%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/bgfg_KNN.cpp.o
  [ 99%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/bgfg_gaussmix2.cpp.o
  [ 99%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/camshift.cpp.o
  [ 99%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/dis_flow.cpp.o
  [ 99%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/ecc.cpp.o
  [ 99%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/kalman.cpp.o
  [ 99%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/lkpyramid.cpp.o
  [100%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/optflowgf.cpp.o
  [100%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/optical_flow_io.cpp.o
  [100%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/src/variational_refinement.cpp.o
  [100%] Building CXX object modules/video/CMakeFiles/opencv_video.dir/opencl_kernels_video.cpp.o
  [100%] Linking CXX static library ../../lib/libopencv_video.a
  [100%] Built target opencv_video
  [100%] Generate files for Python bindings and documentation
  Note: Class Feature2D has more than 1 base class (not supported by Python C extensions)
        Bases:  cv::Algorithm, cv::class, cv::Feature2D, cv::Algorithm
        Only the first base class will be used
  Note: Class detail_GraphCutSeamFinder has more than 1 base class (not supported by Python C extensions)
        Bases:  cv::detail::GraphCutSeamFinderBase, cv::detail::SeamFinder
        Only the first base class will be used
  [100%] Built target gen_opencv_python_source
  [100%] Building CXX object modules/python3/CMakeFiles/opencv_python3.dir/__/src2/cv2.cpp.o
  [100%] Linking CXX shared module ../../lib/python3/cv2.cpython-36m-aarch64-linux-gnu.so
  [100%] Built target opencv_python3
  Install the project...
  -- Install configuration: "Release"
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/opencl-headers-LICENSE.txt
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/cvconfig.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/opencv_modules.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/cmake/opencv4/OpenCVModules.cmake
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/cmake/opencv4/OpenCVModules-release.cmake
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/cmake/opencv4/OpenCVConfig-version.cmake
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/cmake/opencv4/OpenCVConfig.cmake
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/bin/setup_vars_opencv4.sh
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/valgrind.supp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/valgrind_3rdparty.supp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/liblibjpeg-turbo.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/libjpeg-turbo-README.md
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/libjpeg-turbo-LICENSE.md
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/libjpeg-turbo-README.ijg
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/liblibtiff.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/libtiff-COPYRIGHT
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/liblibwebp.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/liblibjasper.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/jasper-LICENSE
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/jasper-README
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/jasper-copyright
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/liblibpng.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/libpng-LICENSE
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/libpng-README
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/libIlmImf.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/openexr-LICENSE
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/openexr-AUTHORS.ilmbase
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/openexr-AUTHORS.openexr
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/liblibprotobuf.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/protobuf-LICENSE
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/protobuf-README.md
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/libquirc.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/quirc-LICENSE
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/libtegra_hal.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/libittnotify.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/ittnotify-LICENSE.BSD
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/ittnotify-LICENSE.GPL
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/opencv.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/opencv4/3rdparty/libade.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/ade-LICENSE
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_core.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/ocl_defs.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/opencl_info.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/opencl_svm.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/autogenerated/opencl_clamdblas.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/autogenerated/opencl_clamdfft.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/autogenerated/opencl_core.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/autogenerated/opencl_core_wrappers.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/autogenerated/opencl_gl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/autogenerated/opencl_gl_wrappers.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/opencl_clamdblas.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/opencl_clamdfft.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/opencl_core.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/opencl_core_wrappers.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/opencl_gl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/opencl_gl_wrappers.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/opencl_svm_20.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/opencl_svm_definitions.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opencl/runtime/opencl_svm_hsa_extension.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/block.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/border_interpolate.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/color.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/common.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/datamov_utils.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/dynamic_smem.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/emulation.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/filters.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/funcattrib.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/functional.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/limits.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/reduce.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/saturate_cast.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/scan.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/simd_functions.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/transform.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/type_traits.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/utility.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/vec_distance.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/vec_math.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/vec_traits.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/warp.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/warp_reduce.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/warp_shuffle.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/detail/color_detail.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/detail/reduce.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/detail/reduce_key_val.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/detail/transform_detail.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/detail/type_traits_detail.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda/detail/vec_distance_detail.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/affine.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/async.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/base.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/bindings_utils.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/bufferpool.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/check.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/core.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/core_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda.inl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda_stream_accessor.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cuda_types.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cv_cpu_dispatch.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cv_cpu_helper.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cvdef.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cvstd.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cvstd.inl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/cvstd_wrapper.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/directx.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/eigen.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/fast_math.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/hal.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/interface.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin_avx.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin_avx512.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin_cpp.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin_forward.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin_msa.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin_neon.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin_sse.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin_sse_em.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin_vsx.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/intrin_wasm.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/msa_macros.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/hal/simd_utils.impl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/mat.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/mat.inl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/matx.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/neon_utils.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/ocl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/ocl_genbase.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/opengl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/operations.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/optim.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/ovx.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/persistence.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/saturate.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/simd_intrinsics.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/softfloat.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/sse_utils.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/traits.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/types.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/types_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/utility.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/utils/allocator_stats.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/utils/allocator_stats.impl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/utils/filesystem.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/utils/instrumentation.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/utils/logger.defines.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/utils/logger.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/utils/logtag.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/utils/tls.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/utils/trace.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/va_intel.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/version.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/vsx_utils.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/detail/async_promise.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/core/detail/exception_ptr.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/licenses/opencv4/SoftFloat-COPYING.txt
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_flann.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/all_indices.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/allocator.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/any.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/autotuned_index.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/composite_index.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/config.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/defines.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/dist.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/dummy.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/dynamic_bitset.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/flann.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/flann_base.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/general.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/ground_truth.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/hdf5.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/heap.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/hierarchical_clustering_index.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/index_testing.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/kdtree_index.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/kdtree_single_index.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/kmeans_index.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/linear_index.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/logger.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/lsh_index.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/lsh_table.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/matrix.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/miniflann.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/nn_index.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/object_factory.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/params.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/random.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/result_set.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/sampling.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/saving.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/simplex_downhill.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/flann/timer.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_imgproc.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgproc.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgproc/hal/hal.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgproc/hal/interface.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgproc/imgproc.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgproc/imgproc_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgproc/types_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgproc/detail/gcgraph.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_ml.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/ml.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/ml/ml.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/ml/ml.inl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_photo.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/photo.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/photo/cuda.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/photo/legacy/constants_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/photo/photo.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_dnn.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/dnn.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/dnn/all_layers.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/dnn/dict.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/dnn/dnn.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/dnn/dnn.inl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/dnn/layer.details.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/dnn/layer.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/dnn/shape_utils.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/dnn/utils/inference_engine.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/dnn/version.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_features2d.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/features2d.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/features2d/features2d.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/features2d/hal/interface.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_gapi.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/core.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/cpu/core.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/cpu/gcpukernel.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/cpu/imgproc.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/fluid/core.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/fluid/gfluidbuffer.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/fluid/gfluidkernel.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/fluid/imgproc.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/garg.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/garray.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gasync_context.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gcall.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gcommon.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gcompiled.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gcompiled_async.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gcompoundkernel.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gcomputation.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gcomputation_async.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gkernel.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gmat.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gmetaarg.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gopaque.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gproto.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gpu/core.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gpu/ggpukernel.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gpu/imgproc.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gscalar.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gstreaming.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gtransform.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gtype_traits.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/gtyped.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/imgproc.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/infer.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/infer/ie.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/ocl/core.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/ocl/goclkernel.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/ocl/imgproc.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/opencv_includes.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/operators.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/own/assert.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/own/convert.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/own/cvdefs.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/own/exports.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/own/mat.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/own/saturate.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/own/scalar.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/own/types.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/plaidml/core.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/plaidml/gplaidmlkernel.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/plaidml/plaidml.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/render.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/render/render.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/streaming/cap.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/streaming/source.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/util/any.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/util/compiler_hints.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/util/optional.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/util/throw.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/util/util.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/gapi/util/variant.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_imgcodecs.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgcodecs.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgcodecs/imgcodecs.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgcodecs/imgcodecs_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgcodecs/ios.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/imgcodecs/legacy/constants_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_videoio.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/videoio.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/videoio/cap_ios.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/videoio/legacy/constants_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/videoio/registry.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/videoio/videoio.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/videoio/videoio_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_calib3d.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/calib3d.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/calib3d/calib3d.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/calib3d/calib3d_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_highgui.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/highgui.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/highgui/highgui.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/highgui/highgui_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_objdetect.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/objdetect.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/objdetect/detection_based_tracker.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/objdetect/objdetect.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_stitching.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/warpers.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/autocalib.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/blenders.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/camera.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/exposure_compensate.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/matchers.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/motion_estimators.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/seam_finders.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/timelapsers.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/util.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/util_inl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/warpers.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/stitching/detail/warpers_inl.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib/libopencv_video.a
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/video.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/video/background_segm.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/video/legacy/constants_c.h
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/video/tracking.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/include/opencv4/opencv2/video/video.hpp
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/python/cv2.cpython-36m-aarch64-linux-gnu.so
  -- Set non-toolchain portion of runtime path of "/tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/python/cv2.cpython-36m-aarch64-linux-gnu.so" to "/tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/lib"
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_eye.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_eye_tree_eyeglasses.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalcatface.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalcatface_extended.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalface_alt.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalface_alt2.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalface_alt_tree.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalface_default.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_fullbody.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_lefteye_2splits.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_licence_plate_rus_16stages.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_lowerbody.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_profileface.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_righteye_2splits.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_russian_plate_number.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_smile.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_upperbody.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/lbpcascades/lbpcascade_frontalcatface.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/lbpcascades/lbpcascade_frontalface.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/lbpcascades/lbpcascade_frontalface_improved.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/lbpcascades/lbpcascade_profileface.xml
  -- Installing: /tmp/pip-install-pqgzl1kg/opencv-python_9e1a1c17644f47a7b93bfb081d02c86d/_skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/lbpcascades/lbpcascade_silverware.xml
  Copying files from CMake output
  creating directory _skbuild/linux-aarch64-3.6/cmake-install/cv2
  copying _skbuild/linux-aarch64-3.6/cmake-install/python/cv2.cpython-36m-aarch64-linux-gnu.so -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/cv2.cpython-36m-aarch64-linux-gnu.so
  creating directory _skbuild/linux-aarch64-3.6/cmake-install/cv2/data
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_eye.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_eye.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_eye_tree_eyeglasses.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_eye_tree_eyeglasses.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalcatface.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_frontalcatface.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalcatface_extended.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_frontalcatface_extended.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalface_alt.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_frontalface_alt.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalface_alt2.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_frontalface_alt2.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalface_alt_tree.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_frontalface_alt_tree.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_frontalface_default.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_frontalface_default.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_fullbody.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_fullbody.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_lefteye_2splits.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_lefteye_2splits.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_licence_plate_rus_16stages.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_licence_plate_rus_16stages.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_lowerbody.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_lowerbody.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_profileface.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_profileface.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_righteye_2splits.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_righteye_2splits.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_russian_plate_number.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_russian_plate_number.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_smile.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_smile.xml
  copying _skbuild/linux-aarch64-3.6/cmake-install/share/opencv4/haarcascades/haarcascade_upperbody.xml -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/data/haarcascade_upperbody.xml
  Copying files from non-default sourcetree locations
  copying LICENSE.txt -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/LICENSE.txt
  copying LICENSE-3RD-PARTY.txt -> _skbuild/linux-aarch64-3.6/cmake-install/cv2/LICENSE-3RD-PARTY.txt
  Traceback (most recent call last):
    File "/home/nexaiot/.local/lib/python3.6/site-packages/pip/_vendor/pep517/in_process/_in_process.py", line 363, in <module>
      main()
    File "/home/nexaiot/.local/lib/python3.6/site-packages/pip/_vendor/pep517/in_process/_in_process.py", line 345, in main
      json_out['return_val'] = hook(**hook_input['kwargs'])
    File "/home/nexaiot/.local/lib/python3.6/site-packages/pip/_vendor/pep517/in_process/_in_process.py", line 262, in build_wheel
      metadata_directory)
    File "/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/setuptools/build_meta.py", line 231, in build_wheel
      wheel_directory, config_settings)
    File "/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/setuptools/build_meta.py", line 215, in _build_with_temp_dir
      self.run_setup()
    File "/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/setuptools/build_meta.py", line 268, in run_setup
      self).run_setup(setup_script=setup_script)
    File "/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/setuptools/build_meta.py", line 158, in run_setup
      exec(compile(code, __file__, 'exec'), locals())
    File "setup.py", line 448, in <module>
      main()
    File "setup.py", line 248, in main
      cmake_source_dir=cmake_source_dir,
    File "/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/skbuild/setuptools_wrap.py", line 683, in setup
      cmake_install_dir,
    File "setup.py", line 399, in _classify_installed_files_override
      cmake_install_dir=cmake_install_reldir,
  TypeError: _classify_installed_files() got an unexpected keyword argument 'cmake_install_dir'
  ----------------------------------------
  ERROR: Failed building wheel for opencv-python
Failed to build opencv-python
ERROR: Could not build wheels for opencv-python, which is required to install pyproject.toml-based projects
    File "/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/setuptools/build_meta.py", line 158, in run_setup
      exec(compile(code, __file__, 'exec'), locals())
    File "setup.py", line 448, in <module>
      main()
    File "setup.py", line 248, in main
      cmake_source_dir=cmake_source_dir,
    File "/tmp/pip-build-env-nvwudqyi/overlay/lib/python3.6/site-packages/skbuild/setuptools_wrap.py", line 683, in setup
      cmake_install_dir,
    File "setup.py", line 399, in _classify_installed_files_override
      cmake_install_dir=cmake_install_reldir,
  TypeError: _classify_installed_files() got an unexpected keyword argument 'cmake_install_dir'
  ----------------------------------------
  ERROR: Failed building wheel for opencv-python
Failed to build opencv-python
ERROR: Could not build wheels for opencv-python, which is required to install pyproject.toml-based projects

