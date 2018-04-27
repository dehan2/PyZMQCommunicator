import zmq
import time
from ZMQCommunicator import ZMQCommunicator

communicator = ZMQCommunicator()
communicator.bind_server("tcp://*:5556")
communicator.connect_client("tcp://localhost:5555")

for request in range(100):
    message = communicator.receive()
    print("Received msg: %s" % message)
    communicator.reply_to_client("Well received: %s" % message)

    print("Send message")
    communicator.send("World")

    time.sleep(1)
    print("Waiting for receiving reply...")
    message = communicator.receive_reply()
    print("Received reply: %s" % message)
    print("Cycle complete")
    print("")