# 本项目为使用机器学习方式解决验证码问题（摸索过程）

## 摸索过程
* 识别的图片验证码为纯数字的验证码，而且相对简单，使用此方式可以处理【不适用】
* 通过使用分割图片的方式训练，也是不适用于此处验证码【不适用】
* 通过神经网络训练识别整个图片【应该是最适用】


## 过程说明：
1. 下载足够多的验证码图片(downPic.py)
2. 分析图片后，对图片进行裁剪，裁剪出单独的数字，因为每个验证码是4个数字组成，我的思路是把验证码切割成四个，然后逐一识别，这样的准确率应该比较高一些；这里值得一提的就是：切割图片的参数（通过PS可以看到相隔的像素值，然后可以推算出一个公式）、将图片二值化，把图片变成黑白图片、我们需要读取某个文件夹下的所有图片，然后保存下来。(cutPic.py)
3. 将裁剪出的数字进行分类，使用pytesseract无法识别出数字图片（也是醉了，全是手动分类的）(sortPic.py)
4. 提取特征值，批量将切割后并且已经分好类的图像，得到的图片进行二值化（0,1）处理，变成像素值，然后保存在TXT文件下；这里要注意的是保存的格式以及每一个图片的像素值后面要加上它的标签即是什么数字。为下一步的模型训练做准备。
4. 使用svm进行模型训练，使用sklearn中的SVM（支持向量机）对第四步得到的数据进行训练，SVM是有监督分类，通过调一些参数可以改善它的预测正确率，比如说核函数-rbf、poly、sigmoid、linear等；(svmPic.py)
5. 测试训练结果(CheckPic.py)

## 使用方式：
* 按照上述步骤顺序逐步运行对应的文件，根据结果适当处理


