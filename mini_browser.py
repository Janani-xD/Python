# pick ONE of these (PyQt5 is the most common):
# pip install PyQt5 PyQtWebEngine
# or
# pip install PySide6


import sys

# ===== Choose your toolkit =====
# Default: PyQt5
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import (
    QApplication, QLineEdit, QToolBar, QAction, QTabWidget, QMainWindow
)
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView

# --- If you prefer PySide6, replace the imports above with:
# from PySide6.QtCore import QUrl
# from PySide6.QtWidgets import (
#     QApplication, QLineEdit, QToolBar, QAction, QTabWidget, QMainWindow
# )
# from PySide6.QtGui import QIcon
# from PySide6.QtWebEngineWidgets import QWebEngineView


DEFAULT_HOME = "https://www.google.com"


class BrowserTab(QWebEngineView):
    def __init__(self, parent=None, url=DEFAULT_HOME):
        super().__init__(parent)
        self.loadFinished.connect(self._on_load_finished)
        self.urlChanged.connect(self._on_url_changed)
        self.titleChanged.connect(self._on_title_changed)
        self.load(QUrl(url))
        self._parent_main = parent  # reference to MainWindow for updating URL bar

    def _on_load_finished(self, ok: bool):
        if not ok:
            self.setHtml("<h3 style='font-family:sans-serif'>Failed to load page.</h3>")

    def _on_url_changed(self, qurl: QUrl):
        # keep URL bar in sync for the active tab
        if self._parent_main and self._parent_main.current_tab() is self:
            self._parent_main.url_bar.setText(qurl.toString())

    def _on_title_changed(self, title: str):
        # update tab text when page title changes
        if self._parent_main:
            idx = self._parent_main.tabs.indexOf(self)
            if idx != -1:
                self._parent_main.tabs.setTabText(idx, title if title else "New Tab")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini Browser")
        self.resize(1200, 800)

        # Tabs
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.sync_url_bar)
        self.setCentralWidget(self.tabs)

        # Toolbar
        nav = QToolBar("Navigation")
        self.addToolBar(nav)

        back_act = QAction("◀", self)
        back_act.setStatusTip("Back")
        back_act.triggered.connect(lambda: self.current_tab().back())
        nav.addAction(back_act)

        fwd_act = QAction("▶", self)
        fwd_act.setStatusTip("Forward")
        fwd_act.triggered.connect(lambda: self.current_tab().forward())
        nav.addAction(fwd_act)

        reload_act = QAction("⟲", self)
        reload_act.setStatusTip("Reload")
        reload_act.triggered.connect(lambda: self.current_tab().reload())
        nav.addAction(reload_act)

        home_act = QAction("🏠", self)
        home_act.setStatusTip("Home")
        home_act.triggered.connect(self.navigate_home)
        nav.addAction(home_act)

        nav.addSeparator()

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav.addWidget(self.url_bar)

        new_tab_act = QAction("＋ Tab", self)
        new_tab_act.setStatusTip("Open new tab")
        new_tab_act.triggered.connect(lambda: self.add_tab(DEFAULT_HOME))
        nav.addAction(new_tab_act)

        # First tab
        self.add_tab(DEFAULT_HOME)

    # Helpers
    def current_tab(self) -> BrowserTab:
        return self.tabs.currentWidget()

    def add_tab(self, url: str):
        view = BrowserTab(parent=self, url=url)
        i = self.tabs.addTab(view, "Loading…")
        self.tabs.setCurrentIndex(i)

    def close_tab(self, index: int):
        if self.tabs.count() > 1:
            self.tabs.widget(index).deleteLater()
            self.tabs.removeTab(index)
        else:
            self.close()  # close app if last tab closed

    def navigate_home(self):
        self.current_tab().load(QUrl(DEFAULT_HOME))

    def navigate_to_url(self):
        text = self.url_bar.text().strip()
        # Add scheme if missing
        if text and not text.startswith(("http://", "https://")):
            text = "https://" + text
        self.current_tab().load(QUrl(text))

    def sync_url_bar(self, _index: int):
        tab = self.current_tab()
        if tab:
            self.url_bar.setText(tab.url().toString())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())  # PyQt5/PySide6 compatible


if __name__ == "__main__":
    main()


# step 3

# python mini_browser.py

# Features you get
#
# URL bar (Enter to navigate)
#
# Back / Forward / Reload / Home
#
# Multiple tabs
#
# Titles synced to tab text
#
# Auto-prefix https:// if you type a bare domain (e.g., example.com)
#
# Ideas to extend
#
# Bookmarks sidebar (persist in JSON/SQLite)
#
# Download manager
#
# Ad-blocking via request interceptor

Dark mode toggle

Save/restore session tabs