import gradio as gr

# 按元素分类的角色列表
characters_by_element = {
    "火": ["玛薇卡", "仆人", "宵宫", "胡桃", "可莉", "迪卢克", "林尼", "艾梅莉埃", "香菱", "班尼特", "安柏", "辛焱", "烟绯", "托马", "嘉明", "夏沃蕾"],
    "水": ["那维莱特", "芙宁娜", "夜兰", "珊瑚宫心海", "神里绫人", "达达利亚", "莫娜", "妮露", "行秋", "芭芭拉", "坎蒂丝", "希格雯", "爱可菲", "伊涅芙"],
    "风": ["枫原万叶", "魈", "温迪", "流浪者", "闲云", "琴", "砂糖", "鹿野院平藏", "琳妮特", "珐露珊", "早柚", "蓝砚"],
    "雷": ["雷电将军", "八重神子", "赛诺", "刻晴", "克洛琳德", "菲谢尔", "久岐忍", "北斗", "丽莎", "雷泽", "九条裟罗", "多莉", "赛索斯", "欧洛伦", "瓦雷莎"],
    "草": ["纳西妲", "提纳里", "艾尔海森", "基尼奇", "艾梅莉埃", "白术", "绮良良", "卡维", "柯莱", "瑶瑶", "旅行者(草)"],
    "冰": ["丝柯克", "莱欧斯利", "神里绫华", "甘雨", "优菈", "申鹤", "七七", "埃洛伊", "迪奥娜", "罗莎莉亚", "菲米尼", "夏洛蒂", "茜特菈莉", "莱依拉", "重云", "米卡", "爱诺"],
    "岩": ["钟离", "娜维娅", "千织", "荒泷一斗", "阿贝多", "五郎", "云堇", "诺艾尔", "凝光", "卡齐娜", "希诺宁"]
}

# 所有角色列表（用于匹配）
all_characters = []
for chars in characters_by_element.values():
    all_characters.extend(chars)
all_characters.sort()

# 角色技能序列
skill_sequences = {
    "茜特菈莉": "e,attack(0.2),keypress(q),wait(0.2),keypress(q),attack(0.2),keypress(q),attack(0.2),keypress(e)",
    "钟离": "s(0.2), e(hold), wait(0.2), w(0.2),keypress(q),wait(0.2),keypress(q),attack(0.1)",
    "纳西妲": "e(hold),click(middle),keypress(q),wait(0.3),keypress(q),attack(0.3),keypress(q),attack(0.2)",
    "夜兰": "attack(0.5),e,e,wait(0.8),e,e,wait(1.5),q",
    "枫原万叶": "attack(0.08),keypress(q),wait(0.3),keypress(q),wait(0.3),attack(0.2),e,wait(0.48),attack(0.3)",
    "芙宁娜": "e,attack(0.85), keypress(e), keypress(Q), attack(0.2)",
    "那维莱特": "attack(0.05),click(middle),e,wait(0.15),keydown(VK_LBUTTON),wait(0.27),keyup(VK_LBUTTON)",
    "丝柯克": "attack(0.2),click(middle),keypress(q),wait(0.05),keypress(q),attack(0.05),click(middle),keydown(E),wait(0.22),attack(0.08),click(middle),keyup(E),keypress(q),wait(0.08),keypress(q)",
    "雷电将军": "e,attack(0.22),keypress(q),wait(0.1),keypress(q),attack(0.2),keypress(q),attack(0.2)",
    "香菱": "e,wait(0.3),keypress(q),attack(0.2),keypress(q),wait(0.2),keypress(q),attack(0.2)",
    "班尼特": "e,q",
    "行秋": "e,e,q",
    "久岐忍": "e,wait(0.2),keypress(q),attack(0.15),keypress(q),e",
    "珊瑚宫心海": "e",
    "白术": "e,attack(0.2)",
    "菲谢尔": "e",
    "砂糖": "e,attack(0.2),keypress(q),attack(0.2),keypress(q),e,attack(0.2)",
    "琴": "attack(0.21),e,wait(0.14),attack(0.12),keypress(q),attack(0.11),keypress(q),attack",
    "娜维娅": "keypress(q),attack(0.1),keypress(q),attack(0.1),keypress(q),attack(0.1),keypress(q),e,wait(0.8),attack(1.6)"
}


def build_team(role1, role2, role3, role4):
    """生成配队方案"""
    team = [c for c in [role1, role2, role3, role4] if c]
    if len(team) != len(set(team)):
        return "⚠️ 错误：队伍中存在重复角色！"

    output_lines = [f"{char} {skill_sequences[char]}" for char in team if char in skill_sequences]
    output_text = "\n".join(output_lines)

    if output_text:
        filename = "".join([c[0] for c in team]) + ".txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(output_text)

    return output_text


def save_strategy(character, strategy, filename):
    """保存策略到文件"""
    if not character or not strategy:
        return "⚠️ 错误：角色和策略不能为空！"
    if not filename.endswith(".txt"):
        filename += ".txt"
    
    # 清理中文标点
    character = clean_punctuation(character)
    strategy = clean_punctuation(strategy)
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"{character} {strategy}")
    return f"✅ 策略已保存到 {filename}"


def add_character(character, strategy):
    """添加角色名到新行"""
    print(f"\n[add_character] 输入: character='{character}', strategy='{strategy}'")
    if not character:
        print("[add_character] 角色为空，返回原策略")
        return strategy
    result = (strategy.rstrip() + f"\n{character} ") if strategy else f"{character} "
    print(f"[add_character] 输出: '{result}'")
    return result


def clean_punctuation(text):
    """清理中文标点，转换为英文标点"""
    if not text:
        return text
    # 中文标点转英文标点
    text = text.replace('，', ',').replace('（', '(').replace('）', ')')
    text = text.replace('。', '.').replace('；', ';').replace('：', ':')
    text = text.replace('"', '"').replace('"', '"').replace('\'', '\'')
    text = text.replace('【', '[').replace('】', ']').replace('、', ',')
    return text


def add_command(strategy, command):
    """添加命令到策略"""
    # 清理命令中的中文标点
    command = clean_punctuation(command)
    
    print(f"\n[add_command] 输入: strategy='{strategy}', command='{command}'")
    if not strategy:
        print(f"[add_command] 策略为空，直接返回命令: '{command}'")
        return command

    # 清理策略中的中文标点
    strategy = clean_punctuation(strategy)
    
    # 只移除首尾换行符，保留空格
    strategy_clean = strategy.strip('\n')
    lines = strategy_clean.split('\n') if strategy_clean else []
    if not lines:
        print(f"[add_command] 清理后策略为空，返回命令: '{command}'")
        return command

    # 只移除换行符，不移除空格
    last_line = lines[-1].rstrip('\n')
    print(f"[add_command] 最后一行: '{last_line}'")

    # 按角色名长度降序排序，优先匹配最长的角色名
    sorted_characters = sorted(all_characters, key=len, reverse=True)

    # 检查最后一行是否以角色名开头（角色名+空格）
    for char in sorted_characters:
        prefix = f"{char} "
        if last_line.startswith(prefix):
            # 获取角色名后的内容并清理
            content = last_line[len(prefix):].strip()
            print(f"[add_command] 匹配到角色: '{char}', prefix='{prefix}', content='{content}'")
            # 如果内容为空，直接添加命令，不加逗号
            if content:
                lines[-1] = prefix + content + "," + command
                print(f"[add_command] 内容非空，添加逗号分隔: '{lines[-1]}'")
            else:
                lines[-1] = prefix + command
                print(f"[add_command] 内容为空，直接添加命令: '{lines[-1]}'")
            result = '\n'.join(lines)
            print(f"[add_command] 输出: '{result}'")
            return result

    # 没有角色名前缀的情况
    print(f"[add_command] 未匹配到角色名前缀")
    if last_line:
        lines[-1] = last_line + "," + command
        print(f"[add_command] 最后一行非空，添加逗号: '{lines[-1]}'")
    else:
        lines[-1] = command
        print(f"[add_command] 最后一行为空，直接添加命令: '{lines[-1]}'")
    result = '\n'.join(lines)
    print(f"[add_command] 输出: '{result}'")
    return result


# 创建界面
with gr.Blocks(title="原神配队工具") as demo:
    gr.Markdown("# 🎮 原神配队工具")

    with gr.Tabs():
        with gr.TabItem("快速配队"):
            with gr.Row():
                with gr.Column():
                    roles = [gr.Dropdown(all_characters, label=f"角色{i+1}", value=["钟离", "纳西妲", "夜兰", "枫原万叶"][i]) for i in range(4)]
                    generate_btn = gr.Button("生成配队方案", variant="primary")
                with gr.Column():
                    output = gr.Textbox(label="配队方案", lines=20)
            generate_btn.click(build_team, inputs=roles, outputs=output)

        with gr.TabItem("自定义战斗策略"):
            with gr.Row():
                with gr.Column(scale=2, min_width=400):
                    # 元素选择和角色选择
                    element = gr.Dropdown(list(characters_by_element.keys()), label="元素", value="火")
                    character = gr.Dropdown(characters_by_element["火"], label="角色")
                    strategy = gr.Textbox(label="策略", lines=15, placeholder="输入战斗策略...", visible=False)

                    with gr.Row():
                        add_char_btn = gr.Button("添加角色", variant="primary")
                        clear_btn = gr.Button("清空")

                    gr.Markdown("战斗命令")
                    
                    # 基础命令 - 默认展开（文档中的标准语法）
                    with gr.Accordion("⚔️ 基础命令", open=True):
                        with gr.Row():
                            e_btn = gr.Button("e")
                            e_hold_btn = gr.Button("e(hold)")
                            q_btn = gr.Button("q")
                        with gr.Row():
                            j_btn = gr.Button("j")
                            ready_btn = gr.Button("ready")
                        with gr.Row():
                            attack_dur = gr.Textbox(label="时间", value="0.2", container=False)
                            attack_btn = gr.Button("attack")
                        with gr.Row():
                            charge_dur = gr.Textbox(label="时间", value="0.5", container=False)
                            charge_btn = gr.Button("charge")
                        with gr.Row():
                            wait_time = gr.Textbox(label="时间", value="0.2", container=False)
                            wait_btn = gr.Button("wait")
                        with gr.Row():
                            dash_dur = gr.Textbox(label="时间", value="0.1", container=False)
                            dash_btn = gr.Button("dash")
                        with gr.Row():
                            walk_time = gr.Textbox(label="时间", value="0.2", container=False)
                        with gr.Row():
                            w_btn = gr.Button("w")
                            a_btn = gr.Button("a")
                            s_btn = gr.Button("s")
                            d_btn = gr.Button("d")
                    
                    # 高级语法 - 默认折叠（文档中的键鼠操作）
                    with gr.Accordion("🔧 高级语法", open=False):
                        with gr.Row():
                            keypress_q_btn = gr.Button("keypress(q)")
                            keypress_e_btn = gr.Button("keypress(e)")
                        with gr.Row():
                            keydown_e_btn = gr.Button("keydown(E)")
                            keyup_e_btn = gr.Button("keyup(E)")
                        with gr.Row():
                            keydown_w_btn = gr.Button("keydown(W)")
                            keyup_w_btn = gr.Button("keyup(W)")
                        with gr.Row():
                            keydown_s_btn = gr.Button("keydown(S)")
                            keyup_s_btn = gr.Button("keyup(S)")
                        with gr.Row():
                            keydown_a_btn = gr.Button("keydown(A)")
                            keyup_a_btn = gr.Button("keyup(A)")
                        with gr.Row():
                            keydown_lbtn = gr.Button("keydown(VK_LBUTTON)")
                            keyup_lbtn = gr.Button("keyup(VK_LBUTTON)")
                        with gr.Row():
                            keydown_rbtn = gr.Button("keydown(VK_RBUTTON)")
                            keyup_rbtn = gr.Button("keyup(VK_RBUTTON)")
                        with gr.Row():
                            moveby_x = gr.Textbox(label="X", value="1800", container=False)
                            moveby_y = gr.Textbox(label="Y", value="0", container=False)
                            moveby_btn = gr.Button("moveby")
                        with gr.Row():
                            click_middle_btn = gr.Button("click(middle)")

                with gr.Column(scale=3, min_width=500):
                    strategy_display = gr.Textbox(label="策略", lines=15, placeholder="输入战斗策略...")
                    with gr.Row():
                        filename = gr.Textbox(label="文件名", value="strategy.txt", container=False)
                        save_btn = gr.Button("保存", variant="primary")
                    save_output = gr.Textbox(label="结果", lines=1)
                    
                    # 按键介绍
                    with gr.Accordion("📖 按键说明", open=False):
                        gr.Markdown("""
                        **基础命令：**
                        - `e` - 元素战技（短按）
                        - `e(hold)` - 元素战技（长按）
                        - `q` - 元素爆发
                        - `j` - 跳跃
                        - `ready` - 准备就绪（等待大招动画）
                        - `attack(时间)` - 普通攻击，持续指定秒数
                        - `charge(时间)` - 重击，持续指定秒数
                        - `wait(时间)` - 等待指定秒数
                        - `dash(时间)` - 冲刺，持续指定秒数
                        - `w/a/s/d(时间)` - 向指定方向行走
                        
                        **高级语法：**
                        - `keypress(q/e)` - 按下并释放指定按键
                        - `keydown/keyup(E/W/S/A)` - 按下/释放指定按键
                        - `keydown/keyup(VK_LBUTTON)` - 鼠标左键按下/释放
                        - `keydown/keyup(VK_RBUTTON)` - 鼠标右键按下/释放
                        - `moveby(X,Y)` - 鼠标移动指定像素
                        - `click(middle)` - 鼠标中键点击
                        """)

            # 事件绑定
            add_char_btn.click(add_character, inputs=[character, strategy_display], outputs=strategy_display)
            clear_btn.click(lambda: "", outputs=strategy_display)

            # 基础技能
            e_btn.click(lambda s: add_command(s, "e"), inputs=strategy_display, outputs=strategy_display)
            e_hold_btn.click(lambda s: add_command(s, "e(hold)"), inputs=strategy_display, outputs=strategy_display)
            q_btn.click(lambda s: add_command(s, "q"), inputs=strategy_display, outputs=strategy_display)
            j_btn.click(lambda s: add_command(s, "j"), inputs=strategy_display, outputs=strategy_display)
            ready_btn.click(lambda s: add_command(s, "ready"), inputs=strategy_display, outputs=strategy_display)
            click_middle_btn.click(lambda s: add_command(s, "click(middle)"), inputs=strategy_display, outputs=strategy_display)
            
            # 攻击相关
            attack_btn.click(lambda s, d: add_command(s, f"attack({d})"), inputs=[strategy_display, attack_dur], outputs=strategy_display)
            charge_btn.click(lambda s, d: add_command(s, f"charge({d})"), inputs=[strategy_display, charge_dur], outputs=strategy_display)
            
            # 等待和冲刺
            wait_btn.click(lambda s, t: add_command(s, f"wait({t})"), inputs=[strategy_display, wait_time], outputs=strategy_display)
            dash_btn.click(lambda s, d: add_command(s, f"dash({d})"), inputs=[strategy_display, dash_dur], outputs=strategy_display)
            
            # 方向行走
            w_btn.click(lambda s, t: add_command(s, f"w({t})"), inputs=[strategy_display, walk_time], outputs=strategy_display)
            a_btn.click(lambda s, t: add_command(s, f"a({t})"), inputs=[strategy_display, walk_time], outputs=strategy_display)
            s_btn.click(lambda s, t: add_command(s, f"s({t})"), inputs=[strategy_display, walk_time], outputs=strategy_display)
            d_btn.click(lambda s, t: add_command(s, f"d({t})"), inputs=[strategy_display, walk_time], outputs=strategy_display)
            
            # keypress
            keypress_q_btn.click(lambda s: add_command(s, "keypress(q)"), inputs=strategy_display, outputs=strategy_display)
            keypress_e_btn.click(lambda s: add_command(s, "keypress(e)"), inputs=strategy_display, outputs=strategy_display)
            
            # keydown/keyup
            keydown_e_btn.click(lambda s: add_command(s, "keydown(E)"), inputs=strategy_display, outputs=strategy_display)
            keyup_e_btn.click(lambda s: add_command(s, "keyup(E)"), inputs=strategy_display, outputs=strategy_display)
            keydown_w_btn.click(lambda s: add_command(s, "keydown(W)"), inputs=strategy_display, outputs=strategy_display)
            keyup_w_btn.click(lambda s: add_command(s, "keyup(W)"), inputs=strategy_display, outputs=strategy_display)
            keydown_s_btn.click(lambda s: add_command(s, "keydown(S)"), inputs=strategy_display, outputs=strategy_display)
            keyup_s_btn.click(lambda s: add_command(s, "keyup(S)"), inputs=strategy_display, outputs=strategy_display)
            keydown_a_btn.click(lambda s: add_command(s, "keydown(A)"), inputs=strategy_display, outputs=strategy_display)
            keyup_a_btn.click(lambda s: add_command(s, "keyup(A)"), inputs=strategy_display, outputs=strategy_display)
            keydown_lbtn.click(lambda s: add_command(s, "keydown(VK_LBUTTON)"), inputs=strategy_display, outputs=strategy_display)
            keyup_lbtn.click(lambda s: add_command(s, "keyup(VK_LBUTTON)"), inputs=strategy_display, outputs=strategy_display)
            keydown_rbtn.click(lambda s: add_command(s, "keydown(VK_RBUTTON)"), inputs=strategy_display, outputs=strategy_display)
            keyup_rbtn.click(lambda s: add_command(s, "keyup(VK_RBUTTON)"), inputs=strategy_display, outputs=strategy_display)
            
            # moveby
            moveby_btn.click(lambda s, x, y: add_command(s, f"moveby({x},{y})"), inputs=[strategy_display, moveby_x, moveby_y], outputs=strategy_display)

            save_btn.click(save_strategy, inputs=[character, strategy_display, filename], outputs=save_output)

            # 元素选择变化时更新角色列表
            def update_characters_by_element(element):
                return gr.Dropdown(choices=characters_by_element[element])

            element.change(update_characters_by_element, inputs=element, outputs=character)

if __name__ == "__main__":
    import webbrowser
    import threading
    import time
    
    def open_browser():
        time.sleep(2)  # 等待服务器启动
        webbrowser.open("http://127.0.0.1:7860")
    
    # 在后台线程中打开浏览器
    threading.Thread(target=open_browser, daemon=True).start()
    
    demo.launch(server_name="127.0.0.1", server_port=7860)
