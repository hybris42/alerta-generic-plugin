from alerta.plugins import PluginBase
import os.path

class AlertaGenericPlugin(PluginBase):
    def pre_receive(self, alert):
        if os.path.isfile('/etc/alerta/pre_receive'):
            os.system('/etc/alerta/pre_receive "%s"' % alert)
        return alert

    def post_receive(self, alert):
        if os.path.isfile('/etc/alerta/post_receive'):
            os.system('/etc/alerta/post_receive "%s"' % alert)
        return

    def status_change(self, alert, status, text):
        if os.path.isfile('/etc/alerta/status_change'):
            os.system('/etc/alerta/status_change "%s"' % alert)
        return
