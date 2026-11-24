# 定义支付处理函数，接收支付方式和支付金额
def process_payment(payment_method, amount):
    
    # 定义系统支持的支付方式列表（白名单）
    supported_methods = ["alipay", "wechat", "credit_card", "paypal"]
    
    # 校验支付方式：如果传入的方式不在白名单中
    if payment_method not in supported_methods:
        # 返回失败字典，提示不支持该方式，并直接退出函数
        return {
            "success": False,
            "message": f"支付失败：系统不支持 '{payment_method}' 支付方式。"
        }
    
    # 根据不同的支付方式，拼接不同的成功提示信息
    if payment_method == "alipay":
        msg = f"已跳转至支付宝，成功扣款 {amount} 元。"
    elif payment_method == "wechat":
        msg = f"微信支付成功，已扣款 {amount} 元。"
    elif payment_method == "credit_card":
        msg = f"信用卡验证通过，已扣款 {amount} 元。"
    else:
        msg = f"PayPal 支付成功，已扣款 {amount} 元。"

    # 支付成功，返回包含 True 和 成功信息的字典
    return {"success": True, "message": msg}
