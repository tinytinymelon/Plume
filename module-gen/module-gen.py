#/bin/python3
import argparse
import yaml
import sys
import os

# modules & built-ins
class Module:
    def __init__(self, name, base_clz, parameters, ports, csr_registers, connections):
        self.name = name
        self.base_clz = base_clz
        self.parameters = parameters
        self.ports = ports
        self.csr_registers = csr_registers
        self.connections = connections

    @staticmethod
    def from_yaml(yaml_data):
        name = yaml_data.get('name')
        base_clz = yaml_data.get('base_clz')
        parameters = yaml_data.get('parameters', [])
        ports = yaml_data.get('ports', [])
        csr_registers = yaml_data.get('registers', {}).get('csrRegisters', [])
        connections = yaml_data.get('connections', [])
        return Module(name, base_clz, parameters, ports, csr_registers, connections)

    @classmethod
    def from_yaml(cls, yaml_data):
        name = yaml_data.get('name')
        base_clz = yaml_data.get('base_clz')
        parameters = yaml_data.get('parameters', [])
        ports = yaml_data.get('ports', [])
        csr_registers = yaml_data.get('registers', {}).get('csrRegisters', [])
        connections = yaml_data.get('connections', [])
        return cls(name, base_clz, parameters, ports, csr_registers, connections)
    
# messages
class Message:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields

    @staticmethod
    def from_yaml(yaml_data):
        name = yaml_data.get('name')
        fields = yaml_data.get('fields', [])
        return Message(name, fields)

# registers: csr registers and other register
class Register:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields

    @staticmethod
    def from_yaml(yaml_data):
        name = yaml_data.get('name')
        fields = yaml_data.get('fields', [])
        return Register(name, fields)

# help infos : enum
class Enum:
    def __init__(self, name, values):
        self.name = name
        self.values = values

    @staticmethod
    def from_yaml(yaml_data):
        name = yaml_data.get('name')
        values = yaml_data.get('values', [])
        return Enum(name, values)

# help infos : constants
class Constant:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    @staticmethod
    def from_yaml(yaml_data):
        name = yaml_data.get('name')
        value = yaml_data.get('value')
        return Constant(name, value)


class ModelGenerator:
    def __init__(self, module):
        self.module = module

    def generate(self):
        # Placeholder for code generation logic
        print(f"Generating code for module: {self.module.name}")
        print(f"Base class: {self.module.base_clz}")
        print(f"Parameters: {self.module.parameters}")
        print(f"Ports: {self.module.ports}")
        print(f"CSR Registers: {self.module.csr_registers}")
        print(f"Connections: {self.module.connections}")


class ConfigWrapper:
    def __init__(self, config_file):
        self.config_file = config_file
        self.configs = self.load_configs()

    def load_configs(self):
        with open(self.config_file, 'r') as f:
            return yaml.safe_load(f)

def _main(input_file, output_file, configs):
    with open(input_file, 'r') as f:
        data = yaml.safe_load(f)

    # Update the data based on configs
    for key, value in configs.items():
        if key in data:
            data[key] = value

    with open(output_file, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)


if __name__ == "__main__":
    _main()