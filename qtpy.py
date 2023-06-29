from PySide2 import QtWidgets
from qtdesigner import rvm_interface


class MyQtApp(rvm_interface.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)

        self.start_p.clicked.connect(self.fill_form)
        self.source_p.clicked.connect(self.select_source)
        self.dest_p.clicked.connect(self.select_destination)
        self.output_p.clicked.connect(self.select_output)
        self.open_p.clicked.connect(self.select_output)

    def fill_form(self):
        source_path = self.source_l.text()
        if not source_path:
            QtWidgets.QMessageBox.about(self, "Source_Path is Required", "Hey Fill the path")
            return
        print(source_path)
        destination_path = self.dest_l.text()
        output_path = self.output_l.text()

    def select_source(self):
        source_video_path, ext = QtWidgets.QFileDialog.getOpenFileName(self, "selected file", 'D:\\',
                                                                       "Video File (*.mp4 *.mov)")
        self.source_l.setText(source_video_path)
        self.source_l.setReadOnly(True)

    def select_destination(self):
        dest_video_path, ext = QtWidgets.QFileDialog.getOpenFileName(self, "selected file", 'D:\\',
                                                                     "Video File (*.mp4 *.mov)")
        self.dest_l.setText(dest_video_path)
        self.dest_l.setReadOnly(True)

    def select_output(self):
        output_videos_path = QtWidgets.QFileDialog.getExistingDirectory(self, "selected Dir")
        self.output_l.setText(output_videos_path)
        self.output_l.setReadOnly(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
