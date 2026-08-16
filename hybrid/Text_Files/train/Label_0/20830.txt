#include <bits/stdc++.h>
using namespace std;
int a[4000001];
long long b[4000001];
long long qsum[4000001];
int rakha[4000001];
struct node {
  long long x, y, sum;
};
struct cmp {
  bool operator()(const node &a, const node &b) { return a.sum < b.sum; }
};
priority_queue<node, vector<node>, cmp> pq;
int ar[100][100];
int main() {
  long long n, t, i, j, n1, k, ans, m, f = 0, s = 0, c = 0, p = 1, c1 = 0,
                                       p1 = 0, p2 = 0, res = 0, c2, s1, s2, ss,
                                       pp, x, y;
  string st, str;
  cin >> st >> str;
  if (st == str) {
    cout << "YES" << endl;
  } else {
    if (st == "sunday" && (str == "tuesday" || str == "wednesday")) {
      cout << "YES" << endl;
    } else if (st == "tuesday" && (str == "thursday" || str == "friday")) {
      cout << "YES" << endl;
    } else if (st == "saturday" && (str == "monday" || str == "tuesday")) {
      cout << "YES" << endl;
    } else if (st == "monday" && (str == "wednesday" || str == "thursday")) {
      cout << "YES" << endl;
    } else if (st == "wednesday" && (str == "friday" || str == "saturday")) {
      cout << "YES" << endl;
    } else if (st == "thursday" && (str == "sunday" || str == "saturday")) {
      cout << "YES" << endl;
    } else if (st == "friday" && (str == "sunday" || str == "monday")) {
      cout << "YES" << endl;
    } else {
      cout << "NO" << endl;
    }
  }
  return 0;
}
