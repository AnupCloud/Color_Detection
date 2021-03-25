import cv2
import matplotlib.pyplot as plt
import pandas as pd

img1_path = 'U14.png'
csv_path = 'colours.csv'

img2 = cv2.imread(img1_path)
img2 = cv2.resize(img2, (800, 600))

plt.figure(figsize=(20, 8))
plt.imshow(img2)

grid_RGB = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(20, 8))
plt.imshow(grid_RGB)

index = ['colour', 'colour_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv(csv_path, names=index, header=None)

clicked = False
r = g = b = xpos = ypos = 0


def get_color_name(R, G, B):
    minimum = 1000
    for i in range(len(df)):
        d = abs(R - int(df.loc[i, 'R'])) + abs(G - int(df.loc[i, 'G'])) + abs(
            B - int(df.loc[i, 'B']))
        if d <= minimum:
            minimum = d
            cname = df.loc[i, 'colour_name']

    return cname


def draw_function(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img2[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow('Detection')
cv2.setMouseCallback('Detection', draw_function)

while True:
    cv2.imshow('Detection', img2)
    if clicked:
        cv2.rectangle(img2, (20, 20), (600, 60), (b, g, r), -1)

        text = get_color_name(r, g, b) + ' R  =' + str(r) + ' G = ' + str(
            g) + ' B = ' + str(b)

        cv2.putText(img2, text, (50, 50), 2, 0.8, (0, 255, 255), 2, cv2.LINE_AA)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
