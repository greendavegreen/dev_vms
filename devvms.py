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
        """
        List current Vms inside vmsareus.
        """

        response = requests.get('http://%s/api/vms' % self.config['API_HOST'])
        s = 'created   owner   branch   \n\r'
        for item in response.json():
            s +=  '%s %s %s \n\r' % (item.get('created'), item.get('owner'), item.get('branch'))
        return s