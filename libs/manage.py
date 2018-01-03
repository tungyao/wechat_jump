from wechat_jump.libs.adb_operations import adb
from wechat_jump.libs.calculation_pressure_time import calcula

press_time = calcula()

flag = True
while flag:
    command =input()
    press = adb()
    press_time.LENGTH = int(command)
    times = press_time.run()
    press.press(times)
    # if command =='1':
    #     press = adb()
    #     press_time.LENGTH = 20
    #     times = press_time.run()
    #     press.press(times)
    # elif command =='2':
    #     press = adb()
    #     press_time.LENGTH = 35
    #     times = press_time.run()
    #     press.press(times)
    # elif command =='3':
    #     press = adb()
    #     press_time.LENGTH = 45
    #     times = press_time.run()
    #     press.press(times)
    # elif command =='3':
    #     press = adb()
    #     press_time.LENGTH = 450
    #     times = press_time.run()
    #     press.press(times)
    # elif command =='3':
    #     press = adb()
    #     press_time.LENGTH = 450
    #     times = press_time.run()
    #     press.press(times)