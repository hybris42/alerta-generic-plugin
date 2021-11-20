import logging
from alerta.plugins import PluginBase
import os.path

logging.basicConfig(filename='/var/log/alerta/alerta.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='-%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)
LOG = logging.getLogger('alerta.plugins.alertagenericplugin')

class AlertaGenericPlugin(PluginBase):
    def pre_receive(self, alert):
        if os.path.isfile('/etc/alerta/pre_receive'):
            os.system('/etc/alerta/pre_receive "%s"' % alert)
        return alert

    def post_receive(self, alert):
        LOG.debug(alert)
        if os.path.isfile('/etc/alerta/post_receive'):
            os.system('/etc/alerta/post_receive "%s"' % alert)
        return

    def status_change(self, alert, status, text):
        LOG.info(alert)
        if os.path.isfile('/etc/alerta/status_change'):
            os.system('/etc/alerta/status_change "%s"' % alert)
        return
