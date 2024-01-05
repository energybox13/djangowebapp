from django.shortcuts import render, redirect
from .models import *
import os
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3



def cricket(request):
    if request.method=="POST":
        Player_Name=request.POST.get("player_name")
        fifty=request.POST.get("fiftees")
        hundred=request.POST.get("hundreds")
        wicket=request.POST.get("wickets")
        avg=eval(request.POST.get("average"))
        c_image=request.FILES.get('image')
        ivideos=request.FILES.get('videos')
        cric_stats.objects.create(player_name=Player_Name,
                                  fiftees=fifty,
                                  hundreds=hundred,
                                  wickets=wicket,
                                  average=avg, photo=c_image,
                                  video=ivideos
                                  )
        print(c_image)
        # cricket_data_p = cric_stats.objects.all()
        # data2={
        #     'cdata':cricket_data_p
        # }
        return redirect('/cricket/')  
    cricket_data = cric_stats.objects.all()
    data3={
               'cdata':cricket_data
           }
    return render(request,'crickets.html',data3)




def cal(request):
    c=''
    data2={}
    n1=0
    n2=0
    try:
        if request.method=="GET":
            n1=eval(request.GET.get('num1'))
            n2=eval(request.GET.get('num2'))
            opr=(request.GET.get('opr'))
            if opr=="+":
                c=f"SUM = {n1+n2}"
            elif opr=="-":
                c=f"SUB = {n1-n2}"
            elif opr=="*":
                c=f"MUL = {(n1*n2)}"
            elif opr=="/":
                c=f"QUO = {n1/n2}"
            elif opr =="P/L":
                if n2 > n1:
                    profit = n2 - n1
                    if n2 != 0:
                        profit_per = ((n2 - n1) / n2) * 100
                        c = f"Profit = {profit} and Profit % = {profit_per}"
                    else:
                        c = "Cannot calculate profit percentage"
                elif n1>n2 :
                    loss = n1- n2
                    if n2 != 0:
                        loss_per = ((n1 - n2) / n2) * 100
                        c = f"Loss = {loss} and Loss % = {loss_per}"
                    else:
                        c = "Cannot calculate loss percentage"

            elif opr=="E/D":
                 if(n1==0 and n2==0):
                    c=f"Invalid input you have entered {n1} and {n2}"
                 elif(n1%2==0 and n2%2==0):
                    c=f"Both {n1} and {n2} are even"
                 elif(n1%2==0 and n2%2!=0):
                    c=f"{n1} is even and {n2} is odd"
                 elif(n1%2!=0 and n2%2==0):
                    c=f"{n1} is odd and {n2} is even "
                 elif(n1==0 and n2==0):
                    c=f"Invalid input you have entered {n1} and {n2}"
                 else:
                    c=f"{n1} and {n2} are odd numbers"

        data2= {"n1":n1,"n2":n2,"cal":c}
    except:
        c="Invalid user input"

    return render(request,"calculator.html",data2)




    
   
