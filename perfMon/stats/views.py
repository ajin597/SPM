from django.shortcuts import render
from .models import Stats
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
import io
import base64
from django.http import HttpResponse
from django.db import OperationalError

matplotlib.use('Agg')  # Use non-interactive backend
# Create your views here.

def formatDate(date):
    dt = datetime.strptime(date, "%Y-%m-%dT%H:%M")
    dateTime = dt.strftime("%Y-%m-%d %H:%M:%S")
    return dateTime

def genarateStats(request):
    chart = None

    from_date = request.POST.get("from_date")
    to_date = request.POST.get("to_date")
    

    if request.method == 'POST':

        parameter = request.POST.getlist('parameter')

        try:
            data = Stats.objects.filter(
                time__gte=formatDate(from_date),
                time__lte=formatDate(to_date)
            ).order_by('time')

            timestamps = [d.time for d in data]        
            chart = {}
            for x in parameter:
                values = [getattr(d, x) for d in data]

                plt.figure(figsize=(10, 4))
                plt.plot(timestamps, values, marker=',',color='b')
                plt.title(f"{x.replace('_', ' ').title()} from {from_date} to {to_date}",fontdict ={'family':'serif','color':'blue','size':20})
                plt.xlabel("Time", fontdict = {'family':'serif','color':'darkred','size':15})
                plt.ylabel(x.replace('_', ' ').title(), fontdict = {'family':'serif','color':'darkred','size':15})
                plt.xticks(rotation=45)
                plt.tight_layout()

                buf = io.BytesIO()
                plt.savefig(buf, format='png')
                buf.seek(0)
                image_base64 = base64.b64encode(buf.read()).decode('utf-8')
                buf.close()
                chart[x] = image_base64
                plt.close()

        except OperationalError as e:
            message = f"Unable to connect to the DB server. Please try again.[ERROR]:{str(e)}"
            return render(request, 'index.html', {"message" : message})

    return render(request, 'index.html', {"chart" : chart})