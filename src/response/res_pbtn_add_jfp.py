
from PySide6.QtWidgets import QMessageBox
from functions.io.func_io_write_json_file import write_json_file

def res_pbtn_add_jfp(self) -> None:
    # print(self.file_data)
    if 'sac_jfp' not in self.file_data.keys():
        try:
            write_json_file(self.file_data , self.file_path)

        except:
            QMessageBox.warning(self , 'SAC_JFP 警告' , f'加密json文件时发生错误。\n文件路径 : {self.file_path}')

    else:
        QMessageBox.warning(self , 'SAC_JFP 警告' , '该json文件已经被SAC_JFP加密保护。')
