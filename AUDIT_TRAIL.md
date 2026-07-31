# MDS 7: Audit Trail
 
## Week 1: Environment Setup
* **Milestone:** Repository created and structured.
* **Notes:** Environment initialized and Professor invited.

## Week 2: Distributed Data & SQL
* **Date:** 2026-04-18
* **Milestone:** Uploaded the Central Park squirrel census dataset to the `week-02-sql` directory.
* **Notes:** Pushed the local SQL assignment data to the repository using Colab interactive upload.

## Week 3-4: Data Engineering & PowerBI Prep
* **Date:** 2026-04-25
* **Milestone:** Uploaded `titanic_clean.csv` to the `week-03-04-powerbi` directory.
* **Notes:** Built an ETL pipeline fetching raw Titanic data from AWS S3, engineered it in Colab (handling nulls and dummy variables), pushed the processed data back to S3, and synced it to GitHub for visualization in PowerBI.

## Week 3-4: Machine Learning
* **Date:** 2026-04-30 22:29:04
* **Milestone:** Trained and compared Logistic Regression and XGBoost models, then saved `Titanic_ML_Lecture4.ipynb` and `best_titanic_model.pkl` in `week-03-04-powerbi/machine_learning`.
* **Notes:** Used the cleaned Titanic data from AWS S3, evaluated the models with F1 score and confusion matrices, and retained the better-performing model.

## Week 5-6: Advanced Power BI & BigQuery Prep
* **Date:** 2026-05-06
* **Milestone:** Completed the Germany beverage sales pipeline and saved the cleaned data, notebook, Power BI report, and PDF in `week-05-06-bigquery/PowerBI`.
* **Notes:** Cleaned the Germany sales workbook with Pandas, added `Total Revenue`, synchronized the clean CSV with AWS S3 and GitHub, and connected Power BI to the GitHub raw-data URL.

## Week 5-6: Titanic Deep Learning Pipeline
* **Date:** 2026-05-14 17:39:22
* **Milestone:** Pulled the Week 3-4 clean Titanic dataset programmatically from GitHub, trained three-layer and five-layer neural networks, and saved `model_3_layers.h5`, `model_5_layers.h5`, `README.md`, and `titanic_dl_pipeline.ipynb` in `week-05-06-bigquery/deeplearning`.
* **Results:** Both models achieved 81.01% test accuracy. The three-layer model achieved 0.8571 precision, 0.6087 recall, and a 0.7119 F1 score. The five-layer model achieved 0.8302 precision, 0.6377 recall, and a 0.7213 F1 score with a lower test loss of 0.4560.
* **Notes:** The five-layer model provided the better overall balance based on recall, F1 score, and test loss. Both models used Adam, Binary Crossentropy, standardised numeric features, stratified data splits, and early stopping. All local artifacts are ready; GitHub and AWS S3 deployment is pending.

## Week 5-6: Computer Vision with Deep Learning
* **Date:** 2026-05-20 12:14:41
* **Milestone:** Trained and evaluated a custom CIFAR-10 CNN and saved the best model as `cifar_custom_cnn.h5` in the `week-05-06-bigquery/cifar_cnn` directory.
* **Results:** Achieved 69.79% test accuracy, 0.9085 test loss, and a 0.6938 macro F1 score. Early stopping restored the best model weights to reduce overfitting.
* **Notes:** Generated training curves, a confusion matrix, and a per-class classification report. Tested a real cat image with both the custom CNN and pre-trained MobileNetV2. The notebook, model, and README are prepared locally; GitHub and AWS S3 deployment is pending.

## Week 8: MLOps, CI/CD, Fork & Pull Request Workflow
* **Date:** 2026-05-27
* **Milestone:** Forked the baseline MLOps repository, implemented competing classical ML and deep-learning models, saved only the winning model, and added automated model tests and a GitHub Actions CI workflow.
* **Results:** Logistic Regression won with 98.25% accuracy and a 0.9861 F1 score; all four automated tests passed.
* **Notes:** The upgraded files are prepared in the forked project. The original assignment also requested pushing the feature branch and opening a pull request to the professor's repository.

## Week 10-12: Green AI Trade-Off
* **Date:** 2026-06-16
* **Milestone:** Completed the four-scenario Fashion-MNIST experiment comparing 50% versus 100% data and 50 versus 100 training epochs, with CodeCarbon emissions tracking.
* **Results:** `C_100pct_50epochs` was selected as the Green AI winner with 88.55% test accuracy and 3.664331 grams of CO2 emissions.
* **Notes:** Saved the executed notebook, experiment results, emissions logs, comparison plot, and conclusion in `week-10-12-async-lab`. The teacher confirmed that a normal GitHub push is sufficient and no pull request is required for this assignment.
