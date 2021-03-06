"""
Script to start server to drive your car.
"""

import donkey as dk 

import keras

#Load a trained keras model and use it in the KerasAngle pilot
#model_file = '/home/wroscoe/code/donkey/whiteline_model.hdf5'
model_file = '/home/ubuntu/will_car/ac_all-cnn3_full1-valloss623.82'
model = keras.models.load_model(model_file)
pilot = dk.pilots.KerasAngle(model=model, throttle=20)

#specify where sessions data should be saved
sh = dk.sessions.SessionHandler(sessions_path='~/donkey_data/sessions')
session = sh.new()

#start server 
w = dk.remotes.RemoteServer(session, pilot, port=8886)
w.start()

#in a browser go to localhost:8887 to drive your car
