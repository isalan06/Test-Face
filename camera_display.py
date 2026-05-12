#!/usr/bin/env python3
"""
USB Camera 打开和显示程序
使用 OpenCV 打开 USB 摄像头并实时显示视频流
"""

import cv2
import sys


def open_camera_and_display():
    """打开 USB 摄像头并显示视频"""
    
    # 打开默认摄像头 (0 表示第一个摄像头)
    cap = cv2.VideoCapture(0)
    
    # 检查摄像头是否成功打开
    if not cap.isOpened():
        print("错误: 无法打开 USB 摄像头")
        print("请检查摄像头是否正确连接")
        sys.exit(1)
    
    print("✓ USB 摄像头已打开")
    print("按 'q' 键或 ESC 退出程序")
    print("按 's' 键保存截图")
    
    frame_count = 0
    
    while True:
        # 读取摄像头的一帧
        ret, frame = cap.read()
        
        if not ret:
            print("错误: 无法读取摄像头帧")
            break
        
        frame_count += 1
        
        # 获取帧的宽度和高度
        height, width = frame.shape[:2]
        
        # 在帧上添加信息文字
        cv2.putText(frame, f"Frame: {frame_count}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, f"Resolution: {width}x{height}", (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # 显示帧
        cv2.imshow("USB Camera - Press 'q' to Exit", frame)
        
        # 捕获按键
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q') or key == 27:  # 'q' 或 ESC 键
            print("\n程序已退出")
            break
        elif key == ord('s'):  # 's' 键保存截图
            filename = f"screenshot_{frame_count}.png"
            cv2.imwrite(filename, frame)
            print(f"✓ 截图已保存: {filename}")
    
    # 释放摄像头和关闭窗口
    cap.release()
    cv2.destroyAllWindows()
    print("摄像头已关闭")


if __name__ == "__main__":
    open_camera_and_display()
