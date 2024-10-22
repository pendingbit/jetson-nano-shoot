from time import sleep
from time import time


class trigger:
    def __init__(self, info, routine, period):
        self.info = info
        self.routine = routine
        self.period = period
        self.currentstatus = False
        self.laststatus = False
        self.triggerflag = False
    
    def getInfo(self):
        return self.info

    def getFlag(self):
        return self.triggerflag
    
    def clearFlag(self):
        self.triggerflag = False

    def task(self):
        while True:
            sleep(self.period)
            self.laststatus = self.currentstatus
            self.currentstatus = self.routine()
            if self.laststatus==False and self.currentstatus==True :
                self.triggerflag = True



###################Config trigger task######################    
count = 0
def period_update():
    global count
    count+=1
    if count > 99:
        print("trigger is True")
        count = 0
        return True
    else:
        return False

my_trigger = trigger("get trigger per 10s", period_update, 0.1)
###########################################################

def Trigger_GetFlag():
    return my_trigger.getFlag()

def Trigger_ClearFlag():
    my_trigger.clearFlag()

def Trigger_Task():
    my_trigger.task()

if __name__ == '__main__':
   Trigger_Task()
