from mlforkids import MLforKidsImageProject

# treat this key like a password and keep it secret!
key = "8dc00c60-87c6-11eb-8ffd-ff79b8fb1ef086bda874-fde6-4455-b5ae-59aa4bce3387"
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