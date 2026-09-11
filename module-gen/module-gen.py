#/bin/python3
import argparse
from email import message
import yaml
import sys
import os

# global context for module generation
# - dictionary of modules, messages, registers, enums, constants
# - helps to quick find reference target objects by name 
class GenContext:
    def __init__(self, modules, messages, registers, enums, constants):
        self.modules = modules
        self.messages = messages
        self.registers = registers
        self.enums = enums
        self.constants = constants

# modules & built-ins
class Module:
    def __init__(self, context, name, base_clz, parameters, ports, csr_registers, connections):
        self.context = context
        self.name = name
        self.base_clz = base_clz
        self.parameters = parameters
        self.ports = ports
        self.csr_registers = csr_registers
        self.connections = connections

    # input is one 
    @classmethod
    def from_yaml(cls, yaml_data):
        name = yaml_data.get('name')
        base_clz = yaml_data.get('base_clz', None)
        parameters = yaml_data.get('parameters', [])
        ports = [{pd.get('name'): {message: pd.get('message', None), 'kind': pd.get('kind', None)}} for pd in yaml_data.get('ports', [])]
        csr_registers = yaml_data.get('csrRegisters', [])
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
    def __init__(self, yaml_data):
        self.yaml_data = yaml_data

    def generate(self):
        modules = [Module.from_yaml(m) for m in self.yaml_data.get('modules', [])]
        messages = [Message.from_yaml(m) for m in self.yaml_data.get('messages', [])]
        registers = [Register.from_yaml(r) for r in self.yaml_data.get('registers', {}).get('csrRegisters', [])]
        enums = [Enum.from_yaml(e) for e in self.yaml_data.get('enums', [])]
        constants = [Constant.from_yaml(c) for c in self.yaml_data.get('constants', [])]

        return {
            'modules': modules,
            'messages': messages,
            'registers': registers,
            'enums': enums,
            'constants': constants
        }


class ArgumentsParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Module Generator")
        self.parser.add_argument('-i', '--input', default="module-gen/module.yaml", help="Input YAML file")
        self.parser.add_argument('-o', '--output-dir', default="src/gen/include/module", help="Output Module Definition Path")

    def parse(self):
        return self.parser.parse_args()

def _main():
    args_parser = ArgumentsParser()
    args = args_parser.parse()

    input_file = args.input
    output_dir = args.output_dir

    # Load module from input YAML
    with open(input_file, 'r') as f:
        module_yaml = yaml.safe_load(f)
        print(module_yaml)

# self-testing
def self_testing():
    print(os.getcwd())
    module_yaml_file = 'module-gen/module.yaml'
    with open(module_yaml_file, 'r') as f:
        module_yaml = yaml.safe_load(f) 

        print("Module YAML:")
        print(module_yaml)


if __name__ == "__main__":
    _main()