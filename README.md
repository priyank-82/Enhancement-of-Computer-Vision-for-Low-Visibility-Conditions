# Enhancement-of-Computer-Vision-for-Low-Visibility-Conditions
Proposing an approach to improve upon the performance of SOTA object detection models in low visibility conditions.

## Steps to execute the code:
 NOTE: Update the paths in the scripts according to your own system.
 
 - Clone the repo by entering the following command in cmd.
 ```bash
git clone https://github.com/priyank-82/Enhancement-of-Computer-Vision-for-Low-Visibility-Conditions
```      
 - Run the following command to create a virtual environment in the same folder of the downloaded repo.
 ```bash
python -m venv <Path-to-the-directory-where-the-repo-is-downloaded>
```
 - Activate the virtual environment.
  
 - Go to the requirements.txt file of the repo and install the required libraries for running the scripts.
  
 - After installing the required libraries, place your normal images in the images and gt_data folders (example provided in the repo).
  
 - Obtain the depth images from the following repo : https://github.com/nianticlabs/monodepth2. Place the obtained depth image in the depth_images folder.
  
 - Now to create the sandstorm image run the following command, the images will be saved in the sandstorm_images folder.
 ```bash
python Create_Sandstorm_images.py
```
 - Now for the enhancement part of the images, Firstly color correct the images with the color compensation formula in the following paper:
        https://link.springer.com/article/10.1007/s00371-022-02448-8
 
 - After obtaining the color corrected images run the following command to perform ZID on the color corrected images. (Choose you desired iteration in the code on the basis of your computational resources)
```bash
python RW_dehazing.py
```
 - After obtaining the dehazed color corrected images, run the following command to perform object detection ( YOLOv3 in this case that is pre trained on teh Pascal VOC dataset)
```bash
python YOLOv3_obj_dect.py
```
 - The results of the object detection will be stored in the sand_d_res and zid_d_res folders.

## References
- Liang, P., Dong, P., Wang, F. et al. Learning to remove sandstorm for image enhancement. Vis Comput (2022). https://doi.org/10.1007/s00371-022-02448-8

- B. Li, Y. Gou, J. Z. Liu, H. Zhu, J. T. Zhou and X. Peng, "Zero-Shot Image Dehazing," in IEEE Transactions on Image Processing, vol. 29, pp. 8457-8466, 2020, 
doi: 10.1109/TIP.2020.3016134.

- W. Yang et al., "Advancing Image Understanding in Poor Visibility Environments: A Collective Benchmark Study," in IEEE Transactions on Image Processing, vol. 29, pp. 5737-5752, 2020, doi: 10.1109/TIP.2020.2981922.

- C. Godard, O. M. Aodha, M. Firman and G. Brostow, "Digging Into Self-Supervised Monocular Depth Estimation," 2019 IEEE/CVF International Conference on Computer Vision (ICCV), 2019, pp. 3827-3837, doi: 10.1109/ICCV.2019.00393.

