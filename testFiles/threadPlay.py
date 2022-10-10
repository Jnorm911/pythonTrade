import threading as t
import page1
import page2

t.Thread(target=page1.num2).start()
t.Thread(target=page2.num1).start()


    