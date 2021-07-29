from mlforkids import MLforKidsImageProject

# treat this key like a password and keep it secret!
#key from ml for kids
key = "key from ml for kids"
def create_model():
    myProject = MLforKidsImageProject(key)
    myProject.train_model()
    return myProject
myProject = create_model()
def model():
    return myProject
# this will train your model and might take a little while


# CHANGE THIS to the image file you want to recognize
# demo = myproject.prediction("my-test-image.jpg")

# label = demo["class_name"]
# confidence = demo["confidence"]

# CHANGE THIS to do something different with the result
# print ("result: '%s' with %d%% confidence" % (label, confidence))