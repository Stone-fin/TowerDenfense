from sys import exit
import pygame as pg
from config import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        # 计算游戏区域大小和位置
        self.grid_rows = 30
        self.grid_cols = 30
        # 计算屏幕80%的高度和宽度
        max_size = min(WIDTH * 0.8, HEIGHT * 0.8)
        # 计算每个格子的大小
        self.cell_size = max_size / max(self.grid_rows, self.grid_cols)
        # 计算游戏区域的实际大小
        self.grid_width = self.grid_cols * self.cell_size
        self.grid_height = self.grid_rows * self.cell_size
        # 计算游戏区域的位置，使其居中
        self.grid_x = (WIDTH - self.grid_width) // 2
        self.grid_y = (HEIGHT - self.grid_height) // 2

    def main_loop(self):
        while True:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
            # 绘制白色背景
            self.screen.fill((255, 255, 255))
            
            # 绘制格子
            grid_color = (128, 128, 128)  # 灰色
            # 绘制垂直线条
            for x in range(self.grid_cols + 1):
                start_pos = (int(self.grid_x + x * self.cell_size), int(self.grid_y))
                end_pos = (int(self.grid_x + x * self.cell_size), int(self.grid_y + self.grid_height))
                pg.draw.line(self.screen, grid_color, start_pos, end_pos, 1)
            # 绘制水平线条
            for y in range(self.grid_rows + 1):
                start_pos = (int(self.grid_x), int(self.grid_y + y * self.cell_size))
                end_pos = (int(self.grid_x + self.grid_width), int(self.grid_y + y * self.cell_size))
                pg.draw.line(self.screen, grid_color, start_pos, end_pos, 1)
            
            pg.display.update()

