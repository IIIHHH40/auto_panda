import pyautogui
import time
#直前にpandaにログインしていない場合のみ使用可
def panda_auto():
    #パスワード、ユーザーネームの入力を得る
    password=pyautogui.password(text="パスワード?",title="パスワード入力",default="",mask="*")
    if password is not None:
        print("パスワードが入力されました。")
        user_input=pyautogui.prompt(text="ユーザー名?",title="入力要求",default=" ")
        if user_input is not None:
            print("ユーザー名が入力されました")
        else:
            print("ユーザー入力がキャンセルされました。")
    else:
        print("パスワード入力がキャンセルされました")

    pyautogui.press("winleft")
    time.sleep(1.5)
    pyautogui.typewrite("klusis")
    pyautogui.press("enter")
    time.sleep(1.5)
    pyautogui.click(300,350)
    time.sleep(1.5)
    pyautogui.click(400,680)
    #2パターンある
    """
    もとからの入力を削除
    pyautogui.hotkey('ctrl', 'a')  # 全選択（macなら 'command', 'a'）
    pyautogui.press('delete') 
    """
    time.sleep(2)
    pyautogui.click(700,400)
    pyautogui.hotkey("ctrl","a")
    pyautogui.press("delete")
    pyautogui.typewrite(user_input)
    pyautogui.click(700,500)
    pyautogui.hotkey("ctrl","a")
    pyautogui.press("delete")
    pyautogui.typewrite(password)
    pyautogui.press("enter")
    time.sleep(1.5)
    pyautogui.click(1350,950)
    time.sleep(1.5)
    pyautogui.click(1800,150)  
    #panda側のログインをする
    time.sleep(1.5)
    pyautogui.click(800,700)
    pyautogui.hotkey("ctrl","a")
    pyautogui.press("delete")
    pyautogui.typewrite(user_input)
    time.sleep(1.5)
    pyautogui.click(800,750)
    pyautogui.hotkey("ctrl","a")
    pyautogui.press("delete")
    pyautogui.typewrite(password)
    pyautogui.press("enter")
    return 
        
    #pandaのユーザー名、パスワードをサイトに入力

    

panda_auto()