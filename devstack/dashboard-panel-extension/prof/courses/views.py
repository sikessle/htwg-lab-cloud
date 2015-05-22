from horizon import tables
import json
from .tables import CoursesTable
from .course import Course


class IndexView(tables.DataTableView):
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
