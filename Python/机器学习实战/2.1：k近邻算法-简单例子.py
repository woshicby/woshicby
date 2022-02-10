import numpy
import operator


def classify0(in_x, data_set, labels, k):  # k近邻分类器（对单个测试数据）
    data_set_size = data_set.shape[0]  # 4行2列，data_set_size=4
    diff_mat = numpy.tile(in_x, (data_set_size, 1)) - data_set  # 矩阵求差
    sq_diff_mat = diff_mat ** 2  # 矩阵各项求平方
    sq_distances = sq_diff_mat.sum(axis=1)  # 平方和
    distances = sq_distances ** 0.5  # 开方得距离
    sorted_dist_indices = distances.argsort()  # 按距离大小排序，返回index
    class_count = {}  # 创建近邻字典
    # 开始抓k个近邻
    for i in range(k):
        vote_i_label = labels[sorted_dist_indices[i]]  # 取对应label
        class_count[vote_i_label] = class_count.get(vote_i_label, 0) + 1  # 对label对应计数+1，没有则置为零
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)  # 对class_count按第一维排序
    return sorted_class_count[0][0]  # 返回计数最多的label


def create_data_set():  # 创建并返回数据集和标签
    group = numpy.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    print('测试数据集为：\n', group)
    print('对应的测试标签为：\n', labels)
    return group, labels


Group, Labels = create_data_set()
print('k近邻算法（k=3）对[0, 0]得出的结果为:', classify0([0, 0], Group, Labels, 3))
print('k近邻算法（k=3）对[0.1, 0.1]得出的结果为:', classify0([0.1, 0.1], Group, Labels, 3))
print('k近邻算法（k=3）对[0.2, 0.2]得出的结果为:', classify0([0.2, 0.2], Group, Labels, 3))
print('k近邻算法（k=3）对[0.3, 0.3]得出的结果为:', classify0([0.3, 0.3], Group, Labels, 3))
print('k近邻算法（k=3）对[0.4, 0.4]得出的结果为:', classify0([0.4, 0.4], Group, Labels, 3))
print('k近邻算法（k=3）对[0.5, 0.5]得出的结果为:', classify0([0.5, 0.5], Group, Labels, 3))
print('k近邻算法（k=3）对[0.6, 0.6]得出的结果为:', classify0([0.6, 0.6], Group, Labels, 3))
print('k近邻算法（k=3）对[0.7, 0.7]得出的结果为:', classify0([0.7, 0.7], Group, Labels, 3))
print('k近邻算法（k=3）对[0.8, 0.8]得出的结果为:', classify0([0.8, 0.8], Group, Labels, 3))
print('k近邻算法（k=3）对[0.9, 0.9]得出的结果为:', classify0([0.9, 0.9], Group, Labels, 3))
print('k近邻算法（k=3）对[1, 1]得出的结果为:', classify0([1, 1], Group, Labels, 3))
