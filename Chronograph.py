import time
class Chronograph:
        """docstring for Chronograph"""
        def __init__(self):
                self.status = None
                self.start = 0
                self.stop = 0

        def get_time(self):
                return self.status.get_time()

        def start_chronograph(self):
                self.change_status(False)
                self.status.start_chronograph()
                
        def stop_chronograph(self):
                self.status.stop_chronograph()
                self.change_status(True)
        
        def change_status(self,stopped):
                if stopped:
                        self.status = Stopped(self.status.start)
                else:
                        self.status = Started()

class Started(Chronograph):
        """docstring for Started"""
        def __init__(self):
                self.start = time.time()

        def get_time(self):
                return time.time() - self.start

        def start_chronograph(self):
                self.status = Started()

        def stop_chronograph(self):
                self.status = Stopped(self.start)

class Stopped(Chronograph):
        """docstring for Stopped"""
        def __init__(self,start):
                self.stop = time.time()
                self.start = start

        def get_time(self):
                return self.stop - self.start

        def start_chronograph(self):
                self.status = Started()

        def stop_chronograph(self):
                raise Exception('Already stopped')

#testing

chrono = Chronograph()
print "Starts the chrono:"
chrono.start_chronograph()
time.sleep(10)
print "The chrono stops after 10 secs:"
chrono.stop_chronograph()
print str(chrono.get_time())
print "start the chrono again:"
chrono.start_chronograph()
print "Sleeps 3 segs"
time.sleep(3)
print str(chrono.get_time())
print "Sleeps another 2 segs"
time.sleep(2)
print "Stops the chrono"
chrono.stop_chronograph()
print str(chrono.get_time())
print "stop the chrono again, an exception must be raised"
chrono.stop_chronograph()
