import cv2 
import numpy as np
import time

class OpticalFlowAnalyzer:
    def __init__(self, vid_path, output_path):
        self.cap = cv2.VideoCapture(vid_path)
        self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), self.fps, (self.frame_width, self.frame_height))

    def draw_flow(self, img, flow, step=16):
        h, w = img.shape[:2]
        y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
        fx, fy = flow[y,x].T

        lines = np.vstack([x, y, x-fx, y-fy]).T.reshape(-1, 2, 2)
        lines = np.int32(lines + 0.5)

        img_bgr = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        cv2.polylines(img_bgr, lines, 0, (0, 255, 0))

        for (x1, y1), (_x2, _y2) in lines:
            cv2.circle(img_bgr, (x1, y1), 1, (0, 255, 0), -1)

        return img_bgr

    def draw_hsv(self, flow):
        h, w = flow.shape[:2]
        fx, fy = flow[:,:,0], flow[:,:,1]

        ang = np.arctan2(fy, fx) + np.pi
        v = np.sqrt(fx*fx+fy*fy)

        hsv = np.zeros((h, w, 3), np.uint8)
        hsv[...,0] = ang*(180/np.pi/2)
        hsv[...,1] = 255
        hsv[...,2] = np.minimum(v*4, 255)
        bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

        return bgr

    def process_video(self):
        suc, prev = self.cap.read()
        prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)

        while True:
            suc, img = self.cap.read()
            if not suc:
                break

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Start time to calculate FPS
            start = time.time()

            flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

            prevgray = gray

            # End time
            end = time.time()
            # Calculate the FPS for current frame detection
            fps = 1 / (end-start)

            print(f"{fps:.2f} FPS")

            flow_img = self.draw_flow(gray, flow)
            hsv_img = self.draw_hsv(flow)

            self.out.write(hsv_img)  # Write the frame to the output video

            cv2.imshow("Flow Image", flow_img)
            cv2.imshow("HSV Image", hsv_img)

            key = cv2.waitKey(5)
            if key == ord('q'):
                break

        self.cap.release()
        self.out.release()
        cv2.destroyAllWindows()


