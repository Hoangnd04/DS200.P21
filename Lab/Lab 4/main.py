import threading
from stream_sender import start_sender
from stream_receiver import start_receiver

def main():
    host = 'localhost'
    port = 9999
    batch_size = 256
    epochs = 100
    learning_rate = 0.001

    receiver_thread = threading.Thread(target=start_receiver, args=(host, port, batch_size, learning_rate))
    sender_thread = threading.Thread(target=start_sender, args=(host, port, batch_size, epochs))

    receiver_thread.start()
    sender_thread.start()

    receiver_thread.join()
    sender_thread.join()

if __name__ == "__main__":
    main()
