import logging
from alerta.plugins import PluginBase
import os.path

logging.basicConfig(filename='/var/log/alerta/alerta.log', level=logging.INFO)
LOG = logging.getLogger('alerta.plugins.alertagenericplugin')

class AlertaGenericPlugin(PluginBase):
    def pre_receive(self, alert):
        if os.path.isfile('/etc/alerta/pre_receive'):
            os.system('/etc/alerta/pre_receive "%s"' % alert)
        return alert

    def post_receive(self, alert):
        logging.debug(alert)
        if os.path.isfile('/etc/alerta/post_receive'):
            os.system('/etc/alerta/post_receive "%s"' % alert)
        return

    def status_change(self, alert, status, text):
        logging.info(alert)
        if os.path.isfile('/etc/alerta/status_change'):
            os.system('/etc/alerta/status_change "%s"' % alert)
        return
