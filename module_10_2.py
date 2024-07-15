import time
from threading import Thread

class Knight(Thread):

    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(self.name+', на нас напали!')
        count_war = 100
        count_day = 0

        for i in range(count_war):
            count_war -= self.power
            count_day += 1
            time.sleep(1)
            if count_war < 0:
                break


            print(self.name+' сражается '+str(count_day)+' дней(день), осталось '+str(count_war)+' воинов.')

        print(self.name+' одержал победу спустя '+str(count_day-1)+' дней!')

Knight1 = Knight('Keny', 20)
Knight2 = Knight('Harry', 10)
Knight1.start()
Knight2.start()
Knight1.join()
Knight2.join()
print('Битвы закончились!')
