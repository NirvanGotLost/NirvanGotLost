import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTabWidget, QPushButton, QLineEdit, QLabel, QMessageBox
from quantum_interface import (
    QuantumStateVisualizer, BackendProcessVisualizer, NetworkVisualizerWidget,
    QuantumCircuitVisualizer, PasswordStrengthAnalyzer, QuantumEntanglementVisualizer,
    PasswordGeneratorDialog, NeonKeyboard, MatrixRainEffect, HolographicEffect,
    StrengthHistoryGraph, PasswordComparisonWidget, UltraHDVisualizer,
    AdvancedNetworkMetrics
)
from quantum_brain import QuantumBrain, PasswordAnalyzer
from quantum_visualizer import QuantumVisualizer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quantum Password Analyzer")
        self.setMinimumSize(1200, 800)
        
        # Initialize components
        try:
            self.quantum_brain = QuantumBrain()
            self.password_analyzer = PasswordAnalyzer()
            print("✅ Neural core initialized")
        except Exception as e:
            print(f"⚠️ Neural core initialization warning (using fallback): {e}")
            
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # Create input section
        input_layout = QVBoxLayout()
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter password to analyze...")
        self.password_input.textChanged.connect(self.analyze_password)
        input_layout.addWidget(self.password_input)
        
        # Add generate button
        generate_btn = QPushButton("Generate Strong Password")
        generate_btn.clicked.connect(self.generate_password)
        input_layout.addWidget(generate_btn)
        
        layout.addLayout(input_layout)
        
        # Create tab widget
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)
        
        # Add visualization tabs
        self.add_visualization_tabs()
        
        # Initialize state
        self.current_password = ""
        self.password_history = []
        
        print("✅ Interface initialized")
        
    def add_visualization_tabs(self):
        # Quantum State Visualization
        self.quantum_state = QuantumStateVisualizer()
        self.tabs.addTab(self.quantum_state, "Quantum State")
        
        # Neural Network Visualization
        self.network_viz = NetworkVisualizerWidget()
        self.tabs.addTab(self.network_viz, "Neural Network")
        
        # Circuit Analysis
        self.circuit_viz = QuantumCircuitVisualizer()
        self.tabs.addTab(self.circuit_viz, "Quantum Circuit")
        
        # Password Strength Analysis
        self.strength_analyzer = PasswordStrengthAnalyzer()
        self.tabs.addTab(self.strength_analyzer, "Strength Analysis")
        
        # Entanglement View
        self.entanglement_viz = QuantumEntanglementVisualizer()
        self.tabs.addTab(self.entanglement_viz, "Quantum Entanglement")
        
        # Matrix Rain Effect
        self.matrix_effect = MatrixRainEffect()
        self.tabs.addTab(self.matrix_effect, "Matrix Effect")
        
        # Advanced Metrics
        self.network_metrics = AdvancedNetworkMetrics()
        self.tabs.addTab(self.network_metrics, "Network Metrics")
        
        # Backend Process
        self.backend_viz = BackendProcessVisualizer()
        self.tabs.addTab(self.backend_viz, "Backend Process")
        
        # Ultra HD Visualization
        self.ultra_viz = UltraHDVisualizer()
        self.tabs.addTab(self.ultra_viz, "Ultra HD")
        
        print("✅ Visualization components loaded")
        
    def analyze_password(self, password):
        try:
            if not password:
                return
                
            self.current_password = password
            
            # Analyze password
            analysis = self.password_analyzer.analyze_password(password)
            
            # Update visualizations
            self.quantum_state.update_quantum_state(analysis)
            self.circuit_viz.set_circuit(password)
            self.strength_analyzer.analyze_password(password)
            self.entanglement_viz.set_password(password)
            self.matrix_effect.set_strength(analysis['strength'])
            self.ultra_viz.set_strength(analysis['strength'])
            
            # Add to history if different
            if not self.password_history or password != self.password_history[-1]:
                self.password_history.append(password)
            
        except Exception as e:
            print(f"Analysis error (non-critical): {e}")
            
    def generate_password(self):
        dialog = PasswordGeneratorDialog(self)
        if dialog.exec():
            # Get user preferences
            length = dialog.length_spin.value()
            strength = dialog.strength_slider.value()
            use_upper = dialog.uppercase.isChecked()
            use_lower = dialog.lowercase.isChecked()
            use_numbers = dialog.numbers.isChecked()
            use_special = dialog.special.isChecked()
            
            try:
                # Generate password based on preferences
                chars = ""
                if use_lower:
                    chars += "abcdefghijklmnopqrstuvwxyz"
                if use_upper:
                    chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                if use_numbers:
                    chars += "0123456789"
                if use_special:
                    chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
                
                if not chars:
                    QMessageBox.warning(self, "Error", "Please select at least one character type!")
                    return
                
                # Generate password with quantum entropy
                import random
                password = ""
                for _ in range(length):
                    password += random.choice(chars)
                
                # Set the generated password
                self.password_input.setText(password)
                
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Password generation failed: {e}")

def main():
    # Create application
    app = QApplication(sys.argv)
    
    # Set style
    app.setStyle("Fusion")
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    # Start event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    try:
        print("🚀 Starting Quantum Password Analyzer...")
        print("⚡ Initializing components...")
        main()
    except Exception as e:
        print(f"❌ Critical error: {e}")
        input("Press Enter to exit...") 