import sys
print("Python:", sys.version)
try:
 import pip
 print("pip:", pip.__version__)
except Exception:
 print("pip indisponível no ambiente.")
