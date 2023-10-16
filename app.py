from streamlit_webrtc import webrtc_streamer, RTCConfiguration
import av
import cv2
import time
import streamlit as st

cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

st.title(":violet[FACE DETECTION NOTIFIER]")
a = st.button(":blue[PUSH NOTIFICATIONS]")


if a:
    st.toast("PUSH NOTIFICATION ENABLED")
    time.sleep(5)
    st.toast("WAKE UP!DON'T SLEEP")
	
	
class VideoProcessor:
	def recv(self, frame):
		frm = frame.to_ndarray(format="bgr24")

		faces = cascade.detectMultiScale(cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY), 1.1, 3)

		for x,y,w,h in faces:
			cv2.rectangle(frm, (x,y), (x+w, y+h), (0,255,0), 3)

		return av.VideoFrame.from_ndarray(frm, format='bgr24')

webrtc_streamer(key="key", video_processor_factory=VideoProcessor,
				rtc_configuration=RTCConfiguration(
					{"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
					)
	)

	
