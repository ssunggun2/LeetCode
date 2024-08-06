#include <vector>
#include <unordered_map>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        // 그래프 초기화
        unordered_map<int, vector<int>> graph;
        for (const auto& prereq : prerequisites) {
            graph[prereq[1]].push_back(prereq[0]);
        }

        vector<int> visited(numCourses, 0); // 방문 상태 (0: 미방문, 1: 방문 중, 2: 방문 완료)
        stack<int> order; // 위상 정렬 순서를 저장할 스택
        for (int i = 0; i < numCourses; ++i) {
            if (visited[i] == 0) {
                if (!dfs(i, graph, visited, order)) {
                    return {}; // 사이클이 발견되면 빈 벡터 반환
                }
            }
        }

        // 스택에서 결과를 벡터로 변환
        vector<int> result;
        while (!order.empty()) {
            result.push_back(order.top());
            order.pop();
        }

        return result;
    }

private:
    bool dfs(int node, unordered_map<int, vector<int>>& graph, vector<int>& visited, stack<int>& order) {
        if (visited[node] == 1) {
            return false; // 사이클 발견
        }
        if (visited[node] == 2) {
            return true; // 이미 방문 완료된 노드
        }

        visited[node] = 1; // 방문 중으로 표시
        for (int neighbor : graph[node]) {
            if (!dfs(neighbor, graph, visited, order)) {
                return false; // 사이클 발견
            }
        }

        visited[node] = 2; // 방문 완료로 표시
        order.push(node); // 스택에 노드 추가
        return true;
    }
};
