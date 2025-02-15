# Generated by Django 4.2.4 on 2023-12-07 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("apppedidosnow", "0013_entregapedido_itensentregapedido"),
    ]

    operations = [
        migrations.CreateModel(
            name="Entrega",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("endereco", models.TextField()),
                (
                    "taxa_entrega",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(1, "Pendente"), (2, "Entregue")], default=1
                    ),
                ),
                ("cliente", models.CharField(max_length=200)),
                (
                    "bairro",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="apppedidosnow.bairro",
                    ),
                ),
                (
                    "motoboy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="apppedidosnow.motoboy",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ItensEntrega",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantidade", models.IntegerField(default=1)),
                ("preco_item", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "entrega",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="itens_entrega",
                        to="apppedidosnow.entrega",
                    ),
                ),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="apppedidosnow.produto",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="itensentregapedido",
            name="entrega_pedido",
        ),
        migrations.RemoveField(
            model_name="itensentregapedido",
            name="produto",
        ),
        migrations.DeleteModel(
            name="EntregaPedido",
        ),
        migrations.DeleteModel(
            name="ItensEntregaPedido",
        ),
    ]
