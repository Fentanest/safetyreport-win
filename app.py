import sys
import os
import subprocess
import json
import base64
from pathlib import Path
import shutil
import configparser

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QDialog,
    QFileDialog,
    QMessageBox,
)
from PySide6.QtCore import QProcess, QProcessEnvironment

from main_ui import Ui_MainWindow
from options_ui import Ui_Dialog
from settings.settings import config_path, google_api_auth_file
import start
import bot
import debug_save
import notifier
import asyncio
from version import __version__

class OptionsDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(f"옵션 v{__version__}")

        self.radioButtonUseChrome.setChecked(True)

        self.config = configparser.ConfigParser()
        self.config_path = Path(config_path)

        self.load_settings()
        self.connect_signals()
        self.update_ui_state()

    def connect_signals(self):
        self.checkBoxTelegrambot.stateChanged.connect(self.update_ui_state)
        self.checkBoxGoogleSheet.stateChanged.connect(self.update_ui_state)
        self.radioButtonUseHub.toggled.connect(self.update_ui_state)
        self.pushButtonGoogleSheetJSON.clicked.connect(self.select_json_file)
        
        # Immediate save
        self.checkBoxTelegrambot.stateChanged.connect(self.save_settings)
        self.lineEditToken.editingFinished.connect(self.save_settings)
        self.lineEditChatID.editingFinished.connect(self.save_settings)
        self.checkBoxGoogleSheet.stateChanged.connect(self.save_settings)
        self.lineEditGoogleSheet.editingFinished.connect(self.save_settings)
        self.radioButtonUseChrome.toggled.connect(self.save_settings)
        self.radioButtonUseHub.toggled.connect(self.save_settings)
        self.lineEditHubURL.editingFinished.connect(self.save_settings)
        self.checkBoxHeadless.stateChanged.connect(self.save_settings)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def update_ui_state(self):
        # Telegram
        telegram_enabled = self.checkBoxTelegrambot.isChecked()
        self.lineEditToken.setEnabled(telegram_enabled)
        self.labelToken.setEnabled(telegram_enabled)
        self.lineEditChatID.setEnabled(telegram_enabled)
        self.labelChatID.setEnabled(telegram_enabled)

        # Google Sheet
        gsheet_enabled = self.checkBoxGoogleSheet.isChecked()
        self.lineEditGoogleSheet.setEnabled(gsheet_enabled)
        self.labelGoogleSheet.setEnabled(gsheet_enabled)
        self.pushButtonGoogleSheetJSON.setEnabled(gsheet_enabled)
        self.labelGoogleSheetJSON.setEnabled(gsheet_enabled)
        self.labelGoogleSheetJSONstatus.setEnabled(gsheet_enabled)

        # Selenium Hub
        hub_enabled = self.radioButtonUseHub.isChecked()
        self.lineEditHubURL.setEnabled(hub_enabled)
        self.checkBoxHeadless.setEnabled(self.radioButtonUseChrome.isChecked())

    def load_settings(self):
        if not self.config_path.is_file():
            return

        self.config.read(self.config_path)

        # Telegram
        if "TELEGRAM" in self.config:
            self.checkBoxTelegrambot.setChecked(self.config.getboolean("TELEGRAM", "use_telegram_bot", fallback=False))
            self.lineEditToken.setText(self.config.get("TELEGRAM", "telegram_token", fallback=""))
            self.lineEditChatID.setText(self.config.get("TELEGRAM", "chat_id", fallback=""))

        # Google Sheet
        if "GOOGLESHEET" in self.config:
            self.checkBoxGoogleSheet.setChecked(self.config.getboolean("GOOGLESHEET", "use_gspread", fallback=False))
            self.lineEditGoogleSheet.setText(self.config.get("GOOGLESHEET", "sheet_key", fallback=""))

        # Selenium
        if "SELENIUM" in self.config:
            use_hub = self.config.getboolean("SELENIUM", "use_hub", fallback=False)
            if use_hub:
                self.radioButtonUseHub.setChecked(True)
            else:
                self.radioButtonUseChrome.setChecked(True)
            self.lineEditHubURL.setText(self.config.get("SELENIUM", "remotepath", fallback=""))
            self.checkBoxHeadless.setChecked(self.config.getboolean("SELENIUM", "headless", fallback=False))
        
        self.check_json_file_status()

    def save_settings(self):
        if not self.config_path.parent.exists():
            self.config_path.parent.mkdir(parents=True)

        # Telegram
        if not self.config.has_section("TELEGRAM"):
            self.config.add_section("TELEGRAM")
        self.config.set("TELEGRAM", "use_telegram_bot", str(self.checkBoxTelegrambot.isChecked()))
        self.config.set("TELEGRAM", "telegram_token", self.lineEditToken.text())
        self.config.set("TELEGRAM", "chat_id", self.lineEditChatID.text())

        # Google Sheet
        if not self.config.has_section("GOOGLESHEET"):
            self.config.add_section("GOOGLESHEET")
        self.config.set("GOOGLESHEET", "use_gspread", str(self.checkBoxGoogleSheet.isChecked()))
        self.config.set("GOOGLESHEET", "sheet_key", self.lineEditGoogleSheet.text())

        # Selenium
        if not self.config.has_section("SELENIUM"):
            self.config.add_section("SELENIUM")
        self.config.set("SELENIUM", "use_hub", str(self.radioButtonUseHub.isChecked()))
        self.config.set("SELENIUM", "remotepath", self.lineEditHubURL.text())
        self.config.set("SELENIUM", "headless", str(self.checkBoxHeadless.isChecked()))

        with open(self.config_path, "w") as configfile:
            self.config.write(configfile)

    def select_json_file(self):
        gspread_json_path = Path(google_api_auth_file)
        gspread_json_path.parent.mkdir(parents=True, exist_ok=True)

        file_path, _ = QFileDialog.getOpenFileName(self, "JSON 파일 선택", "", "JSON Files (*.json)")
        if file_path:
            try:
                with open(file_path, "r") as f:
                    data = json.load(f)
                
                if data.get("universe_domain") != "googleapis.com":
                    QMessageBox.warning(self, "오류", "선택한 JSON 파일의 universe_domain이 'googleapis.com'이 아닙니다.")
                    return

                shutil.copy(file_path, gspread_json_path)
                self.check_json_file_status()

            except Exception as e:
                QMessageBox.critical(self, "오류", f"파일을 처리하는 중 오류가 발생했습니다: {e}")

    def check_json_file_status(self):
        gspread_json_path = Path(google_api_auth_file)
        if gspread_json_path.is_file():
            self.labelGoogleSheetJSONstatus.setText("정상")
        else:
            self.labelGoogleSheetJSONstatus.setText("찾을 수 없음")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(f"안전신문고 크롤러 v{__version__}")

        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)
        self.process.finished.connect(self.process_finished)

        self.bot_process = QProcess()
        self.bot_process.readyReadStandardOutput.connect(self.handle_bot_stdout)
        self.bot_process.readyReadStandardError.connect(self.handle_bot_stderr)

        self.config_path = Path(config_path)
        self.pushButtonCancel.setEnabled(False)

        self.create_default_config_if_missing()
        self.connect_signals()
        self.update_ui_state()
        self.load_settings()
        self.log_settings_status()
        self.manage_bot_process()

    def create_default_config_if_missing(self):
        if not self.config_path.is_file():
            self.append_log("[정보] 설정 파일(config.ini)이 없어 새로 생성합니다.")
            config = configparser.ConfigParser()
            
            config.add_section("LOGIN")
            config.set("LOGIN", "username", "your_username")
            config.set("LOGIN", "password", "your_password")

            config.add_section("SETTINGS")
            config.set("SETTINGS", "max_empty_pages", "3")
            config.set("SETTINGS", "log_level", "INFO")
            config.set("SETTINGS", "interval", "60")
            config.set("SETTINGS", "max_retry", "10")

            config.add_section("TELEGRAM")
            config.set("TELEGRAM", "use_telegram_bot", "False")
            config.set("TELEGRAM", "telegram_token", "your_token")
            config.set("TELEGRAM", "chat_id", "your_chat_id")

            config.add_section("GOOGLESHEET")
            config.set("GOOGLESHEET", "use_gspread", "False")
            config.set("GOOGLESHEET", "sheet_key", "your_sheet_key")

            config.add_section("SELENIUM")
            config.set("SELENIUM", "use_hub", "False")
            config.set("SELENIUM", "headless", "False")
            config.set("SELENIUM", "remotepath", "http://localhost:4444/wd/hub")

            config.add_section("RUN_OPTIONS")
            config.set("RUN_OPTIONS", "pages", "")

            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.config_path, "w") as configfile:
                config.write(configfile)

    def connect_signals(self):
        self.pushButtonStart.clicked.connect(self.start_crawling)
        self.pushButtonSavefile.clicked.connect(self.save_file)
        self.pushButtonCancel.clicked.connect(self.cancel_process)
        self.actionOptions.triggered.connect(self.open_options_dialog)
        self.actionDebug.triggered.connect(self.handle_debug_toggle)

        self.radioButtonStart.toggled.connect(self.update_ui_state)
        self.radioButtonStartmin.toggled.connect(self.update_ui_state)
        self.radioButtonStartpage.toggled.connect(self.update_ui_state)

        # Immediate save
        self.lineEditID.editingFinished.connect(self.save_settings)
        self.lineEditPW.editingFinished.connect(self.save_settings)
        self.spinBoxValuemin.valueChanged.connect(self.save_settings)
        self.lineEditValuepage.editingFinished.connect(self.save_settings)

    def update_ui_state(self):
        self.spinBoxValuemin.setEnabled(self.radioButtonStartmin.isChecked())
        self.lineEditValuepage.setEnabled(self.radioButtonStartpage.isChecked())
        
        if not self.radioButtonStart.isChecked() and not self.radioButtonStartmin.isChecked() and not self.radioButtonStartpage.isChecked() and not self.radioButtonStartforce.isChecked() and not self.radioButtonStartreset.isChecked():
            self.radioButtonStart.setChecked(True)

    def load_settings(self):
        config = configparser.ConfigParser()
        if self.config_path.is_file():
            config.read(self.config_path)
            if "LOGIN" in config:
                username_b64 = config.get("LOGIN", "username", fallback="")
                password_b64 = config.get("LOGIN", "password", fallback="")
                if username_b64 and username_b64 != 'your_username':
                    self.lineEditID.setText(base64.b64decode(username_b64).decode('utf-8'))
                if password_b64 and password_b64 != 'your_password':
                    self.lineEditPW.setText(base64.b64decode(password_b64).decode('utf-8'))

            if "SETTINGS" in config:
                self.spinBoxValuemin.setValue(config.getint("SETTINGS", "max_empty_pages", fallback=3))
                log_level = config.get("SETTINGS", "log_level", fallback="INFO")
                if log_level == "DEBUG":
                    self.actionDebug.setChecked(True)
                else:
                    self.actionDebug.setChecked(False)
            
            if "RUN_OPTIONS" in config:
                self.lineEditValuepage.setText(config.get("RUN_OPTIONS", "pages", fallback=""))

    def save_settings(self):
        config = configparser.ConfigParser()
        
        # Ensure the parent directory exists
        self.config_path.parent.mkdir(parents=True, exist_ok=True)

        if self.config_path.is_file():
            config.read(self.config_path)

        if not config.has_section("LOGIN"):
            config.add_section("LOGIN")
        
        username = self.lineEditID.text()
        password = self.lineEditPW.text()
        config.set("LOGIN", "username", base64.b64encode(username.encode('utf-8')).decode('utf-8'))
        config.set("LOGIN", "password", base64.b64encode(password.encode('utf-8')).decode('utf-8'))

        if not config.has_section("SETTINGS"):
            config.add_section("SETTINGS")
        config.set("SETTINGS", "max_empty_pages", str(self.spinBoxValuemin.value()))

        if not config.has_section("RUN_OPTIONS"):
            config.add_section("RUN_OPTIONS")
        config.set("RUN_OPTIONS", "pages", self.lineEditValuepage.text())

        with open(self.config_path, "w") as configfile:
            config.write(configfile)

    def start_crawling(self):
        if self.process.state() == QProcess.ProcessState.Running:
            QMessageBox.warning(self, "진행 중", "이미 크롤링 프로세스가 실행 중입니다.")
            return

        self.save_settings()

        command = ["--start"]
        if self.radioButtonStartmin.isChecked():
            command.extend(["--min", str(self.spinBoxValuemin.value())])
        elif self.radioButtonStartpage.isChecked():
            command.extend(["--p", self.lineEditValuepage.text()])
        elif self.radioButtonStartforce.isChecked():
            command.append("--force")
        self.textBrowserLogview.clear()
        self.append_log(f"명령어 실행: {sys.executable} {' '.join(command)}")
        
        env = QProcessEnvironment.systemEnvironment()
        env.insert("PYTHONIOENCODING", "utf-8")
        self.process.setProcessEnvironment(env)
        
        self.process.start(sys.executable, command)
        self.pushButtonStart.setEnabled(False)
        self.pushButtonSavefile.setEnabled(False)
        self.pushButtonCancel.setEnabled(True)

    def save_file(self):
        if self.process.state() == QProcess.ProcessState.Running:
            QMessageBox.warning(self, "진행 중", "프로세스가 실행 중입니다.")
            return

        self.save_settings()
        
        command = ["--debug-save"]
        self.textBrowserLogview.clear()
        self.append_log(f"명령어 실행: {sys.executable} {' '.join(command)}")

        env = QProcessEnvironment.systemEnvironment()
        env.insert("PYTHONIOENCODING", "utf-8")
        self.process.setProcessEnvironment(env)

        self.process.start(sys.executable, command)
        self.pushButtonStart.setEnabled(False)
        self.pushButtonSavefile.setEnabled(False)
        self.pushButtonCancel.setEnabled(True)

    def cancel_process(self):
        if self.process.state() == QProcess.ProcessState.Running:
            self.process.kill()
            self.append_log("사용자에 의해 프로세스가 중단되었습니다.")

    def handle_debug_toggle(self, checked):
        new_level = "DEBUG" if checked else "INFO"
        self.append_log(f"로그 레벨을 {new_level}로 설정합니다. 다음 실행부터 적용됩니다.")
        
        config = configparser.ConfigParser()
        if self.config_path.is_file():
            config.read(self.config_path)
        
        if not config.has_section("SETTINGS"):
            config.add_section("SETTINGS")
            
        config.set("SETTINGS", "log_level", new_level)
        
        with open(self.config_path, "w") as configfile:
            config.write(configfile)

    def log_settings_status(self):
        self.append_log("--- 설정 확인 ---")
        config = configparser.ConfigParser()
        if not self.config_path.is_file():
            self.append_log("설정 파일(config.ini)을 찾을 수 없습니다.")
            self.append_log("--------------------")
            return

        config.read(self.config_path)

        # Telegram
        use_telegram = config.getboolean('TELEGRAM', 'use_telegram_bot', fallback=False)
        token = config.get('TELEGRAM', 'telegram_token', fallback='')
        chat_id = config.get('TELEGRAM', 'chat_id', fallback='')
        if use_telegram:
            if token and chat_id:
                self.append_log("[성공] 텔레그램 봇이 활성화되었습니다.")
            else:
                self.append_log("[실패] 텔레그램 봇이 활성화되었지만, 토큰 또는 채팅 ID가 없습니다.")
        else:
            self.append_log("[정보] 텔레그램 봇이 비활성화되었습니다.")

        # Google Sheets
        use_gsheet = config.getboolean('GOOGLESHEET', 'use_gspread', fallback=False)
        sheet_key = config.get('GOOGLESHEET', 'sheet_key', fallback='')
        json_path = Path("data/auth/gspread.json")
        if use_gsheet:
            if sheet_key and json_path.is_file():
                self.append_log("[성공] 구글 시트 기능이 활성화되었습니다.")
            else:
                log_msg = "[실패] 구글 시트 기능이 활성화되었지만, "
                if not sheet_key:
                    log_msg += "시트 키가 없습니다. "
                if not json_path.is_file():
                    log_msg += "인증 JSON 파일이 없습니다."
                self.append_log(log_msg)
        else:
            self.append_log("[정보] 구글 시트 기능이 비활성화되었습니다.")
        
        self.append_log("--------------------")

    def open_options_dialog(self):
        dialog = OptionsDialog(self)
        dialog.exec()
        self.log_settings_status()
        self.manage_bot_process()

    def manage_bot_process(self):
        config = configparser.ConfigParser()
        if not self.config_path.is_file():
            return

        config.read(self.config_path)

        use_telegram = config.getboolean('TELEGRAM', 'use_telegram_bot', fallback=False)
        token = config.get('TELEGRAM', 'telegram_token', fallback='')
        chat_id = config.get('TELEGRAM', 'chat_id', fallback='')
        
        is_running = self.bot_process.state() == QProcess.ProcessState.Running

        if use_telegram and token and chat_id:
            if not is_running:
                self.append_log("[정보] 텔레그램 봇 프로세스를 시작합니다.")
                env = QProcessEnvironment.systemEnvironment()
                env.insert("PYTHONIOENCODING", "utf-8")
                self.bot_process.setProcessEnvironment(env)
                self.bot_process.start(sys.executable, ["--bot"])
        else:
            if is_running:
                self.append_log("[정보] 텔레그램 봇 프로세스를 중지합니다.")
                self.bot_process.kill()

    def append_log(self, text):
        self.textBrowserLogview.append(text)
        self.textBrowserLogview.verticalScrollBar().setValue(
            self.textBrowserLogview.verticalScrollBar().maximum()
        )

    def handle_stdout(self):
        data = self.process.readAllStandardOutput()
        self.append_log(bytes(data).decode('utf-8', errors='ignore'))

    def handle_stderr(self):
        data = self.process.readAllStandardError()
        self.append_log(bytes(data).decode('utf-8', errors='ignore'))

    def handle_bot_stdout(self):
        data = self.bot_process.readAllStandardOutput()
        self.append_log(f"[BOT] {bytes(data).decode('utf-8', errors='ignore')}")

    def handle_bot_stderr(self):
        data = self.bot_process.readAllStandardError()
        self.append_log(f"[BOT ERROR] {bytes(data).decode('utf-8', errors='ignore')}")

    def process_finished(self):
        self.append_log("프로세스가 종료되었습니다.")
        self.pushButtonStart.setEnabled(True)
        self.pushButtonSavefile.setEnabled(True)
        self.pushButtonCancel.setEnabled(False)

    def closeEvent(self, event):
        if self.process.state() == QProcess.ProcessState.Running:
            self.process.kill()
        if self.bot_process.state() == QProcess.ProcessState.Running:
            self.bot_process.kill()
        event.accept()


if __name__ == "__main__":
    # Check for command-line arguments to run subprocess logic
    if len(sys.argv) > 1:
        if sys.argv[1] == '--start':
            # Remove the --start argument so start.py can parse its own args
            sys.argv = [sys.argv[0]] + sys.argv[2:]
            start.main()
        elif sys.argv[1] == '--bot':
            bot.main()
        elif sys.argv[1] == '--debug-save':
            debug_save.main()
        elif sys.argv[1] == '--notify':
            # Remove the --notify argument
            sys.argv = [sys.argv[0]] + sys.argv[2:]
            asyncio.run(notifier.main())
    else:
        # Run the main GUI application
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())