import pydicom as dicom
import os
import cv2
import PIL # optional

maindir_path="/Users/mkaracabey/Downloads/dataset/mass_test_mamogram/CBIS-DDSM/"
outputdir_path="/Users/mkaracabey/Downloads/dataset/mass_test_image_png/"
PNG=True

subdirs = os.listdir(maindir_path)
for n, s in enumerate(subdirs):
    try:
        subdir_path = os.path.join(maindir_path, s)
        #print(n, subdir_path)

        subsubdirs = os.listdir(subdir_path)
        for n1, s1 in enumerate(subsubdirs):
            subsubdir_path = os.path.join(subdir_path, s1)
            #print(n1, subsubdir_path)

            subsubsubdirs = os.listdir(subsubdir_path)
            for n2, s2 in enumerate(subsubsubdirs):
                subsubsubdir_path = os.path.join(subsubdir_path, s2)
                #print(n2, subsubsubdir_path)
                dcms = os.listdir(subsubsubdir_path)
                for n3, s3 in enumerate(dcms):
                    dcm_path = os.path.join(subsubsubdir_path, s3)
                    #print(n3, dcm_path)
                    try:
                        ds = dicom.dcmread(dcm_path)
                        pixel_array_numpy = ds.pixel_array

                        image_path = outputdir_path+s+"-"+s3
                        print("Convert: ",dcm_path)
                        if PNG == False:
                            image_path = image_path.replace('.dcm', '.jpg')
                        else:
                            image_path = image_path.replace('.dcm', '.png')
                        cv2.imwrite(image_path, pixel_array_numpy)
                    except:
                        print("One file failed:", dcm_path)
    except:
        print("System error occured")
