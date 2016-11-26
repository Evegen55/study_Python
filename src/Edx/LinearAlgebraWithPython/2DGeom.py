'''
@author: Evegen

'''
import numpy as np

def experiments():
    print -np.sin(np.deg2rad(90))
    print np.cos(np.deg2rad(90)) #@see http://stackoverflow.com/questions/15980819/exact-sine-cosine-tangent-of-various-angles
    print np.cos(np.pi/2)
    print np.sin(np.pi/2)
    print np.sin(np.pi)


def createRotateMatrix(grad):
    theta = np.deg2rad(grad)
    #c, s = np.cos(theta), np.sin(theta) #first way with exactly 
    c, s = np.round(np.cos(theta), 5), np.sin(theta)
    return np.matrix('{} {}; {} {}'.format(c, -s, s, c))
    #R = np.matrix([[c, -s], [s, c]]) #the same thing

    
"""
Assume your robot flew 2 m in x direction, 3 m in y direction and turned 90 degrees (counterclockwise) around its yaw axis. 
Please enter the translation vector:
"""    
def translation_vector(distance_x, distanse_y):
    return np.array([[distance_x], [distanse_y]]) 

"""
Together, t and R form a homogeneous transformation matrix T10 transforming local into global coordinates. 
Please define the homogeneous transformation matrix:
x = 2
y = 3
theta = 90
"""
def homogeneous_trans_matrix(degree, distance_x, distanse_y):
    theta = np.deg2rad(degree)
    c, s = np.cos(theta), np.sin(theta)
    return np.matrix('{} {} {}; {} {} {}; {} {} {}'.format(c, -s,distance_x, s, c, distanse_y, 0, 0, 1))
   
    
"""
During the mission, the robot's pose is continuously reestimated relative to its last known pose.
The transformations describing the poses can simply be concatenated by multiplication to yield 
the transformation from local to global frame.

degree1 = 45, 
distance_x1 = 1, 
distanse_y1 = 2

degree2 = 45, 
distance_x2 = -4, 
distanse_y2 = 2
"""    
def transformation_concatenation():
    htm1 = homogeneous_trans_matrix(45, 1, 2)
    htm2 = homogeneous_trans_matrix(45, -4, 2)
    return htm1*htm2


"""
Often the robot has detected a marker in its local coordinate system and we want to know 
where the marker is on our global map. This can be achieved by finding the translation 
and rotation that transforms the global into the local coordinate system and applying it 
to our point of interest.
"""
def local_to_global_ransformation():
    Plocal = np.array([[1], [-1], [1]])
    Tglobal_local = np.array([[0, -1, -3], [1, 0, 3], [0, 0, 1]])
    return Tglobal_local.dot(Plocal)

"""
Moreover, we are often interested in reaching a goal position in the world coordinate frame 
but can only give local commands to the robot i.e. we need to translate the global 
to local commands in order to execute them. This can be achieved by applying the inverse rotation
"""
def global_to_local_transformation():
    R = np.array([[0, -1], [1, 0]])
    Vglobal = 1.5 #Now assume you want to fly in Y(!!!) direction of your GLOBAL coordinate frame with speed 1.5 m/s.
    TranslationVector = np.array([[0], [Vglobal]]) #first - X, second - Y
    return R.transpose().dot(TranslationVector) #return speed in LOCAL ROBOTS coordinate frame
    
    
    
#Test
print global_to_local_transformation()
print
print local_to_global_ransformation()
print
print transformation_concatenation()
print
print homogeneous_trans_matrix(90, 2, 3)
print
print "translation vector"
print  translation_vector(2,3)
print
print "rotate matrixes"
print createRotateMatrix(30)
print
print createRotateMatrix(45)
print
print createRotateMatrix(90)