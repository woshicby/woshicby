import numpy
import operator
import matplotlib
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as p3d

# #####设置区域#####
sourceFilePath = r'D:\Desktop\新建文件夹\machinelearninginaction3x-master\Ch02\datingTestSet.txt'  # 训练数据源文件路径


# #####函数声明区域#####
def classify0(in_x, data_set, labels, k):  # k近邻分类器（对单个测试数据）
    data_set_size = data_set.shape[0]  # 若data_set为4行2列，data_set.shape[0]=4
    diff_mat = numpy.tile(in_x, (data_set_size, 1)) - data_set  # 矩阵求差
    sq_diff_mat = diff_mat ** 2  # 矩阵各项求平方
    sq_distances = sq_diff_mat.sum(axis=1)  # 平方和
    distances = sq_distances ** 0.5  # 开方得距离
    sorted_dist_indices = distances.argsort()  # 按距离大小排序，返回index
    class_count = {}  # 创建近邻字典
    # 开始抓k个近邻
    for j in range(k):
        vote_j_label = labels[sorted_dist_indices[j]]  # 取对应label
        class_count[vote_j_label] = class_count.get(vote_j_label, 0) + 1  # 对label对应计数+1，没有则置为零
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)  # 对class_count按第一维排序
    return sorted_class_count[0][0]  # 返回计数最多的label


def file2matrix(filename):  # 文件转矩阵
    love_dictionary = {'largeDoses': 3, 'smallDoses': 2, 'didntLike': 1}  # 字典型
    fr = open(filename)
    array_of_lines = fr.readlines()
    number_of_lines = len(array_of_lines)  # 获取文件行数
    return_mat = numpy.zeros((number_of_lines, 3))  # 创建返回的Numpy矩阵
    class_label_vector = []  # 准备返回的标签
    index = 0  # 初始化行数为0
    for line in array_of_lines:  # 逐行添加
        line = line.strip()
        list_from_line = line.split('\t')
        return_mat[index, :] = list_from_line[0:3]  # 前三列是三个特征值
        if list_from_line[-1].isdigit():  # isdigit() 方法检测字符串是否只由数字组成
            class_label_vector.append(int(list_from_line[-1]))
        else:
            class_label_vector.append(love_dictionary.get(list_from_line[-1]))
        index += 1  # 下一行
    return return_mat, class_label_vector


def auto_norm(data_set):  # 归一化
    min_vals = data_set.min(0)
    max_vals = data_set.max(0)
    ranges = max_vals - min_vals
    # norm_data_set = numpy.zeros(numpy.shape(data_set))  # 预设为全零（并没有用）
    data_set_num = data_set.shape[0]
    norm_data_set = data_set - numpy.tile(min_vals, (data_set_num, 1))  # 减去各项的最小值
    norm_data_set = norm_data_set / numpy.tile(ranges, (data_set_num, 1))  # 除以各项的极差
    return norm_data_set, ranges, min_vals


def draw2d(dating_data_mat, dating_labels, j, k):
    fig = matplotlib.pyplot.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dating_data_mat[:, j], dating_data_mat[:, k], 15.0 * numpy.array(dating_labels),
               15.0 * numpy.array(dating_labels))
    matplotlib.pyplot.show()


def draw3d(dating_data_mat, dating_labels):
    # 绘制散点图
    matplotlib.rcParams['font.family'] = matplotlib.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文支持，中文字体为简体黑体
    fig = matplotlib.pyplot.figure()
    ax = p3d.Axes3D(fig, auto_add_to_figure=False)
    fig.add_axes(ax)
    ax.scatter(dating_data_mat[:, 0], dating_data_mat[:, 1], dating_data_mat[:, 2], 15.0 * numpy.array(dating_labels),
               15.0 * numpy.array(dating_labels), 15.0 * numpy.array(dating_labels))
    '''
    # 绘制图例
    ax.legend(loc='best')
    '''
    # 添加坐标轴
    ax.set_xlabel('每年获得的飞行常客里程数', fontdict={'size': 10, 'color': 'red'})
    ax.set_ylabel('玩视频游戏所耗时间百分比', fontdict={'size': 10, 'color': 'red'})
    ax.set_zlabel('每年所消费的冰淇淋公升数', fontdict={'size': 10, 'color': 'red'})
    ax.set_title('三维点云图')
    matplotlib.pyplot.show()


# #####执行区域#####
ho_ratio = 0.50  # 设置测试数据占全部数据的比重
datingDataMat, datingLabels = file2matrix(sourceFilePath)  # 从sourceFilePath读取数据
print('约会数据矩阵为\n', datingDataMat, '\n约会标签矩阵为\n', datingLabels)
normMat, Ranges, minVals = auto_norm(datingDataMat)  # 归一化
print('各项极差为', Ranges, '\n各项最小值为', minVals, '\n归一化后的数据矩阵为\n', normMat, )
# draw3d(datingDataMat, datingLabels)
# draw2d(datingDataMat, datingLabels, 0, 1)
# draw2d(datingDataMat, datingLabels, 1, 2)
# draw2d(datingDataMat, datingLabels, 0, 2)
Num = normMat.shape[0]  # 获取数据条目数量
numTestVectors = int(Num * ho_ratio)  # 其中部分作为测试数据
errorCount = 0.0  # 重置错误计数
for i in range(numTestVectors):  # 开始测试
    classifierResult = classify0(normMat[i, :], normMat[numTestVectors:Num, :], datingLabels[numTestVectors:Num], 3)
    if classifierResult == datingLabels[i]:
        result = ',正确'
    else:
        errorCount += 1.0
        result = ',错误,当前错误数为：' + str(errorCount)
    print("分类器返回的值为:%d,正确答案为:%d" % (classifierResult, datingLabels[i]) + result)
print("总测试数为:" + str(numTestVectors))
print("总错误数为:" + str(errorCount))
print("总错误率为:%f" % (errorCount / float(numTestVectors)))
print("总错误数为:" + str(errorCount))
