# -*- coding=utf-8 -*-

# Time      :  14:35

# Author    : dz

import pandas as pd

filePath = 'F:/ML5/ali/ccf_offline_stage1_train.csv'

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

    # 以Coupon_id为例，数据进行转换
    # coupon_id_new = []
    coupon_id_old = data_offline_train['Coupon_id']
    for coupon_id in coupon_id_old:
        if coupon_id == 'null':
            coupon_id_new.append(0)
        else:
            coupon_id_new.append(1)
    coupon_id_new = pd.Series(coupon_id_new)
    data_offline_train.insert(3,'coupon_id_new',coupon_id_new)
    print data_offline_train.head()

    """
     1、对Coupon_id数据进行转换：{null -> 0; 非空 -> 1}
     2、对Discount_rate数据进行转换：{转换成float，范围0到1；例如 200:20 -> 0.9}，空值转为1，表示没有折扣
     3、对Distance距离进行处理：距离大小为 0到10，分别表示小于500米，大于5公里；已有的数据不再处理，null值表示没有距离信息，转化为数值 5
     4、对优惠券接受日期进行处理，暂时只处理是否为空，空值转化为 0，其他暂不做处理
     5、新增结果列：
       负样本（0）：Date为空，Coupon_id不为空；
       正样本（1）：Date不为空，Coupon_id不为空；
       普通消费日期（2）：Date不为空，Coupon_id为空；
    """
    coupon_id_new = []
    Discount_rate_new = []
    Distance_new = []
    Date_received_new = []
    result_newCreate = []








if __name__ == '__main__':
    main()



