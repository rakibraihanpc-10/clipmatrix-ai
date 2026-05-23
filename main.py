"""
ClipMatrix AI - All-in-one Facebook Movie Automation Suite
Main Application Entry Point
"""

import sys
import os
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap, QColor, QPainter, QBrush, QLinearGradient, QFont

from ui.main_window import MainWindow
from ui.sidebar import SidebarNavigation
from ui.video_editor import VideoEditorModule
from ui.profile_manager import ProfileManagerModule
from ui.group_finder import GroupFinderModule
from ui.support import SupportModule
from config.theme import DarkTheme


class ClipMatrixAI(QMainWindow):
    """Main Application Window"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ClipMatrix AI - Facebook Movie Automation Suite")
        self.setWindowIcon(QIcon(self.create_app_icon()))
        self.setGeometry(100, 100, 1600, 900)
        
        # Apply Dark Theme
        theme = DarkTheme()
        self.setStyleSheet(theme.get_stylesheet())
        
        # Initialize UI
        self.init_ui()
        
    def init_ui(self):
        """Initialize main user interface"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Sidebar Navigation
        self.sidebar = SidebarNavigation()
        main_layout.addWidget(self.sidebar, 0)
        
        # Content Stack
        self.content_layout = QVBoxLayout()
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        
        # Initialize Modules
        self.video_editor = VideoEditorModule()
        self.profile_manager = ProfileManagerModule()
        self.group_finder = GroupFinderModule()
        self.support = SupportModule()
        
        # Module Map
        self.modules = {
            "video_editor": self.video_editor,
            "profile_manager": self.profile_manager,
            "group_finder": self.group_finder,
            "support": self.support,
        }
        
        # Create container widget for modules
        self.module_container = QWidget()
        self.module_layout = QVBoxLayout(self.module_container)
        self.module_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.addWidget(self.module_container, 1)
        
        # Connect sidebar navigation
        self.sidebar.navigation_clicked.connect(self.switch_module)
        
        # Show Video Editor by default
        self.switch_module("video_editor")
        
        content_widget = QWidget()
        content_widget.setLayout(self.content_layout)
        main_layout.addWidget(content_widget, 1)
        
    def switch_module(self, module_name):
        """Switch between application modules"""
        # Clear previous module
        for i in reversed(range(self.module_layout.count())):
            widget = self.module_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)
        
        # Load new module
        if module_name in self.modules:
            self.module_layout.addWidget(self.modules[module_name])
    
    def create_app_icon(self):
        """Create application icon"""
        pixmap = QPixmap(256, 256)
        pixmap.fill(QColor("#121212"))
        
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Draw gradient background
        gradient = QLinearGradient(0, 0, 256, 256)
        gradient.setColorAt(0, QColor("#A020F0"))
        gradient.setColorAt(1, QColor("#00FFFF"))
        painter.fillRect(pixmap.rect(), gradient)
        
        # Draw text
        painter.setPen(QColor("#121212"))
        font = QFont("Arial", 20, QFont.Weight.Bold)
        painter.setFont(font)
        painter.drawText(pixmap.rect(), Qt.AlignmentFlag.AlignCenter, "CA")
        
        painter.end()
        return pixmap


def main():
    """Application Entry Point"""
    app = QApplication(sys.argv)
    
    # Ensure data directories exist
    Path("data").mkdir(exist_ok=True)
    Path("logs").mkdir(exist_ok=True)
    Path("temp").mkdir(exist_ok=True)
    
    window = ClipMatrixAI()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
