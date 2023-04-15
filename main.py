import sys

from PyQt5 import QtCore, QtWidgets

import db


def handle_res(command):
    if command == "f":
        return "rr"
        print("s")
        return "g"
    else:
        return None, None
if __name__ == "__main__":
    p, t = handle_res("g")

