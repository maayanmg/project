import socket
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
from login import Ui_LoginD
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

def run_app():
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_LoginD()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
def start_client():
    run_app()

    while True:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 8080))
        # Receive public key from server
        public_pem = client_socket.recv(1024)

        # Deserialize public key
        public_key = serialization.load_pem_public_key(
            public_pem,
            backend=default_backend()
        )
        # Encrypt message using public key
        message = input("write something")
        message.encode()
        encrypted_message = public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
            )

        # Send encrypted message to server
        client_socket.send(encrypted_message)

        # Receive encrypted message from server
        msg = client_socket.recv(1024)
        print(msg.decode())

start_client()