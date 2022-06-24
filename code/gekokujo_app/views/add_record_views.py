from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models import ScoreTable
from ..forms import RecordsForm
#from django.http import HttpResponseRedirect

# from django.contrib import messages

# 成績登録処理


def addRecord(request):
    if request.method == 'POST':
        recordsform = RecordsForm(request.POST)
        if recordsform.is_valid():
            print('OK')
            recordsform.save()
        else:
            print(recordsform.errors.as_text())
            # print('form error')
            # return render(request, 'records.html')
    return redirect('showRecords')
    # redirect()
    # else:
    #     print(recordsform.errors)
    #     print(recordsform.errors.get_json_data())

    #     # メッセージだけ取り出す。
    #     values = recordsform.errors.get_json_data().values()

    #     for value in values:
    #         for v in value:
    #             messages.error(request, v["message"])

    # return redirect("bbs:index")


# def redirect():
#     scoretable = ScoreTable.objects.all()
#     context = {
#         'scoretable': scoretable,
#         'count': scoretable.count,
#     }
#     return redirect('showRecords')

# def add_record_views():
#     return redirect('showRecords')
