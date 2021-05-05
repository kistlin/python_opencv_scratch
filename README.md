# OpenCV with CUDA and other modules
## Custom-built OpenCV
### Windows
#### Preparations
Compile or download all libraries required for the custom build. (Qt5, TBB, VTK, gstreamer and so on)

##### Get OpenCV
[OpenCV Releases](https://github.com/opencv/opencv/releases)

##### OpenCV contrib
Copy content of `modules\` from `https://github.com/opencv/opencv_contrib` into `C:\libs\opencv-4.5.1\modules`
> **NOTE**: Proper way would we to use `-DOPENCV_EXTRA_MODULES_PATH=<opencv_contrib>/modules`

#### NVIDIA architecture of video card
[NVIDIA GPU architecture](https://en.wikipedia.org/wiki/CUDA)

Here it is a `Quadro P2000` which results in `Compute capability (version)`=`6.1` and `Micro-architecture`=`Pascal`.

CMake options
```
-DCUDA_ARCH_BIN:STRING=6.1
-DCUDA_GENERATION:STRING=Pascal
```

#### Prepare build structure
```
mkdir C:/libs/opencv-4.5.1/_build
cd C:/libs/opencv-4.5.1/_build
```
Escape or concatenate the following string to generate the solution. Last two dots are important, they tell CMake where the sources are (one directory up).
```
"C:\Program Files\CMake\bin\cmake.exe" -G "Visual Studio 16 2019" -A x64
-DCMAKE_CONFIGURATION_TYPES:STRING=Release
-DCMAKE_INSTALL_PREFIX:PATH=C:/libs/opencv-4.5.1/_install
-DINSTALL_CREATE_DISTRIB:BOOL=ON
-DBUILD_opencv_apps:BOOL=ON
-DBUILD_opencv_aruco:BOOL=ON
-DBUILD_opencv_bgsegm:BOOL=ON
-DBUILD_opencv_bioinspired:BOOL=ON
-DBUILD_opencv_calib3d:BOOL=ON
-DBUILD_opencv_ccalib:BOOL=ON
-DBUILD_opencv_core:BOOL=ON
-DBUILD_opencv_cudaarithm:BOOL=ON
-DBUILD_opencv_cudabgsegm:BOOL=ON
-DBUILD_opencv_cudacodec:BOOL=ON
-DBUILD_opencv_cudafeatures2d:BOOL=ON
-DBUILD_opencv_cudafilters:BOOL=ON
-DBUILD_opencv_cudaimgproc:BOOL=ON
-DBUILD_opencv_cudalegacy:BOOL=ON
-DBUILD_opencv_cudaobjdetect:BOOL=ON
-DBUILD_opencv_cudaoptflow:BOOL=ON
-DBUILD_opencv_cudastereo:BOOL=ON
-DBUILD_opencv_cudawarping:BOOL=ON
-DBUILD_opencv_cudev:BOOL=ON
-DBUILD_opencv_cvv:BOOL=ON
-DBUILD_opencv_datasets:BOOL=ON
-DBUILD_opencv_dnn:BOOL=ON
-DBUILD_opencv_dnn_objdetect:BOOL=ON
-DBUILD_opencv_dnn_superres:BOOL=ON
-DBUILD_opencv_dpm:BOOL=ON
-DBUILD_opencv_face:BOOL=ON
-DBUILD_opencv_features2d:BOOL=ON
-DBUILD_opencv_flann:BOOL=ON
-DBUILD_opencv_fuzzy:BOOL=ON
-DBUILD_opencv_gapi:BOOL=ON
-DBUILD_opencv_hfs:BOOL=ON
-DBUILD_opencv_highgui:BOOL=ON
-DBUILD_opencv_img_hash:BOOL=ON
-DBUILD_opencv_imgcodecs:BOOL=ON
-DBUILD_opencv_imgproc:BOOL=ON
-DBUILD_opencv_intensity_transform:BOOL=ON
-DBUILD_opencv_java_bindings_generator:BOOL=ON
-DBUILD_opencv_js:BOOL=OFF
-DBUILD_opencv_js_bindings_generator:BOOL=ON
-DBUILD_opencv_line_descriptor:BOOL=ON
-DBUILD_opencv_mcc:BOOL=ON
-DBUILD_opencv_ml:BOOL=ON
-DBUILD_opencv_objc_bindings_generator:BOOL=ON
-DBUILD_opencv_objdetect:BOOL=ON
-DBUILD_opencv_optflow:BOOL=ON
-DBUILD_opencv_phase_unwrapping:BOOL=ON
-DBUILD_opencv_photo:BOOL=ON
-DBUILD_opencv_plot:BOOL=ON
-DBUILD_opencv_python3:BOOL=ON
-DBUILD_opencv_python_bindings_generator:BOOL=ON
-DBUILD_opencv_python_tests:BOOL=ON
-DBUILD_opencv_quality:BOOL=ON
-DBUILD_opencv_rapid:BOOL=ON
-DBUILD_opencv_reg:BOOL=ON
-DBUILD_opencv_rgbd:BOOL=ON
-DBUILD_opencv_saliency:BOOL=ON
-DBUILD_opencv_shape:BOOL=ON
-DBUILD_opencv_stereo:BOOL=ON
-DBUILD_opencv_stitching:BOOL=ON
-DBUILD_opencv_structured_light:BOOL=ON
-DBUILD_opencv_superres:BOOL=ON
-DBUILD_opencv_surface_matching:BOOL=ON
-DBUILD_opencv_text:BOOL=ON
-DBUILD_opencv_tracking:BOOL=ON
-DBUILD_opencv_ts:BOOL=ON
-DBUILD_opencv_video:BOOL=ON
-DBUILD_opencv_videoio:BOOL=ON
-DBUILD_opencv_videostab:BOOL=ON
-DBUILD_opencv_viz:BOOL=ON
-DBUILD_opencv_world:BOOL=OFF
-DBUILD_opencv_xfeatures2d:BOOL=ON
-DBUILD_opencv_ximgproc:BOOL=ON
-DBUILD_opencv_xobjdetect:BOOL=ON
-DBUILD_opencv_xphoto:BOOL=ON
-DCUDA_ARCH_BIN:STRING=6.1
-DCUDA_GENERATION:STRING=Pascal
-DGSTREAMER_app_LIBRARY:FILEPATH=C:/libs/gstreamer/1.0/msvc_x86_64/lib/gstapp-1.0.lib
-DGSTREAMER_base_LIBRARY:FILEPATH=C:/libs/gstreamer/1.0/msvc_x86_64/lib/gstbase-1.0.lib
-DGSTREAMER_glib_INCLUDE_DIR:PATH=C:/libs/gstreamer/1.0/msvc_x86_64/include/glib-2.0
-DGSTREAMER_glib_LIBRARY:FILEPATH=C:/libs/gstreamer/1.0/msvc_x86_64/lib/glib-2.0.lib
-DGSTREAMER_glibconfig_INCLUDE_DIR:PATH=C:/libs/gstreamer/1.0/msvc_x86_64/lib/glib-2.0/include
-DGSTREAMER_gobject_LIBRARY:FILEPATH=C:/libs/gstreamer/1.0/msvc_x86_64/lib/gobject-2.0.lib
-DGSTREAMER_gst_INCLUDE_DIR:PATH=C:/libs/gstreamer/1.0/msvc_x86_64/include/gstreamer-1.0
-DGSTREAMER_gstreamer_LIBRARY:FILEPATH=C:/libs/gstreamer/1.0/msvc_x86_64/lib/gstreamer-1.0.lib
-DGSTREAMER_pbutils_LIBRARY:FILEPATH=C:/libs/gstreamer/1.0/msvc_x86_64/lib/gstpbutils-1.0.lib
-DGSTREAMER_riff_LIBRARY:FILEPATH=C:/libs/gstreamer/1.0/msvc_x86_64/lib/gstriff-1.0.lib
-DPYTHON3_EXECUTABLE:FILEPATH=C:/tools/WinPython/WPy64-3920/python-3.9.2.amd64/python.exe
-DPYTHON3_INCLUDE_DIR:PATH=C:/tools/WinPython/WPy64-3920/python-3.9.2.amd64/include
-DPYTHON3_INCLUDE_DIR2:PATH=C:/tools/WinPython/WPy64-3920/python-3.9.2.amd64/include
-DPYTHON3_LIBRARY:FILEPATH=C:/tools/WinPython/WPy64-3920/python-3.9.2.amd64/libs/python39.lib
-DPYTHON3_NUMPY_INCLUDE_DIRS:PATH=C:/tools/WinPython/WPy64-3920/python-3.9.2.amd64/Lib/site-packages/numpy/core/include
-DPYTHON3_PACKAGES_PATH:PATH=C:/tools/WinPython/WPy64-3920/python-3.9.2.amd64/Lib/site-packages
-DQt5Concurrent_DIR:PATH=C:/libs/Qt/5.15.2/msvc2019_64/lib/cmake/Qt5Concurrent
-DQt5Core_DIR:PATH=C:/libs/Qt/5.15.2/msvc2019_64/lib/cmake/Qt5Core
-DQt5Gui_DIR:PATH=C:/libs/Qt/5.15.2/msvc2019_64/lib/cmake/Qt5Gui
-DQt5OpenGL_DIR:PATH=C:/libs/Qt/5.15.2/msvc2019_64/lib/cmake/Qt5OpenGL
-DQt5Test_DIR:PATH=C:/libs/Qt/5.15.2/msvc2019_64/lib/cmake/Qt5Test
-DQt5Widgets_DIR:PATH=C:/libs/Qt/5.15.2/msvc2019_64/lib/cmake/Qt5Widgets
-DQt5_DIR:PATH=C:/libs/Qt/5.15.2/msvc2019_64/lib/cmake/Qt5
-DTBB_DIR:PATH=C:/libs/oneTBB-2020_U3/cmake
-DTBB_ENV_INCLUDE:PATH=C:/libs/oneTBB-2020_U3/include
-DTBB_ENV_LIB:FILEPATH=C:/libs/oneTBB-2020_U3/build/vs2013/x64/Release/tbb.lib
-DTBB_ENV_LIB_DEBUG:FILEPATH=C:/libs/oneTBB-2020_U3/build/vs2013/x64/Debug/tbb_debug.lib
-DTBB_VER_FILE:FILEPATH=C:/libs/oneTBB-2020_U3/include/tbb/tbb_stddef.h
-DVTK_DIR:PATH=C:/libs/VTK-9.0.1/_install/lib/cmake/vtk-9.0
-DWITH_CUDA:BOOL=ON
-DWITH_CUDNN:BOOL=ON
-DCUDNN_INCLUDE_DIR:PATH=C:/libs/cudnn-11.2-windows-x64-v8.1.1.33/cuda/include
-DCUDNN_LIBRARY:FILEPATH=C:/libs/cudnn-11.2-windows-x64-v8.1.1.33/cuda/lib/x64/cudnn.lib
-DWITH_FFMPEG:BOOL=ON
-DWITH_MATLAB:BOOL=ON
-DWITH_OPENGL:BOOL=ON
-DWITH_QT:BOOL=ON
-DWITH_TBB:BOOL=ON
-DWITH_VTK:BOOL=ON
..
```

## Changes to Python
### Auto-completion
Create a symbolic link to enable auto-completion in PyCharm and most likely other IDEs.
```
mklink "C:\tools\WinPython\WPy64-3920\python-3.9.2.amd64\Lib\site-packages\cv2.cp39-win_amd64.pyd" "C:\tools\WinPython\WPy64-3920\python-3.9.2.amd64\Lib\site-packages\cv2\python-3.9\cv2.cp39-win_amd64.pyd"
```
### DLL paths
In `C:\tools\WinPython\WPy64-3920\python-3.9.2.amd64\Lib\site-packages\cv2\__init__.py` add the following code `import os ...`
```
...
def bootstrap():
    import sys
    import os
    os.add_dll_directory(r'C:\libs\opencv-4.5.1\_install\x64\vc16\bin')
    os.add_dll_directory(r'C:\libs\oneTBB-2020_U3\build\vs2013\x64\Release')
    os.add_dll_directory(r'C:\libs\Qt\5.15.2\msvc2019_64\bin')
    os.add_dll_directory(r'C:\libs\opencv-4.5.1\_install\bin')
    os.add_dll_directory(r'C:\libs\ffmpeg-n4.3.2-162-g4bbcaf7559-win64-gpl-shared-4.3\bin')
    os.add_dll_directory(r'C:\libs\gstreamer\1.0\msvc_x86_64\bin')
    os.add_dll_directory(r'C:\libs\gstreamer-runtime\1.0\msvc_x86_64\bin')
    os.add_dll_directory(r'C:\libs\VTK-9.0.1\_install\bin')
    os.add_dll_directory(r'C:\libs\cudnn-11.2-windows-x64-v8.1.1.33\cuda\bin')
    os.add_dll_directory(r'C:\tools\WinPython\WPy64-3920\python-3.9.2.amd64')
    os.add_dll_directory(r'C:\tools\WinPython\WPy64-3920\python-3.9.2.amd64\DLLs')
    os.add_dll_directory(r'C:\tools\WinPython\WPy64-3920\python-3.9.2.amd64\Lib\site-packages\cv2\python-3.9')
    os.add_dll_directory(r'C:\tools\WinPython\WPy64-3920\python-3.9.2.amd64\Lib\site-packages\numpy\DLLs')
...
```

### Test build in Python
```
python
Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import cv2
>>> print(cv2.getBuildInformation())

General configuration for OpenCV 4.5.1 =====================================
  Version control:               unknown

  Platform:
    Timestamp:                   2021-04-05T06:45:31Z
    Host:                        Windows 10.0.19042 AMD64
    CMake:                       3.20.0
    CMake generator:             Visual Studio 16 2019
    CMake build tool:            C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe
    MSVC:                        1928

  CPU/HW features:
    Baseline:                    SSE SSE2 SSE3
      requested:                 SSE3
    Dispatched code generation:  SSE4_1 SSE4_2 FP16 AVX AVX2 AVX512_SKX
      requested:                 SSE4_1 SSE4_2 AVX FP16 AVX2 AVX512_SKX
      SSE4_1 (15 files):         + SSSE3 SSE4_1
      SSE4_2 (1 files):          + SSSE3 SSE4_1 POPCNT SSE4_2
      FP16 (0 files):            + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 AVX
      AVX (4 files):             + SSSE3 SSE4_1 POPCNT SSE4_2 AVX
      AVX2 (29 files):           + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 FMA3 AVX AVX2
      AVX512_SKX (4 files):      + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 FMA3 AVX AVX2 AVX_512F AVX512_COMMON AVX512_SKX

  C/C++:
    Built as dynamic libs?:      YES
    C++ standard:                11
    C++ Compiler:                C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.28.29910/bin/Hostx64/x64/cl.exe  (ver 19.28.29913.0)
    C++ flags (Release):         /DWIN32 /D_WINDOWS /W4 /GR  /D _CRT_SECURE_NO_DEPRECATE /D _CRT_NONSTDC_NO_DEPRECATE /D _SCL_SECURE_NO_WARNINGS /Gy /bigobj /Oi  /fp:precise     /EHa /wd4127 /wd4251 /wd4324 /wd4275 /wd4512 /wd4589 /MP  /MD /O2 /Ob2 /DNDEBUG
    C++ flags (Debug):           /DWIN32 /D_WINDOWS /W4 /GR  /D _CRT_SECURE_NO_DEPRECATE /D _CRT_NONSTDC_NO_DEPRECATE /D _SCL_SECURE_NO_WARNINGS /Gy /bigobj /Oi  /fp:precise     /EHa /wd4127 /wd4251 /wd4324 /wd4275 /wd4512 /wd4589 /MP  /MDd /Zi /Ob0 /Od /RTC1
    C Compiler:                  C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.28.29910/bin/Hostx64/x64/cl.exe
    C flags (Release):           /DWIN32 /D_WINDOWS /W3  /D _CRT_SECURE_NO_DEPRECATE /D _CRT_NONSTDC_NO_DEPRECATE /D _SCL_SECURE_NO_WARNINGS /Gy /bigobj /Oi  /fp:precise     /MP   /MD /O2 /Ob2 /DNDEBUG
    C flags (Debug):             /DWIN32 /D_WINDOWS /W3  /D _CRT_SECURE_NO_DEPRECATE /D _CRT_NONSTDC_NO_DEPRECATE /D _SCL_SECURE_NO_WARNINGS /Gy /bigobj /Oi  /fp:precise     /MP /MDd /Zi /Ob0 /Od /RTC1
    Linker flags (Release):      /machine:x64  /INCREMENTAL:NO
    Linker flags (Debug):        /machine:x64  /debug /INCREMENTAL
    ccache:                      NO
    Precompiled headers:         YES
    Extra dependencies:          opengl32 glu32 cudart_static.lib nppc.lib nppial.lib nppicc.lib nppidei.lib nppif.lib nppig.lib nppim.lib nppist.lib nppisu.lib nppitc.lib npps.lib cublas.lib cudnn.lib cufft.lib -LIBPATH:C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.2/lib/x64 -LIBPATH:C:/libs/cudnn-11.2-windows-x64-v8.1.1.33/cuda/lib/x64
    3rdparty dependencies:

  OpenCV modules:
    To be built:                 aruco bgsegm bioinspired calib3d ccalib core cudaarithm cudabgsegm cudacodec cudafeatures2d cudafilters cudaimgproc cudalegacy cudaobjdetect cudaoptflow cudastereo cudawarping cudev cvv datasets dnn dnn_objdetect dnn_superres dpm face features2d flann fuzzy gapi hfs highgui img_hash imgcodecs imgproc intensity_transform line_descriptor mcc ml objdetect optflow phase_unwrapping photo plot python3 quality rapid reg rgbd saliency shape stereo stitching structured_light superres surface_matching text tracking ts video videoio videostab viz xfeatures2d ximgproc xobjdetect xphoto
    Disabled:                    world
    Disabled by dependency:      -
    Unavailable:                 alphamat cnn_3dobj freetype hdf java julia matlab matlab ovis python2 sfm
    Applications:                apps
    Documentation:               NO
    Non-free algorithms:         NO

  Windows RT support:            NO

  GUI:
    QT:                          YES (ver 5.15.2)
      QT OpenGL support:         YES (Qt5::OpenGL 5.15.2)
    Win32 UI:                    YES
    OpenGL support:              YES (opengl32 glu32)
    VTK support:                 YES (ver 9.0.1)

  Media I/O:
    ZLib:                        build (ver 1.2.11)
    JPEG:                        build-libjpeg-turbo (ver 2.0.6-62)
    WEBP:                        build (ver encoder: 0x020f)
    PNG:                         build (ver 1.6.37)
    TIFF:                        build (ver 42 - 4.0.10)
    JPEG 2000:                   build (ver 2.3.1)
    OpenEXR:                     build (ver 2.3.0)
    HDR:                         YES
    SUNRASTER:                   YES
    PXM:                         YES
    PFM:                         YES

  Video I/O:
    DC1394:                      NO
    FFMPEG:                      YES (prebuilt binaries)
      avcodec:                   YES (58.91.100)
      avformat:                  YES (58.45.100)
      avutil:                    YES (56.51.100)
      swscale:                   YES (5.7.100)
      avresample:                YES (4.0.0)
    GStreamer:                   YES (1.18.4)
    DirectShow:                  YES
    Media Foundation:            YES
      DXVA:                      YES

  Parallel framework:            TBB (ver 2020.3 interface 11103)

  Trace:                         YES (with Intel ITT)

  Other third-party libraries:
    Intel IPP:                   2020.0.0 Gold [2020.0.0]
           at:                   C:/libs/opencv-4.5.1/_build/3rdparty/ippicv/ippicv_win/icv
    Intel IPP IW:                sources (2020.0.0)
              at:                C:/libs/opencv-4.5.1/_build/3rdparty/ippicv/ippicv_win/iw
    Lapack:                      NO
    Eigen:                       NO
    Custom HAL:                  NO
    Protobuf:                    build (3.5.1)

  NVIDIA CUDA:                   YES (ver 11.2, CUFFT CUBLAS)
    NVIDIA GPU arch:             60 61
    NVIDIA PTX archs:

  cuDNN:                         YES (ver 8.1.1)

  OpenCL:                        YES (NVD3D11)
    Include path:                C:/libs/opencv-4.5.1/3rdparty/include/opencl/1.2
    Link libraries:              Dynamic load

  Python 3:
    Interpreter:                 C:/tools/WinPython/WPy64-3920/python-3.9.2.amd64/python.exe (ver 3.9.2)
    Libraries:                   C:/tools/WinPython/WPy64-3920/python-3.9.2.amd64/libs/python39.lib (ver 3.9.2)
    numpy:                       C:/tools/WinPython/WPy64-3920/python-3.9.2.amd64/Lib/site-packages/numpy/core/include (ver 1.20.1)
    install path:                C:/tools/WinPython/WPy64-3920/python-3.9.2.amd64/Lib/site-packages/cv2/python-3.9

  Python (for build):            C:/tools/WinPython/WPy64-3920/python-3.9.2.amd64/python.exe

  Java:
    ant:                         NO
    JNI:                         NO
    Java wrappers:               NO
    Java tests:                  NO

  Matlab:                        NO

  Install to:                    C:/libs/opencv-4.5.1/_install
-----------------------------------------------------------------
```
#### Check if CUDA is available
```
>>> cv2.cuda.getCudaEnabledDeviceCount()
1
```

## Misc
### Get a list of supported video IO backends
```
>>> [cv2.videoio_registry.getBackendName(b) for b in cv2.videoio_registry.getBackends()]
['FFMPEG', 'GSTREAMER', 'INTEL_MFX', 'MSMF', 'DSHOW', 'CV_IMAGES', 'CV_MJPEG', 'UEYE']
```

### DLL problems
Dump linked dll's
```
dumpbin.exe cv2.cp39-win_amd64.pyd /IMPORTS | findstr dll
```
