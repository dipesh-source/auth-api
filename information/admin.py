from django.contrib import admin
from .models import Cities, Country, State, Person_info


class data_tabular(admin.TabularInline):
    model = State


class city_tabular(admin.TabularInline):
    model = Cities


@admin.register(Country)
class Country_data(admin.ModelAdmin):
    # inlines = [data_tabular]
    list_display = ("id", "user", "country_name", "population", "pm", "state")
    search_fields = ["country_name", "pm"]
    list_filter = ["country_name", "pm"]
    list_editable = ["user", "country_name", "population", "pm", "state"]
    ordering = ["country_name"]
    # pagination
    list_per_page = 10


@admin.register(State)
class State_data(admin.ModelAdmin):
    list_display = ["id", "user", "state_name", "cm", "food"]
    search_fields = ["state_name", "state_name"]
    list_editable = ["user", "state_name", "cm", "food"]


@admin.register(Cities)
class Cities_dat(admin.ModelAdmin):
    # inlines = [data_tabular]
    list_display = ("id", "user", "city_name", "area", "popular")
    search_fields = ["city_name", "area", "popular"]
    list_filter = ["city_name", "popular", "area"]
    list_editable = ["user", "city_name", "area", "popular"]
    ordering = ["city_name"]


@admin.register(Person_info)
class Person_data(admin.ModelAdmin):
    list_display = ["id", "name", "email", "age", "age", "city", "country"]
