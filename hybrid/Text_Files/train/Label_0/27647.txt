#include <bits/stdc++.h>
using namespace std;
const int M = 1000 + 5;
vector<int> edge[M];
int rep_node[M];
vector<int> repete_edge;
bool visited[M];
char flag[M][M];
void DFS(int node, int fathernode) {
  for (int i = 0; i < edge[node].size(); i++) {
    int child_node = edge[node][i];
    if (visited[child_node] == false) {
      visited[child_node] = true;
      DFS(child_node, node);
    } else {
      if (child_node != fathernode && flag[child_node][node] == 'n') {
        repete_edge.push_back(child_node);
        repete_edge.push_back(node);
        flag[child_node][node] = 'v';
        flag[node][child_node] = 'v';
      }
    }
  }
  return;
}
int main() {
  for (int i = 0; i < M; i++) {
    visited[i] = false;
    for (int j = 0; j < M; j++) {
      flag[i][j] = 'n';
    }
  }
  int n;
  cin >> n;
  for (int i = 0; i < n - 1; i++) {
    int a, b;
    cin >> a >> b;
    edge[a].push_back(b);
    edge[b].push_back(a);
  }
  int current_subcomponent = 0;
  int current_visited_nodes = 0;
  int num_repete_edge = 0;
  bool allvisited = false;
  while (allvisited == false) {
    int current_node = -1;
    for (int i = 1; i <= n; i++) {
      if (visited[i] == false) {
        current_node = i;
        break;
      }
    }
    visited[current_node] = true;
    rep_node[current_subcomponent++] = current_node;
    DFS(current_node, -1);
    allvisited = true;
    for (int i = 1; i <= n; i++) {
      if (visited[i] == false) {
        allvisited = false;
        break;
      }
    }
  }
  if (current_subcomponent == 1) {
    cout << "0" << endl;
  } else {
    cout << current_subcomponent - 1 << endl;
    int num_repete_edge = 0;
    for (int i = 1; i < current_subcomponent; i++) {
      cout << repete_edge[num_repete_edge] << " "
           << repete_edge[num_repete_edge + 1] << " ";
      num_repete_edge = num_repete_edge + 2;
      cout << rep_node[i - 1] << " " << rep_node[i] << endl;
    }
  }
  return 0;
}
