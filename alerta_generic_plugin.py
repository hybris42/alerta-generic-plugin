import logging
from alerta.plugins import PluginBase

LOG = logging.getLogger('alerta.plugins.alertagenericplugin')

class AlertaGenericPlugin(PluginBase):
    def pre_receive(self, alert):
        return alert

    def post_receive(self, alert):
        print(alert)
        return

    def status_change(self, alert, status, text):
        return
