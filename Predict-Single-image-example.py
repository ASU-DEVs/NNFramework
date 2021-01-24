from modules.saver import *
from modules.Preprocessing import *
from modules.model import *


def main():
    
         
    loaded_model = saver.restore()
    
    loaded_model.predict_ext_image("J:/College/Projects/Neurals/NNFrameWork/MyModel/Images/mnist3.png")

    
if __name__ == "__main__":
    main()
    