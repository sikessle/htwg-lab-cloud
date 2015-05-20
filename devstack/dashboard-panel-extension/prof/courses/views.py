from horizon import tables
import json
from .tables import CoursesTable
from .course import Course


class CoursesTableView(tables.DataTableView):
    # A very simple class-based view...
    table_class = CoursesTable
    template_name = 'prof/courses/index.html'

    def get_data(self):
        dummyData = '[{"name": "WebTech", "description": "WebTechnologien", "id": 1, "enabled": "Yes"}, {"name": "DBSYS", "description": "Datenbanksysteme", "id": 2, "enabled": "No"},{"name": "CloudAppDev", "description": "Cloud Application Development", "id": 3, "enabled": "Yes"}]'
        instances = json.loads(dummyData)
        ret = []
        for inst in instances:
            ret.append(Course(inst['name'], inst['description'], inst['id'], inst['enabled']))
        return ret

'''
class CreateSnapshotView(forms.ModalFormView):
    form_class = project_forms.CreateSnapshot
    template_name = 'prof/courses/templates/courses/create_snapshot.html'
    success_url = reverse_lazy("horizon:project:images:index")
    modal_id = "create_snapshot_modal"
    modal_header = _("Create Snapshot")
    submit_label = _("Create Snapshot")
    submit_url = "horizon:prof:courses:create_snapshot"

    @memoized.memoized_method
    def get_object(self):
        try:
            return api.nova.server_get(self.request,
                                       self.kwargs["instance_id"])
        except Exception:
            exceptions.handle(self.request,
                              _("Unable to retrieve instance."))

    def get_initial(self):
        return {"instance_id": self.kwargs["instance_id"]}

    def get_context_data(self, **kwargs):
        context = super(CreateSnapshotView, self).get_context_data(**kwargs)
        instance_id = self.kwargs['instance_id']
        context['instance_id'] = instance_id
        context['instance'] = self.get_object()
        context['submit_url'] = reverse(self.submit_url, args=[instance_id])
        return context
'''





