# 差分二值化（DB）文本检测代码使用说明
[本文代码主要来自](https://github.com/WenmuZhou/DBNet.pytorch)

## 环境要求

* pytorch 1.4+
* torchvision 0.5+
* gcc 4.9+

# 使用说明

## 下载步骤

**依次执行以下命令** 
1. mkdir DB
2. cd DB/
3. git init
4. git clone https://github.com/WenmuZhou/DBNet.pytorch.git

## 数据准备工作

将训练的图片导入`./DBNet.pytorch/datasets/train/img `中
将训练的图片数据导入`./DBNet.pytorch/datasets/train/gt `中
将测试的图片导入`./DBNet.pytorch/datasets/test/img `中
将测试的图片数据导入`./DBNet.pytorch/datasets/test/gt `中

```
- 图片要求用`.jpg`格式
- 图片数据要求用`.txt`格式，其内部格式要求如下：
`x1, y1, x2, y2, x3, y3, x4, y4, 文字内容`
```

**设置`train.txt`数据**

打开`my_standard output.py`文件，按照注释更改路径
用命令窗口运行 `. my_standard output.py`
生成名为 `train.txt`的文件，再将其移动到 `dataset`中


**设置`test.txt`数据**

打开`my_standard output.py`文件，按照注释更改路径
用命令窗口运行 `. my_standard output.py`
生成名为 `test.txt`的文件，再将其移动到 `dataset`中

## 训练

1. 在配置文件[config/icdar2015_resnet18_fpn_DBhead_polyLR.yaml](cconfig/icdar2015_resnet18_fpn_DBhead_polyLR.yaml)中对以下两个路径进行设置
	1. `dataset['train']['dataset'['data_path']'`----上一步`train.txt`的路径
	2. `dataset['validate']['dataset'['data_path']`--------上一步`test.txt`的路径

2. 在DBNet.pytorch文件夹下用命令窗口执行 `bash singlel_gpu_train.sh`
* 生成的model在` /DBNet.pytorch/output/DBNet_resnet18_FPN_DBHead/checkpoint/`里

## 测试

1. 在[eval.sh]最后的`''`中输入model的路径(有两个，选一个就行）
2. 在DBNet.pytorch文件夹下用命令窗口执行 `bash eval.sh`



**If this repository helps you，please star it. Thanks.**
