# CIFAR-10 Convolutional Neural Network

## Project overview

This project implements and evaluates a custom Convolutional Neural Network
(CNN) for image classification using the CIFAR-10 dataset. It also compares
the custom model with a pre-trained MobileNetV2 model on a real-world image.

## Dataset

CIFAR-10 contains 60,000 colour images of size 32 x 32 pixels:

- 50,000 training images
- 10,000 test images
- 10 balanced classes: airplane, automobile, bird, cat, deer, dog, frog,
  horse, ship, and truck

Pixel values are converted to `float32` and normalised from 0-255 to 0-1.

## Custom CNN architecture

1. Conv2D with 32 filters and ReLU activation
2. MaxPooling2D
3. Conv2D with 64 filters and ReLU activation
4. MaxPooling2D
5. Flatten
6. Dense layer with 64 units and ReLU activation
7. Output layer with 10 logits

The model has 167,562 trainable parameters.

## Training configuration

- Optimizer: Adam
- Loss: Sparse Categorical Crossentropy (`from_logits=True`)
- Maximum epochs: 100
- Batch size: 64
- Early stopping patience: 8
- Best weights restored automatically

## Results

- Test accuracy: **69.79%**
- Test loss: **0.9085**
- Macro F1 score: **0.6938**
- Saved model size: **1.95 MB**

The strongest recall scores were achieved for truck, ship, automobile, frog,
and horse. Bird, cat, and dog were more difficult to distinguish because the
source images are low resolution and visually similar.

## Real-image comparison

A real cat image was used for inference:

- Custom CIFAR-10 CNN: `cat` at **43.26%**
- Pre-trained MobileNetV2: `tiger_cat` at **52.62%**

MobileNetV2 produced more specific predictions because it was pre-trained on
the larger ImageNet dataset.

## Artifact

The trained model is stored as:

`cifar_custom_cnn.h5`

## Deployment targets

- GitHub: `week-05-06-bigquery/cifar_cnn/`
- AWS S3: `s3://mds7-hui-zhang-titanic/deeplearning/`
