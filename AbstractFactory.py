class AbstractFactory:
        """docstring for AbstractFactory"""
        def __init__(self,flag):
                if flag == 0:
                        self.factory = WindowsFactory()
                else:
                        self.factory = LinuxFactory()

        def create_button(self):
                return self.factory.create_button()

        def create_text(self,text):
                return self.factory.create_text(text)

class WindowsFactory:
        """docstring for WindowsFactory"""
        def create_button(self):
                b = ButtonWindows()
                return b.click()
        def create_text(self,text):
                b = textWindows()
                return b.set_text(text)

class ButtonWindows:
        """docstring for ButtonWindows"""
        def click(self):
                return "a Windows button has been pressed"

class textWindows:
        """docstring for textWindows"""
        def set_text(self,text):
                return text + "text on Windows!"

class LinuxFactory:
        """docstring for LinuxFactory"""
        def create_button(self):
                b = ButtonLinux()
                return b.click()
        def create_text(self,text):
                b = textLinux()
                return b.set_text(text)

class ButtonLinux:
        """docstring for ButtonLinux"""
        def click(self):
                return "a Linux button has been pressed"

class textLinux:
        """docstring for textLinux"""
        def set_text(self,text):
                return text + "text on Linux!"


# testing
# Windows Factory
factory = AbstractFactory(0)
print str(factory.create_button())
print str(factory.create_text("Hello Windows!"))
# Linux Factory
factory = AbstractFactory(1)
print str(factory.create_button())
print str(factory.create_text("Hello Linux!"))