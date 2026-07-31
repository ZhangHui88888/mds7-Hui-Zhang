# MDS7 项目学习笔记

本文件集中记录整个项目的学习内容，按照课程推进顺序整理，不再把笔记分散在各周目录中。

## 目录

- Week 1：环境搭建与项目初始化
- Week 2：分布式数据与 SQL 基础
- Week 3–4：S3、ETL、PowerBI 准备与机器学习
- Lecture 4：机器学习任务实操补充

---

## Week 1：环境搭建与项目初始化

### 1. 老师要求是什么

Week 1 主要不是做算法，而是先把课程项目环境搭起来。

你需要完成：

- 创建课程 GitHub 仓库。
- 保持清晰的项目目录结构，后续每周任务都能放到对应位置。
- 邀请老师，或者确保老师可以查看你的仓库。
- 维护 `AUDIT_TRAIL.md`，记录每次重要提交和任务进展。

当前仓库里的 Week 1 审计记录是：

```text
Repository created and structured.
Environment initialized and Professor invited.
```

意思是：仓库已经创建，基础结构已经初始化，老师也已经被邀请或具备查看权限。

### 2. 这周应该交付什么

Week 1 的核心交付物是：

- 一个可用的 GitHub repository。
- 一个基础 `README.md`。
- 一个 `AUDIT_TRAIL.md`。
- 后续 week 使用的目录结构。

`AUDIT_TRAIL.md` 很重要，因为它是你完成任务的时间线证据。以后老师看仓库时，不只是看文件，还会看你是否记录了“做了什么、什么时候做、为什么做”。

### 3. 你真正需要学会什么

这一周真正要掌握的是 GitHub 项目工作流：

```text
本地项目文件
-> Git 跟踪变化
-> commit 保存快照
-> push 上传到 GitHub
-> 老师在 GitHub 查看
```

你应该能解释这些问题：

- 本地文件和 GitHub 文件有什么区别？
- `git status` 是看什么的？
- `git add` 是做什么的？
- `git commit` 是做什么的？
- `git push` 是做什么的？
- 为什么 AWS key、GitHub token 这种密钥不能提交到仓库？

### 4. 核心概念

#### Repository

Repository 是项目仓库。它既存放文件，也保存文件的修改历史。

#### Commit

Commit 是一次变更快照。你可以理解为“我在这个时间点完成了一小块工作”。

#### Remote

Remote 是远程仓库，通常就是 GitHub 上的那一份。

#### Audit Trail

Audit trail 是审计记录。它用人能读懂的方式记录项目进展。

在这门课里，`AUDIT_TRAIL.md` 就是你每周任务完成情况的证明。

### 5. 常见误区

- 本地改了文件，但忘记 push 到 GitHub。
- 文件上传到了错误目录。
- 把 API key、token、password 提交到 GitHub。
- 觉得 `AUDIT_TRAIL.md` 可有可无。
- 所有任务都直接在 `main` 上乱改，导致难以回退。

### 6. 自查

如果你能解释下面这句话，就说明 Week 1 的核心掌握了：

```text
我创建了课程仓库，用 Git 管理本地文件，用 GitHub 保存远程版本，并用 AUDIT_TRAIL.md 记录项目进展。
```

---

## Week 2：分布式数据与 SQL 基础

### 1. 老师要求是什么

Week 2 的老师代码主要做了一件事：让你选择本地文件，上传到 GitHub 指定目录，然后自动更新 `AUDIT_TRAIL.md`。

代码流程是：

```text
用 GitHub token 认证
-> 选择本地文件
-> 上传到目标文件夹
-> 如果文件已存在，就更新它
-> 追加 AUDIT_TRAIL.md 记录
```

你这次本地涉及的文件是：

```text
label.csv
```

目前它在本地临时目录：

```text
week2/label.csv
```

而仓库中正式的 Week 2 目录是：

```text
week-02-sql/
```

如果以后老师要求正式提交 Week 2 文件，应该优先放到正式目录，而不是临时的 `week2/`。

### 2. 这周应该交付什么

Week 2 的交付物通常包括：

- 指定的数据文件或 SQL 文件。
- 文件放在正确的 week 目录下。
- `AUDIT_TRAIL.md` 更新上传记录。

老师代码里使用的是 GitHub API：

```text
repo.create_file(...)
repo.update_file(...)
```

这说明它不是简单保存到本地，而是直接把文件推到 GitHub 远程仓库。

### 3. 你真正需要学会什么

这一周真正要理解的是“文件如何进入一个可审查的数据项目”：

```text
本地文件
-> 项目目录
-> GitHub 仓库
-> AUDIT_TRAIL.md 记录
```

你还需要学会检查数据文件本身：

- 有哪些列？
- 分隔符是什么？
- 有没有缺失值？
- 文件是否放在老师要求的目录？

比如 `label.csv` 的第一行是：

```text
id|treatment
```

这说明它的分隔符是 `|`，不是普通逗号。如果用 pandas 读取，要这样写：

```python
pd.read_csv("label.csv", sep="|")
```

### 4. 核心概念

#### CSV

CSV 是表格数据文件。虽然名字叫 comma-separated values，但真实项目里不一定用逗号，也可能用 `|`、tab 或分号。

#### Delimiter

Delimiter 是分隔符，用来区分每一列。`label.csv` 里使用的是 `|`。

#### SQL

SQL 是查询关系型数据库的语言。即使这一周只是上传 CSV，它背后的主题也是结构化数据如何被存储、查询和管理。

#### GitHub API 上传

GitHub API 上传是用代码上传文件。它和手动打开 GitHub 网页拖文件不同，更适合自动化流程。

### 5. 常见误区

- 把文件上传到错误目录。
- 以为所有 CSV 都是逗号分隔。
- 本地更新了 `AUDIT_TRAIL.md`，但忘记 push。
- 没有处理文件已存在的情况。
- 把临时目录当成正式提交目录。

### 6. 自查

你理解 Week 2，如果你能解释：

```text
老师的脚本通过 GitHub token 登录，选择本地文件，上传或更新 GitHub 文件，并把这次操作追加到 AUDIT_TRAIL.md。
```

你还应该能打开一个 CSV，判断它的列名、分隔符和基本结构。

---

## Week 3–4：S3、ETL、PowerBI 准备与机器学习

### 1. 老师要求是什么

Week 3–4 分成两个相连的部分。

第一部分是数据工程 pipeline：

```text
下载 Titanic 原始数据
-> 上传 raw data 到 AWS S3
-> 再从 S3 下载 raw data
-> 用 pandas 清洗和特征工程
-> 把清洗后的数据上传回 S3
-> 把清洗后的数据同步到 GitHub
-> 更新 AUDIT_TRAIL.md
```

第二部分是 Lecture 4 机器学习任务：

```text
创建 week-03-04-powerbi/machine_learning/
-> 从 S3 读取 titanic_clean.csv
-> 做 EDA
-> 做 correlation analysis
-> 选择和 Survived 最相关的前 5 个特征
-> 训练 Logistic Regression
-> 训练 XGBoost
-> 用 confusion matrix 和 F1 score 评估
-> 保存表现更好的模型为 .pkl
-> 上传 notebook 和 .pkl 到 GitHub 和 S3
-> 更新 AUDIT_TRAIL.md
```

### 2. 数据文件与字段结构

Week 3–4 的核心数据文件是清洗后的 Titanic 数据：

```text
week-03-04-powerbi/titanic_clean.csv
```

这个文件是 PowerBI 和机器学习共同使用的数据源。清洗后的主要列包括：

```text
PassengerId
Survived
Pclass
Name
Age
SibSp
Parch
Ticket
Fare
Sex_male
Embarked_Q
Embarked_S
```

原来的文字列 `Sex` 和 `Embarked` 会被转换成数值型 dummy variables，这样 PowerBI 可以更容易做分组统计，机器学习模型也可以直接使用这些字段。

### 3. 你真正需要学会什么

这几周最重要的是理解完整的数据生命周期：

```text
原始数据
-> 云存储
-> 数据清洗
-> 可分析数据
-> 可视化
-> 机器学习
-> 保存模型
-> 可复现提交
```

你真正要掌握的不是某一行代码，而是每一步为什么存在：

- 为什么 raw data 和 clean data 要分开？
- 为什么用 AWS S3 存文件？
- 为什么用 pandas 清洗？
- 为什么 PowerBI 需要干净的 CSV？
- 为什么机器学习模型需要数值特征？
- 为什么用 F1 score 评估模型？
- 为什么要把最佳模型保存成 `.pkl`？

### 4. AWS S3 是什么

S3 是 AWS 的对象存储服务。你可以把它理解成云端文件桶。

在这个任务里，S3 用来存：

```text
titanic_raw.csv
titanic_clean.csv
best_titanic_model.pkl
Titanic_ML_Lecture4.ipynb
```

S3 不是普通 SQL 数据库，它更像云端文件系统。

Python 操作 S3 使用：

```python
import boto3
```

常见操作：

```python
s3_client.upload_file(...)
s3_client.download_file(...)
```

最重要的安全规则：

```text
不要把 AWS key 提交到 GitHub。
```

### 5. ETL 和 ELT

你这次做的 pipeline 更接近 ETL：

```text
Extract: 抽取或下载 Titanic 原始数据
Transform: 用 pandas 清洗和转换
Load: 上传 clean data 到 S3 和 GitHub
```

ETL 是先清洗再加载。

ELT 是先加载原始数据，再在数据仓库里清洗，比如 BigQuery、Snowflake、Redshift。

一句话记忆：

```text
ETL: 先洗，再放进去
ELT: 先放进去，再洗
```

### 6. Titanic 数据是怎么清洗的

#### 6.1 填补 Age 缺失值

```python
df["Age"] = df["Age"].fillna(df["Age"].median())
```

`Age` 有缺失值。这里用年龄中位数填补。

为什么用中位数？因为中位数比平均数更不容易受极端值影响。

#### 6.2 填补 Embarked 缺失值

```python
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
```

`Embarked` 是登船港口。缺失值用出现次数最多的港口填补。

`mode()` 返回众数，`[0]` 表示取第一个众数。

#### 6.3 删除 Cabin

```python
df.drop(columns=["Cabin"], inplace=True)
```

`Cabin` 缺失太多，直接删除比随便猜更合理。

#### 6.4 创建 dummy variables

```python
pd.get_dummies(df, columns=["Sex", "Embarked"], drop_first=True)
```

这句把文字分类变量转成数字列：

```text
Sex -> Sex_male
Embarked -> Embarked_Q, Embarked_S
```

`drop_first=True` 会少保留一个类别，作为基准类别。

例如：

```text
Sex_male = 1 表示 male
Sex_male = 0 表示 female
```

对于 `Embarked`：

```text
Embarked_Q = 0 且 Embarked_S = 0 表示基准港口 C
```

### 7. PowerBI Prep 是什么

Python 脚本没有自动生成 PowerBI 报表，它只是为 PowerBI 准备数据。

`PowerBI Prep` 的意思是：

```text
把数据清洗成 PowerBI 可以导入和可视化的 CSV
```

所以老师要求中的 PowerBI 体现在这里：

```text
titanic_clean.csv 是给 PowerBI 使用的分析数据源
week-03-04-powerbi/ 是存放 PowerBI 准备数据和相关成果的目录
```

也就是说，Python / pandas / S3 / GitHub 负责把数据整理到 PowerBI 能直接使用的状态；PowerBI Desktop 负责导入 CSV 并制作图表。

#### 完成 S3 验证后的下一步

完成 `titanic_clean.csv` 的上传、下载和读取验证后，数据工程部分就已经闭环。此时应切换到 PowerBI Desktop 做展示；Notebook 中的快速柱状图只是 Python 端的简单检查，不代替 PowerBI dashboard。

完整学习顺序是：

```text
raw CSV -> 上传到 S3 -> pandas 清洗 -> clean CSV 上传到 S3
-> 从 S3 下载并验证 -> PowerBI 导入 clean CSV -> 制作交互式 dashboard
```

初次制作时，先从本地已经验证过的 `titanic_clean.csv` 导入即可；不要求 PowerBI 必须直接连接 S3。

在 PowerBI Desktop 里导入：

```text
Get Data -> Text/CSV -> titanic_clean.csv -> Load
```

如果使用中文界面，路径通常是：

```text
获取数据 -> 文本/CSV -> 选择 titanic_clean.csv -> 加载
```

导入后，一个合理的 dashboard 应该体现这些问题：

```text
总体生还情况如何？
不同性别的生还率是否不同？
不同舱位 Pclass 的生还率是否不同？
年龄 Age 和票价 Fare 的分布是什么样？
```

可以做的图包括：

- 生还人数 vs 未生还人数。
- 按 `Sex_male` 看生还率。
- 按 `Pclass` 看生还率。
- 年龄分布。
- 票价分布。
- 用 `Pclass` 或 `Sex_male` 做 slicer。

建议的最低可交付 dashboard：

- 卡片（Card）：`PassengerId` 的计数，表示总乘客数。
- 簇状柱形图：按 `Survived` 计数，表示生还与未生还人数。
- 簇状柱形图：按 `Pclass` 比较生还人数或生还率。
- 切片器（Slicer）：`Pclass` 或 `Sex_male`，用于交互筛选其他图表。

PowerBI 的价值不是看几行数据，而是做交互式 dashboard，帮助别人理解数据故事。

### 8. Lecture 4 机器学习

Lecture 4 是从数据准备进入预测建模。

要求目录是：

```text
week-03-04-powerbi/machine_learning/
```

最终应该有：

```text
Titanic_ML_Lecture4.ipynb
best_titanic_model.pkl
更新后的 AUDIT_TRAIL.md
S3 中的 notebook 和 .pkl 备份
GitHub 中的 notebook 和 .pkl
```

标准机器学习流程是：

```text
干净数据
-> 理解数据
-> 选择特征
-> 训练模型
-> 评估模型
-> 保存最佳模型
-> 发布结果
```

这比单独会调用某个模型更重要。

### 9. 从 S3 加载机器学习数据

老师要求从 AWS S3 下载 `titanic_clean.csv` 到 Colab。

概念上：

```text
S3 是数据存储位置
Colab 是运行代码的计算环境
pandas 是读取和分析数据的工具
```

典型代码结构是：

```python
s3_client.download_file(BUCKET_NAME, "titanic_clean.csv", "titanic_clean.csv")
df = pd.read_csv("titanic_clean.csv")
```

这证明机器学习任务使用的是上周 pipeline 的输出，而不是随便找的本地文件。

### 10. EDA 是什么

EDA 是 exploratory data analysis，中文叫探索性数据分析。

训练模型之前，先看数据：

```text
数据多少行多少列
有哪些字段
有没有缺失值
每列分布如何
变量之间有什么关系
```

Univariate analysis 是单变量分析，比如：

```text
Age 分布
Fare 分布
Survived 数量
Pclass 数量
```

Multivariate analysis 是多变量分析，比如：

```text
Pclass 和 Survived 的关系
Sex_male 和 Survived 的关系
Fare 和 Survived 的关系
Age 和 Survived 的关系
```

EDA 的目的：不要闭着眼睛训练模型。

### 11. Correlation 和 Feature Selection

Correlation 衡量两个数值变量之间的相关程度。

本任务中，目标变量是：

```text
Survived
```

你要比较每个 feature 和 `Survived` 的相关性，然后选绝对相关性最高的前 5 个特征。

常见代码思路：

```python
corr = df.corr(numeric_only=True)["Survived"].abs().sort_values(ascending=False)
top_features = corr.drop("Survived").head(5).index.tolist()
```

这里用绝对值，是因为正相关和负相关都可能有用。

注意：

```text
相关性不是因果关系。
```

某个特征和生还有关，不代表它一定直接导致生还。

### 12. Logistic Regression

Logistic Regression 是分类模型。

虽然名字里有 regression，但它常用于二分类：

```text
Survived = 0 或 1
```

它适合作为 baseline model，因为简单、快速、容易解释。

### 13. XGBoost

XGBoost 是基于树的增强模型，常用于表格数据。

它通常比 Logistic Regression 更强，因为它能学习非线性关系和特征组合。

比如：

```text
Pclass + Sex_male
Age + Fare
Pclass + Fare
```

这些组合关系，XGBoost 往往能捕捉得更好。

### 14. Confusion Matrix

Confusion matrix 用来比较预测结果和真实结果。

对 Titanic 来说，就是：

```text
真实未生还，预测未生还
真实未生还，预测生还
真实生还，预测未生还
真实生还，预测生还
```

它比单纯 accuracy 更具体，因为你能看出模型是哪类错误更多。

### 15. F1 Score

F1 score 结合了 precision 和 recall。

它回答的是：

```text
模型预测生还时，有多少是真的？
所有真实生还的人里，模型找出了多少？
```

老师要求用 F1 score 比较模型，判断规则是：

```text
F1 score 更高的模型 = 最佳模型
```

### 16. 保存最佳模型

`.pkl` 是 Python 对象序列化文件。

保存模型示例：

```python
import pickle

with open("best_titanic_model.pkl", "wb") as f:
    pickle.dump(best_model, f)
```

这样以后可以直接加载模型，不用重新训练。

### 17. 上传到 GitHub 和 S3

任务不是训练完就结束。最终要上传到两个地方：

```text
GitHub: 方便老师检查和保留版本历史
S3: 保持云端数据管道完整
```

GitHub 目标路径：

```text
week-03-04-powerbi/machine_learning/best_titanic_model.pkl
week-03-04-powerbi/machine_learning/Titanic_ML_Lecture4.ipynb
```

S3 目标对象：

```text
best_titanic_model.pkl
Titanic_ML_Lecture4.ipynb
```

### 18. Teams 回复模板

完成后可以在 Teams 发：

```text
Hi Professor, I have completed the Lecture 4 asynchronous task. I trained and evaluated Logistic Regression and XGBoost models on the Titanic dataset, saved the best model as a .pkl file, uploaded the notebook and model to GitHub and AWS S3, and updated the audit trail. Thanks.
```

### 19. Week 3–4 概念检查清单

数据工程部分需要理解：

- `titanic_raw.csv` 和 `titanic_clean.csv` 的区别。
- 为什么要把 raw CSV 上传到 S3。
- 为什么要再从 S3 下载 raw CSV 进行处理。
- pandas 清洗数据时处理了哪些字段。
- clean CSV 为什么要同时放到 S3 和 GitHub。
- `AUDIT_TRAIL.md` 为什么要记录 pipeline 的关键动作。

机器学习部分需要理解：

- 为什么机器学习任务要从 S3 加载 clean CSV。
- EDA 在建模前解决什么问题。
- correlation analysis 如何帮助选择 top 5 features。
- Logistic Regression 和 XGBoost 的区别。
- confusion matrix 说明了哪些预测错误。
- F1 score 为什么可以用于比较两个模型。
- `.pkl` 文件为什么能保存训练好的模型。
- notebook 和模型为什么要同时上传到 GitHub 和 S3。

### 20. 最终自查

Week 4 结束后，你应该能解释：

```text
我用 S3 做云端存储，用 pandas 完成 ETL，用 PowerBI 作为可视化目标，并用机器学习模型预测 Titanic 乘客是否生还。
```

你还应该能完整说明 Lecture 4 的实操流程：

```text
我从 S3 读取清洗后的 Titanic 数据，做 EDA，选择与 Survived 最相关的 5 个特征，训练两个分类模型，用 F1 score 比较它们，保存最佳模型，并把 notebook 和模型上传到 GitHub 与 S3。
```
