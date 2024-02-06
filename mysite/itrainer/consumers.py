import cv2
import asyncio
import base64
from channels.generic.websocket import AsyncWebsocketConsumer

class WebcamConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.cap = cv2.VideoCapture(0)  # 0 for default camera

        while self.scope["client"]:
            ret, frame = self.cap.read()
            _, buffer = cv2.imencode('.jpg', frame)

            # await self.send(text_data=buffer.tobytes())
            
            # Encode the buffer as base64
            encoded_image = base64.b64encode(buffer).decode('utf-8')
            await self.send(text_data=encoded_image)
            await asyncio.sleep(0.1)

    async def disconnect(self, close_code):
        # Close the webcam and release resources when the connection is closed
        if hasattr(self, 'cap'):
            self.cap.release()
        await super().disconnect(close_code)
