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

    # 对Coupon_id的数据进行转换
    coupon_id_new = []
    coupon_id_old = data_offline_train['Coupon_id']
    for coupon_id in coupon_id_old:
        if coupon_id == 'null':
            coupon_id_new.append(0)
        else:
            coupon_id_new.append(1)
    coupon_id_new = pd.Series(coupon_id_new)
    data_offline_train.insert(3,'coupon_id_new',coupon_id_new)
    print data_offline_train.head()

    # 对Coupon_id数据进行转换：{null -> 0; 非空 -> 1}
    # 对Discount_rate数据进行转换：{转换成float，范围0到1；例如 200:20 -> 0.9}
    # 新增结果列









if __name__ == '__main__':
    main()



