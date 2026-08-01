
# ==========================================
# 4. 自动化模型质量测试
# ==========================================

import json
import os

import joblib
import numpy as np
import tensorflow as tf

from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


RANDOM_STATE = 42
MINIMUM_ACCURACY = 0.85
METRICS_FILE = "metrics.json"


def load_metrics():
    """读取训练流程生成的模型指标。"""

    assert os.path.exists(METRICS_FILE), (
        "metrics.json does not exist. "
        "Run train.py before running the tests."
    )

    with open(
        METRICS_FILE,
        "r",
        encoding="utf-8"
    ) as file:
        return json.load(file)


def prepare_test_data():
    """使用与训练流程相同的方式准备测试数据。"""

    data = load_breast_cancer()

    X = data.data.astype("float32")
    y = data.target.astype("int32")

    _, X_test, _, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=RANDOM_STATE,
        stratify=y
    )

    return X_test, y_test


def test_metrics_structure():
    """检查 metrics.json 是否包含必要内容。"""

    metrics = load_metrics()

    assert "models" in metrics
    assert "winner" in metrics

    winner = metrics["winner"]

    required_fields = [
        "name",
        "model_type",
        "model_file",
        "accuracy",
        "f1_score"
    ]

    for field in required_fields:
        assert field in winner, (
            f"Missing winner field: {field}"
        )


def test_only_winning_model_is_saved():
    """确认只保存一个获胜模型。"""

    metrics = load_metrics()
    winner_file = metrics["winner"]["model_file"]

    assert os.path.exists(winner_file), (
        f"Winning model file does not exist: "
        f"{winner_file}"
    )

    generated_models = [
        filename
        for filename in [
            "best_model.pkl",
            "best_model.h5"
        ]
        if os.path.exists(filename)
    ]

    assert len(generated_models) == 1, (
        "Exactly one winning model must be saved."
    )

    assert generated_models[0] == winner_file


def test_winning_accuracy_threshold():
    """阻止准确率低于 85% 的模型通过 CI。"""

    metrics = load_metrics()
    winner_accuracy = metrics["winner"]["accuracy"]

    assert winner_accuracy >= MINIMUM_ACCURACY, (
        f"Winning model accuracy "
        f"{winner_accuracy:.4f} is below "
        f"the required threshold "
        f"{MINIMUM_ACCURACY:.2f}."
    )


def test_saved_model_can_be_loaded_and_used():
    """重新加载模型并验证实际预测准确率。"""

    metrics = load_metrics()
    winner = metrics["winner"]

    model_file = winner["model_file"]
    model_type = winner["model_type"]

    X_test, y_test = prepare_test_data()

    if model_type == "classical_machine_learning":
        model = joblib.load(model_file)
        predictions = model.predict(X_test)

    elif model_type == "deep_learning":
        model = tf.keras.models.load_model(
            model_file
        )

        probabilities = model.predict(
            X_test,
            verbose=0
        ).ravel()

        predictions = (
            probabilities >= 0.5
        ).astype("int32")

    else:
        raise ValueError(
            f"Unsupported model type: {model_type}"
        )

    actual_accuracy = accuracy_score(
        y_test,
        predictions
    )

    assert actual_accuracy >= MINIMUM_ACCURACY

    assert np.isclose(
        actual_accuracy,
        winner["accuracy"],
        atol=0.001
    ), (
        "Saved model accuracy does not match "
        "metrics.json."
    )
