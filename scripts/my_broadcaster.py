import roslib
import rospy
import tf
import turtlesim.msg


def handle_turtle_pose(msg, turtlename):
    # msg：海龟的x、y、θ
    
    # 创建tf广播器
    br = tf.TransformBroadcaster()
    
    # 广播数据
    br.sendTransform((msg.x, msg.y, 0),
                     tf.transformations.quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     turtlename,
                     "world")


if __name__ == '__main__':
    
    # 初始化节点
    rospy.init_node('turtle_tf_broadcaster')

    # 获取海龟名
    turtlename = rospy.get_param('~turtle')
    
    # 订阅海龟位置 '海龟名/pose'
    rospy.Subscriber('/%s/pose' % turtlename,
                     turtlesim.msg.Pose,
                     handle_turtle_pose,
                     turtlename)
    
    # 阻塞等待callback
    rospy.spin()