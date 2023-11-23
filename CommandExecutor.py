from Command import Command
from ComputerControl import ComputerControl
from DataAnalysis import DataAnalysis


class CommandExecutor:
    def execute_command(self, command: Command):
        data_analysis = DataAnalysis(command.get_data())
        analysis_result = data_analysis.analyze()

        command.set_analyze(analysis_result)
        action = command.get_action()

        computer_control = ComputerControl()
        computer_control.control_computer(action)
