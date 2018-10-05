import frappe


no_cache = True

def get_context(context):
	context.settings = frappe.get_doc("CorpoWeb Settings")
