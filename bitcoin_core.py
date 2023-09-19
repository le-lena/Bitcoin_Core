import time
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import pyautogui
from datetime import datetime
import keyboard

file = open("C:\\Users\\Lena\\Downloads\\dict.txt", "r")  #путь на файл словаря, не забудьте его скорректировать
m = time.localtime().tm_min
stop = False
while True:
    if stop:
        break
    m = m - 1
    if m == 0:
        m = 59

    app = Application(backend="uia").start('C:\\Program Files\\Bitcoin\\bitcoin-qt')  # не забудьте проверить путь
    dlg_spec = app.window(title = 'Bitcoin Core - test4')  #test4-название кошелька, поменяйте на свое
    actionable_dlg = dlg_spec.wait('visible', timeout=20)
    w = dlg_spec.child_window(title="Window", control_type="MenuItem")
    w.click_input()
    dlg_spec.menu_select("Window->Console")
    dlg = app.top_window()
    text=dlg.child_window(auto_id="RPCConsole.tabWidget.qt_tabwidget_stackedwidget.tab_console.lineEdit", control_type="Edit")
    while True:
        line = file.readline().rstrip('\n')
        text.set_text('walletpassphrase '+"'"+line+"'" + ' 604800')
        text.type_keys('{ENTER}')
        if not line:
            stop=True
            local_time = datetime.now()
            screen = pyautogui.screenshot()
            file_path = r'C:\Users\Lena\Desktop\screen\screenshot' + "_" + str(local_time).replace(":", "_").replace(
                ".", "_") + ".png"  #путь на папку для сохранения скриншотов, поменяйте на свое
            screen.save(file_path)
            dlg.minimize()
            time.sleep(2)
            local_time = datetime.now()
            screen = pyautogui.screenshot()
            file_path = r'C:\Users\Lena\Desktop\screen\screenshot' + "_" + str(local_time).replace(":", "_").replace(
                ".", "_") + ".png" #путь на папку для сохранения скриншотов, поменяйте на свое
            screen.save(file_path)
            break
        if time.localtime().tm_min==m:
            local_time = datetime.now()
            screen = pyautogui.screenshot()
            file_path = r'C:\Users\Lena\Desktop\screen\screenshot' + "_" + str(local_time).replace(":", "_").replace(
                ".", "_") + ".png" #путь на папку для сохранения скриншотов, поменяйте на свое
            screen.save(file_path)
            dlg.minimize()
            time.sleep(2)
            local_time = datetime.now()
            screen = pyautogui.screenshot()
            file_path = r'C:\Users\Lena\Desktop\screen\screenshot' + "_" + str(local_time).replace(":", "_").replace(
                ".", "_") + ".png" #путь на папку для сохранения скриншотов, поменяйте на свое
            screen.save(file_path)
            dlg_spec.close()
            time.sleep(20)
            break
file.close



