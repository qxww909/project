# 定义结账主函数，接收原价、顾客类型（默认成人）、优惠券（默认0）
def calculate_final_total(total, customer_type="adult", coupon_amount=0):
    
    # 金额合法性校验：如果原价小于或等于0，直接返回0.0，防止抛出异常或出现负数
    if total <= 0:
        return 0.0

    # 初始化折扣率为0（默认无折扣）
    discount_rate = 0.0
    # 判断顾客身份并赋予对应折扣
    if customer_type == "student":
        discount_rate = 0.10  # 学生打9折
    elif customer_type == "child":
        discount_rate = 0.20  # 儿童打8折
    elif customer_type == "senior":
        discount_rate = 0.15  # 老年人打85折
        
    # 计算折后金额：原价 * (1 - 折扣率)
    discounted_total = total * (1 - discount_rate)

    # 如果使用了优惠券，在折后金额基础上减去优惠券金额
    if coupon_amount > 0:
        discounted_total -= coupon_amount

    # 极值保护：确保减去优惠券后，金额不会变成负数（最低为0）
    if discounted_total < 0:
        discounted_total = 0

    # 初始化运费为0
    shipping_fee = 0.0
    # 满额包邮逻辑：折后金额大于0且不满99元时，收取10元运费
    if 0 < discounted_total < 99:
        shipping_fee = 10.0

    # 计算最终总价：折后金额 + 运费
    final_total = discounted_total + shipping_fee
    # 四舍五入保留两位小数并返回
    return round(final_total, 2)
