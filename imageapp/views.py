from django.shortcuts import redirect, render
from imageapp.models import register
import os
# Create your views here.
def pdt(request):
 return render(request,'product.html')
def add(request):
   if request.method=='POST':
        pname=request.POST['productname']
        eqt=request.POST['Quantity']
        epr=request.POST['Price']
        image=request.FILES['file']
        epp=register(productname=pname,Quantity=eqt,Price=epr,image=image)
        print("save data")
        epp.save()
        return redirect('show')
def show(request):
   prdt=register.objects.all()
   return render(request,'show_product.html',{'ps':prdt})
def editpage(request,pk):
   prdt=register.objects.get(id=pk)
   return render(request,'edit.html',{'ps':prdt})
def edit_product(request,pk):
   if request.method=='POST':
      prdcts=register.objects.get(id=pk)
      prdcts.productname=request.POST.get('productname')
      prdcts.Quantity=request.POST.get('Quantity')
      prdcts.Price=request.POST.get('Price')
      if len(request.FILES)!=0:
         if len(prdcts.image)>0:
            os.remove(prdcts.image.path)
         prdcts.image=request.FILES['file']
      prdcts.save()
      return redirect('show')
   return render(request,'edit.html')
    
def delete(request,pk):
   p=register.objects.get(id=pk)
   p.delete()
   return redirect('show')
