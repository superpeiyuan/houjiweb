from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # 首页介绍页

@app.route('/form')
def form():
    return render_template('form.html')  # 原评估表单页面

@app.route('/result', methods=['POST'])
def result():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    age = int(request.form['age'])
    sex = request.form['sex']
    injury = request.form['injury']

    bmi = round(weight / ((height / 100) ** 2), 1)
    ideal_weight = round(22 * ((height / 100) ** 2), 1)
    weight_diff = round(weight - ideal_weight, 1)

    if bmi < 18.5:
        weight_status = "偏瘦"
        train_advice = (
            "建议进行以增肌为目标的力量训练，例如哑铃卧推、深蹲等。\n"
            "每周至少进行3次，每次30~45分钟，避免高强度有氧训练。\n"
            "重视训练后的休息与营养补充。"
        )
        diet_advice = (
            "建议增加总热量摄入（基础代谢 + 500千卡）。\n"
            "多摄入高蛋白和复合碳水，如鸡蛋、牛奶、糙米、坚果。\n"
            "可适量加餐，如水果酸奶、花生酱三明治等。"
        )
    elif 18.5 <= bmi <= 23.9:
        weight_status = "正常"
        train_advice = (
            "建议保持综合训练计划，包括有氧（跑步、游泳）和力量训练。\n"
            "每周运动3~5次，每次30~60分钟。\n"
            "注重训练多样性，增强心肺和肌肉平衡发展。"
        )
        diet_advice = (
            "保持均衡饮食，合理搭配碳水、蛋白和脂肪的比例。\n"
            "注意控制油、盐、糖的摄入，养成规律饮食和睡眠习惯。\n"
            "日常可多食用新鲜蔬果、瘦肉和粗粮类主食。"
        )
    elif 24.0 <= bmi <= 27.9:
        weight_status = "偏重"
        train_advice = (
            "建议加强中低强度有氧运动，如快走、骑行、游泳等。\n"
            "每周至少5次，每次40~60分钟。\n"
            "配合适量力量训练提高基础代谢，避免跳跃类高冲击动作。"
        )
        diet_advice = (
            "建议每日热量减少500~800千卡，控制碳水和脂肪摄入。\n"
            "多吃富含纤维的蔬菜、豆类，减少主食比例。\n"
            "避免含糖饮料、油炸和高热量零食。"
        )
    else:
        weight_status = "肥胖"
        train_advice = (
            "建议从低冲击有氧运动开始，如水中行走、椭圆机训练。\n"
            "每天进行30~60分钟，循序渐进提高运动强度。\n"
            "必要时结合康复训练，保护关节并预防运动损伤。"
        )
        diet_advice = (
            "建议制定个性化减重食谱，减少精制碳水与饱和脂肪摄入。\n"
            "多食用低热量、高纤维、高蛋白的食物，如豆腐、蔬菜、鸡胸肉。\n"
            "避免暴饮暴食，三餐定量，必要时就医咨询营养师。"
        )

    injury_clean = injury.strip().replace(" ", "")
    if not injury_clean or injury_clean in ["无", "没有", "无伤病", "暂无", "暂无伤病", "无病史"]:
        injury_advice = "您暂时无伤病信息，建议正常训练前做好热身，注意身体信号，避免受伤。"
    else:
        injury_advice = f"您填写的伤病信息为：“{injury.strip()}”。建议避免对相关部位造成负担的动作，必要时请咨询专业康复师。"

    return render_template('result.html',
                           bmi=bmi,
                           weight_status=weight_status,
                           ideal_weight=ideal_weight,
                           weight_diff=weight_diff,
                           train_advice=train_advice,
                           diet_advice=diet_advice,
                           injury_advice=injury_advice)

#if __name__ == '__main__':
   # app.run(host='0.0.0.0', port=5000, debug=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # 允许局域网访问