#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2019 Wuhan PS-Micro Technology Co., Itd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rospy, sys
import moveit_commander
from geometry_msgs.msg import PoseStamped, Pose


class MoveItIkDemo:
    def __init__(self):
        # 初始化move_group的API
        moveit_commander.roscpp_initialize(sys.argv)
        
        # 初始化ROS节点
        rospy.init_node('moveit_ik_demo')
      
                
        # 初始化需要使用move group控制的机械臂中的arm group
        arm = moveit_commander.MoveGroupCommander('L_xarm')
        rarm = moveit_commander.MoveGroupCommander('R_xarm')
        gripper = moveit_commander.MoveGroupCommander('L_gripper')
        rgripper = moveit_commander.MoveGroupCommander('R_gripper')
        xarms = moveit_commander.MoveGroupCommander('xrams')
                
        # 获取终端link的名称
        end_effector_link = arm.get_end_effector_link()
        rend_effector_link = rarm.get_end_effector_link()
        xarms_effector_link = xarms.get_end_effector_link()
                        
        # 设置目标位置所使用的参考坐标系
        reference_frame = 'bottom_link'
        arm.set_pose_reference_frame(reference_frame)
        rarm.set_pose_reference_frame(reference_frame)
        xarms.set_pose_reference_frame(reference_frame)
                
        # 当运动规划失败后，允许重新规划
        arm.allow_replanning(True)
        rarm.allow_replanning(True)
        
        # 设置位置(单位：米)和姿态（单位：弧度）的允许误差
        rarm.set_goal_position_tolerance(0.001)
        rarm.set_goal_orientation_tolerance(0.001)
       
        # 设置允许的最大速度和加速度
        rarm.set_max_acceleration_scaling_factor(0.5)
        rarm.set_max_velocity_scaling_factor(0.5)

        # 控制机械臂先回到初始化位置
        #arm.set_named_target('home')
        #arm.go()
        #rospy.sleep(1)
               
        # 设置机械臂工作空间中的目标位姿，位置使用x、y、z坐标描述，
        # 姿态使用四元数描述，基于base_link坐标系


        rospy.set_param("lor",1)




        target_pose = PoseStamped()
        target_pose.header.frame_id = reference_frame
        target_pose.header.stamp = rospy.Time.now()     
        target_pose.pose.position.x = -0.0776
        target_pose.pose.position.y = 0.5
        target_pose.pose.position.z = 0.83
        target_pose.pose.orientation.x = 1.0
        target_pose.pose.orientation.y = 0.0
        target_pose.pose.orientation.z = 0.0
        target_pose.pose.orientation.w = 0.0
        
        # 设置机器臂当前的状态作为运动初始状态
        arm.set_start_state_to_current_state()
        
        # 设置机械臂终端运动的目标位姿
        arm.set_pose_target(target_pose, end_effector_link)
        
        # 规划运动路径
        traj = arm.plan()
        
        # 按照规划的运动路径控制机械臂运动
        arm.execute(traj)
        rospy.sleep(1)


        target_pose = PoseStamped()
        target_pose.header.frame_id = reference_frame
        target_pose.header.stamp = rospy.Time.now()     
        target_pose.pose.position.x = -0.0776
        target_pose.pose.position.y = 0.5
        target_pose.pose.position.z = 0.76
        target_pose.pose.orientation.x = 1.0
        target_pose.pose.orientation.y = 0.0
        target_pose.pose.orientation.z = 0.0
        target_pose.pose.orientation.w = 0.0

        # 设置机器臂当前的状态作为运动初始状态
        arm.set_start_state_to_current_state()
        
        # 设置机械臂终端运动的目标位姿
        arm.set_pose_target(target_pose, end_effector_link)
        
        # 规划运动路径
        traj = arm.plan()
        
        # 按照规划的运动路径控制机械臂运动
        arm.execute(traj)
        rospy.sleep(1)


        gripper.set_joint_value_target([0.67])
        gripper.go()
        rospy.sleep(1)


        target_pose = PoseStamped()
        target_pose.header.frame_id = reference_frame
        target_pose.header.stamp = rospy.Time.now()     
        target_pose.pose.position.x = -0.076
        target_pose.pose.position.y = -0.006
        target_pose.pose.position.z = 0.85
        target_pose.pose.orientation.x = 1.0

        # 设置机器臂当前的状态作为运动初始状态
        arm.set_start_state_to_current_state()
        
        # 设置机械臂终端运动的目标位姿
        arm.set_pose_target(target_pose, end_effector_link)
        
        # 规划运动路径
        traj = arm.plan()
        
        # 按照规划的运动路径控制机械臂运动
        arm.execute(traj)
        rospy.sleep(1)

        gripper.set_joint_value_target([0.1])
        gripper.go()
        rospy.sleep(1)





        target_pose = PoseStamped()
        target_pose.header.frame_id = reference_frame
        target_pose.header.stamp = rospy.Time.now()     
        target_pose.pose.position.x = -0.0776
        target_pose.pose.position.y = 0.5
        target_pose.pose.position.z = 0.83
        target_pose.pose.orientation.x = 1.0
        target_pose.pose.orientation.y = 0.0
        target_pose.pose.orientation.z = 0.0
        target_pose.pose.orientation.w = 0.0

        # 设置机器臂当前的状态作为运动初始状态
        arm.set_start_state_to_current_state()
        
        # 设置机械臂终端运动的目标位姿
        arm.set_pose_target(target_pose, end_effector_link)
        
        # 规划运动路径
        traj = arm.plan()
        
        # 按照规划的运动路径控制机械臂运动
        arm.execute(traj)
        rospy.sleep(1)



        rospy.set_param("lor",2)

        target_pose = PoseStamped()
        target_pose.header.frame_id = reference_frame
        target_pose.header.stamp = rospy.Time.now()     
        target_pose.pose.position.x = -0.0776
        target_pose.pose.position.y = 0
        target_pose.pose.position.z = 0.85
        target_pose.pose.orientation.x = 1.0
        target_pose.pose.orientation.y = 0.0
        target_pose.pose.orientation.z = 0.0
        target_pose.pose.orientation.w = 0.0

        # 设置机器臂当前的状态作为运动初始状态
        rarm.set_start_state_to_current_state()
        
        # 设置机械臂终端运动的目标位姿
        rarm.set_pose_target(target_pose, rend_effector_link)
        
        # 规划运动路径
        traj = rarm.plan()
        
        # 按照规划的运动路径控制机械臂运动
        rarm.execute(traj)
        rospy.sleep(1)


        target_pose = PoseStamped()
        target_pose.header.frame_id = reference_frame
        target_pose.header.stamp = rospy.Time.now()     
        target_pose.pose.position.x = -0.0776
        target_pose.pose.position.y = 0
        target_pose.pose.position.z = 0.76
        target_pose.pose.orientation.x = 1.0
        target_pose.pose.orientation.y = 0.0
        target_pose.pose.orientation.z = 0.0
        target_pose.pose.orientation.w = 0.0

        # 设置机器臂当前的状态作为运动初始状态
        rarm.set_start_state_to_current_state()
        
        # 设置机械臂终端运动的目标位姿
        rarm.set_pose_target(target_pose, rend_effector_link)
        
        # 规划运动路径
        traj = rarm.plan()
        
        # 按照规划的运动路径控制机械臂运动
        rarm.execute(traj)
        rospy.sleep(1)


        rgripper.set_joint_value_target([0.67])
        rgripper.go()
        rospy.sleep(1)

        target_pose = PoseStamped()
        target_pose.header.frame_id = reference_frame
        target_pose.header.stamp = rospy.Time.now()     
        target_pose.pose.position.x = -0.0776
        target_pose.pose.position.y = -0.5
        target_pose.pose.position.z = 0.85
        target_pose.pose.orientation.x = 1.0
        target_pose.pose.orientation.y = 0.0
        target_pose.pose.orientation.z = 0.0
        target_pose.pose.orientation.w = 0.0

        # 设置机器臂当前的状态作为运动初始状态
        rarm.set_start_state_to_current_state()
        
        # 设置机械臂终端运动的目标位姿
        rarm.set_pose_target(target_pose, rend_effector_link)
        
        # 规划运动路径
        traj = rarm.plan()
        
        # 按照规划的运动路径控制机械臂运动
        rarm.execute(traj)
        rospy.sleep(1)

      #   target_pose1 = PoseStamped()
      #   target_pose1.header.frame_id = reference_frame
       #  target_pose1.header.stamp = rospy.Time.now()     
        # target_pose1.pose.position.x = -0.0776
       #  target_pose1.pose.position.y = 0.5
       #  target_pose1.pose.position.z = 0.92
        # target_pose1.pose.orientation.x = 1.0
       #  target_pose1.pose.orientation.y = 0.0
       #  target_pose1.pose.orientation.z = 0.0
       #  target_pose1.pose.orientation.w = 0.0

        # 设置机器臂当前的状态作为运动初始状态
       #  xarms.set_start_state_to_current_state()
        
        # 设置机械臂终端运动的目标位姿
        # xarms.set_pose_target(target_pose, rend_effector_link)
       #  xarms.set_pose_target(target_pose1, end_effector_link)
        
        # 规划运动路径
       #  traj = xarms.plan()
        
        # 按照规划的运动路径控制机械臂运动
        #xarms.execute(traj)
        #rospy.sleep(1)


        rgripper.set_joint_value_target([0.1])
        rgripper.go()
        rospy.sleep(1)
           
        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__ == "__main__":
    MoveItIkDemo()

    
    
