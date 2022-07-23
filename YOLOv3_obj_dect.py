from gluoncv import model_zoo, data, utils
from matplotlib import pyplot as plt
import os

net = model_zoo.get_model('yolo3_darknet53_voc', pretrained=True)

for i in os.listdir("C:\Users\priya\Downloads\Enhancement of Computer Vision for Low Visibility conditions/sandstorm_images"):
  x, img = data.transforms.presets.yolo.load_test("C:\Users\priya\Downloads\Enhancement of Computer Vision for Low Visibility conditions/sandstorm_images/"+i, short=512)
  class_IDs, scores, bounding_boxs = net(x)
  ax = utils.viz.plot_bbox(img, bounding_boxs[0], scores[0],
                          class_IDs[0], class_names=net.classes)
  plt.savefig("C:\Users\priya\Downloads\Enhancement of Computer Vision for Low Visibility conditions/sand_d_res/"+i)
  
for i in os.listdir("C:\Users\priya\Downloads\Enhancement of Computer Vision for Low Visibility conditions/sandstorm_images"):
  y, img = data.transforms.presets.yolo.load_test("/content/drive/MyDrive/obj_d/"+i.split(".")[0] + "_run_final.jpg", short=512)
  class_IDs, scores, bounding_boxs = net(y)

  ax = utils.viz.plot_bbox(img, bounding_boxs[0], scores[0],
                          class_IDs[0], class_names=net.classes)
  plt.savefig("C:\Users\priya\Downloads\Enhancement of Computer Vision for Low Visibility conditions/zid_d_res/"+i)