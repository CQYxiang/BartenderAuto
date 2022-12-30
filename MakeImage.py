from pywinauto import application, keyboard, mouse
import os
import time


def setVersion(version):
    mouse.click(button='left', coords=(500, 900))
    keyboard.send_keys("^a")
    keyboard.send_keys("^a")
    time.sleep(1)
    # {Alt Enter} Open Setting Version Window
    keyboard.send_keys("%{ENTER}")
    time.sleep(5)
    keyboard.send_keys("z")
    time.sleep(2)
    # 版本归到自动
    keyboard.send_keys("{VK_HOME}")
    time.sleep(2)
    # setting Code Version
    # if version == DMRectVersion[0]:
    #     for i in range(26):
    #         print(i)
    #         keyboard.send_keys("{DOWN}")
    #         # time.sleep(1)
    if version in DMRectVersion:
        for i in range(26+DMRectVersion.index(version)):
            DMRectVersion.index(version)
            keyboard.send_keys("{DOWN}")

    time.sleep(1)
    keyboard.send_keys("{ENTER}")
    time.sleep(2)


def outputImage(imgname, coderesult):
    # select Code
    mouse.click(button='left', coords=(500, 900))
    keyboard.send_keys("^a")
    # write result
    keyboard.send_keys("{ENTER}")
    time.sleep(2)
    keyboard.send_keys(coderesult)
    time.sleep(2)
    keyboard.send_keys("{ENTER}")
    # output images
    time.sleep(2)
    mouse.click(button='left', coords=(500, 900))
    keyboard.send_keys("^e")
    time.sleep(2)
    keyboard.send_keys("{ENTER}")
    time.sleep(2)
    keyboard.send_keys(imgname)
    time.sleep(2)
    keyboard.send_keys("{ENTER}")


if __name__ == "__main__":
    '''
    Datamatrix rect 

    '''
    app = application.Application("uia").start(
        "D:\\Program Files (x86)\\BarTender\\bartend.exe /F=\"DMRectauto.btw\"")
    DMRectVersion = ['8x18', '8x32', '12x26', '12x36', '16x36', '16x48']
    print(app)
    keyboard.send_keys("{F3}")
    time.sleep(5)
    imgname = "12x26.bmp"
    coderesult = "12x26"
    # .btw version = Auto
    version = "12x26"

    setVersion(version)
    outputImage(imgname, coderesult)

    time.sleep(1)
    os.system("taskkill /F /IM bartend.exe")
