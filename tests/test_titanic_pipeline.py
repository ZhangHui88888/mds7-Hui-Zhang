import pandas as pd

from scripts.titanic_s3_pipeline import clean_titanic_data


def test_clean_titanic_data_imputes_drops_and_encodes_columns():
    raw = pd.DataFrame(
        {
            "PassengerId": [1, 2, 3],
            "Survived": [0, 1, 1],
            "Pclass": [3, 1, 3],
            "Name": ["A", "B", "C"],
            "Sex": ["male", "female", "female"],
            "Age": [22.0, None, 26.0],
            "SibSp": [1, 1, 0],
            "Parch": [0, 0, 0],
            "Ticket": ["X", "Y", "Z"],
            "Fare": [7.25, 71.28, 7.92],
            "Cabin": [None, "C85", None],
            "Embarked": ["S", None, "C"],
        }
    )

    cleaned = clean_titanic_data(raw)

    assert "Cabin" not in cleaned.columns
    assert cleaned["Age"].isna().sum() == 0
    assert cleaned["Embarked_Q"].isna().sum() == 0
    assert cleaned["Embarked_S"].isna().sum() == 0
    assert "Sex_male" in cleaned.columns
    assert "Embarked_S" in cleaned.columns
    assert cleaned.loc[1, "Age"] == 24.0
