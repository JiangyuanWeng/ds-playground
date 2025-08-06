import pandas as pd
import numpy as np


def analyze_data(cleaned_file: str):
    df = pd.read_csv(cleaned_file)

    scores = df[["math", "english", "science"]].to_numpy()

    print("📊 学生成绩矩阵：\n", scores)

    avg = np.mean(scores, axis=0)
    std = np.std(scores, axis=0)

    print("\n📈 各科平均分：", avg)
    print("📉 各科标准差：", std)
