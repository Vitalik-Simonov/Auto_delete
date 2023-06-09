import os
import win10toast


toast = win10toast.ToastNotifier()
# toast.show_toast(title='Уведомление от чистильщика', msg='через 5 минут очистка', duration=7)
# time.sleep(3)
os.chdir(r'C:\Users\a320m\Desktop\only now')
try:
    os.mkdir('for delete')
except:
    pass

s = []
d = []

for dirpach, dirnames, filenames in os.walk(r'C:\Users\a320m\Desktop\only now'):
    for dirname in dirnames:
        s.append(os.path.join(dirpach, dirname))
    for filename in filenames:
        d.append(os.path.join(dirpach, filename))

for item in d:
    os.remove(item)
def whell():
    for dirpach, dirnames, filenames in os.walk(r'C:\Users\a320m\Desktop\only now'):
        for dirname in dirnames:
            s.append(os.path.join(dirpach, dirname))
            try:
                os.removedirs(s[-1])
            except:
                os.chdir(s[-1])

while os.listdir(r'C:\Users\a320m\Desktop\only now') != []:
    whell()
    try:
        os.removedirs(os.listdir(r'C:\Users\a320m\Desktop\only now'))
    except:
        pass

a = os.listdir(r'C:\Users\a320m\Desktop\only now')
# not
