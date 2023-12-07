from django.contrib import admin

from .models import Produto, Categoria, Pedido, ItensPedido, Bairro, Motoboy, Funcionario, Entrega, ItensEntrega

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("descricao",)
    search_fields = ("descricao",)
    list_filter = ("descricao",)
    ordering = ("descricao",)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria")
    search_fields = ("titulo", "categoria__descricao")
    list_filter = (
        "categoria",
    )
    ordering = ("titulo", "categoria")
    list_per_page = 25


class ItensPedidoInline(admin.TabularInline):
    model = ItensPedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    inlines = [ItensPedidoInline]

@admin.register(Bairro)
class BairroAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    list_filter = ("nome",)
    ordering = ("nome",)

@admin.register(Motoboy)
class MotoboyAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    list_filter = ("nome",)
    ordering = ("nome",)


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    list_filter = ("nome",)
    ordering = ("nome",)

class ItensEntregaInline(admin.TabularInline):
    model = ItensEntrega

@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    inlines = [ItensEntregaInline]

@admin.register(ItensEntrega)
class ItensEntregaAdmin(admin.ModelAdmin):
    list_display = ("entrega", "produto", "quantidade", "preco_item")
    search_fields = ("entrega__id", "produto__titulo")
    list_filter = ("entrega__id",)
    ordering = ("entrega__id",)