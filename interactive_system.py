def run_interactive_system():
    print("========================================")
    print("   欢迎使用第八组结账及账号管理系统   ")
    print("========================================")
    
    while True:
        print("\n【主菜单】")
        print("1. 🛒 进行新结账")
        print("2. 📊 查看历史订单")
        print("3. 🗑️ 删除历史订单")
        print("4. 📝 注册新账号")
        print("5. 👥 查看所有账号")
        print("6. ❌ 删除账号")
        print("0. 🚪 退出系统")
        
        choice = input("请输入选项数字: ").strip()
        
        if choice == "0":
            print("系统已退出，再见！")
            break
            
        elif choice == "1":
            print("\n--- 🛒 结账流程 ---")
            uid = input("请输入您的账号ID: ").strip()
            
            # 使用你原来的验证函数
            if not verify_user_identity(uid):
                print("❌ 拦截：账号为空！")
                continue
                
            # 判断账号是否在系统中注册过
            if uid not in user_database:
                print("❌ 错误：该账号不存在，请先在菜单选择 4 进行注册！")
                continue
                
            # 自动获取账号身份
            identity = user_database[uid]
            print(f"✅ 欢迎回来，{uid} (身份: {identity})")
                
            try:
                total = float(input("请输入商品原价: "))
            except ValueError:
                print("❌ 错误：金额格式不正确！")
                continue
                
            payment_method = input("支付方式(alipay/wechat/bitcoin): ").strip().lower() or "alipay"
            
            # 调用原核心计算与支付
            final_amount = calculate_final_total(total, identity)
            result = process_payment(payment_method, final_amount)
            
            print(f"\n[结果] 实付金额: {final_amount} 元")
            print(result["message"])
            
            if result["success"]:
                save_order(uid, total, final_amount, payment_method)
                print("💾 订单已成功存入系统！")
                
        elif choice == "2":
            view_orders()
        elif choice == "3":
            delete_order()
        elif choice == "4":
            register_account()
        elif choice == "5":
            view_accounts()
        elif choice == "6":
            delete_account()
        else:
            print("❌ 无效输入，请重新选择。")
