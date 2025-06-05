import frappe

def criar_doctype():
    if not frappe.db.exists("DocType", "MeuDocType"):
        doc = frappe.get_doc({
            "doctype": "DocType",
            "name": "MeuDocType",
            "module": "Meu App",
            "custom": 1,
            "fields": [
                {"label": "Nome", "fieldname": "nome", "fieldtype": "Data"},
                {"label": "Descrição", "fieldname": "descricao", "fieldtype": "Text"}
            ],
            "permissions": [
                {"role": "System Manager", "read": 1, "write": 1, "create": 1, "delete": 1}
            ]
        })
        doc.insert()
        frappe.db.commit()
