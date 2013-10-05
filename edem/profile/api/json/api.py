import json
from zope.formlib import form as formlib
from gs.content.form.api.json import SiteEndpoint
from zope.interface import Interface
from zope.schema import Text

class IGroupApiForm(Interface):
  textField = Text(title=u'Test', required=False)

class GroupApi(SiteEndpoint):

  def __init__(self, site, request):
    super(GroupApi, self).__init__(site, request)

  @property
  def form_fields(self):
    retval = formlib.Fields(IGroupApiForm, render_context=False)
    return retval

  @formlib.action(label=u'Submit', prefix='', failure='get_user_failure')
  def process(self, action, data):
    retval = {}
    retval['id'] = self.loggedInUser.id
    retval['url'] = self.loggedInUser.url
    retval['name'] = self.loggedInUser.name
    return json.dumps(retval)

  def get_user_failure(self, action, data, errors):
    return self.build_error_response(action, data, errors)
