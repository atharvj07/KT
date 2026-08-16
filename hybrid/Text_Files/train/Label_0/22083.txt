#include <bits/stdc++.h>
using namespace std;
int mais = 1, menos, n, qnt;
vector<char> sinal;
string eq;
char x;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  getline(cin, eq);
  for (int i = 0; i < eq.size(); ++i) {
    if (eq[i] == '?')
      qnt++;
    else if (eq[i] == '-') {
      menos++;
      sinal.push_back('-');
    } else if (eq[i] == '+') {
      mais++;
      sinal.push_back('+');
    } else if (eq[i] == '=') {
      string sla;
      for (int j = i + 2; j < eq.size(); ++j) sla += eq[j];
      n = atoi(sla.c_str());
      break;
    }
  }
  long long int L = mais - (long long int)menos * n,
                R = (long long int)mais * n - menos;
  if (L <= n && n <= R) {
    cout << "Possible\n";
    vector<int> nums(mais + menos);
    long long int sum = L;
    for (int i = 0; i < mais; ++i) {
      int add = (int)min(n - 1LL, n - sum);
      nums[i] = 1 + add;
      sum += add;
    }
    for (int i = 0; i < menos; ++i) {
      int sub = (int)min(n - 1LL, n - sum);
      nums[mais + i] = n - sub;
      sum += sub;
    }
    cout << nums[0];
    int indices[2] = {1, mais};
    for (int i = 0; i < sinal.size(); ++i) {
      int x = nums[indices[sinal[i] == '+' ? 0 : 1]++];
      cout << " " << sinal[i] << " " << x;
    }
    cout << " = " << n << "\n";
  } else
    cout << "Impossible\n";
  return 0;
}
