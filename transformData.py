# -*- coding=utf-8 -*-

# Time      :  14:35

# Author    : dz

import pandas as pd

filePath = 'F:/ML5/ali/ccf_offline_stage1_train.csv'


# 数据预处理
def handle_data(data_offline_train):

    """
     1、对Coupon_id数据进行转换：{null -> 0; 非空 -> 1}
     2、对Discount_rate数据进行转换：{转换成float，范围0到1；例如 200:20 -> 0.9}，空值转为1，表示没有折扣; {若形式为float，保持不变，例如:0.9->0.9}
     3、对Distance距离进行处理：距离大小为 0到10，0、10分别表示小于500米，大于5公里；已有的数据0为方便计算转为0.1 ；null值表示没有距离信息，默认为中间距离5，其余不变
     4、对优惠券接受日期进行处理，暂时只处理是否为空，空值转化为 0，其他暂不做处理
     5、新增结果列：
       负样本（0）：Date为空，Coupon_id不为空；
       正样本（1）：Date不为空，Coupon_id不为空；
       普通消费日期（2）：Date不为空，Coupon_id为空；
    """
    Coupon_id_new = []
    Discount_rate_new = []
    Distance_new = []
    Date_received_new = []
    result_newCreate = []
    # i = 0 # 控制输出次数
    for index, row in data_offline_train.iterrows():
        # i = i+1
        # 处理Coupon_id数据
        if row['Coupon_id'] == 'null':
            Coupon_id_new.append(0)
        else:
            Coupon_id_new.append(1)

        # 处理Discount_rate数据
        if row['Discount_rate'] == 'null':
            Discount_rate_new.append(1)
        elif ':' in row['Discount_rate']:
            rate_list = (row['Discount_rate']).split(':')
            # print rate_list
            rate_num = float(rate_list[1]) / float(rate_list[0])
            Discount_rate_new.append(1 - rate_num)
        else:
            Discount_rate_new.append(float(row['Discount_rate']))

        # 处理Distance数据
        if row['Distance'] == 'null':
            Distance_new.append(5)
        elif row['Distance'] == '0':
            Distance_new.append(0.1)
        else:
            Distance_new.append(float(row['Distance']))

        # 处理Date_received数据
        if row['Date_received'] == 'null':
            Date_received_new.append(0)
        else:
            Date_received_new.append(row['Date_received'])

        # 新增结果列
        if row['Date'] == 'null' and row['Coupon_id'] != 'null':
            result_newCreate.append(0)
        elif row['Date'] != 'null' and row['Coupon_id'] != 'null':
            result_newCreate.append(1)
        elif row['Date'] != 'null' and row['Coupon_id'] == 'null':
            result_newCreate.append(2)

    Coupon_id_new_series = pd.Series(Coupon_id_new)
    Discount_rate_new_series = pd.Series(Discount_rate_new)
    Distance_new_series = pd.Series(Distance_new)
    Date_received_new_series = pd.Series(Date_received_new)
    result_newCreate_series = pd.Series(result_newCreate)

    return Coupon_id_new_series, Discount_rate_new_series, Distance_new_series, Date_received_new_series, result_newCreate_series


def main():

    """
        数据预处理：

    """
    # 数据加载
    data_offline_train = pd.read_csv(filePath)
    print data_offline_train.head()             #数据预览
    print '\n'

    print data_offline_train.columns            #列标
    print '\n'

    Coupon_id_new, Discount_rate_new, Distance_new, Date_received_new, result_newCreate = handle_data(data_offline_train)

    data_offline_train_new = data_offline_train
    data_offline_train_new.insert(3, 'Coupon_id_new', Coupon_id_new)
    data_offline_train_new.insert(5, 'Discount_rate_new', Discount_rate_new)
    data_offline_train_new.insert(7, 'Distance_new', Distance_new)
    data_offline_train_new.insert(9, 'Date_received_new', Date_received_new)
    data_offline_train_new.insert(11, 'result_newCreate', result_newCreate)


    print data_offline_train_new.head()
    with open('F:/ML5/ali/new_ccf_offline_stage1_train.csv', 'w') as file:
        data_offline_train_new.to_csv(file, sep=',', header=True, index=False)


if __name__ == '__main__':
    main()



