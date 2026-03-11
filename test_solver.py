import sys
import os
# 将src目录加入路径，方便导入
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from solver import solve_n_queens

def test_queens_n4():
    """测试 N=4 时应该有 2 个解"""
    assert len(solve_n_queens(4)) == 2

def test_queens_n8():
    """测试 N=8 时应该有 92 个解"""
    assert len(solve_n_queens(8)) == 92
