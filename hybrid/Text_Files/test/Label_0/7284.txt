#include <bits/stdc++.h>
using namespace std;
int const oo = 1000000007, e5 = 100007, e6 = 1000007;
int N;
int edge[e6];
bool check[e6];
vector<int> loops;
void __init__() {
  for (int i = 1; i <= int(N); i++) {
    check[i] = 0;
  }
  loops.erase((loops).begin(), (loops).end());
}
int findLoop(int node) {
  int next;
  check[node] = 1;
  next = edge[node];
  if (check[next] == 1) return next;
  return findLoop(next);
}
void printLoop(int loopElement) {
  int firstElement = loopElement;
  loops.push_back(loopElement);
  loopElement = edge[loopElement];
  while (loopElement != firstElement) {
    loops.push_back(loopElement);
    loopElement = edge[loopElement];
  }
  cout << loops.size() << "\n";
  for (int i = 0; i < int(loops.size()); i++) {
    cout << loops[i] << " ";
  }
  cout << "\n";
}
void runTest() {
  int a;
  int loopElement;
  cin >> N;
  __init__();
  for (int i = 1; i <= int(N); i++) {
    cin >> a;
    edge[i] = i - a;
  }
  for (int i = 1; i <= int(N); i++) {
    loopElement = findLoop(i);
    if (loopElement != 0) break;
  }
  printLoop(loopElement);
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  int T;
  cin >> T;
  while (T--) {
    runTest();
  }
}
