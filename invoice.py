# coding: utf8
from flask.views import View
from flask import render_template
from models.invoice import InvoiceModel


class Invoice(View):

    def list_invoices(self):
        invoices_ok = []
        invoices_todo = []
        return render_template(
            'invoice.html',
            current_page='invoice',
            invoices_ok=invoices_ok,
            invoices_todo=invoices_todo
        )

    def edit_invoice(self, student_id, lesson_id):
        invoice_id = InvoiceModel().get_invoice(student_id, lesson_id)
        return render_template(
            'invoice_edit.html',
            current_page='invoice',
            invoice_id=invoice_id
        )
