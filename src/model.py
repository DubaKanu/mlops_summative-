import os
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping
from src.preprocessing import data_augmentation, load_datasets

MODEL_PATH = os.environ.get("MODEL_PATH", "models/plant_disease_model.h5")
CLASS_NAMES = ["Potato___Early_blight", "Potato___Late_blight", "Potato___healthy"]


def build_model(num_classes=3):
    base_model = MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
    base_model.trainable = False

    inputs = tf.keras.Input(shape=(224, 224, 3))
    x = data_augmentation(inputs)
    x = tf.keras.applications.mobilenet_v2.preprocess_input(x)
    x = base_model(x, training=False)
    x = GlobalAveragePooling2D()(x)
    outputs = Dense(num_classes, activation='softmax')(x)

    model = Model(inputs, outputs)
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model


def retrain_model(data_dir, epochs=10):
    train_dataset, val_dataset = load_datasets(data_dir)

    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        # Unfreeze last 20 layers for fine-tuning on new data
        for layer in model.layers[-20:]:
            layer.trainable = True
        model.compile(optimizer=tf.keras.optimizers.Adam(1e-5),
                      loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    except Exception:
        model = build_model(num_classes=len(train_dataset.class_names))

    early_stop = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
    history = model.fit(train_dataset, validation_data=val_dataset,
                        epochs=epochs, callbacks=[early_stop])
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    model.save(MODEL_PATH)
    return history
