# -*- coding:utf-8 -*-

# 采用paddleOCR
from PyQt5.QtCore import QObject,pyqtSignal,pyqtSlot
from PyQt5.QtGui import QPixmap,QImage
from paddleocr import PaddleOCR, draw_ocr
from paddleocr import PPStructure,draw_structure_result,save_structure_res
# 显示结果
from PIL import Image
import os

class OCR_qt(QObject):
    sendResult = pyqtSignal(list)

    def __init__(self,parent=None):
        super(OCR_qt, self).__init__(parent)
        self.img_path = ""
        self.use_angle = True
        self.cls = True
        self.default_lan = "en"
        self.result = []

    def set_task(self,img_path='./imgs/11.jpg',use_angle=True,cls=True, lan="en"):
        self.img_path = img_path
        self.use_angle = use_angle
        self.cls = cls
        self.default_lan = lan

    def start(self):
        if not self.img_path:
            print("No img_path input.")
            return

        # 用于线程启动
        self.ocr(self.img_path,self.use_angle,self.cls,self.default_lan)

    def ocr(self,img_path='./imgs/11.jpg',use_angle=True,cls=True, lan="en", use_gpu=0):
        self.img_path = img_path
        self.default_lan = lan
        ocr = PaddleOCR(use_angle_cls=use_angle,
                        use_gpu=use_gpu,
                        lang=lan)  # need to run only once to download and load model into memory
        result = ocr.ocr(img_path, cls=cls)
        self.result = result
        for line in result:
            print(line)
        self.sendResult.emit(result)

    def vis_ocr_result(self,save_folder = './output/'):
        image = Image.open(self.img_path).convert('RGB')
        boxes = [line[0] for line in self.result]
        txts = [line[1][0] for line in self.result]
        scores = [line[1][1] for line in self.result]
        im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
        im_show = Image.fromarray(im_show)
        im_show.save(os.path.join(save_folder, 'result_ocr.jpg'))
        return im_show



