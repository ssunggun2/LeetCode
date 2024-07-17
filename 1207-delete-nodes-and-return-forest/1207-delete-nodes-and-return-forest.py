from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # 1.1. DFS탐색
        # 1.2. to_delete set으로 변환
        to_delete = set(to_delete)
        forest = []
        # 2.1. 탐색하면서 삭제여부 결정하는 재귀함수 정의
        def dfs(node):
            if not node:
                return None
            
            # 자식노드 먼저 탐색
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            # 현재 노드가 삭제 대상인 경우
            if node.val in to_delete:
                # 자식 노드들이 null이 아니면 새로운 트리를 루트로 추가
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return None
            return node
        
        # 초기 루트가 삭제되지 않는 경우를 위해
        root = dfs(root)
        if root:
            forest.append(root)

        return forest

        # 2.2. 현재 노드 인수로 받아 해당 노드의 자식들에 대해 재귀적으로 호출
        # 3.1. 현재 노드가 to_delete에 있는지 확인
        # 3.2. 현재 노드 삭제해야하면, 해당 노드 왼쪽 자식, 오른쪽 자식을 각각 새로운 서브 트리 루트로 간주
        # 3.3. 이때, 삭제한 노드의 자식 노드들이 null이 아닌 경우에만 결과 리스트에 추가
        # 3.4. 현재, 노드가 삭제되지 않는다면, 자식 노드들에 대한 재귀 호출결과를 현재 노드의 자식으로 업데이트
        # 4.1. 최초 호출시 루트 노드가 삭제되지 않는 경우, 루트 노드를 결과 리스트에 추가
        # 4.2. 최종적으로 결과 리스트에는 삭제후 남은 서브 트리들의 루트노드들이 포함됨.