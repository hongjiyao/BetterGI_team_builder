import gradio as gr

# ============================================
# 数据层 - 角色和技能序列数据
# ============================================

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

# 角色技能序列（来自万能战斗策略）
# 支持一个角色拥有多种策略，格式为：角色名: {策略名: 技能序列}
skill_sequences = {
    # 盾（刚需）
    "茜特菈莉": {
        "默认": "e,attack(0.2),keypress(q),wait(0.2),keypress(q),attack(0.2),keypress(q),attack(0.2),keypress(e)"
    },
    "伊涅芙": {
        "默认": "e,attack(0.22),keypress(q),wait(0.1),keypress(q),attack(0.2),keypress(q),attack(0.2)"
    },
    "钟离": {
        "默认": "s(0.2),e(hold),wait(0.2),w(0.2),keypress(q),wait(0.2),keypress(q),attack(0.1)"
    },
    "莱依拉": {
        "默认": "e,wait(0.2),keypress(q),wait(0.2),keypress(q),attack(0.2),keypress(q),attack(0.2)"
    },
    "绮良良": {
        "默认": "e,attack(0.2),keypress(q),attack(0.2),keypress(q),wait(0.2),keypress(q),attack(0.2)"
    },
    "托马": {
        "默认": "e,attack(0.22),keypress(q),wait(0.1),keypress(q),attack(0.2),keypress(q),attack(0.2)"
    },
    "蓝砚": {
        "默认": "e,wait(0.8),s(0.2),attack(0.33),dash(0.1),attack(0.55),keypress(q),attack(0.1)"
    },
    # 后台、挂元素、副C、先手
    "玛薇卡": {
        "后台挂火": "attack(0.2),e,wait(0.2),keypress(q),attack(0.15)",
        "爆发输出": "attack(0.08),keydown(E),wait(0.4),attack(0.2),wait(0.01),keyup(E),click(middle),attack(0.08),keypress(Q),wait(0.2),keypress(Q),charge(3.8),keydown(space),wait(0.1),keyup(space),attack(0.2),wait(0.2)",
        "AZS手法": "q,attack(0.1),e,charge(0.6),dash(0.3),moveby(500,0),moveby(2300,0),attack(0.1),charge(0.7),dash(0.3),moveby(-500,0),moveby(-2300,-0),attack(0.1),charge(0.7),dash(0.3),moveby(500,0),moveby(2600,0),attack(0.1),charge(0.8),dash(0.3),moveby(-500,0),moveby(-2300,-0),attack(0.1),charge(0.8),dash(0.3),moveby(500,0),moveby(2300,0),attack(0.1),charge(0.8),dash(0.3),moveby(-500,0),moveby(-2300,-0)",
        "ZZS手法": "attack(0.08),keypress(q),attack(0.03),keypress(q),keydown(E),wait(0.35),keyup(E),attack(0.03),wait(0.25),keydown(VK_LBUTTON),wait(0.155),keydown(VK_RBUTTON),wait(0.18),keyup(VK_LBUTTON),wait(0.02),keyup(VK_RBUTTON),wait(0.02),keydown(VK_LBUTTON),wait(0.16),keydown(VK_RBUTTON),wait(0.18),keyup(VK_LBUTTON),wait(0.02),keyup(VK_RBUTTON),wait(0.1),keydown(VK_LBUTTON),wait(0.05),keyup(VK_LBUTTON),wait(0.05),keydown(VK_LBUTTON),wait(0.05),keyup(VK_LBUTTON),wait(1.25),keydown(VK_LBUTTON),wait(0.155),keydown(VK_RBUTTON),wait(0.18),keyup(VK_LBUTTON),wait(0.02),keyup(VK_RBUTTON),wait(0.02),keydown(VK_LBUTTON),wait(0.16),keydown(VK_RBUTTON),wait(0.18),keyup(VK_LBUTTON),wait(0.02),keyup(VK_RBUTTON),wait(0.1),keydown(VK_LBUTTON),wait(0.05),keyup(VK_LBUTTON),wait(0.05),keydown(VK_LBUTTON),wait(0.05),keyup(VK_LBUTTON),wait(0.83)",
        "回身QEZZS": "attack(0.03),keypress(q),keypress(q),keydown(E),wait(0.45),keyup(E),wait(0.2),keydown(VK_LBUTTON),wait(0.155),wait(0.359),keyup(VK_LBUTTON),wait(0.05),wait(0.05),keydown(VK_LBUTTON),wait(0.1),keyup(VK_LBUTTON),wait(0.05),keydown(VK_LBUTTON),wait(0.1),keyup(VK_LBUTTON),click(middle),wait(0.45),moveby(5500,0),wait(0.05),keydown(VK_LBUTTON),wait(0.125),keydown(VK_RBUTTON),wait(0.15),s(0.1),wait(0.1),keyup(VK_LBUTTON),wait(0.01),keyup(VK_RBUTTON),wait(0.08),keydown(VK_LBUTTON),wait(0.125),keydown(VK_RBUTTON),wait(0.1),s(0.1),wait(0.1),keyup(VK_LBUTTON),wait(0.01),keyup(VK_RBUTTON),wait(0.1),keydown(VK_LBUTTON),wait(0.05),keyup(VK_LBUTTON),wait(0.05),keydown(VK_LBUTTON),wait(0.05),keyup(VK_LBUTTON),wait(0.3)"
    },
    "杜林": {
        "默认": "attack(0.1),keypress(q),attack(0.2),click(middle),e,wait(0.2),e,keypress(q),wait(0.2),keypress(q),attack(0.2),keypress(q),attack(0.2)"
    },
    "迪希雅": {
        "后台挂火": "e,attack(0.2),e",
        "爆发输出": "keypress(q),attack(0.1),dash(0.2),keypress(q),attack(0.3),keypress(q),attack(0.3),keypress(q),attack(0.3),keydown(S),attack(0.5),keyup(S),keydown(W),attack(0.5),keyup(W),keydown(S),attack(0.5),keyup(S),keydown(W),attack(0.5),keyup(W),keydown(S),attack(0.5),keyup(S),keydown(W),attack(0.5),keyup(W),keydown(S),attack(0.5),keyup(S)"
    },
    "香菱": {
        "默认": "e,wait(0.3),keypress(q),attack(0.2),keypress(q),wait(0.2),keypress(q),attack(0.2)"
    },
    "仆人": {
        "快速切人": "attack,e",
        "收尾输出": "charge(0.35),j,keydown(s),attack(1.17),attack(0.45),keyup(s),keydown(w),attack(0.38),attack(0.6),keyup(w),wait(0.2),keydown(s),attack(1.17),attack(0.45),keyup(s),keydown(w),attack(0.38),attack(0.6),keyup(w),wait(0.2)"
    },
    "夜兰": {
        "顺时针": "attack(0.5),keydown(VK_W),wait(0.05),keydown(VK_E),wait(0.4),keyup(VK_E),wait(0.1),keydown(VK_D),keyup(VK_W),wait(0.4),keydown(VK_S),keyup(VK_D),wait(0.4),keydown(VK_A),keyup(VK_S),wait(0.4),keydown(VK_W),keyup(VK_A),wait(0.3),keydown(VK_S),keyup(VK_W),wait(0.15),keyup(VK_S),keypress(e),attack(0.2),keypress(Q),attack(0.2),keypress(Q),attack(0.2)",
        "逆时针": "attack(0.5),keydown(VK_W),wait(0.05),keydown(VK_E),wait(0.4),keyup(VK_E),wait(0.1),keydown(VK_A),keyup(VK_W),wait(0.4),keydown(VK_S),keyup(VK_A),wait(0.4),keydown(VK_D),keyup(VK_S),wait(0.4),keydown(VK_W),keyup(VK_D),wait(0.3),keydown(VK_S),keyup(VK_W),wait(0.15),keyup(VK_S),keypress(e),attack(0.2),keypress(Q),attack(0.2),keypress(Q),attack(0.2)"
    },
    "哥伦比娅": {
        "默认": "e,keypress(q),attack(0.2),keypress(q),attack"
    },
    "那维莱特": {
        "常规输出": "attack(0.05),click(middle),e,wait(0.15),keydown(VK_LBUTTON),wait(0.27),keyup(VK_LBUTTON)",
        "收尾长轴": "attack(0.05),keypress(q),wait(0.05),keypress(q),click(middle),e,wait(0.15),keydown(VK_LBUTTON),wait(0.27),keyup(VK_LBUTTON),wait(0.15),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),keydown(VK_LBUTTON),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,-2100),wait(0.05),moveby(1800,-2100),wait(0.05),moveby(1800,-1100),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,1200),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,1300),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,-2100),wait(0.05),moveby(1800,-2100),wait(0.05),moveby(1800,-1100),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,1200),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,1300),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,-2100),wait(0.05),moveby(1800,-2100),wait(0.05),moveby(1800,-1100),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,1200),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,1300),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),click(middle),j,click(middle),keyup(VK_LBUTTON),wait(0.5),attack(0.2),click(middle),wait(0.2),keydown(VK_LBUTTON),wait(0.35),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),keydown(VK_LBUTTON),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,-2100),wait(0.05),moveby(1800,-2100),wait(0.05),moveby(1800,-1100),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,1200),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,1300),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,-2100),wait(0.05),moveby(1800,-2100),wait(0.05),moveby(1800,-1100),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,1200),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,1300),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),moveby(1800,0),wait(0.05),click(middle),j,click(middle),keyup(VK_LBUTTON)"
    },
    "纳西妲": {
        "默认": "e(hold),click(middle),keypress(q),wait(0.3),keypress(q),attack(0.3),keypress(q),attack(0.2)"
    },
    "艾梅莉埃": {
        "默认": "e,attack(0.2),keypress(q),attack(0.2),keypress(q),wait(0.2),keypress(q),attack(0.2)"
    },
    "丝柯克": {
        "常规输出": "attack(0.2),click(middle),keypress(q),wait(0.05),keypress(q),attack(0.05),click(middle),keydown(E),wait(0.22),attack(0.08),click(middle),keyup(E),keypress(q),wait(0.08),keypress(q)",
        "收尾长轴": "attack(0.05),keypress(e),wait(0.05),keypress(e),wait(0.2),attack(2.27),keypress(Q),dash,attack(2.27),keydown(S),keypress(Q),dash,keyup(S),attack(2.27),wait(0.11),charge(0.3),attack(1)"
    },
    "芙宁娜": {
        "后台辅助": "e,attack(0.85),keypress(e),keypress(Q),attack(0.2)",
        "满命6刀": "attack(0.01),e,attack(0.1),dash(0.1),jump,wait(0.2),keypress(q),keydown(W),attack(0.3),keypress(q),keyup(W),attack(0.3),keypress(q),attack(0.1),keydown(S),attack(0.33),keyup(S),keydown(W),attack(0.3),keyup(W),keydown(S),attack(0.3),keyup(S),keydown(W),attack(0.3),keyup(W),keydown(S),attack(0.3),keyup(S),keydown(W),attack(0.3),keyup(W)"
    },
    "爱诺": {
        "默认": "e,wait(0.3),keypress(q),attack(0.22),keypress(q),attack(0.21)"
    },
    "夏洛蒂": {
        "默认": "e,click(middle),attack(0.3),keypress(q),attack(0.22),click(middle),dash(0.1),wait(0.3),keypress(q),attack(0.21)"
    },
    "菈乌玛": {
        "长E输出": "attack(0.1),keypress(q),attack(0.15),keydown(E),wait(0.4),attack(0.3),keyup(E),attack(0.15),keypress(q),attack(0.15),keydown(E),wait(0.4),attack(0.3),keyup(E),attack(0.2),wait(0.1)",
        "短E循环": "e,attack(0.2),keypress(q),attack(0.2),keypress(q),wait(0.2),keypress(q),attack(0.2)"
    },
    "白术": {
        "盾奶": "e,attack(0.2)",
        "中置位": "attack(0.2),keypress(q),attack(0.2),keypress(q),wait(0.2),keypress(q),attack(0.2)"
    },
    "珊瑚宫心海": {
        "默认": "e"
    },
    "芭芭拉": {
        "快速治疗": "e,attack(0.2)",
        "持续治疗": "e,attack(0.6),keypress(q),attack(2),charge(0.5),keypress(q),attack(0.2)"
    },
    "希格雯": {
        "常规治疗": "e(hold),wait(0.2),attack(0.21),keypress(q),wait(0.2),keypress(q)",
        "满命转圈": "e(hold),keypress(q),wait(0.2),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1),moveby(300,0),wait(0.1)"
    },
    "爱可菲": {
        "默认": "e,attack(0.2),keypress(q),attack(0.2),keypress(q),wait(0.2),keypress(q),attack(0.2)"
    },
    "菲谢尔": {
        "默认": "e"
    },
    "欧洛伦": {
        "常规输出": "e,attack(0.3),keypress(q),wait(0.2),attack(0.3),keypress(q),wait(0.2),attack(0.3),keypress(q),wait(0.3)",
        "带冲刺": "e,attack(0.3),keypress(q),wait(0.2),attack(0.3),keypress(q),wait(0.2),dash(0.1),attack(0.3),keypress(q),wait(0.3)"
    },
    "雷电将军": {
        "默认": "e,attack(0.22),keypress(q),wait(0.1),keypress(q),attack(0.2),keypress(q),attack(0.2)"
    },
    "久岐忍": {
        "默认": "e,wait(0.2),keypress(q),attack(0.15),keypress(q),e"
    },
    "瓦雷莎": {
        "常规输出": "e,attack(1.25),wait(0.45),s(0.4),click(middle),e,attack(1.25),wait(0.3),keypress(q),wait(0.45)",
        "带转向": "e,attack(1.25),click(middle),wait(0.45),keydown(s),e,attack(1.25),keyup(s),wait(0.3),keypress(q),click(middle),wait(0.45)"
    },
    # 中置位
    "夏沃蕾": {
        "默认": "attack(0.08),keypress(q),wait(0.2),keypress(q),wait(0.2),attack(0.21),keydown(e),wait(0.15),moveby(0,1300),wait(0.18),keyup(e),attack(0.15)"
    },
    "雅珂达": {
        "默认": "attack(0.2),click(middle),attack(0.2),keydown(E),keydown(W),wait(0.4),keyup(W),keydown(S),wait(0.25),keydown(W),wait(0.25),keyup(W),keydown(S),wait(0.25),keyup(S),keydup(E),attack(0.2),keypress(q),attack(0.2),keypress(q),attack(0.3)"
    },
    # 减抗
    "希诺宁": {
        "默认": "s(0.2),e,w(0.2),attack(0.35),wait(0.1),attack(0.35),keypress(x),wait(0.2),keypress(q),wait(0.3),keypress(q),keypress(x),wait(0.08),keypress(x),attack(0.2)"
    },
    "枫原万叶": {
        "默认": "attack(0.08),keypress(q),wait(0.3),keypress(q),wait(0.3),attack(0.2),keydown(E),wait(0.48),keyup(E),attack(0.3),wait(0.5),attack(0.1)"
    },
    "砂糖": {
        "默认": "e,attack(0.2),keypress(q),attack(0.2),keypress(q),e,attack(0.2)"
    },
    "琴": {
        "默认": "attack(0.21),keydown(e),wait(0.14),moveby(0,1300),wait(0.75),keyup(e),attack(0.12),keypress(q),attack(0.11),keypress(q),attack"
    },
    # 其他角色
    "温迪": {
        "默认": "attack(0.1),keypress(Q),e,click(middle),attack(0.2),keypress(Q),attack(0.22),e,click(middle),dash(0.1),attack(1.2),e,attack(0.5),click(middle),attack(0.2),dash(0.1),attack(1.2)"
    },
    "娜维娅": {
        "默认": "keypress(q),attack(0.1),keypress(q),attack(0.1),keypress(q),attack(0.1),keypress(q),keydown(E),wait(0.8),keyup(E),attack(1.6),keydown(E),wait(0.8),keyup(E),attack(0.1),keydown(S),attack(0.33),keyup(S),keydown(W),attack(0.3),keyup(W),keydown(S),attack(0.3),keyup(S),keydown(W),attack(0.3),keyup(W),keydown(S),attack(0.3),keyup(S),keydown(W),attack(0.3),keyup(W),attack(0.2)"
    }
}


def get_character_strategies(character):
    """获取角色的所有策略名称"""
    if character in skill_sequences:
        strategies = skill_sequences[character]
        if isinstance(strategies, dict):
            return list(strategies.keys())
        else:
            return ["默认"]
    return []


def get_skill_sequence(character, strategy_name="默认"):
    """获取角色指定策略的技能序列"""
    if character in skill_sequences:
        strategies = skill_sequences[character]
        if isinstance(strategies, dict):
            return strategies.get(strategy_name, strategies.get("默认", ""))
        else:
            return strategies
    return ""


# ============================================
# 工具函数层 - 通用工具函数
# ============================================

def clean_punctuation(text):
    """清理中文标点，转换为英文标点"""
    if not text:
        return text
    text = text.replace('，', ',').replace('（', '(').replace('）', ')')
    text = text.replace('。', '.').replace('；', ';').replace('：', ':')
    text = text.replace('"', '"').replace('"', '"').replace('\'', '\'')
    text = text.replace('【', '[').replace('】', ']').replace('、', ',')
    return text


# ============================================
# 快速配队模块 - 独立功能
# ============================================

class QuickTeamModule:
    """快速配队功能模块"""

    # 获取有技能序列的角色列表（万能战斗策略中有的角色）
    available_characters = sorted(skill_sequences.keys())

    @staticmethod
    def get_strategies_for_character(character):
        """获取角色的所有策略选项"""
        return get_character_strategies(character)

    @staticmethod
    def build_team(role1, strategy1, role2, strategy2, role3, strategy3, role4, strategy4):
        """生成配队方案"""
        team = [(role1, strategy1), (role2, strategy2), (role3, strategy3), (role4, strategy4)]
        team = [(c, s) for c, s in team if c]

        # 检查重复角色
        char_names = [c for c, s in team]
        if len(char_names) != len(set(char_names)):
            return "⚠️ 错误：队伍中存在重复角色！"

        output_lines = []
        for char, strategy in team:
            if char in skill_sequences:
                sequence = get_skill_sequence(char, strategy)
                output_lines.append(f"{char} {sequence}")

        output_text = "\n".join(output_lines)

        if output_text:
            filename = "".join([c[0] for c, s in team]) + ".txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(output_text)

        return output_text

    @staticmethod
    def update_strategies_dropdown(character):
        """根据选择的角色更新策略下拉框"""
        strategies = get_character_strategies(character)
        default_value = strategies[0] if strategies else None
        return gr.Dropdown(choices=strategies, value=default_value)

    @staticmethod
    def create_ui():
        """创建快速配队界面"""
        # 设置默认值（前4个有技能序列的角色）
        default_values = QuickTeamModule.available_characters[:4] if len(QuickTeamModule.available_characters) >= 4 else QuickTeamModule.available_characters + [""] * (4 - len(QuickTeamModule.available_characters))

        with gr.TabItem("快速配队"):
            with gr.Row():
                with gr.Column():
                    # 角色和策略选择
                    role_components = []
                    strategy_components = []

                    for i in range(4):
                        with gr.Row():
                            role = gr.Dropdown(QuickTeamModule.available_characters, label=f"角色{i+1}", value=default_values[i] if i < len(default_values) else None)
                            # 获取该角色的策略列表
                            default_strategies = get_character_strategies(default_values[i]) if i < len(default_values) and default_values[i] else []
                            default_strategy = default_strategies[0] if default_strategies else None
                            strategy = gr.Dropdown(default_strategies, label=f"策略{i+1}", value=default_strategy)
                            role_components.append(role)
                            strategy_components.append(strategy)

                    generate_btn = gr.Button("生成配队方案", variant="primary")
                with gr.Column():
                    output = gr.Textbox(label="配队方案", lines=20)

            # 绑定角色选择变化时更新策略下拉框
            for i in range(4):
                role_components[i].change(
                    QuickTeamModule.update_strategies_dropdown,
                    inputs=role_components[i],
                    outputs=strategy_components[i]
                )

            # 绑定生成按钮
            all_inputs = []
            for i in range(4):
                all_inputs.extend([role_components[i], strategy_components[i]])
            generate_btn.click(QuickTeamModule.build_team, inputs=all_inputs, outputs=output)


# ============================================
# 自定义策略模块 - 独立功能
# ============================================

class CustomStrategyModule:
    """自定义战斗策略功能模块"""
    
    @staticmethod
    def add_character(character, strategy):
        """添加角色名到新行"""
        print(f"\n[add_character] 输入: character='{character}', strategy='{strategy}'")
        if not character:
            print("[add_character] 角色为空，返回原策略")
            return strategy
        result = (strategy.rstrip() + f"\n{character} ") if strategy else f"{character} "
        print(f"[add_character] 输出: '{result}'")
        return result
    
    @staticmethod
    def add_command(strategy, command):
        """添加命令到策略"""
        command = clean_punctuation(command)
        
        print(f"\n[add_command] 输入: strategy='{strategy}', command='{command}'")
        if not strategy:
            print(f"[add_command] 策略为空，直接返回命令: '{command}'")
            return command

        strategy = clean_punctuation(strategy)
        strategy_clean = strategy.strip('\n')
        lines = strategy_clean.split('\n') if strategy_clean else []
        if not lines:
            print(f"[add_command] 清理后策略为空，返回命令: '{command}'")
            return command

        last_line = lines[-1].rstrip('\n')
        print(f"[add_command] 最后一行: '{last_line}'")

        sorted_characters = sorted(all_characters, key=len, reverse=True)

        for char in sorted_characters:
            prefix = f"{char} "
            if last_line.startswith(prefix):
                content = last_line[len(prefix):].strip()
                print(f"[add_command] 匹配到角色: '{char}', prefix='{prefix}', content='{content}'")
                if content:
                    lines[-1] = prefix + content + "," + command
                    print(f"[add_command] 内容非空，添加逗号分隔: '{lines[-1]}'")
                else:
                    lines[-1] = prefix + command
                    print(f"[add_command] 内容为空，直接添加命令: '{lines[-1]}'")
                result = '\n'.join(lines)
                print(f"[add_command] 输出: '{result}'")
                return result

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
    
    @staticmethod
    def save_strategy(character, strategy, filename):
        """保存策略到文件"""
        if not character or not strategy:
            return "⚠️ 错误：角色和策略不能为空！"
        if not filename.endswith(".txt"):
            filename += ".txt"
        
        character = clean_punctuation(character)
        strategy = clean_punctuation(strategy)
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"{character} {strategy}")
        return f"✅ 策略已保存到 {filename}"
    
    @staticmethod
    def update_characters_by_element(element):
        """根据元素更新角色列表，并设置默认值为第一个角色"""
        characters = characters_by_element[element]
        default_value = characters[0] if characters else None
        return gr.Dropdown(choices=characters, value=default_value)
    
    @staticmethod
    def load_param(key, default_value):
        """从文件加载参数"""
        try:
            import json
            with open('params.json', 'r', encoding='utf-8') as f:
                params = json.load(f)
                return params.get(key, default_value)
        except:
            return default_value
    
    @staticmethod
    def create_ui():
        """创建自定义策略界面"""
        # 加载保存的参数值
        attack_dur_val = CustomStrategyModule.load_param('attack_dur', '0.2')
        charge_dur_val = CustomStrategyModule.load_param('charge_dur', '0.5')
        wait_time_val = CustomStrategyModule.load_param('wait_time', '0.2')
        dash_dur_val = CustomStrategyModule.load_param('dash_dur', '0.1')
        walk_time_val = CustomStrategyModule.load_param('walk_time', '0.2')
        moveby_x_val = CustomStrategyModule.load_param('moveby_x', '1800')
        moveby_y_val = CustomStrategyModule.load_param('moveby_y', '0')
        
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
                    
                    # 基础命令 - 默认展开
                    with gr.Accordion("⚔️ 基础命令", open=True):
                        with gr.Row():
                            e_btn = gr.Button("e")
                            e_hold_btn = gr.Button("e(hold)")
                            q_btn = gr.Button("q")
                        with gr.Row():
                            j_btn = gr.Button("j")
                            ready_btn = gr.Button("ready")
                        with gr.Row():
                            attack_dur = gr.Textbox(label="时间", value=attack_dur_val, container=False)
                            attack_btn = gr.Button("attack")
                        with gr.Row():
                            charge_dur = gr.Textbox(label="时间", value=charge_dur_val, container=False)
                            charge_btn = gr.Button("charge")
                        with gr.Row():
                            wait_time = gr.Textbox(label="时间", value=wait_time_val, container=False)
                            wait_btn = gr.Button("wait")
                        with gr.Row():
                            dash_dur = gr.Textbox(label="时间", value=dash_dur_val, container=False)
                            dash_btn = gr.Button("dash")
                        with gr.Row():
                            walk_time = gr.Textbox(label="时间", value=walk_time_val, container=False)
                        with gr.Row():
                            w_btn = gr.Button("w")
                            a_btn = gr.Button("a")
                            s_btn = gr.Button("s")
                            d_btn = gr.Button("d")
                    
                    # 高级语法 - 默认折叠
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
                            moveby_x = gr.Textbox(label="X", value=moveby_x_val, container=False)
                            moveby_y = gr.Textbox(label="Y", value=moveby_y_val, container=False)
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
                        - `ready` - 准备就绪（等待大招动画，只有5星角色能使用）
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
            add_char_btn.click(CustomStrategyModule.add_character, inputs=[character, strategy_display], outputs=strategy_display)
            clear_btn.click(lambda: "", outputs=strategy_display)

            # 基础技能
            e_btn.click(lambda s: CustomStrategyModule.add_command(s, "e"), inputs=strategy_display, outputs=strategy_display)
            e_hold_btn.click(lambda s: CustomStrategyModule.add_command(s, "e(hold)"), inputs=strategy_display, outputs=strategy_display)
            q_btn.click(lambda s: CustomStrategyModule.add_command(s, "q"), inputs=strategy_display, outputs=strategy_display)
            j_btn.click(lambda s: CustomStrategyModule.add_command(s, "j"), inputs=strategy_display, outputs=strategy_display)
            ready_btn.click(lambda s: CustomStrategyModule.add_command(s, "ready"), inputs=strategy_display, outputs=strategy_display)
            click_middle_btn.click(lambda s: CustomStrategyModule.add_command(s, "click(middle)"), inputs=strategy_display, outputs=strategy_display)
            
            # 攻击相关
            attack_btn.click(lambda s, d: CustomStrategyModule.add_command(s, f"attack({d})"), inputs=[strategy_display, attack_dur], outputs=strategy_display)
            charge_btn.click(lambda s, d: CustomStrategyModule.add_command(s, f"charge({d})"), inputs=[strategy_display, charge_dur], outputs=strategy_display)
            
            # 等待和冲刺
            wait_btn.click(lambda s, t: CustomStrategyModule.add_command(s, f"wait({t})"), inputs=[strategy_display, wait_time], outputs=strategy_display)
            dash_btn.click(lambda s, d: CustomStrategyModule.add_command(s, f"dash({d})"), inputs=[strategy_display, dash_dur], outputs=strategy_display)
            
            # 方向行走
            w_btn.click(lambda s, t: CustomStrategyModule.add_command(s, f"w({t})"), inputs=[strategy_display, walk_time], outputs=strategy_display)
            a_btn.click(lambda s, t: CustomStrategyModule.add_command(s, f"a({t})"), inputs=[strategy_display, walk_time], outputs=strategy_display)
            s_btn.click(lambda s, t: CustomStrategyModule.add_command(s, f"s({t})"), inputs=[strategy_display, walk_time], outputs=strategy_display)
            d_btn.click(lambda s, t: CustomStrategyModule.add_command(s, f"d({t})"), inputs=[strategy_display, walk_time], outputs=strategy_display)
            
            # keypress
            keypress_q_btn.click(lambda s: CustomStrategyModule.add_command(s, "keypress(q)"), inputs=strategy_display, outputs=strategy_display)
            keypress_e_btn.click(lambda s: CustomStrategyModule.add_command(s, "keypress(e)"), inputs=strategy_display, outputs=strategy_display)
            
            # keydown/keyup
            keydown_e_btn.click(lambda s: CustomStrategyModule.add_command(s, "keydown(E)"), inputs=strategy_display, outputs=strategy_display)
            keyup_e_btn.click(lambda s: CustomStrategyModule.add_command(s, "keyup(E)"), inputs=strategy_display, outputs=strategy_display)
            keydown_w_btn.click(lambda s: CustomStrategyModule.add_command(s, "keydown(W)"), inputs=strategy_display, outputs=strategy_display)
            keyup_w_btn.click(lambda s: CustomStrategyModule.add_command(s, "keyup(W)"), inputs=strategy_display, outputs=strategy_display)
            keydown_s_btn.click(lambda s: CustomStrategyModule.add_command(s, "keydown(S)"), inputs=strategy_display, outputs=strategy_display)
            keyup_s_btn.click(lambda s: CustomStrategyModule.add_command(s, "keyup(S)"), inputs=strategy_display, outputs=strategy_display)
            keydown_a_btn.click(lambda s: CustomStrategyModule.add_command(s, "keydown(A)"), inputs=strategy_display, outputs=strategy_display)
            keyup_a_btn.click(lambda s: CustomStrategyModule.add_command(s, "keyup(A)"), inputs=strategy_display, outputs=strategy_display)
            keydown_lbtn.click(lambda s: CustomStrategyModule.add_command(s, "keydown(VK_LBUTTON)"), inputs=strategy_display, outputs=strategy_display)
            keyup_lbtn.click(lambda s: CustomStrategyModule.add_command(s, "keyup(VK_LBUTTON)"), inputs=strategy_display, outputs=strategy_display)
            keydown_rbtn.click(lambda s: CustomStrategyModule.add_command(s, "keydown(VK_RBUTTON)"), inputs=strategy_display, outputs=strategy_display)
            keyup_rbtn.click(lambda s: CustomStrategyModule.add_command(s, "keyup(VK_RBUTTON)"), inputs=strategy_display, outputs=strategy_display)
            
            # moveby
            moveby_btn.click(lambda s, x, y: CustomStrategyModule.add_command(s, f"moveby({x},{y})"), inputs=[strategy_display, moveby_x, moveby_y], outputs=strategy_display)

            save_btn.click(CustomStrategyModule.save_strategy, inputs=[character, strategy_display, filename], outputs=save_output)

            # 元素选择变化时更新角色列表
            element.change(CustomStrategyModule.update_characters_by_element, inputs=element, outputs=character)
            
            # 参数自动保存到本地存储
            def save_param(key, value):
                """保存参数到文件"""
                try:
                    import json
                    params = {}
                    try:
                        with open('params.json', 'r', encoding='utf-8') as f:
                            params = json.load(f)
                    except:
                        pass
                    params[key] = value
                    with open('params.json', 'w', encoding='utf-8') as f:
                        json.dump(params, f, ensure_ascii=False, indent=2)
                except:
                    pass
                return value
            
            # 参数变化时自动保存
            attack_dur.change(lambda v: save_param('attack_dur', v), inputs=attack_dur, outputs=attack_dur)
            charge_dur.change(lambda v: save_param('charge_dur', v), inputs=charge_dur, outputs=charge_dur)
            wait_time.change(lambda v: save_param('wait_time', v), inputs=wait_time, outputs=wait_time)
            dash_dur.change(lambda v: save_param('dash_dur', v), inputs=dash_dur, outputs=dash_dur)
            walk_time.change(lambda v: save_param('walk_time', v), inputs=walk_time, outputs=walk_time)
            moveby_x.change(lambda v: save_param('moveby_x', v), inputs=moveby_x, outputs=moveby_x)
            moveby_y.change(lambda v: save_param('moveby_y', v), inputs=moveby_y, outputs=moveby_y)


# ============================================
# 主程序入口
# ============================================

def main():
    """主程序入口"""
    with gr.Blocks(title="原神配队工具") as demo:
        gr.Markdown("# 🎮 原神配队工具")

        with gr.Tabs():
            # 快速配队模块
            QuickTeamModule.create_ui()
            
            # 自定义策略模块
            CustomStrategyModule.create_ui()

    demo.launch(inbrowser=True, server_port=7862)


if __name__ == "__main__":
    main()
