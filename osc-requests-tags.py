import osc.core
import osc.conf
import re

patterns = ["bsc#\w+"]

def do_requests_tags(self, subcmd, opts, project):
  """${cmd_name}: Lists requests with hashtags

  This command will list requests for a given project together
  with the list of hashtags in the request diff, so that you
  can use this information to group them.

  ${cmd_usage}
  ${cmd_option_list}
  """
  conf.get_config()
  api = self.get_api_url()
  requests = get_request_list(api, project = project, req_state =('new', 'review'))
  for request in requests:
    description = request.to_xml().findall("description")[0].text
    req_id = request.to_xml().get("id")
    req_diff = request_diff("https://api.suse.de", req_id)
    to_print = "id " + req_id
    for pattern in patterns:
      match = re.findall(pattern, req_diff)
      if len(match) > 0:
        to_print += str(match)
    print to_print

