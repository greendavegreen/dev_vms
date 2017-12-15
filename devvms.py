from errbot import BotPlugin, botcmd, arg_botcmd
import requests
import json

class DevVms(BotPlugin):
    """
    DevVms offers status about developer vms created in vmsareus
    """
    CONFIG_TEMPLATE = {'API_HOST': 'vmsareus.lebanon.cd-adapco.com'}

    def get_configuration_template(self):
        return self.CONFIG_TEMPLATE

    @botcmd(split_args_with=None)
    def vm_list(self, message, args):

        url = 'http://%s/api/vms' % self.config['API_HOST']
        response = requests.get(url)
        r = response.json()
        s = 'created   owner   branch   \n\r'
        for item in r:
            s +=  '%s %s %s \n\r' % (item.get('created'), item.get('owner'), item.get('branch'))
        return s