class Weight:
    def __init__(self,
                 W_conv1,
                 W_conv2,
                 W_fc1,
                 W_fc2):
        self.W_conv1 = W_conv1
        self.W_conv2 = W_conv2
        self.W_fc1 = W_fc1
        self.W_fc2 = W_fc2

class Placebundle:
    def __init__(self,
                 x,
                 y_,
                 W,
                 B,
                 keep_prob):
        self.x = x
        self.y_ = y_
        self.W = W
        self.B = B
        self.keep_prob = keep_prob