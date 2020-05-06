import os
import numpy as np
import pandas as pd
import sys
from shutil import copyfile


train_dir = "./train/"
validation_dir = "./validation/"

x = os.listdir("./gate")
x = [ s.split('_')[2] for s in x]

data = pd.read_csv("coordinates_0_6999.csv")

train_df = data.copy()
valid_df = data.copy()

keep_training = []
keep_validation = []

np.random.seed(0)
for index, pic_number in enumerate(data['pic number']):
	#print(pic_number)
	rand = np.random.rand()
	if rand < 0.8:
		print("training ", index)
		keep_training.append(index)
		gate_name = "screen_640x480_{}.jpg".format(pic_number)
		copyfile("./gate/" + gate_name, "./train/gate/" + gate_name)
	else:
		print("validation ", index)
		keep_validation.append(index)
		gate_name = "screen_640x480_{}.jpg".format(pic_number)
		copyfile("./gate/" + gate_name, "./validation/gate/" + gate_name)


train_df = train_df.iloc[keep_training]
train_df.to_csv("./train.csv")

valid_df = valid_df.iloc[keep_validation]
valid_df.to_csv("./validation.csv")

# print(x)
