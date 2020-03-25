import os

f = open("/path/按照要求命名 train.txt 或者 test.txt", "w")#【改】*生成数据所保存的路径和名字
f_t=[]
for root_txt,dirs_txt,files_txt in os.walk("/datasets/test/gt"):#【改】*图像的数据路径
    for i in range(len(files_txt)):
        f_t.append(files_txt[i][:-3])
for root_img, dirs_img, files_img in os.walk("/datasets/test/img",topdown=True):#【改】*图像本身路径
    for img_name in  files_img:
        if img_name[-3:]=="jpg":
            if img_name[:-3] in f_t:
                f.write("./datasets/train/img/"+img_name+"	./datasets/train/gt/"+img_name[:-3]+"txt"+"\n")
            else:
                continue
        else:
            continue
f.close()
