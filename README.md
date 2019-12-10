# Face Orientation Resnet Project
## Results
**Face Orientation Classifier**
|  |  Up| Down | Left | Right | Total|
|--|--|--|--|--|--|
|Train Accuracy  |90%  | 80%| 60%|80% |100%|
|Validation Accuracy  |90%  | 80%| 60%|80% |100%|
These results come from running the Predict.ipynb notebook.

## Instructions

 1. Download the [CelebA Database](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html). This should be saved as "img_align_celeba".
 2. Run the ImageProcessor.py to convert the data into the correct size and folders. Note you will need to create the "processedImages/" folders. This includes a train and validate folder with the each label "up" , "down", "left" , and "right". **See Command #1 for help**.
 3. clone the github repo for [Tensorflow Models](https://github.com/tensorflow/models.git) and follow the instructions in the official folder README. This should be in the same folder as this repo.
 4. Run the build_image_data.py command using **Command #2**. The "tfRecords/" will also have to be created. With the latest Tensorflow binaries you will need to add the following lines to line 77-78.
`import tensorflow.compat.v1 as tf
tf.disable_eager_execution()`
 5. Download the latest model from the official/r1/resnet/ README. Rename this to "PreResNet/".
 6. Finally you can run the code using **Command #3**.  You will need to make the following changes.
	 1. Line 714 of resnet_run_loop.py change to `classifier.export_saved_model("results/", input_receiver_fn)`
	 2. Line 91 of imagenet_preprocessing.py comment out the random_flip_left_right flip code.
 7. Explore the data using the Predict.ipynb

## Commands

 1. mkdir -p processedImages/train/up && mkdir -p processedImages/train/down && mkdir -p processedImages/train/left && mkdir -p processedImages/train/right && mkdir -p processedImages/validate/up && mkdir -p processedImages/validate/down && mkdir -p processedImages/validate/left && mkdir -p processedImages/validate/right
 2. python models/research/inception/inception/data/build_image_data.py --train_directory processedImages/train/ --validation_directory processedImages/validate/ --output_directory tfrecords/ --labels_file labels.txt --train_shards 1024 --validation_shards 128
 3. python models/official/r1/resnet/imagenet_main.py --data_dir tfrecords/ --pretrained_model_checkpoint_path PreResNet --fine_tune False --rv 2 --export_dir results/ --train_epoch 10
