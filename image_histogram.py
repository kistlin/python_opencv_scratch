import cv2
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import plotnine as pn


# matplotlib.use('Qt5Agg')


def image_histogram():
    # create windows
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.namedWindow('image_bw', cv2.WINDOW_NORMAL)
    cv2.namedWindow('image_bw_eq', cv2.WINDOW_NORMAL)

    # read and work with image
    image = cv2.imread(r"image.jpg")
    image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_bw_eq = cv2.equalizeHist(image_bw)

    # display images
    cv2.imshow('image', image)
    cv2.imshow('image_bw', image_bw)
    cv2.imshow('image_bw_eq', image_bw_eq)

    # calculate histogram
    # np_hist_y, bins = np.histogram(image_bw.ravel(), 256, [0, 256])
    # hist = np.bincount(image_bw.ravel(), minlength=256) # faster version of np.histogram
    # plt.hist(image_bw.ravel(), bins=256)
    hist_bw = cv2.calcHist([image_bw], [0], None, [256], [0, 255])
    hist_bw_eq = cv2.calcHist([image_bw_eq], [0], None, [256], [0, 255])
    np_hist_x = np.arange(len(hist_bw))
    d = {'np_hist_x': np_hist_x, 'hist_bw': hist_bw.flatten(), 'hist_bw_eq': hist_bw_eq.flatten()}
    df = pd.DataFrame(data=d)

    # plot histogram
    pn_handle = pn.ggplot(df) + pn.geom_col(pn.aes(x='np_hist_x', y='hist_bw'), color=None, fill='red', alpha=0.5) + pn.ylab('occurences') \
                              + pn.geom_col(pn.aes(x='np_hist_x', y='hist_bw_eq'), color=None, fill='green', alpha=0.5) \
                              + pn.ggtitle('Histograms of bw images')
    pn_handle.draw()
    plt.show()

    while True:
        pressed_key = cv2.waitKey(16)
        if pressed_key == ord('q'):
            break

    # cleanup opencv
    cv2.destroyAllWindows()
