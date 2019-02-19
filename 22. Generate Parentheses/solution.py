iclass Solution:
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        res = []
        def dfs(l: int, r: int, item: str) -> None:
            if l == 0 and r == 0:
                res.append(item)
            
            if l > 0:
                dfs(l-1, r, item+"(")
            if r > l:
                dfs(l, r-1, item+")")
        dfs(n, n, "")
        return res

