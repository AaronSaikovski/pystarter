import utils.console_helper as ch


def test_main():
    ch.print_ok_message("ok")
    ch.print_warning_message("warning")
    ch.print_error_message("error")
    ch.print_confirmation_message("confirmed")
    ch.print_command_message("command")
    ch.print_bold_message("bold")
