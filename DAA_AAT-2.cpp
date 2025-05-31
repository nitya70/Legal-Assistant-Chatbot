// Bicoloring a graph using BFS
// This program checks if a graph is bicolorable using BFS.
// A graph is bicolorable if we can color its vertices using two colors such that no two adjacent vertices have the same color.
// The program uses a queue to perform BFS and colors the vertices as it traverses the graph.
//#include <iostream>
//#include <algorithm>
//#include <vector>
//#include <queue>
using namespace std;

bool isBicolorable(vector<vector<int>>& graph, int n) {
    vector<int> color(n, -1);
    for (int start = 0; start < n; start++) {
        if (color[start] == -1) {
            queue<int> q;
            q.push(start);
            color[start] = 0;
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                for (int v : graph[u]) {
                    if (color[v] == -1) {
                        color[v] = 1 - color[u];
                        q.push(v);
                    } else if (color[v] == color[u]) {
                        return false;
                    }
                }
            }
        }
    }												 
    return true;
}

int main() {
    int n, e;
    cout << "Enter number of nodes and edges: ";
    cin >> n >> e;
    vector<vector<int>> graph(n);
    cout << "Enter edges (u v):" << endl;
    for (int i = 0; i < e; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    if (isBicolorable(graph, n))
        cout << "Graph is BICOLORABLE." << endl;
    else
        cout << "Graph is NOT BICOLORABLE." << endl;
    return 0;
}
