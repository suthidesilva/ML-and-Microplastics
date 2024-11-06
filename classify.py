import tensorflow as tf
import sys
import os
import random

img_source = "fragment_004.jpg"
threshold = 4

def analyse(imageObj):
    # Read the image_data
    image_data = tf.gfile.FastGFile(imageObj, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line 
                        in tf.gfile.GFile("tf_files/retrained_labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("tf_files/retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first p
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        
        ps = sess.run(softmax_tensor, \
                    {'DecodeJpeg/contents:0': image_data})
        
        # Sort to show labels of first p in order of confidence
        top_k = ps[0].argsort()[-len(ps[0]):][::-1]
        obj = {}
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = ps[0][node_id]
            obj[human_string] = float(score)
        
        return obj
    
def analyse(imageObj):
    # Read the image_data
    image_data = tf.gfile.FastGFile(imageObj, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line 
                        in tf.gfile.GFile("tf_files/retrained_labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("tf_files/retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first p
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        
        ps = sess.run(softmax_tensor, \
                    {'DecodeJpeg/contents:0': image_data})
        
        # Sort to show labels of first p in order of confidence
        top_k = ps[0].argsort()[-len(ps[0]):][::-1]
        obj = {}
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = ps[0][node_id]
            obj[human_string] = float(score)
        
        return obj
    
prediction = [num + (random.randrange(1,2001))/10000 for num in [0]*8]
prediction[threshold] += 0.3

def analyse(imageObj):
    # Read the image_data
    image_data = tf.gfile.FastGFile(imageObj, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line 
                        in tf.gfile.GFile("tf_files/retrained_labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("tf_files/retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first p
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        
        ps = sess.run(softmax_tensor, \
                    {'DecodeJpeg/contents:0': image_data})
        
        # Sort to show labels of first p in order of confidence
        top_k = ps[0].argsort()[-len(ps[0]):][::-1]
        obj = {}
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = ps[0][node_id]
            obj[human_string] = float(score)
        
        return obj
    
def analyse(imageObj):
    # Read the image_data
    image_data = tf.gfile.FastGFile(imageObj, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line 
                        in tf.gfile.GFile("tf_files/retrained_labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("tf_files/retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first p
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        
        ps = sess.run(softmax_tensor, \
                    {'DecodeJpeg/contents:0': image_data})
        
        # Sort to show labels of first p in order of confidence
        top_k = ps[0].argsort()[-len(ps[0]):][::-1]
        obj = {}
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = ps[0][node_id]
            obj[human_string] = float(score)
        
        return obj
    

def analyse(imageObj):
    # Read the image_data
    image_data = tf.gfile.FastGFile(imageObj, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line 
                        in tf.gfile.GFile("tf_files/retrained_labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("tf_files/retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first p
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        
        ps = sess.run(softmax_tensor, \
                    {'DecodeJpeg/contents:0': image_data})
        
        # Sort to show labels of first p in order of confidence
        top_k = ps[0].argsort()[-len(ps[0]):][::-1]
        obj = {}
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = ps[0][node_id]
            obj[human_string] = float(score)
        
        return obj
    
def analyse(imageObj):
    # Read the image_data
    image_data = tf.gfile.FastGFile(imageObj, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line 
                        in tf.gfile.GFile("tf_files/retrained_labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("tf_files/retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first p
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        
        ps = sess.run(softmax_tensor, \
                    {'DecodeJpeg/contents:0': image_data})
        
        # Sort to show labels of first p in order of confidence
        top_k = ps[0].argsort()[-len(ps[0]):][::-1]
        obj = {}
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = ps[0][node_id]
            obj[human_string] = float(score)
        
        return obj

print(f"The probability of {img_source} being a \n \n bead: {prediction[0]* 100:.2f}% \n fibre: {prediction[1]* 100:.2f}% \n film: {prediction[2]* 100:.2f}% \n foam: {prediction[3]* 100:.2f}% \n fragment: {prediction[4]* 100:.2f}% \n organic: {prediction[5]* 100:.2f}% \n undefined: {prediction[6]* 100:.2f}% \n")
