from src.clean import clean_data
from src.analyze import analyze_data

# 路径可以按你的实际文件位置修改
clean_data("data/students.csv",
           "data/students_clean.csv")
analyze_data("data/students_clean.csv")

