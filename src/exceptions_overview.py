import sys
import traceback


class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


try:
    raise CustomException("Some exception...")
except:
    print("Handling exception...", file=sys.stderr)
    traceback.print_exc()

print(file=sys.stderr)

try:
    {}["a"]
except KeyError as e:
    print(f"No key in the map...{e}", file=sys.stderr)
    traceback.print_exc()
