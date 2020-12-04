import uuid


class FileUUID():
    fileTransferTasks = {}
    def getFileUUID(self, fileName):
        return str(uuid.uuid5(uuid.NAMESPACE_DNS, fileName))

    def isExistFileTrasferTask(self, fileUUID):
        if(fileUUID in self.fileTransferTasks):
            return True
        else:
            return False

    def addFileTransferTask(self, fileName, fileSock):
        fileUUID = self.getFileUUID(fileName)
        if self.isExistFileTrasferTask(self.isExistFileTrasferTask(fileUUID)):
            return False
        self.fileTransferTasks[fileUUID] = fileSock
        print(self.fileTransferTasks)
        print('添加文件传输任务:', fileName)
        return True

    def removeFileTransferTask(self, fileName):
        fileUUID = self.getFileUUID(fileName)
        if not self.isExistFileTrasferTask(fileUUID):
            return None
        fileSock =  self.fileTransferTasks[fileUUID]
        del self.fileTransferTasks[fileUUID]
        print(self.fileTransferTasks)
        print('成功移除文件传输任务', fileName)
        return fileSock


if __name__ == '__main__':
    tt = FileUUID()
    fileName1 = 'main.py'
    print(tt.addFileTransferTask(fileName1, 1))
    print(tt.isExistFileTrasferTask('4fb8316f-4911-55cb-942c-8ba1af084d1e'))
    print(tt.removeFileTransferTask(fileName1))
