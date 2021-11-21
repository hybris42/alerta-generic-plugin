from alerta.plugins import PluginBase
import os.path

class AlertaGenericPlugin(PluginBase):
    def __init__(self, name=None):
        self.changed = []
        super(AlertaGenericPlugin, self).__init__(name)

    def pre_receive(self, alert):
        if os.path.isfile('/etc/alerta/pre_receive'):
            os.system('/etc/alerta/pre_receive %s %s %s %s %s' % (alert.id,
                                                                  alert.environment,
                                                                  alert.resource,
                                                                  alert.event,
                                                                  alert.severity))
        return alert

    def post_receive(self, alert):
        if alert.id in self.changed and os.path.isfile('/etc/alerta/status_change'):
            os.system('/etc/alerta/status_change %s %s %s %s %s' % (alert.id,
                                                                    alert.environment,
                                                                    alert.resource,
                                                                    alert.event,
                                                                    alert.severity))
            self.changed.remove(alert.id)
        if os.path.isfile('/etc/alerta/post_receive'):
            os.system('/etc/alerta/post_receive %s %s %s %s %s' % (alert.id,
                                                                   alert.environment,
                                                                   alert.resource,
                                                                   alert.event,
                                                                   alert.severity))
        return

    def status_change(self, alert, status, text):
        self.changed.append(alert.id)
        return
