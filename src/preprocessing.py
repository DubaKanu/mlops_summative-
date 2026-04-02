import tensorflow as tf
from tensorflow.keras.layers import RandomFlip, RandomRotation
from tensorflow.keras.models import Sequential
import numpy as np
from PIL import Image
import io

IMG_SIZE = (224, 224)
BATCH_SIZE = 32

data_augmentation = Sequential([
    RandomFlip('horizontal'),
    RandomRotation(0.2),
])


def load_datasets(data_dir):
    train_dataset = tf.keras.utils.image_dataset_from_directory(
        data_dir, validation_split=0.2, subset="training", seed=123,
        image_size=IMG_SIZE, batch_size=BATCH_SIZE
    )
    val_dataset = tf.keras.utils.image_dataset_from_directory(
        data_dir, validation_split=0.2, subset="validation", seed=123,
        image_size=IMG_SIZE, batch_size=BATCH_SIZE
    )
    AUTOTUNE = tf.data.AUTOTUNE
    train_dataset = train_dataset.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    val_dataset = val_dataset.cache().prefetch(buffer_size=AUTOTUNE)
    return train_dataset, val_dataset


def preprocess_image(file_bytes):
    img = Image.open(io.BytesIO(file_bytes)).convert("RGB").resize(IMG_SIZE)
    arr = np.array(img, dtype=np.float32)
    arr = np.expand_dims(arr, axis=0)
    return arr
