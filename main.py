easy_peace= int(8)
tempo = int(6)
leaving_hour= int(6)
leaving_minute=int( 52)
easy_time= int(1+2)
tempo_time=int(3)
time_running=int(easy_peace*easy_time+tempo*tempo_time)
x= float(leaving_minute+time_running)-60
y=int(leaving_hour+1)
print()
print ("time is:",y,".",x )