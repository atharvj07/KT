#include <bits/stdc++.h>
using namespace std;
typedef struct node {
  int index;
  long long num;
  node() {}
  node(int _index, long long _num) {
    index = _index;
    num = _num;
  }
} node;
bool cmp(const node& a, const node& b) { return a.num < b.num; }
int mylowerbound(const vector<node>& vec, long long n) {
  int start = 0, end = vec.size() - 1;
  if (n < vec[0].num) return 0;
  if (n > vec.back().num) return vec.size();
  while (start <= end) {
    if (start == end)
      return start;
    else if (start == end - 1) {
      if (vec[start].num >= n) return start;
      return end;
    } else {
      int mid = start + (end - start) / 2;
      if (vec[mid].num >= n)
        end = mid;
      else
        start = mid + 1;
    }
  }
  return -1;
}
int main() {
  int n = 0;
  long long x1 = 0, x2 = 0;
  cin >> n >> x1 >> x2;
  vector<node> vec;
  for (int i = 0; i < n; i++) {
    int curnum = 0;
    scanf("%d", &curnum);
    vec.push_back(node(i, curnum));
  }
  sort(vec.begin(), vec.end(), cmp);
  for (int i = 1; i <= n; i++) {
    long long curNum = (x1 + i - 1) / i;
    int index = mylowerbound(vec, curNum);
    int nextIndex = i + index;
    if (nextIndex < n) {
      curNum = vec[nextIndex].num;
      int len = (x2 + curNum - 1) / curNum;
      if (len <= n - nextIndex) {
        cout << "Yes" << endl;
        cout << i << " " << len << endl;
        for (int j = index; j < nextIndex; j++) {
          cout << vec[j].index + 1 << " ";
        }
        cout << endl;
        for (int j = 0; j < len; j++) {
          cout << vec[j + nextIndex].index + 1 << " ";
        }
        cout << endl;
        return 0;
      }
    }
  }
  for (int i = 1; i <= n; i++) {
    long long curNum = (x2 + i - 1) / i;
    int index = mylowerbound(vec, curNum);
    int nextIndex = i + index;
    if (nextIndex < n) {
      curNum = vec[nextIndex].num;
      int len = (x1 + curNum - 1) / curNum;
      if (len <= n - nextIndex) {
        cout << "Yes" << endl;
        cout << len << " " << i << endl;
        for (int j = 0; j < len; j++) {
          cout << vec[j + nextIndex].index + 1 << " ";
        }
        cout << endl;
        for (int j = index; j < nextIndex; j++) {
          cout << vec[j].index + 1 << " ";
        }
        cout << endl;
        return 0;
      }
    }
  }
  cout << "No" << endl;
  return 0;
}
