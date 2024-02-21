import roslib
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv


if __name__ == '__main__':
    
    # 初始化节点
    rospy.init_node('turtle_tf_listener')
    
    # 在(4, 2, 0)创建第二只海龟
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(4, 2, 0, 'turtle2')
    
    # 发布海龟2速度
    turtle_vel = rospy.Publisher('turtle2/cmd_vel', geometry_msgs.msg.Twist,queue_size=1)
    
    # 创建tf监听器
    listener = tf.TransformListener()
    
    # 循环频率10.0
    rate = rospy.Rate(10.0)
    
    while not rospy.is_shutdown():
        try:
            # 查询海龟1和海龟2之间的平移和旋转关系
            (trans,rot) = listener.lookupTransform('/turtle2', '/turtle1', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        
        # 角速度
        angular = 4 * math.atan2(trans[1], trans[0])
        # 线速度
        linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
        
        # 发布
        cmd = geometry_msgs.msg.Twist()
        cmd.linear.x = linear
        cmd.angular.z = angular
        turtle_vel.publish(cmd)

        rate.sleep()