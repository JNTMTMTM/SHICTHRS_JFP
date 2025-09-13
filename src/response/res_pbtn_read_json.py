
from PySide6.QtWidgets import QFileDialog , QMessageBox
from copy import deepcopy
import os

def res_pbtn_read_json(self):
    file_path, _ = QFileDialog.getOpenFileName(self , "选择需要进行SAC-JFP加密相关操作的json文件" , "json" , "JSON (*.json)")

    if file_path:
        self.file_path = deepcopy(file_path)

        self.pbtn_add_jfp.setEnabled(True)
        self.pbtn_update_jfp.setEnabled(True)

        self.lb_stu.setText("已选择文件 : " + os.path.basename(self.file_path))
    
    else:
        QMessageBox.warning(self , 'SAC_JFP 警告' , '请选择一个json文件。')


