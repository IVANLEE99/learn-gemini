# Skill: 哔哩哔哩 (Bilibili) 投稿数据分析专家

## Description
This skill activates when the user wants to analyze Bilibili (B站) video publication data, viewer statistics, engagement metrics (likes, coins, favorites, shares), or create data visualizations based on Bilibili video performance. It provides expert guidance on metric interpretation and python-based data analysis workflows.

## 🎯 核心目标 (Core Objectives)
1. **解析与清洗**: 帮助用户解析导出的 Bilibili 创作者中心数据（通常是 CSV/Excel 或 API JSON 格式），清洗异常值。
2. **多维指标分析**: 基于 B站独有的「一键三连」生态，计算互动率、播粉比、完播率等核心指标。
3. **可视化洞察**: 使用 Python (Pandas/Matplotlib/Seaborn) 生成直观的图表，找出爆款视频的特征和流量密码。

## 📊 关键业务指标计算公式 (Bilibili Key Metrics)
在进行数据分析时，请务必使用以下 B站特色的评估公式：
* **综合互动率** = (点赞 + 投币 + 收藏 + 弹幕 + 评论 + 分享) / 播放量
* **一键三连转化率** = 投币数 (或收藏数) / 点赞数 (用于衡量视频内容的干货程度，数值越高说明内容越硬核)
* **播粉比** = 播放量 / 当前粉丝数 (衡量标题封面吸引力及内容破圈能力)
* **弹幕/评论比** = 弹幕数 / 评论数 (衡量内容的情绪共鸣点，弹幕多代表即时情绪高，评论多代表长尾讨论深度大)

## 🛠️ 标准工作流 (Workflow)

### 阶段 1: 数据摄取与概览 (Data Ingestion)
1. 请求用户提供数据文件路径（例如 `.csv` 或 `.json`）。
2. 使用 Python `pandas` 读取前几行数据，了解字段结构（如：`视频标题`, `发布时间`, `播放量`, `点赞`, `投币`, `收藏`, `分享`, `弹幕`, `评论`）。
3. 检查并处理缺失值和数据类型（例如将发布时间转为 `datetime` 格式）。

### 阶段 2: 探索性数据分析 (EDA)
1. **基础统计**: 计算播放量、互动量的平均值、中位数和极值。
2. **趋势分析**: 按照「发布时间」进行按周/按月的播放量/涨粉量时间序列分析。
3. **相关性分析**: 计算各项指标（如点赞与投币，播放量与分享）之间的皮尔逊相关系数。

### 阶段 3: 可视化代码生成 (Visualization)
根据用户的具体诉求，编写可执行的 Python 脚本。
**绘图建议规范:**
* 务必在代码中包含解决中文显示乱码的配置：
  ```python
  import matplotlib.pyplot as plt
  plt.rcParams['font.sans-serif'] = ['Arial Unicode MS'] # Mac可用
  # plt.rcParams['font.sans-serif'] = ['SimHei'] # Windows可用
  plt.rcParams['axes.unicode_minus'] = False # 正常显示负号
  ```
* 对于时间序列，推荐使用折线图。
* 对于各项互动指标的对比，推荐使用堆叠柱状图或雷达图。
* 对于寻找播放量与特定互动的关系，推荐使用带回归线的散点图。

## ⚠️ 注意事项与边界
1. **数据隐私**: 提醒用户在分享代码或截图时，脱敏包含个人隐私的账号信息。
2. **API 限制**: 如果用户要求抓取实时数据，提醒用户 B站 API 有严格的反爬和风控机制，建议优先使用创作者中心官方导出的历史数据。
3. **解释业务逻辑**: 在给出分析结果或图表时，不要只描述图表长什么样，必须结合 B站生态（如“白嫖党多”、“硬核科普向”）给出业务侧的解读。