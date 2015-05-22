from django.utils.translation import ugettext_lazy as _

from horizon import tables

class CoursesTable(tables.DataTable):
    name = tables.Column('name', \
                         verbose_name=_("Name"))
    description = tables.Column('description', \
                           verbose_name=_("Description"))
    id = tables.Column('id', \
                         verbose_name=_("ID"))
    enabled = tables.Column('enabled', \
                               verbose_name=_("Enabled"))

    class Meta:
        name = "coursesTbl"
        verbose_name = _("Courses")
