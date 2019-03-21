__author__="Nightwish"
__title__="安卓CPU，内存监控工具"

# 通过adb命令，获取APP的CPU和内存占用，使用pyecharts库，生成测试结果图表
# 获取内存占用：
# adb shell dumpsys meminfo package_name
# 获取CPU占用：
# adb shell cat /proc/pid/stat