from . import __version__ as app_version

app_name = "netmanthan_cms"
app_title = "netmanthan CMS"
app_publisher = "netmanthan"
app_description = "netmanthan CMS"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@netmanthan.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/netmanthan_cms/css/cms.css"
app_include_js = "/assets/netmanthan_cms/js/cms.js"




update_website_context = [
	"netmanthan_cms.netmanthan_cms.api.update_website_context",
]

# include js, css files in header of web template
# web_include_css = "/assets/netmanthan_cms/css/netmanthan_cms.css"
# web_include_js = "/assets/netmanthan_cms/js/netmanthan_cms.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "netmanthan_cms/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "netmanthan_cms.install.before_install"
# after_install = "netmanthan_cms.install.after_install"
after_install = "netmanthan_cms.netmanthan_cms.after_install.after_install"

# Uninstallation
# ------------

# before_uninstall = "netmanthan_cms.uninstall.before_uninstall"
# after_uninstall = "netmanthan_cms.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "netmanthan_cms.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Header Component": {
		"on_update": "netmanthan_cms.netmanthan_cms.api.update_web_themes",
	},
	"Footer Component": {
		"on_update": "netmanthan_cms.netmanthan_cms.api.update_web_themes",
	},
	"Web Page Builder": {
		"on_update": "netmanthan_cms.netmanthan_cms.api.update_web_themes",
	},
	"Color Palette": {
		"on_update": "netmanthan_cms.netmanthan_cms.api.update_web_themes",
	}	

}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"netmanthan_cms.tasks.all"
# 	],
# 	"daily": [
# 		"netmanthan_cms.tasks.daily"
# 	],
# 	"hourly": [
# 		"netmanthan_cms.tasks.hourly"
# 	],
# 	"weekly": [
# 		"netmanthan_cms.tasks.weekly"
# 	]
# 	"monthly": [
# 		"netmanthan_cms.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "netmanthan_cms.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "netmanthan_cms.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "netmanthan_cms.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"netmanthan_cms.auth.validate"
# ]
get_translated_dict = {
	("doctype", "Global Defaults"): "frappe.geo.country_info.get_translated_dict"
}
