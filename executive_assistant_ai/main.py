```python
import sys
from assistant import Assistant

def main():
    try:
        assistant = Assistant()
        assistant.setup()
        assistant.run()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```