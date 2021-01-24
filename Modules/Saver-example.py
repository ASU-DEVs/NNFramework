from saver import *
from Preprocessing import *
from model import *

def main():
    
    _, _, testFeatures, testLabels, _ = preprocessing_online('MNIST')
         
    loaded_model = saver.restore()
        
    pred = loaded_model.predict(testFeatures.T)
    accuracy = accuracy_metrics(pred.T, testLabels.T) * 100
    print(f"\nThe accuracy rate of TEST DATASET is: {accuracy:.2f}%.")
    

if __name__ == "__main__":
    main()