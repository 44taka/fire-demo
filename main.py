import fire
import sys

def hello():
  return "Hello World!"

if __name__ == '__main__':
  fire.Fire(hello)
  sys.exit(0)