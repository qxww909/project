# 模拟账号数据库 (使用字典结构，格式为: { "账号ID": "身份类型" })
user_database = {} 

# 模拟订单数据库 (使用列表结构，用于存储每一笔成功的订单)
order_database = []

# --- 账号管理功能 ---
def register_account():
    """功能：注册新账号，并绑定身份类型"""
    print("\n--- 📝 注册新账号 ---")
    uid = input("请输入新账号ID: ").strip()
    
    # 拦截空账号
    if not uid:
        print("❌ 账号不能为空！")
        return
    # 拦截已存在的账号
    if uid in user_database:
        print("❌ 该账号已存在！")
        return
    
    # 获取身份，如果输入错误，默认视为成人(adult)
    identity = input("请输入身份(student/child/senior/adult): ").strip().lower()
    if identity not in ["student", "child", "senior", "adult"]:
        identity = "adult"
        
    # 将账号和身份存入字典
    user_database[uid] = identity
    print(f"✅ 账号 {uid} 注册成功！身份: {identity}")

def view_accounts():
    """功能：查看系统中已注册的所有账号"""
    print("\n--- 👥 账号列表 ---")
    if not user_database:
        print("暂无注册账号。")
        return
    # 遍历字典并打印
    for uid, identity in user_database.items():
        print(f"👤 账号: {uid} | 身份: {identity}")

def delete_account():
    """功能：从系统中删除指定的账号"""
    print("\n--- 🗑️ 删除账号 ---")
    uid = input("请输入要删除的账号ID: ").strip()
    if uid in user_database:
        del user_database[uid] # 从字典中移除该键值对
        print(f"✅ 账号 {uid} 已删除！")
    else:
        print("❌ 账号不存在。")

# --- 订单管理功能 ---
def save_order(user_id, total, final_amount, method):
    """功能：将支付成功的订单数据打包并存入列表"""
    # 将订单信息组装成字典
    order = {"user_id": user_id, "total": total, "final_amount": final_amount, "method": method}
    order_database.append(order) # 追加到订单列表

def view_orders():
    """功能：查看系统存储的所有历史订单"""
    print("\n--- 📊 历史订单列表 ---")
    if not order_database:
        print("暂无订单记录。")
        return
    # 使用 enumerate 自动生成序号 (从1开始)
    for index, order in enumerate(order_database, start=1):
        print(f"[{index}] 账号: {order['user_id']} | 实付: {order['final_amount']}元 | 方式: {order['method']}")

def delete_order():
    """功能：删除指定的历史订单"""
    view_orders() # 先展示现有订单方便用户选择
    if not order_database:
        return
    try:
        idx = int(input("请输入要删除的订单编号 (如 1): "))
        # 检查输入的编号是否在合理范围内
        if 0 < idx <= len(order_database):
            removed = order_database.pop(idx - 1) # 根据索引删除并获取被删元素
            print(f"✅ 成功删除账号 {removed['user_id']} 的订单。")
        else:
            print("❌ 编号不存在。")
    except ValueError:
        print("❌ 输入错误，请输入数字。")
