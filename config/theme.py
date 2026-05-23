"""
Theme Configuration - Dark Slate with Neon Purple & Electric Blue
"""

class DarkTheme:
    """Application-wide Dark Theme"""
    
    DARK_SLATE = "#121212"
    NEON_PURPLE = "#A020F0"
    ELECTRIC_BLUE = "#00FFFF"
    DARK_BG = "#1A1A1A"
    CARD_BG = "#1E1E1E"
    ACCENT_GRAY = "#2D2D2D"
    TEXT_PRIMARY = "#FFFFFF"
    TEXT_SECONDARY = "#B0B0B0"
    
    def get_stylesheet(self):
        """Get complete stylesheet"""
        return f"""
        * {{
            background-color: {self.DARK_SLATE};
            color: {self.TEXT_PRIMARY};
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 12px;
        }}
        
        QMainWindow {{
            background-color: {self.DARK_SLATE};
            border: none;
        }}
        
        QWidget {{
            background-color: {self.DARK_SLATE};
        }}
        
        QLabel {{
            color: {self.TEXT_PRIMARY};
        }}
        
        QPushButton {{
            background-color: {self.NEON_PURPLE};
            color: {self.TEXT_PRIMARY};
            border: 2px solid {self.NEON_PURPLE};
            border-radius: 8px;
            padding: 10px 20px;
            font-weight: bold;
            transition: all 0.3s ease;
        }}
        
        QPushButton:hover {{
            background-color: {self.ELECTRIC_BLUE};
            border: 2px solid {self.ELECTRIC_BLUE};
            box-shadow: 0 0 20px {self.ELECTRIC_BLUE};
        }}
        
        QPushButton:pressed {{
            background-color: {self.NEON_PURPLE};
        }}
        
        QLineEdit, QTextEdit {{
            background-color: {self.CARD_BG};
            border: 2px solid {self.ACCENT_GRAY};
            border-radius: 6px;
            color: {self.TEXT_PRIMARY};
            padding: 8px;
            selection-background-color: {self.NEON_PURPLE};
        }}
        
        QLineEdit:focus, QTextEdit:focus {{
            border: 2px solid {self.ELECTRIC_BLUE};
            background-color: {self.DARK_BG};
        }}
        
        QComboBox {{
            background-color: {self.CARD_BG};
            border: 2px solid {self.ACCENT_GRAY};
            border-radius: 6px;
            color: {self.TEXT_PRIMARY};
            padding: 8px;
        }}
        
        QComboBox:focus {{
            border: 2px solid {self.ELECTRIC_BLUE};
        }}
        
        QComboBox::drop-down {{
            background-color: {self.NEON_PURPLE};
            border: none;
            border-radius: 4px;
        }}
        
        QSlider::groove:horizontal {{
            background-color: {self.ACCENT_GRAY};
            border-radius: 5px;
            height: 8px;
        }}
        
        QSlider::handle:horizontal {{
            background-color: {self.ELECTRIC_BLUE};
            border: none;
            width: 18px;
            margin: -5px 0px;
            border-radius: 9px;
        }}
        
        QSlider::handle:horizontal:hover {{
            background-color: {self.NEON_PURPLE};
            box-shadow: 0 0 10px {self.ELECTRIC_BLUE};
        }}
        
        QProgressBar {{
            background-color: {self.CARD_BG};
            border: 2px solid {self.ACCENT_GRAY};
            border-radius: 6px;
            text-align: center;
            color: {self.TEXT_PRIMARY};
            height: 20px;
        }}
        
        QProgressBar::chunk {{
            background: qlineargradient(
                x1:0, y1:0, x2:1, y2:0,
                stop:0 {self.NEON_PURPLE},
                stop:1 {self.ELECTRIC_BLUE}
            );
            border-radius: 4px;
        }}
        
        QGroupBox {{
            border: 2px solid {self.ACCENT_GRAY};
            border-radius: 8px;
            margin-top: 10px;
            padding-top: 10px;
            color: {self.NEON_PURPLE};
        }}
        
        QGroupBox::title {{
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 3px 0 3px;
        }}
        
        QScrollBar:vertical {{
            background-color: {self.DARK_BG};
            width: 12px;
            border: none;
        }}
        
        QScrollBar::handle:vertical {{
            background-color: {self.ACCENT_GRAY};
            border-radius: 6px;
            min-height: 20px;
        }}
        
        QScrollBar::handle:vertical:hover {{
            background-color: {self.NEON_PURPLE};
        }}
        
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            border: none;
            background: none;
        }}
        
        QMenuBar {{
            background-color: {self.DARK_BG};
            border-bottom: 1px solid {self.ACCENT_GRAY};
        }}
        
        QMenuBar::item:selected {{
            background-color: {self.NEON_PURPLE};
        }}
        
        QMenu {{
            background-color: {self.DARK_BG};
            border: 1px solid {self.ACCENT_GRAY};
        }}
        
        QMenu::item:selected {{
            background-color: {self.NEON_PURPLE};
        }}
        
        QTableWidget {{
            background-color: {self.DARK_BG};
            gridline-color: {self.ACCENT_GRAY};
            border: 1px solid {self.ACCENT_GRAY};
        }}
        
        QTableWidget::item {{
            padding: 5px;
            border: none;
        }}
        
        QTableWidget::item:selected {{
            background-color: {self.NEON_PURPLE};
        }}
        
        QHeaderView::section {{
            background-color: {self.CARD_BG};
            color: {self.TEXT_PRIMARY};
            padding: 5px;
            border: 1px solid {self.ACCENT_GRAY};
        }}
        
        QCheckBox {{
            color: {self.TEXT_PRIMARY};
        }}
        
        QCheckBox::indicator {{
            width: 18px;
            height: 18px;
        }}
        
        QCheckBox::indicator:unchecked {{
            background-color: {self.CARD_BG};
            border: 2px solid {self.ACCENT_GRAY};
            border-radius: 3px;
        }}
        
        QCheckBox::indicator:checked {{
            background-color: {self.NEON_PURPLE};
            border: 2px solid {self.NEON_PURPLE};
            border-radius: 3px;
        }}
        
        QRadioButton {{
            color: {self.TEXT_PRIMARY};
        }}
        
        QRadioButton::indicator {{
            width: 18px;
            height: 18px;
        }}
        
        QRadioButton::indicator:unchecked {{
            background-color: {self.CARD_BG};
            border: 2px solid {self.ACCENT_GRAY};
            border-radius: 9px;
        }}
        
        QRadioButton::indicator:checked {{
            background-color: {self.ELECTRIC_BLUE};
            border: 2px solid {self.ELECTRIC_BLUE};
            border-radius: 9px;
        }}
        """
