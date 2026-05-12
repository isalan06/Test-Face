# USB Camera 人脸识别项目 - 备忘录

## 项目目标
使用 Python 通过 USB 摄像头进行人脸识别

## 第一阶段：摄像头打开和显示

### 所需的 pip3 套件

```bash
# 核心包
pip3 install opencv-python     # OpenCV - 计算机视觉库
pip3 install opencv-contrib-python  # OpenCV 额外模块（可选）
```

### 测试步骤

1. **确保 USB 摄像头已连接**
   ```bash
   # macOS: 检查摄像头设备
   ls /dev/video*
   
   # 或使用 FFmpeg 检查
   ffmpeg -f avfoundation -list_devices true -i ""
   ```

2. **运行摄像头显示程序**
   ```bash
   cd /Users/alanhuang/Desktop/Program/Test/Test-Face/
   python3 camera_display.py
   ```

3. **程序操作说明**
   - `q` 键：退出程序
   - `ESC` 键：退出程序
   - `s` 键：保存截图（保存为 `screenshot_[帧数].png`）

4. **预期结果**
   - 打开一个窗口显示实时摄像头画面
   - 显示当前帧数和分辨率
   - 程序响应按键命令

---

## 第二阶段：人脸识别（待开发）

### 所需的额外 pip3 套件

```bash
# 人脸检测与识别
pip3 install face-recognition      # 人脸识别库
pip3 install dlib                   # 深度学习库（face-recognition 的依赖）
pip3 install numpy                  # 数值计算库
pip3 install Pillow                 # 图像处理库（可选）
pip3 install matplotlib             # 数据可视化（可选）
```

### 备注
- `dlib` 的安装可能需要 C++ 编译器，可能需要较长时间
- 如果遇到问题，可以使用替代方案如 `mediapipe` 或 `tensorflow`

---

## 完整的一键安装命令

```bash
pip3 install opencv-python face-recognition dlib numpy Pillow matplotlib
```

---

## 文件结构

```
Test-Face/
├── README.md                 # 项目说明
├── Memo.md                   # 本文件 - 项目备忘录
├── camera_display.py         # 第一阶段：摄像头显示程序
└── (待添加人脸识别程序)
```

---

## 常见问题排查

| 问题 | 解决方案 |
|------|--------|
| 摄像头无法打开 | 检查 USB 摄像头是否正确连接，确保没有其他程序占用摄像头 |
| ImportError: No module named 'cv2' | 运行 `pip3 install opencv-python` |
| 视频显示缓慢 | 尝试降低分辨率或检查系统资源占用 |
| 保存的截图显示为黑屏 | 确保摄像头已正确初始化，稍等几帧后再保存 |

---

## 后续改进计划

- [ ] 实现人脸检测功能
- [ ] 实现人脸识别功能
- [ ] 添加人脸标记和标签
- [ ] 人脸库管理
- [ ] 实时性能优化
