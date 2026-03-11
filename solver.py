def solve_n_queens(n):
    """求解N皇后问题，返回所有可能的解"""
    def backtrack(row, cols, diagonals, anti_diagonals):
        if row == n:
            return [[]]
        
        results = []
        for col in range(n):
            d1 = row - col
            d2 = row + col
            if col in cols or d1 in diagonals or d2 in anti_diagonals:
                continue
            
            # 记录当前位置
            for sol in backtrack(row + 1, cols | {col}, diagonals | {d1}, anti_diagonals | {d2}):
                results.append([col] + sol)
        return results

    return backtrack(0, set(), set(), set())

if __name__ == "__main__":
    n = 8
    solutions = solve_n_queens(n)
    print(f"{n}皇后问题共有 {len(solutions)} 个解。")
