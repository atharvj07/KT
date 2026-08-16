#include <bits/stdc++.h>
using namespace std;
void dbg_out() { cerr << "\b\b]\n"; }
template <typename Head, typename... Tail>
void dbg_out(Head H, Tail... T) {
  cerr << H << ", ";
  dbg_out(T...);
}
vector<string> split(string s, char delim) {
  vector<string> v;
  stringstream ss(s);
  while (ss.good()) {
    string stk;
    getline(ss, stk, delim);
    if (stk.empty()) continue;
    v.push_back(stk);
  }
  return v;
}
const int INF = 2e9;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, k;
  cin >> n >> k;
  cin.get();
  string s;
  getline(cin, s);
  vector<string> X = split(s, ' ');
  vector<long long> A(n);
  vector<bool> ques(n, false);
  for (int i = 0; i < n; ++i) {
    A[i] = (X[i] == "?" ? '?' : stoi(X[i]));
    ques[i] = (X[i] == "?");
  }
  for (int i = 0; i < k; ++i) {
    vector<long long> nums;
    vector<bool> ques1;
    for (int j = i; j < n; j += k) {
      if (j > i and !ques[j] and !ques[j - k] and A[j - k] >= A[j]) {
        cout << "Incorrect sequence";
        return 0;
      }
      nums.push_back(A[j]);
      ques1.push_back(ques[j]);
    }
    for (int j = 0; j < (int)nums.size(); ++j) {
      if (!ques1[j]) continue;
      long long l = j;
      while (l < (int)nums.size() and ques1[l]) l++;
      long long left = (j ? nums[j - 1] + 1 : -INF);
      long long right = (l < (int)nums.size() ? nums[l] - 1 : INF);
      if (right - left + 1LL < l * 1LL - j) {
        cout << "Incorrect sequence";
        return 0;
      }
      if (left >= 0 and right >= 0) {
        for (int x = j; x < l; ++x) nums[x] = left++;
      } else if (left <= 0 and right <= 0) {
        for (int x = l - 1; x >= j; --x) nums[x] = right--;
      } else {
        int cnts = (l - j) / 2;
        int p = -cnts, q = cnts;
        if (left <= p and q <= right) {
          for (int x = l - 1; x >= j; --x) {
            nums[x] = cnts--;
          }
        } else if (p < left) {
          cnts = left;
          for (int x = j; x < l; ++x) nums[x] = cnts++;
        } else {
          cnts = right;
          for (int x = l - 1; x >= j; --x) {
            nums[x] = cnts--;
          }
        }
      }
      j = l - 1;
    }
    for (int x = 0, j = i; x < (int)nums.size(); ++x, j += k) {
      A[j] = nums[x];
    }
  }
  for (long long i : A) cout << i << ' ';
  return 0;
}
