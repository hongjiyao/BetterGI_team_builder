import gradio as gr

characters = {
    "盾": ["茜特菈莉", "伊涅芙", "钟离", "莱依拉", "绮良良", "托马", "蓝砚"],
    "后台/副C": ["玛薇卡", "杜林", "迪希雅", "香菱", "仆人", "夜兰", "哥伦比娅", "那维莱特", 
                "纳西妲", "艾梅莉埃", "丝柯克", "芙宁娜", "爱诺", "夏洛蒂", "菈乌玛", "白术", 
                "珊瑚宫心海", "芭芭拉", "希格雯", "爱可菲", "菲谢尔", "欧洛伦", "雷电将军", 
                "久岐忍", "瓦雷莎"],
    "减抗": ["希诺宁", "枫原万叶", "砂糖", "琴"],
    "爆发/主C": ["玛薇卡", "那维莱特", "丝柯克", "迪希雅", "娜维娅", "芙宁娜", "仆人", "瓦雷莎"]
}

skill_sequences = {
    "茜特菈莉": "e,attack(0.2),keypress(q),wait(0.2),keypress(q),attack(0.2),keypress(q),attack(0.2),keypress(e)",
    "伊涅芙": "e,attack(0.22),keypress(q),wait(0.1),keypress(q),attack(0.2),keypress(q),attack(0.2)",
    "钟离": "s(0.2), e(hold), wait(0.2), w(0.2),keypress(q),wait(0.2),keypress(q),attack(0.1)",
    "莱依拉": "e,wait(0.2), keypress(q),wait(0.2),keypress(q),attack(0.2),keypress(q),attack(0.2)",
    "绮良良": "e,attack(0.2), keypress(q),attack(0.2),keypress(q),wait(0.2),keypress(q),attack(0.2)",
    "托马": "e,attack(0.22),keypress(q),wait(0.1),keypress(q),attack(0.2),keypress(q),attack(0.2)",
    "蓝砚": "e,wait(0.8),s(0.2),attack(0.33),dash(0.1),attack(0.55),keypress(q),attack(0.1)",
    "玛薇卡": "attack(0.2),e,wait(0.2),keypress(q),attack(0.15)",
    "杜林": "attack(0.1), keypress(q), attack(0.2), click(middle), e, wait(0.2), e, keypress(q), wait(0.2), keypress(q), attack(0.2), keypress(q), attack(0.2)",
    "迪希雅": "e,attack(0.2),e",
    "香菱": "e,wait(0.3),keypress(q),attack(0.2),keypress(q),wait(0.2),keypress(q),attack(0.2)",
    "仆人": "attack,e",
    "夜兰": "attack(0.5),keydown(VK_W),wait(0.05),keydown(VK_E),wait(0.4),keyup(VK_E),wait(0.1),keydown(VK_D),keyup(VK_W),wait(0.4),keydown(VK_S),keyup(VK_D),wait(0.4),keydown(VK_A),keyup(VK_S),wait(0.4),keydown(VK_W),keyup(VK_A),wait(0.3),keydown(VK_S),keyup(VK_W),wait(0.15),keyup(VK_S),keypress(e), attack(0.2), keypress(Q), attack(0.2), keypress(Q), attack(0.2)",
    "哥伦比娅": "e,keypress(q),attack(0.2),keypress(q),attack",
    "那维莱特": "attack(0.05),click(middle),e,wait(0.15),keydown(VK_LBUTTON),wait(0.27),keyup(VK_LBUTTON),wait(0.15)",
    "纳西妲": "e(hold),click(middle),keypress(q),wait(0.3),keypress(q),attack(0.3),keypress(q),attack(0.2)",
    "艾梅莉埃": "e,attack(0.2), keypress(q),attack(0.2),keypress(q),wait(0.2),keypress(q),attack(0.2)",
    "丝柯克": "attack(0.2),click(middle),keypress(q),wait(0.05),keypress(q),attack(0.05),click(middle),keydown(E),wait(0.22),attack(0.08),click(middle),keyup(E),keypress(q),wait(0.08),keypress(q)",
    "芙宁娜": "e,attack(0.85), keypress(e), keypress(Q), attack(0.2), keydown(S), keypress(e), attack(0.2), keyup(S), keypress(Q), attack(0.2)",
    "爱诺": "e, wait(0.3), keypress(q), attack(0.22), keypress(q), attack(0.21)",
    "夏洛蒂": "e, click(middle), attack(0.3), keypress(q), attack(0.22), click(middle), dash(0.1),wait(0.3),keypress(q), attack(0.21)",
    "菈乌玛": "attack(0.1),keypress(q),attack(0.15),keydown(E),wait(0.4),attack(0.3),keyup(E),attack(0.15),keypress(q),attack(0.15),keydown(E),wait(0.4),attack(0.3),keyup(E),attack(0.2),wait(0.1)",
    "白术": "e,attack(0.2)",
    "珊瑚宫心海": "e",
    "芭芭拉": "e,attack(0.2)",
    "希格雯": "e(hold),wait(0.2),attack(0.21),keypress(q),wait(0.2),keypress(q)",
    "爱可菲": "e,attack(0.2), keypress(q),attack(0.2),keypress(q),wait(0.2),keypress(q),attack(0.2)",
    "菲谢尔": "e",
    "欧洛伦": "e,attack(0.3), keypress(q),wait(0.2),attack(0.3),keypress(q),wait(0.2),attack(0.3),keypress(q),wait(0.3)",
    "雷电将军": "e,attack(0.22),keypress(q),wait(0.1),keypress(q),attack(0.2),keypress(q),attack(0.2)",
    "久岐忍": "e,wait(0.2),keypress(q),attack(0.15),keypress(q),e",
    "瓦雷莎": "e, attack(1.25),wait(0.45), s(0.4), click(middle), e, attack(1.25), wait(0.3),keypress(q), wait(0.45)",
    "希诺宁": "s(0.2),e,w(0.2),attack(0.35),wait(0.1),attack(0.35),keypress(x), wait(0.2), keypress(q), wait(0.3), keypress(q),keypress(x), wait(0.08), keypress(x),attack(0.2)",
    "枫原万叶": "attack(0.08),keypress(q),wait(0.3),keypress(q),wait(0.3),attack(0.2),keydown(E),wait(0.48),keyup(E),attack(0.3), wait(0.5),attack(0.1)",
    "砂糖": "e,attack(0.2),keypress(q),attack(0.2),keypress(q),e,attack(0.2)",
    "琴": "attack(0.21),keydown(e),wait(0.14), moveby(0,1300),wait(0.75),keyup(e),attack(0.12),keypress(q),attack(0.11),keypress(q),attack",
    "娜维娅": "keypress(q),attack(0.1),keypress(q),attack(0.1),keypress(q),attack(0.1),keypress(q),keydown(E),wait(0.8),keyup(E),attack(1.6),keydown(E),wait(0.8),keyup(E),attack(0.1),keydown(S),attack(0.33),keyup(S),keydown(W),attack(0.3),keyup(W),keydown(S),attack(0.3),keyup(S),keydown(W),attack(0.3),keyup(W),keydown(S),attack(0.3),keyup(S),keydown(W),attack(0.3),keyup(W),attack(0.2)"
}

def build_team(shield, subc1, subc2, buffer):
    team = [shield, subc1, subc2, buffer]
    team = [c for c in team if c]
    
    output_lines = []
    for char in team:
        if char in skill_sequences:
            output_lines.append(f"{char} {skill_sequences[char]}")
    
    output_text = "\n".join(output_lines)
    
    filename_chars = [c[0] for c in team if c]
    filename = "".join(filename_chars) + ".txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(output_text)
    
    return output_text

with gr.Blocks(title="原神万能配队工具 - BGI策略") as demo:
    gr.Markdown("# 🎮 原神万能配队工具")
    gr.Markdown("基于BGI战斗配队逻辑：盾【刚需】+ 副C + 副C + 减抗/聚怪")
    
    with gr.Row():
        with gr.Column():
            shield_char = gr.Dropdown(characters["盾"], label="🛡️ 盾角色（刚需）", value="钟离")
            subc1_char = gr.Dropdown(characters["后台/副C"], label="⚔️ 副C/后台1", value="纳西妲")
            subc2_char = gr.Dropdown(characters["后台/副C"], label="⚔️ 副C/后台2", value="夜兰")
            buffer_char = gr.Dropdown(characters["减抗"], label="🍃 减抗/聚怪", value="枫原万叶")
            
            generate_btn = gr.Button("生成配队方案", variant="primary")
        
        with gr.Column():
            output = gr.Textbox(label="配队方案", lines=25)
    
    generate_btn.click(
        build_team,
        inputs=[shield_char, subc1_char, subc2_char, buffer_char],
        outputs=output
    )
    
    with gr.Accordion("战斗配置建议"):
        gr.Markdown("""
        **核心设置：**
        - 战斗配置：开启
        - 自动检测战斗结束：开启
        - 更快检查结束战斗：开启（参数1）
        - 旋转寻找敌人位置：开启
        - Q前检测：开启
        - 盾奶角色优先释放技能：开启
        
        **拾取设置：**
        - 队伍中有万叶/琴时，禁止开启自动拾取！
        - 聚集材料动作：开启
        """)

if __name__ == "__main__":
    demo.launch(inbrowser=True)
