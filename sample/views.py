from django.shortcuts import render
import pandas as pd 

from sqlalchemy import create_engine

def index(request):
    
  
      return  render(request,"index.html")

def save(request):

      geturl=request.POST.get('url')
      lenstr="C:/Users/ELCOT/Documents/"+geturl
      df = pd.read_csv (lenstr) 
        
      df.columns = [c.lower() for c in df.columns] 


      engine = create_engine('postgresql://postgres:12341234@localhost:5432/postgres')

      df.to_sql("sales_engine", engine)
     

      return render(request,"index.html")