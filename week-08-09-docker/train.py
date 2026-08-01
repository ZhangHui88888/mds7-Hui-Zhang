
# ==========================================
# 3. MLOps 模型训练与自动比较流程
# ==========================================

import json
import os
import random

import joblib
import numpy as np
import tensorflow as tf

from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


# ==========================================
# 1. 全局配置
# ==========================================

RANDOM_STATE = 42
METRICS_FILE = "metrics.json"
CLASSICAL_MODEL_FILE = "best_model.pkl"
DEEP_MODEL_FILE = "best_model.h5"

# 保证结果尽可能可重复
os.environ["PYTHONHASHSEED"] = str(RANDOM_STATE)
random.seed(RANDOM_STATE)
np.random.seed(RANDOM_STATE)
tf.keras.utils.set_random_seed(RANDOM_STATE)


# ==========================================
# 2. 加载并划分数据
# ==========================================

data = load_breast_cancer()

X = data.data.astype("float32")
y = data.target.astype("int32")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=RANDOM_STATE,
    stratify=y
)

print("Dataset loaded successfully.")
print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])
print("Number of features:", X_train.shape[1])


# ==========================================
# 3. 模型 A：Logistic Regression
# ==========================================

classical_model = Pipeline(
    steps=[
        ("scaler", StandardScaler()),
        (
            "classifier",
            LogisticRegression(
                max_iter=2000,
                random_state=RANDOM_STATE
            )
        )
    ]
)

print("\nTraining Logistic Regression...")

classical_model.fit(X_train, y_train)

classical_predictions = classical_model.predict(X_test)

classical_accuracy = accuracy_score(
    y_test,
    classical_predictions
)

classical_f1 = f1_score(
    y_test,
    classical_predictions
)

print(
    f"Logistic Regression Accuracy: "
    f"{classical_accuracy:.4f}"
)

print(
    f"Logistic Regression F1 Score: "
    f"{classical_f1:.4f}"
)


# ==========================================
# 4. 模型 B：四层神经网络
# ==========================================

# 将标准化层包含在模型中，使模型文件可以独立使用
normalization_layer = tf.keras.layers.Normalization()
normalization_layer.adapt(X_train)

deep_model = tf.keras.Sequential(
    [
        tf.keras.layers.Input(
            shape=(X_train.shape[1],)
        ),

        normalization_layer,

        # 第一层隐藏层
        tf.keras.layers.Dense(
            64,
            activation="relu"
        ),

        # 第二层隐藏层
        tf.keras.layers.Dense(
            32,
            activation="relu"
        ),

        # 第三层隐藏层
        tf.keras.layers.Dense(
            16,
            activation="relu"
        ),

        # 输出层
        tf.keras.layers.Dense(
            1,
            activation="sigmoid"
        )
    ],
    name="breast_cancer_neural_network"
)

deep_model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor="val_loss",
    patience=10,
    restore_best_weights=True
)

print("\nTraining four-layer neural network...")

history = deep_model.fit(
    X_train,
    y_train,
    validation_split=0.20,
    epochs=100,
    batch_size=32,
    callbacks=[early_stopping],
    verbose=0
)

deep_probabilities = deep_model.predict(
    X_test,
    verbose=0
).ravel()

deep_predictions = (
    deep_probabilities >= 0.5
).astype("int32")

deep_accuracy = accuracy_score(
    y_test,
    deep_predictions
)

deep_f1 = f1_score(
    y_test,
    deep_predictions
)

print(
    f"Neural Network Accuracy: "
    f"{deep_accuracy:.4f}"
)

print(
    f"Neural Network F1 Score: "
    f"{deep_f1:.4f}"
)

print(
    "Neural Network epochs completed:",
    len(history.history["loss"])
)


# ==========================================
# 5. 比较模型并选择最佳模型
# ==========================================

model_results = {
    "logistic_regression": {
        "model_type": "classical_machine_learning",
        "accuracy": round(
            float(classical_accuracy),
            4
        ),
        "f1_score": round(
            float(classical_f1),
            4
        )
    },

    "neural_network": {
        "model_type": "deep_learning",
        "accuracy": round(
            float(deep_accuracy),
            4
        ),
        "f1_score": round(
            float(deep_f1),
            4
        ),
        "epochs_completed": len(
            history.history["loss"]
        )
    }
}

# 首先比较 Accuracy；相同时再比较 F1 Score
classical_score = (
    classical_accuracy,
    classical_f1
)

deep_score = (
    deep_accuracy,
    deep_f1
)

# 删除以前运行时可能产生的模型
for old_model_file in [
    CLASSICAL_MODEL_FILE,
    DEEP_MODEL_FILE
]:
    if os.path.exists(old_model_file):
        os.remove(old_model_file)


if classical_score >= deep_score:
    winner_name = "logistic_regression"
    winner_type = "classical_machine_learning"
    winner_file = CLASSICAL_MODEL_FILE
    winner_accuracy = classical_accuracy
    winner_f1 = classical_f1

    joblib.dump(
        classical_model,
        winner_file
    )

else:
    winner_name = "neural_network"
    winner_type = "deep_learning"
    winner_file = DEEP_MODEL_FILE
    winner_accuracy = deep_accuracy
    winner_f1 = deep_f1

    deep_model.save(
        winner_file
    )


# ==========================================
# 6. 保存实验指标
# ==========================================

metrics = {
    "dataset": "sklearn_breast_cancer",
    "selection_rule": (
        "Highest accuracy; F1 Score used as tie-breaker"
    ),
    "models": model_results,
    "winner": {
        "name": winner_name,
        "model_type": winner_type,
        "model_file": winner_file,
        "accuracy": round(
            float(winner_accuracy),
            4
        ),
        "f1_score": round(
            float(winner_f1),
            4
        )
    }
}

with open(
    METRICS_FILE,
    "w",
    encoding="utf-8"
) as metrics_output:
    json.dump(
        metrics,
        metrics_output,
        indent=4
    )


# ==========================================
# 7. 输出最终结果
# ==========================================

print("\n" + "=" * 55)
print("MODEL COMPARISON COMPLETE")
print("=" * 55)

print(
    f"Winning model: {winner_name}"
)

print(
    f"Winning Accuracy: "
    f"{winner_accuracy:.4f}"
)

print(
    f"Winning F1 Score: "
    f"{winner_f1:.4f}"
)

print(
    f"Saved model: {winner_file}"
)

print(
    f"Saved metrics: {METRICS_FILE}"
)
