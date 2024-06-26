import conversion
from conversion import convert_fits_to_image
from images_Preprocessing.Otsu_Thresholding import otsu_thresholding_folder 
from images_Preprocessing.iterative_Threshholding import iterative_thresholding_folder
from Detection.object_labeling import detect_objects
from   Detection.Classification import DebrisAnalyzer
import cv2 
import os 
from Tracking.optical_flow_fernback import OpticalFlowAnalyzer
from Tracking.Images_to_Vid import images_to_video 
# from Orbit_Determination.orbit_determination import SatelliteAnalyzer
# from Tracking.optical_flow_lucas_kanade import OpticalFlowAnalyzerLucasKanade
# from Tracking.optical_flow_horn_schunk import OpticalFlowAnalyzerHornSchunck




fits_directory=r'C:\Users\USER\Desktop\TechnicalGP\2024-001'
images_directory=r'C:\Users\USER\Desktop\TechnicalGP\2024-001-images'

#convert the fits files 
#convert_fits_to_image(fits_directory,images_directory)

#otsu threshing 
otsu_images=r'C:\Users\USER\Desktop\TechnicalGP\images_Preprocessing\otsu_images'
#otsu_thresholding_folder(images_directory,otsu_images)

#iterative threshing 
iterat_images=r'C:\Users\USER\Desktop\TechnicalGP\images_Preprocessing\iter_images'
#iterative_thresholding_folder(images_directory,iterat_images)

#detect and label the object in the images

# Process each image in the input folder

# for filename in os.listdir(iterat_images):
#     # Load the binary image
#     binary_image = cv2.imread(os.path.join(iterat_images, filename), cv2.IMREAD_GRAYSCALE)

#     # Detect objects in the binary image
#     detected_objects, annotated_image = detect_objects(binary_image)

#     # Save the annotated image to the output folder
#     output_path = os.path.join(iterat_images, filename)
#     cv2.imwrite(output_path, annotated_image)

#call the class and create an instance 
csv_file=r'C:\Users\USER\Desktop\TechnicalGP\groundtruth.xlsx'
#analyzer = DebrisAnalyzer( iterat_images, csv_file)

# Call the process_images method to execute the processing workflow
#analyzer.process_images()



vid_path=r'C:\Users\USER\Desktop\TechnicalGP\Tracking\OG.MP4'
fps=5
#images_to_video(iterat_images, vid_path, fps)

#Applying The optical flow (Dense- Fernback)

output_path=r'C:\Users\USER\Desktop\TechnicalGP\Tracking\fernbackOUT.MP4'
# analyzer = OpticalFlowAnalyzer(vid_path, output_path)
# analyzer.process_video()


#julias code 

# analyzer = SatelliteAnalyzer(fits_directory)
# analyzer.analyze()

# output_path = r"C:\Users\USER\Desktop\TechnicalGP\Tracking\LUC-KANOUT.MP4"
# analyzer = OpticalFlowAnalyzerLucasKanade(vid_path, output_path)
# analyzer.process_video()




# output_path = r"C:\Users\USER\Desktop\TechnicalGP\Tracking\horn-shuckOUT.MP4"
# analyzer = OpticalFlowAnalyzerHornSchunck(vid_path, output_path)
# analyzer.process_video()


#tracking num
# Usage

csv_output_path = r"C:\Users\USER\Desktop\TechnicalGP\trackingvalues.xlsx"

analyzer = OpticalFlowAnalyzer(vid_path, output_path)
analyzer.process_video(csv_output_path)