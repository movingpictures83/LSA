import sys
import numpy
import random


class LSAPlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')
      self.firstline = filestuff.readline()
      lines = []
      for line in filestuff:
         lines.append(line)

      self.m = len(lines)
      self.samples = []
      self.bacteria = self.firstline.split(',')
      print self.bacteria
      if (self.bacteria.count('\"\"') != 0):
         self.bacteria.remove('\"\"')
      self.n = len(self.bacteria)
      self.ADJ = []#numpy.zeros([self.m, self.n])
      self.results=[]
      i = 0
      for i in range(self.m):
            self.ADJ.append([])
            contents = lines[i].split(',')
            self.samples.append(contents[0])
            print i, self.n, len(contents)
            for j in range(self.n):
               value = float(contents[j+1].strip())
               self.ADJ[i].append(value)#[j] = value
      for i in range(self.n):
            self.results.append([])
            for j in range(self.n):
               if (i == j):
                  self.results[i].append(1)
               else:
                  self.results[i].append(0)
   
       # From Ruan et al, 2006
      for b1 in range(0, self.n):
        for b2 in range(b1+1, self.n):
          print "PAIR: ", b1, " AND ", b2
          #if (b1 != b2):
          self.P = []
          self.N = []
          for i in range(0, self.m+2):
             self.P.append([])
             self.N.append([])
             for j in range(0, self.m+2):
                self.P[len(self.P)-1].append(0)
                self.N[len(self.N)-1].append(0)
       
          for i in range(1, self.m+1):
             self.P[0][i] = 0
             self.N[0][i] = 0
             self.P[i][0] = 0
             self.N[i][0] = 0
       
          for i in range(1, self.m+1):
             for j in range(1, self.m+1):
                self.P[i+1][j+1] = max(0, self.P[i][j]+self.ADJ[i-1][b1]*self.ADJ[i-1][b2])
                self.N[i+1][j+1] = max(0, self.N[i][j]-self.ADJ[i-1][b1]*self.ADJ[i-1][b2])
       
          # Find maxP
          maxP = 0
          maxN = 0
          for i in range(1, self.m+1):
             if (max(self.P[i]) > maxP):
                maxP = max(self.P[i])
             if (max(self.N[i]) > maxN):
                maxN = max(self.N[i])
 
          maxScore = max(maxP, maxN)
          if (maxP - maxN < 0):
             maxScore *= -1
          self.results[b1][b2] = maxScore / float(self.m)
          self.results[b2][b1] = maxScore / float(self.m)

 
 
   def output(self, filename):
      filestuff2 = open(filename, 'w')
      
      filestuff2.write(self.firstline)
            
      for i in range(self.n):
         filestuff2.write(self.bacteria[i]+',')
         for j in range(self.n):
            filestuff2.write(str(self.results[i][j]))
            if (j < self.n-1):
               filestuff2.write(",")
            else:
               filestuff2.write("\n")



