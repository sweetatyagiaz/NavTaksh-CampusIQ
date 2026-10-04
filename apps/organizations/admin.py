from django.contrib import admin

from .models import Board, School, SchoolBoardRegistration, SchoolBoardWithdrawal

admin.site.register([Board, School, SchoolBoardRegistration, SchoolBoardWithdrawal])