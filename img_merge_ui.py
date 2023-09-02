import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from img_interpolation import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.file1 = ''
        self.file2 = ''

        self.setWindowTitle("Interploation Tool V1")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # 수평 박스 레이아웃
        horizontal_layout = QHBoxLayout()

        # 버티컬 박스 레이아웃 1 이미지 1
        vertical_layout1 = QVBoxLayout()
        button1 = QPushButton("첫번째 이미지 입력(착시 이미지)")
        label1 = QLabel("")
        image_label1 = QLabel("")
        image_label1.setFixedSize(480,270)
        vertical_layout1.addWidget(button1,1)
        vertical_layout1.addWidget(label1,1)
        vertical_layout1.addWidget(image_label1,2)

        # 버티컬 박스 레이아웃 2 이미지 2
        vertical_layout2 = QVBoxLayout()
        button2 = QPushButton("두번째 이미지 입력(원본 이미지)")
        label2 = QLabel("")
        image_label2 = QLabel("")
        image_label2.setFixedSize(480,270)
        vertical_layout2.addWidget(button2,1)
        vertical_layout2.addWidget(label2,1)
        vertical_layout2.addWidget(image_label2,2)

        # 수평 박스 레이아웃에 버티컬 박스 레이아웃 추가
        horizontal_layout.addLayout(vertical_layout1)
        horizontal_layout.addLayout(vertical_layout2)

        # event
        button1.clicked.connect(lambda : self.showImageFileDialog(label1, image_label1,1))
        button2.clicked.connect(lambda : self.showImageFileDialog(label2, image_label2,2))


        # 수평 박스 레이아웃 1 : 시간 값 입력
        horizontal_layout1 = QHBoxLayout()
        label_noti = QLabel("초(s) 단위로 입력하세요.")

        vertical_time1 = QVBoxLayout()
        label_time1 = QLabel("첫 프레임 지속 시간")
        self.line_edit1 = QLineEdit("1")
        vertical_time1.addWidget(label_time1)
        vertical_time1.addWidget(self.line_edit1)

        vertical_time2 = QVBoxLayout()
        label_time2 = QLabel("interpolation 시간")
        self.line_edit2 = QLineEdit("4")
        vertical_time2.addWidget(label_time2)
        vertical_time2.addWidget(self.line_edit2)

        vertical_time3 = QVBoxLayout()
        label_time3 = QLabel("마지막 프레임 지속 시간")
        self.line_edit3 = QLineEdit("1")
        vertical_time3.addWidget(label_time3)
        vertical_time3.addWidget(self.line_edit3)

        
        horizontal_layout1.addLayout(vertical_time1)
        horizontal_layout1.addLayout(vertical_time2)
        horizontal_layout1.addLayout(vertical_time3)


        # 버튼 3
        button3 = QPushButton("Generate")

        # 수평 박스 레이아웃 2에 버튼 3 추가
        horizontal_layout2 = QHBoxLayout()
        horizontal_layout2.addWidget(button3)

        # 전체 레이아웃 구성
        main_layout = QVBoxLayout()
        main_layout.addLayout(horizontal_layout)
        main_layout.addWidget(label_noti)
        main_layout.addLayout(horizontal_layout1)   
        main_layout.addLayout(horizontal_layout2)

        central_widget.setLayout(main_layout)

        button3.clicked.connect(self.generateVideo)
        
        




    def showImageFileDialog(self, label_name, label_img, tag):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        options |= QFileDialog.Options(0)

        file_name, _ = QFileDialog.getOpenFileName(
            self, "이미지 파일 열기", "", "이미지 파일 (*.jpg *.png)", options=options
        )


        if file_name:
            if tag == 1:
                self.file1 = file_name
            elif tag==2:
                self.file2 = file_name

            label_name.setText(f"선택한 파일: {file_name}")

            pixmap = QPixmap(file_name)
            label_img.setPixmap(pixmap)
            label_img.setScaledContents(True)


    def generateVideo(self):
        save_file_path1(self.file1)
        save_file_path2(self.file2)
        save_time_val(self.line_edit1.text(), self.line_edit2.text(), self.line_edit3.text())
        start_generate_video()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
