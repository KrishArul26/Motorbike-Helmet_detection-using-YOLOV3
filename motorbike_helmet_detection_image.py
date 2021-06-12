import cv2
import numpy as np
from bike_helmet_detector_image import detection
from utils import visualization_utils as vis_util

# Get the category index, images, boxes, scores and classes for helmet

category_index_helmet, image_helmet, boxes_helmet, scores_helmet, classes_helmet, num_helmet = \
    detection('frozen_graphs', '/frozen_inference_graph_helmet.pb', '/labelmap_helmet.pbtxt', 2, 'image10.jpg')

# Get the category index, images, boxes, scores and classes for motorbike and person

category_index_motorbike, image_helmet, boxes_motorbike, scores_motorbike, classes_motorbike, num_motorbike = \
    detection('frozen_graphs', '/frozen_inference_graph_motorbike.pb', '/labelmap_motorbike.pbtxt', 4, 'image10.jpg')

vis_util.visualize_boxes_and_labels_on_image_array(
        image_helmet,
        np.squeeze(boxes_motorbike),
        np.squeeze(classes_motorbike).astype(np.int32),
        np.squeeze(scores_motorbike),
        category_index_motorbike,
        use_normalized_coordinates=True,
        line_thickness=6,
        min_score_thresh=0.75)

k=vis_util.visualize_boxes_and_labels_on_image_array(
        image_helmet,
        np.squeeze(boxes_helmet),
        np.squeeze(classes_helmet).astype(np.int32),
        np.squeeze(scores_helmet),
        category_index_helmet,
        use_normalized_coordinates=True,
        line_thickness=6,
        min_score_thresh=0.70)
cv2.imshow('Object detector', k)
cv2.imwrite('helmet_bike_detection_10.jpg', k)
cv2.waitKey(0)
cv2.destroyAllWindows()