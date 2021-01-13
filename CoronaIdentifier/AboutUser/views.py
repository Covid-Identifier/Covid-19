from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import pandas as pd
from .models import MyResult
from django.views.generic.edit import CreateView, UpdateView


# Create your views here.
def Home(request):
    if not request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return HttpResponseRedirect('/test/')


@login_required
def Test(request):
    The_result = ''
    my_profile = MyResult.objects.get(user=request.user)
    y = request.POST.get('give_my_result')
    if request.method == 'POST':
        my_profile.result = y
        my_profile.save()
    if my_profile.result >= 27:
        The_result = 'Sorry to say, Higher chance of coronat. Visit doctor as soon as possible'
    if 16 <= my_profile.result <= 26:
        The_result = 'Not sure, we recomend you to visit Doctor and please be on quarentine'
    if my_profile.result <= 15:
        The_result = "Congratulation, right now you don't have corona. Please come back after 2 days to check here"

    context = {
        'Result': The_result
    }

    return render(request, 'test.html', context)


@login_required
def Base(request):
    contex = {
        'user': request.user
    }
    return render(request, 'base.html')


@login_required
def Visualization(request):
    countryNameSe = request.POST.get('country')
    Corona_update = pd.read_csv(
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',
        encoding='utf-8', na_values=None)
    last_column = Corona_update[Corona_update.columns[-1]]
    totalcase = last_column.sum()
    CountryAndNumber = Corona_update[['Country/Region', Corona_update.columns[-1]]].groupby('Country/Region').sum()

    CountryAndNumber = CountryAndNumber.reset_index()
    CountryAndNumber.columns = ['Country/Region', 'cases']
    CountryAndNumber = CountryAndNumber.sort_values(by='cases', ascending=False)
    countryName = CountryAndNumber['Country/Region'].values.tolist()
    countryCase = CountryAndNumber['cases'].values.tolist()

    countryDataSpe = pd.DataFrame(Corona_update[Corona_update['Country/Region'] == countryNameSe][
                                      Corona_update.columns[4:-1]].sum()).reset_index()

    countryDataSpe.columns = ['Country/Region', 'values']
    countryDataSpe['logVal'] = countryDataSpe['values'].shift(1).fillna(0)
    countryDataSpe['incrementVal'] = countryDataSpe['values'] - countryDataSpe['logVal']
    countryDataSpe['rollingMean'] = countryDataSpe['incrementVal'].rolling(window=4).mean()
    showMap = 'false'
    axisvalues = countryDataSpe.index.tolist()
    countryDataSpe = countryDataSpe.fillna(0)
    y = countryDataSpe['values'].values.tolist()

    datasetsForLine = [
        {'label': 'Daily Cumulated Data', 'data': countryDataSpe['values'].values.tolist(), 'borderColor': 'red',
         'backgroundColor': 'red', 'fill': 'false'},
        {'label': 'Rolling Mean 4 days', 'data': countryDataSpe['rollingMean'].values.tolist(), 'borderColor': 'blue',
         'backgroundColor': 'blue', 'fill': 'false'}

    ]

    context = {
        'totalcase': totalcase,
        'Name': countryName,
        'Case': countryCase,
        'showMap': showMap,
        'datasetsForLine': datasetsForLine,
        'countryName': countryNameSe,
        'axisvalues': axisvalues,
        'y': y

    }
    return render(request, 'visualization.html', context)


@login_required
def Profile(request):
    The_result = ''
    my_profile = MyResult.objects.get(user=request.user)
    y = request.POST.get('give_my_result')
    if request.method == 'POST':
        my_profile.result = y
        my_profile.save()
    if my_profile.result >= 27:
        The_result = 'Sorry to say, Higher chance of coronat. Visit doctor as soon as possible'

    if my_profile.result>=16 and my_profile.result<=26:
        The_result = 'Not sure, we recommend you to visit Doctor and please be on quarentine'
    if my_profile.result<=15:
        The_result = "Congratulation, right now you don't have corona. Please come back after 2 days to check here"

    context = {
        'Result': The_result
    }

    
    return render(request,'profile.html',context)

class profileEdit(UpdateView):
    model =  MyResult
    fields = ['result']
    template_name = 'ResultEdit.html'
    success_url = '/profile/'
    context_object_name = 'form'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def PK(request):
    current_user = request.user
    context = {
        'pk': current_user.id
    }
    return render(request, 'base.html',context)

