import json
import random

# 四类主题模板（每类定义多个诗句模板，避免重复）
templates = {
    "乡村": [
        "炊烟袅袅绕山梁，\n老牛慢步过石塘。\n稻花香里说丰年，\n溪水潺潺送夕阳。",
        "青瓦白墙篱笆院，\n鸡鸣犬吠伴晨烟。\n阿婆树下摇蒲扇，\n笑看孙儿放纸鸢。",
        "麦浪翻金接远天，\n牧童横笛卧牛肩。\n村头老井苔痕绿，\n一桶清凉汲月眠。",
        "豆架瓜棚小径斜，\n蜻蜓点水戏荷花。\n晚风轻送蛙声起，\n萤火提灯照我家。",
        "晒谷场边枣树高，\n邻家笑语隔墙飘。\n柴门不锁归人晚，\n犬卧阶前月满桥。"
    ],
    "城市": [
        "霓虹闪烁夜未央，\n车流如织穿街巷。\n高楼万丈遮星月，\n谁在窗前望故乡？",
        "地铁呼啸载梦行，\n玻璃幕墙映云晴。\n咖啡凉了文件厚，\n脚步匆匆心未停。",
        "十字街头人似潮，\n广告屏里笑颜娇。\n背包压弯少年背，\n房租催单又一条。",
        "雨打公交站台灯，\n伞下情侣紧相拥。\n写字楼里加班夜，\n一杯泡面慰孤鸿。",
        "共享单车排成行，\n外卖小哥闯红黄。\n广场舞曲争高下，\n鸽群飞过金融港。"
    ],
    "爱情": [
        "你是我眼中的星光，\n照亮长夜不眠的窗。\n纵使岁月染白发，\n仍握你手如初见模样。",
        "春樱落满肩头时，\n你说爱是细水长流。\n夏荷秋枫冬雪后，\n我们还在彼此左右。",
        "信笺折成纸飞机，\n飞越千山到你衣。\n字字未言心已懂，\n相逢一笑胜朝夕。",
        "地铁错过同一班，\n却在转角咖啡店。\n你推门风铃轻响，\n世界忽然静如眠。",
        "争吵之后冷如冰，\n转身又怕你受惊。\n默默煮碗阳春面，\n汤里浮着两颗星。"
    ],
    "友情": [
        "酒逢知己千杯少，\n话到投机夜未央。\n风雨人生同舟渡，\n何须日日共斜阳。",
        "少年同路踏歌行，\n中年各自奔前程。\n偶遇街头一笑暖，\n旧时光影又分明。",
        "电话那头沉默久，\n只说最近还好否。\n无需多言心自知，\n天涯如在隔壁楼。",
        "球鞋跑烂操场边，\n偷摘枇杷被狗撵。\n如今各在人海里，\n梦回仍是十七年。",
        "失意醉倒小馆中，\n你付账单扶我行。\n不说安慰大道理，\n只道明朝再冲锋。"
    ]
}

def generate_poems():
    data = []
    categories = ["乡村", "城市", "爱情", "友情"]
    total_per_category = 250
    prompt_template = "写一首关于{}的诗"

    for idx in range(1000):
        category = categories[idx // total_per_category]
        user_prompt = prompt_template.format(category)
        # 随机选一个模板（可加更多模板避免重复）
        poem = random.choice(templates[category])
        
        item = {
            "id": f"identity_{idx}",
            "conversations": [
                {"from": "user", "value": user_prompt},
                {"from": "assistant", "value": poem}
            ]
        }
        data.append(item)
    
    return data

if __name__ == "__main__":
    poems_data = generate_poems()
    with open("poems_1000.json", "w", encoding="utf-8") as f:
        json.dump(poems_data, f, ensure_ascii=False, indent=2)
    print("已生成 poems_1000.json，包含1000组诗歌对话数据")