import numpy as np 

def sample_Route():
  print("#######################################################################")
  print("For a 20 by 20 feet area")
  print("Scale:  | = 2 feet\n")

  # Prints # 20 feet
  print("                 # 20                __   __    __   __   __   __   __    __   __   __   End = [20, 20]\n")
  # Prints # 18 - 10
  for i in range(5):
    print("                 #",(18-i*2),"","|    |    |     |    |    |    |    |     |    |    |\n")
  
  # Prints # 10 - 2
  for j in range(4):
    print("                 #",(8-j*2), " ","|    |    |     |    |    |    |    |     |    |    |\n")
  
  # Prints # 0
  print("Start = [0,0] =  # 0                  __   __    __   __   __   __   __    __   __   __ \n")

  """ 
  #  20      __   __    __   __   __   __   __    __   __   __   
  #  18    |    |    |     |    |    |    |    |     |    |    |
  #  16    |    |    |     |    |    |    |    |     |    |    |
  #  14    |    |    |     |    |    |    |    |     |    |    |
  #  12    |    |    |     |    |    |    |    |     |    |    |
  #  10    |    |    |     |    |    |    |    |     |    |    |
  #  8     |    |    |     |    |    |    |    |     |    |    |
  #  6     |    |    |     |    |    |    |    |     |    |    |
  #  4     |    |    |     |    |    |    |    |     |    |    |
  #  2     |    |    |     |    |    |    |    |     |    |    |
  #  0      __   __    __   __   __   __   __    __   __   __
  """

def twenybytweny():
  j = 20
  for i in range(6):
    print("\n[0 ,",j,"]", "[2 ,",j,"]", "[4 ,",j,"]", "[6 ,", j ,"]", "[8 ,",j,"]" ,"[10 ," ,j ,"]"  ,"[12 ,",j,"]" ,"[14 ,",j,"]" ,"[16 ,",j,"]" ,"[18 ,",j,"]" ,"[20 ,",j,"]")
    j-=2
  
  for i in range(5):
    print("\n[0 ,",j," ]", "[2 ,",j," ]", "[4 ,",j,"] ", "[6 ,", j ," ]", "[8 ,",j," ]" ,"[10 ," ,j ," ]"  ,"[12 ,",j," ]" ,"[14 ,",j," ]" ,"[16 ,",j," ]" ,"[18 ,",j," ]" ,"[20 ,",j," ]")
    j-=2

def map():
  k = 9
  for i in range(10):
    print("\nA",k, "  B",k, "  C",k, "  D",k, "  E",k, "  F",k, "  G",k, "  H",k, "  I",k, "  J",k, "  K",k)
    k-= 1

def grid():
  # A = [A0, A1, A2, A3, A4, A5, A6, A7, A8, A9]
  # A9 = [0,18]
  #  ......
  # A1 = [0,2]
  # A0 = [0,0]
  ##########################################################################################################################
  """
    A 9   B 9   C 9   D 9 E 9   F 9   G 9   H 9   I 9   J 9   K 9
    A 8   B 8   C 8   D 8 E 8   F 8   G 8   H 8   I 8   J 8   K 8
    A 7   B 7   C 7   D 7 E 7   F 7   G 7   H 7   I 7   J 7   K 7
    A 6   B 6   C 6   D 6 E 6   F 6   G 6   H 6   I 6   J 6   K 6
    A 5   B 5   C 5   D 5 E 5   F 5   G 5   H 5   I 5   J 5   K 5
    A 4   B 4   C 4   D 4 E 4   F 4   G 4   H 4   I 4   J 4   K 4
    A 3   B 3   C 3   D 3 E 3   F 3   G 3   H 3   I 3   J 3   K 3
    A 2   B 2   C 2   D 2 E 2   F 2   G 2   H 2   I 2   J 2   K 2
    A 1   B 1   C 1   D 1 E 1   F 1   G 1   H 1   I 1   J 1   K 1
    A 0   B 0   C 0   D 0 E 0   F 0   G 0   H 0   I 0   J 0   K 0
  """
  A = np.array([ [0,0] , [0,2] , [0,4] , [0,6] , [0,8] , [0,10] ])
  
  B = np.array([ [2,10] , [2,8] , [2,6] , [2,4] , [2,2] , [2,0] ])
 
  C = np.array([ [4,0] , [4,2] , [4,4] , [4,6] , [4,8] , [4,10]  ])

  D = np.array([ [6,10] , [6,8] , [6,6] , [6,4] , [6,2] , [6,0] ])

  E = np.array([ [8,0] , [8,2] , [8,4] , [8,6] , [8,8] , [8,10] ])

  F = np.array([ [10,10] , [10,8] , [10,6] , [10,4] , [10,2] , [10,0] ])

  return [A, B, C, D, E, F];

# Go up
def wp_0():
  list = grid()
  wp0 = list[0]
  Lbx = 0 # sample left & right beacon values
  Lby = 0
  Rbx = 0
  Rby = 0
  Lb = np.array([Lbx,Lby])
  Rb = np.array([Rbx,Rby])

  print("######################################## ")
  print("Route A")
  # Route A = wp0 
  for i in range(6):
    
    # For the first route the X axis remains @ 0
    # while the Y axis slowly increases by 2 feet 
    Lby = i*2 
    Rby = i*2
    Lb = [Lbx,Lby]
    Rb = [Rbx,Rby]
    
    # Check if Left & Right beacon points with map 
    # start checking at the 0th point and increase by 2
    yen = np.equal(wp0[i],Lb) 
    yan = np.equal(wp0[i],Rb)
    
    if( (yen[0] and yan[0]) and (yen[1] and yan[1]) ):
      print("Map A = wp0")
      print("Wp = ", wp0[i])
      print("Lb = ", Lb)
      print("Rb = ", Rb)
      print("|")
      ### Turn on left and right motor
      # IR distance 
      ###################
      # Done with A = wp0
      ##################

# Go Down 
def wp_1():
  list = grid()
  wp1 = list[1]
  Lbx = 0 # sample left & right beacon values
  Lby = 0
  Rbx = 0
  Rby = 0
  Lb = np.array([Lbx,Lby])
  Rb = np.array([Rbx,Rby])
 
  print("######################################## ")
  print("Route B")
  for i in range(6):
    
    Lbx = 2
    Lby = 10 - i*2
    Rbx = 2
    Rby = 10 - i*2
    Lb = [Lbx,Lby]
    Rb = [Rbx,Rby]

    yen = np.equal(wp1[i], Lb)
    yan = np.equal(wp1[i], Rb)

    if( (yen[0] and yan[0]) and (yen[1] and yan[1]) ):
      print("Map B = wp1")
      print("Wp = ", wp1[i])
      print("Lb = ", Lb)
      print("Rb = ", Rb)
      print("|")

# Go Up
def wp_2():
  list = grid()
  wp2 = list[2]
  Lbx = 4 # sample left & right beacon values
  Lby = 0
  Rbx = 4
  Rby = 0
  Lb = np.array([Lbx,Lby])
  Rb = np.array([Rbx,Rby])

  # Route C = wp2 = list[2] 
  print("######################################## ")
  print("Route C")
  for i in range(6):
    Lby = i*2 
    Rby = i*2
    Lb = [Lbx,Lby]
    Rb = [Rbx,Rby]
    
    yen = np.equal(wp2[i],Lb) 
    yan = np.equal(wp2[i],Rb)
    
    if( (yen[0] and yan[0]) and (yen[1] and yan[1]) ):
      print("Map C = wp2")
      print("Wp = ", wp2[i])
      print("Lb = ", Lb)
      print("Rb = ", Rb)
      print("|")

# Go Down 
def wp_3():
  list = grid()
  wp3 = list[3]
  Lbx = 0 # sample left & right beacon values
  Lby = 0
  Rbx = 0
  Rby = 0
  Lb = np.array([Lbx,Lby])
  Rb = np.array([Rbx,Rby])

  # Route D = wp3 = list[3] 
  print("######################################## ")
  print("Route D")

  for i in range(6):
    Lbx = 6
    Rbx = 6
    Lby = 10 - i*2 
    Rby = 10 - i*2
    Lb = [Lbx,Lby]
    Rb = [Rbx,Rby]
    
    yen = np.equal(wp3[i],Lb) 
    yan = np.equal(wp3[i],Rb)

    
    if( (yen[0] and yan[0]) and (yen[1] and yan[1]) ):
      print("Map D = wp3")
      print("Wp = ", wp3[i])
      print("Lb = ", Lb)
      print("Rb = ", Rb)
      print("|")

# Go Up 
def wp_4():
  list = grid()
  wp4 = list[4]
  Lbx = 0 # sample left & right beacon values
  Lby = 0
  Rbx = 0
  Rby = 0
  Lb = np.array([Lbx,Lby])
  Rb = np.array([Rbx,Rby])

  # Route E = wp4 = list[4] 
  print("######################################## ")
  print("Route E")

  for i in range(6):
    Lbx = 8
    Rbx = 8
    Lby = i*2 
    Rby = i*2
    Lb = [Lbx,Lby]
    Rb = [Rbx,Rby]
    
    yen = np.equal(wp4[i],Lb) 
    yan = np.equal(wp4[i],Rb)

    
    if( (yen[0] and yan[0]) and (yen[1] and yan[1]) ):
      print("Map E = wp4")
      print("Wp = ", wp4[i])
      print("Lb = ", Lb)
      print("Rb = ", Rb)
      print("|")

# Go Down 
def wp_5():
  list = grid()
  wp5 = list[5]
  Lbx = 0 # sample left & right beacon values
  Lby = 0
  Rbx = 0
  Rby = 0
  Lb = np.array([Lbx,Lby])
  Rb = np.array([Rbx,Rby])
 
  print("######################################## ")
  print("Map F = wp5")
  print("Route F")
  for i in range(6):
    
    Lbx = 10
    Lby = 10 - i*2
    Rbx = 10
    Rby = 10 - i*2
    Lb = [Lbx,Lby]
    Rb = [Rbx,Rby]

    yen = np.equal(wp5[i], Lb)
    yan = np.equal(wp5[i], Rb)

    if( (yen[0] and yan[0]) and (yen[1] and yan[1]) ):
      
      print("Wp = ", wp5[i])
      print("Lb = ", Lb)
      print("Rb = ", Rb)
      print("|")


def horzMap():
  list = wayp()

  #########################
  # Left Beacon
  Lbx = 0    
  Lby = 0 
  Lb = np.array([Lbx , Lby])

  #########################
  # Right Beacon
  Rbx = 0       
  Rby = 0
  Rb = np.array([Rbx , Rby])

  #####################################
  Now = np.array([Lb , Rb])

  # Now[0] = Lb , Now[1] = Rb
  # list[0][0]) = > wp0[0] = [0,0] 
  T1 = np.equal(Now[0] , list[0][0])
  T2 = np.equal(Now[1] , list[0][0])
  print(T1)
  print(T2)

  #if(( np.equal(Now[0] , list[0][0]) ) and ( np.equal(Now[1] , list[0][0]) )) :
   # print("You are @ start")
  #else:
   # print("Where tf r u ?")
  
def main():
  #sample_Route()
  #twenybytweny()
  #map() 
  #grid()
  wp_0()
  wp_1()
  wp_2()
  wp_3()
  wp_4()
  wp_5()
  
main()