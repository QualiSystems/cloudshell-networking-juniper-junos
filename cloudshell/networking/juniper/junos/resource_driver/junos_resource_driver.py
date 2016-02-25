from cloudshell.shell.core.driver_builder_wrapper import DriverFunction
from cloudshell.networking.resource_driver.networking_generic_resource_dirver import networking_generic_resource_driver
import cloudshell.networking.juniper.junos

class junos_resource_driver(networking_generic_resource_driver):
    ATTRIBUTE_MATRIX = {"resource": ["ResourceAddress", "User", "Password", "Enable Password", "Console Server IP Address",
                                   "Console User", "Console Password", "Console Port", "CLI Connection Type",
                                   "SNMP Version", "SNMP Read Community", "SNMP V3 User", "SNMP V3 Password",
                                   "SNMP V3 Private Key"]}

    @DriverFunction(extraMatrixRows=ATTRIBUTE_MATRIX)
    def Init(self, matrixJSON):
        self.handler_name = 'JUNOS'
        networking_generic_resource_driver.Init(self, matrixJSON)
