import cv2
import os
image_paths=['135_cropped.png','136_cropped.png',]
# image_paths=['135_1.png','135_2.png',]
# initialized a list of images
imgs = []
  
# for i in range(len(image_paths)):
#     imgs.append(cv2.imread(image_paths[i]))
#     # import pdb; pdb.set_trace()
#     # imgs[i]=cv2.resize(imgs[i],(0,0),fx=0.4,fy=0.4)
#     # this is optional if your input images isn't too large
#     # you don't need to scale down the image
#     # in my case the input images are of dimensions 3000x1200
#     # and due to this the resultant image won't fit the screen
#     # scaling down the images 
# # showing the original pictures
# cv2.imshow('1',imgs[0])
# cv2.imshow('2',imgs[1])
  
# stitchy=cv2.Stitcher.create()
# (dummy,output)=stitchy.stitch(imgs)
  
# if dummy != cv2.STITCHER_OK:
#   # checking if the stitching procedure is successful
#   # .stitch() function returns a true value if stitching is 
#   # done successfully
#     print("stitching ain't successful", dummy)
# else: 
#     print('Your Panorama is ready!!!')
  
# # final output
# cv2.imshow('final result',output)
  
# cv2.waitKey(0)
import stitching

settings = {
            "detector": "akaze", 
            # "detector": "orb", 
            # "detector": "sift", 
            "nfeatures": 10000,
            # "match_conf": 0.65,
            # "match_conf": 0.65,
            # "matcher_type": "homography",
            # "matcher_type": "affine",
            # "range_width": 1,
            "confidence_threshold": 0.3, 
            # "estimator": "homography",
            # "estimator": "affine",
            "medium_megapix": 0.9,
            "low_megapix": 0.1,
            "final_megapix": 0.1,
            # "warper_type": "spherical", 
            "warper_type": "fisheye", 
            # "warper_type": "cylindrical", 
            # "warper_type": "stereographic", 
            "crop": False,
            # "finder": "dp_colorgrad",
            # "wave_correct_kind": "no",
            # "wave_correct_kind": "vert",
            # "wave_correct_kind": "auto",
            "timelapse": "as_is",
            # "adjuster": "no",
            # "adjuster": "ray",
            # "refinement_mask": "_____",
            # "compensator": "no",
            "compensator": "gain",
            # "finder": "no",
            # "blender_type": "no",
            # "blend_strength": 100,
            "try_use_gpu": False,
            "matches_graph_dot_file": "graph"
            }
cv2.ocl.setUseOpenCL(False)
stitcher = stitching.Stitcher(**settings)
# image_paths=['135_cropped.png','136_cropped.png',]
# image_paths=['temp/5_clean_small/135.pdf-1.jpg.png','temp/5_clean_small/136.pdf-1.jpg.png',]
# path_dir = 'temp/5_clean'
# path_dir = 'temp/6_clean'
# path_dir = 'temp/5_clean_gray'
# path_dir = 'temp/6_clean_gray'
# path_dir = 'temp/5_subset'
# path_dir = 'temp/6_subset'
# path_dir = 'temp/7_subset'
# path_dir = 'temp/central'
path_dir = 'temp/central_5'
files = os.listdir(path_dir)
image_paths = sorted([os.path.join(path_dir, fname) for fname in os.listdir(path_dir) if '.jpg' in fname])[:]
print(image_paths)
# image_paths=['135_cropped_small.png','136_cropped_small.png',]
panorama = stitcher.stitch(image_paths)
panorama = cv2.transpose(panorama)
# cv2.imwrite('output7.jpg', panorama)
cv2.imwrite('output10.jpg', panorama)
# import pdb; pdb.set_trace()
# cv2.imshow('final result',panorama)
# cv2.waitKey(0)