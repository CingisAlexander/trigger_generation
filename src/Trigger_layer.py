from tensorflow.keras.layers import Layer
import numpy as np
from  tensorflow.keras import backend as K

class Trigger(Layer):
  def __init__(self, **kwargs):
    super(Trigger, self).__init__(**kwargs)

  def build(self, input_shape):
    print(input_shape)
    self.mask1 = np.zeros(input_shape[1:])
    self.mask1 = K.variable(self.mask1, name = "mask")
    
    self.pattern = np.zeros(input_shape[1:])
    self.pattern = K.variable(self.pattern, name = "pattern")
    super(Trigger,self).build(input_shape)

  def call(self, x):
    #return x+self.mask1 
    return x*(K.ones_like(self.mask1)- self.mask1) + self.pattern*self.mask1