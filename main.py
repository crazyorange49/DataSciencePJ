
#         _..._
#       .'     '.      _
#      /    .-""-\   _/ \
#    .-|   /:.   |  |   |
#    |  \  |:.   /.-'-./
#    | .-'-;:__.'    =/
#    .'=  *=|NASA _.='
#   /   _.  |    ;
#  ;-.-'|    \   |
# /   | \    _\  _\
# \__/'._;.  ==' ==\
#          \    \   |
#          /    /   /
#          /-._/-._/
#          \   `\  \
#           `-._/._/

import colorsys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

colors_df = pd.read_csv("responses.csv")

#convert hex color code to hue
def hex_to_hue(hex_code):
    try:
        # Check if the hex is correct format
        if len(hex_code) != 7 or hex_code[0] != '#':
            raise ValueError("Invalid hex color code format")

        #hex to rgb (stupid math)
        rgb = tuple(int(hex_code[i:i+2], 16) for i in (1, 3, 5))
        
        #rgb values to hsv
        hsv = colorsys.rgb_to_hsv(rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0)
        return hsv[0] * 360
    except ValueError as e:
        print(f"Ignoring invalid hex color code '{hex_code}': {e}")
        return None

#converts all hex in data into hue
colors_df['Hue'] = colors_df['Favorite color'].apply(hex_to_hue)

colors_df = colors_df[colors_df['Age in years'] <= 45]

#plots the data
plt.figure(figsize=(10, 6))
plt.scatter(colors_df['Age in years'], colors_df['Hue'], color=colors_df['Favorite color'], alpha=0.7)
plt.xlabel('Age in years')
plt.ylabel('Hue value')
plt.title('Color Hue Distribution Across Ages')

# Plot the line of best fit
X = colors_df['Age in years'].values.reshape(-1, 1)
y = colors_df['Hue'].values.reshape(-1, 1)
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
plt.plot(X, y_pred, color='red', linewidth=2)

plt.grid(True)
plt.show()
#KRISTEN CUFF WAS HERE :)
