
import hashlib,os,shutil

debug =False
def get_abspath():
    return os.path.abspath(os.path.dirname(__file__))+"./../"


def gettimeformat():
    import time
    t =time.strftime("%Y%m%d%H%M", time.localtime())
    return t


class FileBak():

    def test_src_file(self,dirname):
        """
        目标文件夹遍历。去除.py和pyc
        :param dirname:
        :return:
        """
        dirname =get_abspath()+dirname
        print(dirname)
        l =list()
        if os.path.isdir(dirname): #判断是不是文件夹
            res =os.listdir(dirname)#遍历代码
            for i in range(len(res)):
                if(res[i].endswith(".py") and res[i]!="__init__.py"):#init没有意义
                    l.append(res[i])
            return l

    def get_src_file(self,dirname):
        """
        获得源文件地址文件夹
        :param dirname:
        :return:
        """
        dirname =get_abspath()+dirname
        filelist =list()
        if os.path.isdir(dirname):
            files =os.listdir(dirname)
            for i in range(len(files)):
                if files[i].endswith(".py") and files[i]!="__init__.py":
                    filelist.append(files[i])
            return filelist
        else:
            print("src_path isnot dir")

    def make_file(self,target_name):
        """
        创建备份文件夹
        :param target_name:
        :return:
        """
        if os.path.exists(target_name):
            print("正在进行创建")
        else:
            os.makedirs(target_name)
            print("已创建成功")

    def check_target_file(self,dirname):
        """
        end 获得备份文件
        :param dirname:
        :return:
        """
        dirname = get_abspath() + dirname
        filelist = list()
        if os.path.isdir(dirname):
            files = os.listdir(dirname)
            if len(files)>0:
                for i in range(len(files)):
                    if (files[i].endswith(".py") and files[i] != "__init__.py"):
                        filelist.append(files[i])
                return filelist
        else:
            print("target_dir is't dir")

    def get_file_md5(self,dirname):
        files = self.get_src_file(dirname)
        path = get_abspath() + dirname  # 拼接路径
        if not path.endswith('/'):
            path += "/"
        _hash = hashlib.md5()
        for i in range(len(files)):
            f = open(path + files[i], "rb")
            while True:
                byte =f.read(8096)
                if not byte:
                    break
                _hash.update(byte)
            f.close()
            return _hash.hexdigest()


    def get_md5(self,dirname,name): #+"target4\\"+
        """
        读取getmd5的函数
        :param dirname:
        :param name:
        :return:
        """
        f = open(get_abspath()+dirname+"\\"+name, "rb")
        _hash = hashlib.md5()
        while True:#字节拷贝
            byte = f.read(8096)
            if not byte:
                break
            _hash.update(byte)
        f.close()
        return _hash.hexdigest()

    def get_file_md5toDict(self,dirname):
        """
        获取文件的md5
        :param src_name:
        :return:字典格式
        """
        files = self.get_src_file(dirname)
        path =get_abspath()+dirname #拼接路径
        if not path.endswith('/'):
            path+="/"
        _hash = hashlib.md5()
        d =dict()
        for i in range(len(files)):
            f = open(path + files[i], "rb")
            if debug:print("当前文件是", files[i])
            while True:
                byte =f.read(8096)
                if not byte:
                    break
                _hash.update(byte)
                if debug:print(files[i]+":"+_hash.hexdigest()) #调式语句
                d[files[i]]=_hash.hexdigest()
            f.close()  # 文件最后关闭
        return d
        #{'settings.py': 'a3c57d5c0d4183ae95e5da80c923d7e7', 'urls.py': '3fb03141cb1ac78aabc877a7dea80761', 'wsgi.py': '37f1c1b1e5541979b51f08927c631d88'}


    def check_src_md5(self,srcname,targetname):
        """
        检查2个目录md5文件 做匹配
        :param srcname: 源目录
        :param targetname: 最终目录
        :return: 如果有需要拷贝的，则存在列表里
        """
        srclists =self.get_src_file(srcname) #过滤了.__init__.py
        targetlists =self.get_src_file(targetname)
        t =list()
        for i in range(len(targetlists)):
            srcmd5 =self.get_md5("product",srclists[i])
            #print(srclists[i])
            targetmd5 = self.get_md5("target4",targetlists[i])
            #print(targetlists[i])
            if srcmd5 == targetmd5:
                print("文件已存在,不用拷贝")
            else:
                t.append(srclists[i])
                print("文件需要拷贝",srclists[i])
        return t


    # def add_src_files(self,target_name,src_name):
    #     """
    #     转移文件
    #     :param target_name:
    #     :param src_name:
    #     :return:
    #     """
    #     target_files = self.get_src_file(target_name) #提前使用
    #     target_name = get_abspath() + target_name
    #     self.make_file(target_name)
    #     src_files =self.get_src_file(src_name) # 获取源目录文件列表及文件名
    #     src_name =get_abspath() + src_name
    #     for i in range(len(src_files)):
    #         for j in range(len(src_files)):
    #             res_target = os.path.join(target_name, src_files[i])
    #             res_src= os.path.join(src_name,src_files[j])
    #             shutil.copy(res_src,res_target)


    def copy_src_files(self,src_name,target_name):
        """
        遍历src_name目录后拷贝到targetname目录
        :param src_name:
        :param target_name:
        :return:
        """
        target_dir = get_abspath()+target_name
        src_dir = get_abspath()+src_name
        if os.path.isdir(src_dir) and os.path.isdir(target_dir):
            for root, dirs, files in os.walk(src_dir):
                for i in range(0,len(files)):
                    sf = os.path.join(root, files[i])
                    shutil.copy(sf, target_dir)
        else:
            print("检查文件路径")




fb =FileBak()
fb.check_src_md5("product","target4")
#fb.copy_src_files("product","target2")
#print(fb.test_src_file("autotest"))
# print(gettimeformat())
# print(fb.get_src_file("autotest"))
#print(fb.add_src_files("target4","autotest"))
#print(fb.get_file_md5("autotest"))
#print(fb.get_file_md5("target3"))

#print(fb.get_md5("product","admin.py"))