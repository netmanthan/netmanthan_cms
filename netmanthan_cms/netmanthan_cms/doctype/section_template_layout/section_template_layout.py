# Copyright (c) 2022, netmanthan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import json

class SectionTemplateLayout(Document):
	def validate(self):
		pass
	def on_update(self):
		try:
			if self.layout_json and len(self.layout_json) > 0:
				if self.type and self.type == 'Speciality Section': 
					save_flag = 0
					# frappe.log_error(type(self.layout_json),"<< before load json type>>")
					local_layout_json = json.loads(self.layout_json)
					# frappe.log_error(type(local_layout_json),"<< json loads type>>")
					for each_row in local_layout_json:
						if not each_row.get('u_id'):
							each_row['u_id'] = get_random_unique_id()
							save_flag=1
						for each_col in each_row.get('columns'):
							if not each_col.get('u_id'):
								each_col['u_id'] = get_random_unique_id()
								save_flag=1
							for each_col_row in each_col.get('rows'):
								if not each_col_row.get('u_id'):
									each_col_row['u_id'] = get_random_unique_id()
									save_flag=1
								for each_col_row_col in each_col_row.get('columns'):
									if not each_col_row_col.get('u_id'):
										each_col_row_col['u_id'] = get_random_unique_id()
										save_flag=1
				if self.type and self.type == 'Regular Section':
					save_flag = 0
					local_layout_json = json.loads(self.layout_json)
					for each_row in local_layout_json:
						if not each_row.get('u_id'):
							each_row['u_id'] = get_random_unique_id()
							save_flag=1
						
				# frappe.log_error(json.dumps(local_layout_json),">> final data<<")
				if save_flag:
					self.layout_json = json.dumps(local_layout_json)
					self.save()
		except Exception:
			frappe.log_error(frappe.get_traceback(),"netmanthan_cms.netmanthan_cms.doctype.section_template_layout.section_template_layout.on_update")
			frappe.throw("Error in Layout Json..!")
def get_random_unique_id():
		import string
		import random
		res = ''.join(random.choices(string.ascii_lowercase, k = 8))	
		return res


@frappe.whitelist()
def get_layout_data():
	try:
		final_data ={}
		Speciality_Section=[]
		Regular_Section=[]
		import json
		query_1 = ''' SELECT name,layout_json,preview,title,type FROM `tabSection Template Layout` WHERE type="Speciality Section"'''
		data_1 = frappe.db.sql(query_1,as_dict=1)
		for k in data_1:
			Speciality_Section.append({"unique_id":k.name,"title":k.title,"preview_image":k.preview,"layout_json":json.loads(k.layout_json) if len(k.layout_json) > 0 else []})
		query_2 = ''' SELECT name,layout_json,preview,title,type FROM `tabSection Template Layout` WHERE type="Regular Section"'''
		data_2 = frappe.db.sql(query_2,as_dict=1)
		for k in data_2:
			Regular_Section.append({"unique_id":k.name,"title":k.title,"preview_image":k.preview,"layout_json":json.loads(k.layout_json) if len(k.layout_json) > 0 else []})
		final_data['section_template']=get_page_section()
		final_data['Regular_Section']=Regular_Section
		final_data['Speciality_Section']=Speciality_Section
		return final_data
	except Exception:
		frappe.log_error(frappe.get_traceback(),"netmanthan_cms.netmanthan_cms.doctype.section_template_layout.section_template_layout.get_layout_data")

def get_page_section():
	device_type = "Web & Mobile"
	template_groups = frappe.db.sql("SELECT group_name FROM `tabSection Template Group` where name<>'Footer' AND name <>'Page List Style' ",as_dict=1)
	templates = frappe.db.sql('''select name, image ,section_group from `tabSection Template` where ((section_group<>'Footer' AND section_group <>'Page List Style') or section_group is null) and device_type in ("Web & Mobile", %(type)s)''', {'type': device_type}, as_dict=1)
	return {"template_groups":template_groups,"templates":templates}


@frappe.whitelist()
def get_each_layout_data(layout_id,page_route):
	try:
		final_data =[]
		import json
		query_1 = ''' SELECT name,layout_json,preview,title FROM `tabSection Template Layout` WHERE name="%s"'''%layout_id
		data = frappe.db.sql(query_1,as_dict=1)
		for k in data:
			page_section = frappe.new_doc("Page Section")
			page_section.section_title = k.title
			page_section.layout_json = k.layout_json
			page_section.section_type = "Static Section"
			page_section.allow_update_to_style = 1
			page_section.layout_id = layout_id
			page_section.layout_type = frappe.db.get_value("Section Template Layout",layout_id,"type")
			style_fields = frappe.get_list("Field Types Property",filters={"field_type":"Page Section"},fields={"css_properties_list"})
			if style_fields:
				page_section.css_field_list = style_fields[0].css_properties_list
			page_section.insert()
			page_builder = frappe.db.get_all("Web Page Builder",filters={"route":page_route})
			if page_builder:
				p_builder = frappe.get_doc("Web Page Builder",page_builder[0].name)
				p_builder.append("web_section",{
					"allow_update_to_style": 1,
					"section":page_section.name,
					"section_title":k.title,
					"section_type": "Static Section"
				});
				p_builder.save(ignore_permissions=True)
			final_data.append({"page_section":page_section.name,"unique_id":k.name,"title":k.title,"preview_image":k.preview,"layout_json":json.loads(k.layout_json) if len(k.layout_json) > 0 else []})
		return final_data
	except Exception:
		frappe.log_error(frappe.get_traceback(),"netmanthan_cms.netmanthan_cms.doctype.section_template_layout.section_template_layout.get_each_layout_data")

@frappe.whitelist()
def save_predefined_section(layout_id,page_route):
	try:
		final_data =[]
		import json
		# query_1 = ''' SELECT name,layout_json,preview,title FROM `tabSection Template Layout` WHERE name="%s"'''%layout_id
		# data = frappe.db.sql(query_1,as_dict=1)
		# for k in data:
		from frappe.model.mapper import get_mapped_doc
		section = frappe.get_doc("Section Template",layout_id)
		page_section = get_mapped_doc("Section Template", layout_id, {
		"Section Template": {
			"doctype": "Page Section"
		},
		"Section Content":{
			"doctype": "Section Content"
		}
		}, None, ignore_permissions=True)
		page_section.section_title = layout_id
		# if section_name:
		# 	doc.section_title = section_name
		page_section.custom_title = layout_id
		page_section.choose_from_template = 1
		page_section.section_template = layout_id
		page_section.save(ignore_permissions=True)
		page_builder = frappe.db.get_all("Web Page Builder",filters={"route":page_route})
		if page_builder:
			p_builder = frappe.get_doc("Web Page Builder",page_builder[0].name)
			p_builder.append("web_section",{
				"allow_update_to_style": 1,
				"section":page_section.name,
				"section_title":layout_id,
				"section_type": "Static Section"
			});
			p_builder.save(ignore_permissions=True)
		final_data.append({"page_section":page_section.name,"unique_id":layout_id,"title":layout_id,"preview_image":section.image,"layout_json":[]})
		return final_data
	except Exception:
		frappe.log_error(frappe.get_traceback(),"netmanthan_cms.netmanthan_cms.doctype.section_template_layout.section_template_layout.get_each_layout_data")