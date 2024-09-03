import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

def classify_image(image_path):
    # Load your trained model
    model = tf.keras.models.load_model('path_to_your_model.h5')
    
    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(224, 224))  # Adjust target_size as needed
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize if required
    
    # Make prediction
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions[0])  # Get the class with the highest probability
    
    # Return the predicted class
    return predicted_class
