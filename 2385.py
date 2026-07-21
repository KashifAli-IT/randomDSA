
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass


# iterative dfs, tree dp
class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        def iter_dfs(root, start):
            result = -1
            stk = [(1, (root, [-1]*2))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    curr, ret = args
                    if curr is None:
                        continue
                    left, right = [-1]*2, [-1]*2
                    stk.append((2, (curr, left, right, ret)))
                    stk.append((1, (curr.right, right)))
                    stk.append((1, (curr.left, left)))
                elif step == 2:
                    curr, left, right, ret = args
                    d = -1
                    if curr.val == start:
                        d = 0
                        result = max(left[0], right[0])+1
                    elif left[1] >= 0:
                        d = left[1]+1
                        result = max(result, right[0]+1+d)
                    elif right[1] >= 0:
                        d = right[1]+1
                        result = max(result, left[0]+1+d)
                    ret[:] = [max(left[0], right[0])+1, d]  # [height, dist_to_start]
            return result

        return iter_dfs(root, start)
