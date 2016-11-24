'''
@author: Evegen
'''

#TODO 
#install plot via pip2.7
#do https://courses.edx.org/courses/course-v1:TUMx+AUTONAVx+2T2015/courseware/b25665183d4a495f879526eff50b9068/620b86a76124415698af9e8b0c6793c6/

from plot import plot

class UserCode:
    def __init__(self):
        # initialize data you want to store in this object between calls to the measurement_callback() method
        self.last_yaw = 0
        
    def measurement_callback(self, t, dt, navdata):
        """
        :param t: time since simulation start
        :param dt: time since last call to measurement_callback
        :param navdata: measurements of the quadrotor
        """
        # add your plot commands here
        # plot("roll", navdata.rotX);
        # plot("pitch", navdata.rotY);
        # plot("yaw", navdata.rotZ);
        yaw_vel = (navdata.rotZ - self.last_yaw) / dt
        self.last_yaw = navdata.rotZ
        plot("yaw velocity", yaw_vel)
        #plot("Vx", navdata.vx);
        #plot("Vy", navdata.vy);
        # plot("dT", dt);