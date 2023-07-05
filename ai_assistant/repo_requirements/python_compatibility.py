```python
import sys

def validatePythonCompatibility():
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or a more recent version is required.")
    elif sys.version_info[0] == 3 and sys.version_info[1] < 6:
        raise Exception("Python 3.6 or a more recent version is required.")
    else:
        print("Python version is compatible.")

validatePythonCompatibility()
```