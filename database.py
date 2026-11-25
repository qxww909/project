# 模拟账号数据库 (字典结构: { "账号ID": "身份类型" })
user_database = {} 

# 模拟订单数据库 (列表结构)
order_database = []

# --- 账号管理功能 ---
def register_account():
    print("\n--- 📝 注册新账号 ---")
    uid = input("请输入新账号ID: ").strip()
    if not uid:
        print("❌ 账号不能为空！")
        return
    if uid in user_database:
        print("❌ 该账号已存在！")
        return
    
    identity = input("请输入身份(student/child/senior/adult): ").strip().lower()
    if identity not in ["student", "child", "senior", "adult"]:
        identity = "adult"
        
    user_database[uid] = identity
    print(f"✅ 账号 {uid} 注册成功！身份: {identity}")

def view_accounts():
    print("\n--- 👥 账号列表 ---")
    if not user_database:
        print("暂无注册账号。")
        return
    for uid, identity in user_database.items():
        print(f"👤 账号: {uid} | 身份: {identity}")

def delete_account():
    print("\n--- 🗑️ 删除账号 ---")
    uid = input("请输入要删除的账号ID: ").strip()
    if uid in user_database:
        del user_database[uid]
        print(f"✅ 账号 {uid} 已删除！")
    else:
        print("❌ 账号不存在。")

# --- 订单管理功能 ---
def save_order(user_id, total, final_amount, method):
    order = {"user_id": user_id, "total": total, "final_amount": final_amount, "method": method}
    order_database.append(order)

def view_orders():
    print("\n--- 📊 历史订单列表 ---")
    if not order_database:
        print("暂无订单记录。")
        return
    for index, order in enumerate(order_database, start=1):
        print(f"[{index}] 账号: {order['user_id']} | 实付: {order['final_amount']}元 | 方式: {order['method']}")
def delete_order():
    view_orders()
    if not order_database:
        return
    try:
        idx = int(input("请输入要删除的订单编号 (如 1): "))
        if 0 < idx <= len(order_database):
            removed = order_database.pop(idx - 1)
            print(f"✅ 成功删除账号 {removed['user_id']} 的订单。")
        else:
            print("❌ 编号不存在。")
    except ValueError:
        print("❌ 输入错误，请输入数字。")

