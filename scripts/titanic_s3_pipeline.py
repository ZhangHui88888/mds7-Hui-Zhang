from pathlib import Path
import os
import urllib.request

import boto3
import pandas as pd


# Fill these in locally if you want to match the professor's notebook style.
# Do not commit real keys to GitHub.
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
REGION_NAME = "eu-north-1"
BUCKET_NAME = "mds7-hui-zhang-titanic"

RAW_URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
RAW_FILENAME = "titanic_raw.csv"
DOWNLOADED_FILENAME = "downloaded_titanic.csv"
CLEAN_FILENAME = "titanic_clean.csv"
TARGET_FOLDER = "week-03-04-powerbi"


def clean_titanic_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()

    cleaned["Age"] = cleaned["Age"].fillna(cleaned["Age"].median())
    cleaned["Embarked"] = cleaned["Embarked"].fillna(cleaned["Embarked"].mode()[0])

    if "Cabin" in cleaned.columns:
        cleaned = cleaned.drop(columns=["Cabin"])

    cleaned = pd.get_dummies(cleaned, columns=["Sex", "Embarked"], drop_first=True)

    for column in ["Sex_male", "Embarked_Q", "Embarked_S"]:
        if column not in cleaned.columns:
            cleaned[column] = False

    dummy_columns = ["Sex_male", "Embarked_Q", "Embarked_S"]
    cleaned[dummy_columns] = cleaned[dummy_columns].astype(int)

    return cleaned


def get_setting(name: str, default: str = "") -> str:
    return os.environ.get(name, default).strip()


def create_s3_client():
    access_key = get_setting("AWS_ACCESS_KEY_ID", AWS_ACCESS_KEY_ID)
    secret_key = get_setting("AWS_SECRET_ACCESS_KEY", AWS_SECRET_ACCESS_KEY)
    region = get_setting("AWS_DEFAULT_REGION", REGION_NAME)

    if access_key and secret_key:
        return boto3.client(
            "s3",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region,
        )

    return boto3.client("s3", region_name=region)


def require_bucket_name() -> str:
    bucket_name = get_setting("S3_BUCKET_NAME", BUCKET_NAME)
    if not bucket_name:
        raise ValueError(
            "Missing S3 bucket name. Fill BUCKET_NAME in this script or set "
            "the S3_BUCKET_NAME environment variable."
        )
    return bucket_name


def main() -> None:
    bucket_name = require_bucket_name()
    s3_client = create_s3_client()
    project_root = Path(__file__).resolve().parents[1]
    target_dir = project_root / TARGET_FOLDER
    target_dir.mkdir(exist_ok=True)

    raw_path = project_root / RAW_FILENAME
    downloaded_path = project_root / DOWNLOADED_FILENAME
    clean_path = target_dir / CLEAN_FILENAME

    print(f"Downloading raw Titanic data to '{raw_path.name}'...")
    urllib.request.urlretrieve(RAW_URL, raw_path)

    print(f"Uploading '{RAW_FILENAME}' to S3 bucket '{bucket_name}'...")
    s3_client.upload_file(str(raw_path), bucket_name, RAW_FILENAME)
    print("Raw upload complete.")

    print("Downloading raw data from S3 for processing...")
    s3_client.download_file(bucket_name, RAW_FILENAME, str(downloaded_path))

    df = pd.read_csv(downloaded_path)
    print(f"Original Data Shape: {df.shape}")

    df_clean = clean_titanic_data(df)
    print(f"Clean Data Shape: {df_clean.shape}")

    df_clean.to_csv(clean_path, index=False)

    print(f"Uploading engineered data ('{CLEAN_FILENAME}') back to S3...")
    s3_client.upload_file(str(clean_path), bucket_name, CLEAN_FILENAME)
    print("Engineered upload complete.")

    print(f"Clean file saved locally: {clean_path}")


if __name__ == "__main__":
    main()
