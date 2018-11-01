# -*- coding: utf-8 -*-

# # 买入价格
# priceIn = 11.19
# # 卖出价格
# priceOut = 11.22
# # 数量
# count = 2200

brokerage = 0.00025


def calc_shanghai_a(price_in, price_out, num):
    total_price_in = price_in * num
    total_price_out = price_out * num
    origin_return = total_price_out - total_price_in
    print "除税挣了:" + str(origin_return)
    final_return = origin_return - total_price_out * 0.001 - transfer_fee(total_price_in) - transfer_fee(
        total_price_out) - trade_fee(num) * 2
    print "扣税后挣了" + str(final_return)


# 交易佣金
def transfer_fee(price):
    return price * brokerage if price * brokerage > 5 else 5


# 过户费
def trade_fee(num):
    return 1 if num < 1000 else num * 0.001


if __name__ == '__main__':
    priceIn = float(input("输入买入价格："))
    priceOut = float(input("输入卖出价格："))
    count = int(input("输入数量:"))
    brokerage = float(input("佣金比例：")/10000)
    calc_shanghai_a(priceIn, priceOut, count)
