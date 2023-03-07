# Time Complexity :O(V+E)
# Space Complexity :O(V)
# Did this code successfully run on Leetcode :Yes       
# Any problem you faced while coding this :No


from collections import deque


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if(node is None):
            return None
        q=deque()
        nNode=Node(node.val)
        hmap={node:nNode}
        q.append(node)
        while(q):
            curr=q.popleft()
            for i in curr.neighbors:
                if(i not in hmap):
                    hmap[i]=Node(i.val)
                    q.append(i)
                
                if(hmap[curr].neighbors is None):
                    hmap[curr].neighbors=[hmap[i]]
                else:
                    hmap[curr].neighbors.append(hmap[i])
                
                

        return(nNode)


