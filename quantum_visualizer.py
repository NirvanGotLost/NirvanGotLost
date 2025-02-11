import random
import math
import colorsys
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QTimer, QPointF, QRect, QRectF
from PySide6.QtGui import (
    QPainter, QPen, QColor, QLinearGradient, QRadialGradient,
    QBrush, QFont
)

class HolographicEffect(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(150, 400)
        self.particles = []
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_particles)
        self.timer.start(50)
        self.angle = 0
        
    def update_particles(self):
        self.angle += 0.1
        if random.random() < 0.3:
            self.particles.append({
                'x': random.randint(0, self.width()),
                'y': random.randint(0, self.height()),
                'size': random.randint(2, 8),
                'speed': random.uniform(1, 3),
                'angle': random.uniform(0, 2 * math.pi)
            })
        
        # Update existing particles
        for p in self.particles:
            p['x'] += math.cos(p['angle']) * p['speed']
            p['y'] += math.sin(p['angle']) * p['speed']
            
        # Remove particles that are out of bounds
        self.particles = [p for p in self.particles 
                         if 0 <= p['x'] <= self.width() 
                         and 0 <= p['y'] <= self.height()]
        
        self.update()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Draw holographic background
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0, QColor(0, 100, 200, 50))
        gradient.setColorAt(1, QColor(0, 200, 255, 30))
        painter.fillRect(self.rect(), gradient)
        
        # Draw particles
        for p in self.particles:
            color = QColor(0, 200, 255, 150)
            painter.setBrush(color)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(
                QPointF(p['x'], p['y']), 
                p['size'], 
                p['size']
            )
            
        # Draw scanning lines
        pen = QPen(QColor(0, 255, 255, 50))
        pen.setWidth(2)
        painter.setPen(pen)
        
        y = (math.sin(self.angle) + 1) * self.height() / 2
        painter.drawLine(0, y, self.width(), y)
        
        # Draw grid effect
        pen.setWidth(1)
        painter.setPen(pen)
        grid_size = 20
        for i in range(0, self.width(), grid_size):
            x = i + math.sin(self.angle + i/100) * 5
            painter.drawLine(x, 0, x, self.height())
        for i in range(0, self.height(), grid_size):
            y = i + math.cos(self.angle + i/100) * 5
            painter.drawLine(0, y, self.width(), y)

class QuantumVisualizer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(400, 300)
        self.strength = 0
        self.target_strength = 0
        self.particles = []
        self.angle = 0
        
        # Animation timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(16)  # 60 FPS
        
        # Smooth strength transition
        self.strength_timer = QTimer(self)
        self.strength_timer.timeout.connect(self.update_strength)
        self.strength_timer.start(50)
        
    def update_strength(self):
        if abs(self.strength - self.target_strength) > 0.5:
            self.strength += (self.target_strength - self.strength) * 0.2
            self.update()
            
    def update_animation(self):
        self.angle += 0.05
        
        # Update particles based on strength
        if random.random() < self.strength / 200:  # More particles at higher strength
            self.particles.append({
                'x': self.width() / 2,
                'y': self.height() / 2,
                'size': random.randint(3, 10),
                'speed': random.uniform(2, 5),
                'angle': random.uniform(0, 2 * math.pi),
                'color': self.get_strength_color(self.strength),
                'life': 1.0
            })
            
        # Update existing particles
        for p in self.particles:
            p['x'] += math.cos(p['angle']) * p['speed']
            p['y'] += math.sin(p['angle']) * p['speed']
            p['life'] -= 0.02
            
        # Remove dead particles
        self.particles = [p for p in self.particles if p['life'] > 0]
        
        self.update()
        
    def get_strength_color(self, strength):
        hue = min(120, strength * 1.2) / 360  # Green at 100%
        rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        return QColor(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Draw dark background
        painter.fillRect(self.rect(), Qt.GlobalColor.black)
        
        # Draw circular progress
        center = QPointF(self.width() / 2, self.height() / 2)
        radius = min(self.width(), self.height()) * 0.4
        
        # Draw outer ring
        pen = QPen(self.get_strength_color(self.strength))
        pen.setWidth(4)
        painter.setPen(pen)
        painter.setBrush(Qt.BrushStyle.NoBrush)
        
        # Animated ring
        start_angle = -90 * 16  # Start from top
        span_angle = -self.strength * 16 * 3.6  # 3.6 = 360/100
        painter.drawArc(
            center.x() - radius, 
            center.y() - radius,
            radius * 2, 
            radius * 2,
            start_angle,
            span_angle
        )
        
        # Draw particles
        painter.setPen(Qt.PenStyle.NoPen)
        for p in self.particles:
            color = p['color']
            color.setAlpha(int(255 * p['life']))
            painter.setBrush(color)
            painter.drawEllipse(
                QPointF(p['x'], p['y']),
                p['size'] * p['life'],
                p['size'] * p['life']
            )
            
        # Draw strength text
        painter.setFont(QFont('Arial', 24, QFont.Weight.Bold))
        painter.setPen(self.get_strength_color(self.strength))
        painter.drawText(
            QRect(
                int(center.x() - radius),
                int(center.y() - 20),
                int(radius * 2),
                40
            ),
            Qt.AlignmentFlag.AlignCenter,
            f"{self.strength:.1f}%"
        )
        
        # Draw quantum effects
        num_lines = 12
        for i in range(num_lines):
            angle = self.angle + (i * 2 * math.pi / num_lines)
            x1 = center.x() + math.cos(angle) * (radius * 0.8)
            y1 = center.y() + math.sin(angle) * (radius * 0.8)
            x2 = center.x() + math.cos(angle) * (radius * 1.2)
            y2 = center.y() + math.sin(angle) * (radius * 1.2)
            
            color = self.get_strength_color(self.strength)
            color.setAlpha(100)
            pen = QPen(color)
            pen.setWidth(2)
            painter.setPen(pen)
            painter.drawLine(QPointF(x1, y1), QPointF(x2, y2))
            
        # Draw inner glow
        gradient = QRadialGradient(center, radius * 0.7)
        color = self.get_strength_color(self.strength)
        gradient.setColorAt(0, QColor(color.red(), color.green(), color.blue(), 30))
        gradient.setColorAt(1, QColor(0, 0, 0, 0))
        painter.setBrush(gradient)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(center, radius * 0.7, radius * 0.7)
        
    def set_strength(self, strength):
        self.target_strength = strength

    def set_password(self, password):
        # This method is called from the interface but we handle password visualization
        # through the strength value
        pass

    def update_quantum_metrics(self, metrics):
        # This method is called from the interface but we handle visualization
        # through the strength value
        pass 