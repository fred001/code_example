import os
import sys
import time
import websocket
import threading

ws=None

def on_message(ws, message):
    print("ON_MESSAGE",message)

def on_error(ws, error):
    print("ON_ERROR",error)

def on_close(ws, close_status_code, close_msg):
    print("ON_CLOSE",close_status_code,close_msg)

def on_open(ws):
    print("ON_OPEN")
    ws.send("OPEN")


def start_websocket_client():
    global ws

    #websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://127.0.0.1:9527",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever()  


def receive_user_input():
    global ws

    while True:
        msg=input(">")

        if msg == "quit":
            break


        ws.send(msg)
        time.sleep(0.1)


if __name__ == "__main__":
    thread1=threading.Thread(target=start_websocket_client,daemon=True)

    thread2=threading.Thread(target=receive_user_input)

    thread1.start()
    thread2.start()

