import asyncio
import websockets

# create handler for each connection
async def handler(websocket, path):

    while True:
        data = await websocket.recv()
        print(data)

    #reply = f"Data recieved as:  {data}!"
    #await websocket.send(reply)


start_server = websockets.serve(handler, "127.0.0.1", 9527)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
