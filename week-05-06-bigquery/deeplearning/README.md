# Titanic Deep Learning Pipeline

## Project overview

This project transitions the Week 3-4 Titanic pipeline from classical machine
learning to deep learning. The cleaned Titanic dataset is pulled
programmatically from GitHub, prepared for neural-network training, and used
to compare two binary-classification models with different depths.

## Data source

- Repository: `ZhangHui88888/mds7-Hui-Zhang`
- Source file: `week-03-04-powerbi/titanic_clean.csv`
- Rows: 891
- Target: `Survived`

The following eight numeric features are used:

- `Pclass`
- `Age`
- `SibSp`
- `Parch`
- `Fare`
- `Sex_male`
- `Embarked_Q`
- `Embarked_S`

`PassengerId`, `Name`, and `Ticket` are excluded because they are identifiers
or unencoded text fields. Features are standardised using a scaler fitted only
on the training data.

## Data split

- Training set: 569 passengers
- Validation set: 143 passengers
- Test set: 179 passengers
- Random seed: 42
- Stratified split by `Survived`

## Models

### Three-layer neural network

Architecture:

`Dense(32, ReLU) -> Dense(16, ReLU) -> Dense(1, Sigmoid)`

- Trainable parameters: 833
- Test accuracy: 81.01%
- Precision: 0.8571
- Recall: 0.6087
- F1 score: 0.7119
- Test loss: 0.4614
- Artifact: `model_3_layers.h5`

### Five-layer neural network

Architecture:

`Dense(64, ReLU) -> Dense(32, ReLU) -> Dense(16, ReLU) -> Dense(8, ReLU) -> Dense(1, Sigmoid)`

- Trainable parameters: 3,329
- Test accuracy: 81.01%
- Precision: 0.8302
- Recall: 0.6377
- F1 score: 0.7213
- Test loss: 0.4560
- Artifact: `model_5_layers.h5`

## Training configuration

- Optimizer: Adam
- Loss function: Binary Crossentropy
- Maximum epochs: 100
- Batch size: 32
- Early stopping patience: 10
- Best validation-loss weights restored automatically

## Comparison and conclusion

Both models achieved the same test accuracy of 81.01%. The three-layer model
produced higher precision, while the five-layer model achieved higher recall,
a higher F1 score, and a slightly lower test loss. Because the Titanic target
is imbalanced, F1 score and recall provide important context beyond accuracy.
The five-layer model therefore provides the better overall balance for this
experiment, although the performance difference is small.

## Deployment targets

- GitHub: `week-05-06-bigquery/deeplearning/`
- AWS S3: `s3://mds7-hui-zhang-titanic/deeplearning/`

The notebook, both model artifacts, this README, and the repository audit
trail are intended to be published together after local verification.
