class TreeSet:
        """docstring for TreeSet"""

        def __init__(self,Comparator = None):
                if Comparator != None:
                        self.Comparator = Comparator
                        self.flag = True
                else:
                        self.flag = False
                self.inner = []

        
        def add(self,element):

                for a in self.inner:
                        if self.flag == True:
                                if self.Comparator.compare(a,element) == 0:
                                        return 0
                        else:
                                if a.compare_to(element) == 0:
                                        return 0

                self.inner.append(element)
                self.sort()

        def sort(self):
                for time in range(1, len(self.inner)): 
                        for i in range(0,len(self.inner)-1): 
                                if self.flag == True:
                                        if self.Comparator.compare(self.inner[i],self.inner[i+1])>0:
                                                self.inner[i],self.inner[i+1] = self.inner[i+1],self.inner[i]
                                else:
                                        if self.inner[i].compare_to(self.inner[i+1])>0:
                                                self.inner[i],self.inner[i+1] = self.inner[i+1],self.inner[i]
                                
        def to_string(self):
                for a in self.inner:
                        print str(a)

class ComparatorDNI:
        """docstring for ComparatorDNI"""

        def compare(self,person1,person2):
                return cmp(person1.dni,person2.dni)


class Person:
        """docstring for Person"""
        def __init__(self,name,surname,dni):
                self.name = name
                self.surname = surname
                self.dni = dni

        def compare_to(self,other):
                a = cmp(self.surname,other.surname)
                if a!=0 :
                        return cmp(self.name,other.name)
                return a

        def __str__(self):
                return "Person: " + self.name + " " + self.surname + " " + self.dni

#testing
c = ComparatorDNI()
dnis = TreeSet(c)

persons = TreeSet()
print "DNIs: "
print "adding Paquito Rodriguez"
p = Person("Paquito","Rodriguez","45678912H")
dnis.add(p)
print "adding Paquito Rodriguez"
p = Person("Paquito","Rodriguez", "45678912H")
dnis.add(p)
print "adding Manuel Perez"
p = Person("Manuel","Perez","59456886A")
dnis.add(p)
print "adding Ana Martinez"
p = Person("Ana","Martinez","47781499G")
dnis.add(p)
print "adding Ana Martinez"
p = Person("Ana","Martinez","47781499G")
dnis.add(p)
print "adding Laura Lopez"
p = Person("Laura","Lopez","28899932D")
dnis.add(p)
print "Result: (the first and the penultimate have been introduced 2 times, only have to see once)"
dnis.to_string()

print "PERSONS: "
print "adding Manuel Perez"
p = Person("Manuel","Perez","59456886A")
persons.add(p)
print "adding Ana Martinez"
p = Person("Ana","Martinez","47781499G")
persons.add(p)
print "adding Ana Martinez"
p = Person("Ana","Martinez","47781499G")
persons.add(p)
print "adding Paquito Rodriguez"
p = Person("Paquito","Rodriguez","45678912H")
persons.add(p)
print "adding Paquito Rodriguez"
p = Person("Paquito","Rodriguez", "45678912H")
persons.add(p)
print "adding Laura Lopez"
p = Person("Laura","Lopez","28899932D")
persons.add(p)

print "Result:"
persons.to_string()
