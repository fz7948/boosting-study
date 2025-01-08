# https://leetcode.com/problems/design-sql/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.table_info = {}
        self.table = {}
        for i in range(len(names)):
            self.table_info[names[i]] = [columns[i], 1] # size, latest id
            self.table[names[i]] = {}

    def ins(self, name: str, row: List[str]) -> bool:
        if not name in self.table_info:
            return False
        elif self.table_info[name][0] != len(row):
            return False
        
        auto_id = self.table_info[name][1]
        self.table[name][auto_id] = row
        self.table_info[name][1] += 1
        return True

    def rmv(self, name: str, rowId: int) -> None:
        if name in self.table_info and name in self.table:
            if rowId in self.table[name]:
                del self.table[name][rowId]

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        columnId -= 1
        if name in self.table_info and name in self.table:
            if rowId in self.table[name] and len(self.table[name][rowId]) > columnId:
                return self.table[name][rowId][columnId]
        return "<null>"

    def exp(self, name: str) -> List[str]:
        ret = []
        for k, row in self.table[name].items():
            ret.append(str(k)+","+",".join(row))
        return ret


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)