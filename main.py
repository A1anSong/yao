import time
import pyautogui
import random
import winsound
from PIL import Image

# 全局变量配置
confidence = 0.9
duration = 0.5

# 读取配置文件
descriptions = open('description.txt').readlines()  # 话术
choose_item = Image.open('common/choose_items.png')  # 读取物品选择界面的图片
return_choose = Image.open('common/return_choose.png')  # 读取退货选项界面的图片

return_reason_select = Image.open(
    'common/return_reason_select.png')  # 读取选择退货原因图片
return_reason = Image.open('common/return_reason.png')  # 读取退货原因图片
comments = Image.open('common/comments.png')  # 读取退货理由图片
continue_button = Image.open('common/continue.png')  # 读取继续图片

replace_option = Image.open('common/replace_option.png')  # 退货选项图片
other_option = Image.open('common/other_option.png')  # 其他选项图片

# item = Image.open('item.png')  # 读取物品图片


def moveToPos(img, name):
    imgPos = pyautogui.locateOnScreen(image=img, confidence=confidence)
    if imgPos != None:
        pyautogui.moveTo(pyautogui.center(imgPos), duration=duration)
        pyautogui.click()
        return True
    else:
        return False


if __name__ == '__main__':
    pyautogui.alert('点击OK开始摇')
    # 开始摇
    while True:
        time.sleep(5)
        if pyautogui.locateOnScreen(image=choose_item, confidence=confidence) != None:  # 选择商品界面
            # if moveToPos(img=item, name='商品图片'):  # 找到商品图片
            pyautogui.click(500, 330, duration=duration)
            if moveToPos(img=return_reason_select, name='选择退货原因图片'):  # 找选择退货原因图片
                moveToPos(img=return_reason, name='退货原因图片')  # 找退货原因图片
            if moveToPos(img=comments, name='退货理由图片'):  # 找退货理由图片
                pyautogui.typewrite(
                    descriptions[random.randint(0, len(descriptions)-1)])  # 输入退货理由
                moveToPos(img=continue_button, name='退货原因图片')  # 找继续图片

        # 退货选项界面
        elif pyautogui.locateOnScreen(image=return_choose, confidence=confidence) != None:
            moveToPos(img=other_option, name='其它选项')
            if pyautogui.locateOnScreen(image=replace_option, confidence=confidence) != None:
                winsound.Beep(600, 1000)
                time.sleep(3)
                break
            else:
                pyautogui.hotkey('alt', 'left')

        else:
            winsound.Beep(600, 1000)
