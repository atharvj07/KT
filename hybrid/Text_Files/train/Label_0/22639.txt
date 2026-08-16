#include <bits/stdc++.h>
using namespace std;
int inds[5001];
int main() {
  ifstream in("input.txt");
  ofstream out("output.txt");
  int n;
  in >> n;
  int* ci = new int[n];
  for (int i = 0; i < n; i++) {
    in >> ci[i];
  }
  sort(ci, ci + n);
  memset(inds, -1, sizeof inds);
  for (int i = 0; i < n; i++) {
    inds[ci[i]] = i;
  }
  for (int i = 0; i < 5000; i++) {
    if (inds[i + 1] == -1) inds[i + 1] = inds[i];
  }
  int min = 90019001;
  for (int i = 0; i < n; i++) {
    int low = ci[i];
    int rem = i;
    if (low < 2500) {
      cout << "adding " << n - inds[low * 2] - 1 << endl;
      rem += n - inds[low * 2] - 1;
    }
    cout << rem << " for " << i << endl;
    if (min > rem) min = rem;
  }
  for (int i = 0; i < n; i++) cout << ci[i] << " ";
  cout << endl;
  for (int i = 0; i < 20; i++) cout << inds[i] << " ";
  cout << endl;
  out << min << endl;
  out.close();
  return 0;
}
