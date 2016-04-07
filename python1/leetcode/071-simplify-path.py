class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        es = path.split('/')
        rs = []
        for e in es:
            if not e or e == '.':
                continue
            if e == '..' and rs:
                rs.pop()
            else:
                rs.append(e)

        return '/' + '/'.join(rs)
