print("=== 开始测试第八组结账系统 ===")

# 测试 1：验证有效用户、学生身份、支付宝
print("\n[测试 1] 正常流程：")
user1 = "student_007"
if verify_user_identity(user1):
    amount1 = calculate_final_total(200, "student")
    print(f"用户 {user1} 应付金额: {amount1} 元")
    result1 = process_payment("alipay", amount1)
    print(result1["message"])

# 测试 2：验证拦截未登录用户
print("\n[测试 2] 拦截非法用户：")
user2 = ""
if not verify_user_identity(user2):
    print("拦截成功：用户未登录！")

# 测试 3：验证拦截非法支付方式
print("\n[测试 3] 拦截非法支付方式：")
user3 = "user_123"
amount3 = calculate_final_total(50, "adult")
result3 = process_payment("bitcoin", amount3)
print(result3["message"])
