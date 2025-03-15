class Solution:
    def simplifyPath(self, path: str) -> str:
        folder_list = path.split('/')
        folder_list = [a for a in folder_list if a]
        final_path = []
        for a in folder_list: 
            if a == '.':
                continue            
            if a == '..':
                if len(final_path) >0:
                    final_path.pop()
            else:
                final_path.append(a)
        output = '/' + '/'.join(final_path)
        return output