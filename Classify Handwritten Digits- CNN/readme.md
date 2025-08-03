[⬅️ Back to Main Page](../)

## Handwritten Digit Classification
This project recognizes handwritten digits using the MNIST dataset. After scaling the images and converting labels, I trained a compact two-block Convolutional Neural Network (CNN) with dropout and max-pooling. The model achieved 99 percent accuracy in under ten epochs. A confusion matrix showed that the digits 2 and 4 are still challenging, indicating areas for future improvement. The result is a lightweight, high-accuracy classifier that can be useful for any analytics team.

## Summary
- Data processed: Images normalized to [0, 1] range and labels one-hot encoded.
- Model: Two-block CNN with max pooling, dropout, and dense layers for classification.
- Performance: Achieved 99% test accuracy in fewer than 10 epochs.
- Analysis: Confusion matrix revealed that distinguishing between 2s and 4s is more challenging than other digits.

## Limitations & Next Steps
- Model occasionally confuses digits that are visually similar (notably 2 and 4).
- Real-world handwritten data may differ from MNIST, so testing on other datasets would be valuable.
