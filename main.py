import cv2

"""
Attempted to download OpenCV-Python, a library of Python bindings designed to solve computer vision problems
pip install opencv-python 

=================================================================================================================================================================================
Error: 
Collecting opencv-python
  Using cached opencv-python-4.9.0.80.tar.gz (92.9 MB)
  Installing build dependencies ... error
  error: subprocess-exited-with-error

  × pip subprocess to install build dependencies did not run successfully.
  │ exit code: 1
  ╰─> [86 lines of output]
      Ignoring numpy: markers 'python_version == "3.6" and platform_machine != "aarch64" and platform_machine != "arm64"' don't match your environment
      Ignoring numpy: markers 'python_version == "3.7" and platform_machine != "aarch64" and platform_machine != "arm64"' don't match your environment
      Ignoring numpy: markers 'python_version == "3.8" and platform_machine != "aarch64" and platform_machine != "arm64"' don't match your environment
      Ignoring numpy: markers 'python_version <= "3.9" and sys_platform == "linux" and platform_machine == "aarch64"' don't match your environment
      Ignoring numpy: markers 'python_version <= "3.9" and sys_platform == "darwin" and platform_machine == "arm64"' don't match your environment
      Ignoring numpy: markers 'python_version == "3.9" and platform_machine != "aarch64" and platform_machine != "arm64"' don't match your environment
      Ignoring numpy: markers 'python_version == "3.10" and platform_system != "Darwin"' don't match your environment
      Ignoring numpy: markers 'python_version == "3.10" and platform_system == "Darwin"' don't match your environment
      Collecting cmake>=3.1
        Using cached cmake-3.28.1.tar.gz (42 kB)
        Installing build dependencies: started
        Installing build dependencies: finished with status 'done'
        Getting requirements to build wheel: started
        Getting requirements to build wheel: finished with status 'done'
        Preparing metadata (pyproject.toml): started
        Preparing metadata (pyproject.toml): finished with status 'done'
      Collecting numpy==1.22.2
        Using cached numpy-1.22.2.zip (11.4 MB)
        Installing build dependencies: started
        Installing build dependencies: finished with status 'done'
        Getting requirements to build wheel: started
        Getting requirements to build wheel: finished with status 'error'
        error: subprocess-exited-with-error

        Getting requirements to build wheel did not run successfully.
        exit code: 1

        [47 lines of output]
        Traceback (most recent call last):
          File "C:\msys64\mingw64\lib\python3.11\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 353, in <module>
            main()
          File "C:\msys64\mingw64\lib\python3.11\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 335, in main
            json_out['return_val'] = hook(**hook_input['kwargs'])
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          File "C:\msys64\mingw64\lib\python3.11\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 112, in get_requires_for_build_wheel
            backend = _build_backend()
                      ^^^^^^^^^^^^^^^^
          File "C:\msys64\mingw64\lib\python3.11\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 77, in _build_backend
            obj = import_module(mod_path)
                  ^^^^^^^^^^^^^^^^^^^^^^^
          File "C:\msys64\mingw64\lib\python3.11\importlib\__init__.py", line 126, in import_module
            return _bootstrap._gcd_import(name[level:], package, level)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
          File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
          File "<frozen importlib._bootstrap>", line 1126, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
          File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
          File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
          File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
          File "<frozen importlib._bootstrap_external>", line 944, in exec_module
          File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
          File "C:\Users\Ornie\AppData\Local\Temp\pip-build-env-m1plnt67\overlay\lib\python3.11\site-packages\setuptools\__init__.py", line 242, in <module>
            monkey.patch_all()
          File "C:\Users\Ornie\AppData\Local\Temp\pip-build-env-m1plnt67\overlay\lib\python3.11\site-packages\setuptools\monkey.py", line 99, in patch_all
            patch_for_msvc_specialized_compiler()
          File "C:\Users\Ornie\AppData\Local\Temp\pip-build-env-m1plnt67\overlay\lib\python3.11\site-packages\setuptools\monkey.py", line 162, in patch_for_msvc_specialized_compiler
            patch_func(*msvc9('find_vcvarsall'))
                        ^^^^^^^^^^^^^^^^^^^^^^^
          File "C:\Users\Ornie\AppData\Local\Temp\pip-build-env-m1plnt67\overlay\lib\python3.11\site-packages\setuptools\monkey.py", line 149, in patch_params
            mod = import_module(mod_name)
                  ^^^^^^^^^^^^^^^^^^^^^^^
          File "C:\msys64\mingw64\lib\python3.11\importlib\__init__.py", line 126, in import_module
            return _bootstrap._gcd_import(name[level:], package, level)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
          File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
          File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
          File "<frozen importlib._bootstrap_external>", line 944, in exec_module
          File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
          File "C:\Users\Ornie\AppData\Local\Temp\pip-build-env-m1plnt67\overlay\lib\python3.11\site-packages\setuptools\_distutils\msvc9compiler.py", line 295, in <module>
            raise DistutilsPlatformError("VC %0.1f is not supported by this module" % VERSION)
        distutils.errors.DistutilsPlatformError: VC 6.0 is not supported by this module
        [end of output]

        note: This error originates from a subprocess, and is likely not a problem with pip.
      error: subprocess-exited-with-error

      Getting requirements to build wheel did not run successfully.
      exit code: 1

      See above for output.

      note: This error originates from a subprocess, and is likely not a problem with pip.
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: subprocess-exited-with-error

× pip subprocess to install build dependencies did not run successfully.
│ exit code: 1
╰─> See above for output.

note: This error originates from a subprocess, and is likely not a problem with pip.
"""

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("test.jpg")

gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces: 
    cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)

cv2.imshow("img", img)
cv2.waitKey()

cv2.imwrite("face_detected.jpg", img)

# Run this on command prompt. 