import math
def calcAngle(h,m): 
    if (h == 12): 
        h = 0
    if (m == 60): 
        m = 0
        
    # Calculate the angles moved by  
    # hour and minute hands with  
    # reference to 12:00 
    hour_angle = 0.5 * (h * 60 + m) 
    minute_angle = 6 * m 
        
    # Find the difference between two angles 
    angle = abs(hour_angle - minute_angle) 
        
    # Return the smaller angle of two  
    # possible angles 
    angle = min(360 - angle, angle) 
        
    return angle 


A,B,H,M = map(int,input().split())

angle = calcAngle(H,M)
angle_rag = math.radians(angle)
out = (A**2 + B**2 - 2 * A * B * math.cos(angle_rag))**0.5
print(out)