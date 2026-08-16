#include <bits/stdc++.h>
using namespace std;
template <class T>
inline bool Up(T &a, const T &b) {
  if (a < b) {
    a = b;
    return true;
  }
  return false;
}
template <class T>
inline bool Down(T &a, const T &b) {
  if (a > b) {
    a = b;
    return true;
  }
  return false;
}
inline int getus() {
  int tmp, c;
  while (tmp = fgetc(stdin), tmp < '0' || tmp > '9')
    ;
  tmp -= '0';
  while (c = fgetc(stdin), '0' <= c && c <= '9') tmp = tmp * 10 + c - '0';
  return tmp;
}
inline int getint() {
  int tmp, c, flag;
  while (flag = fgetc(stdin), flag != '-' && (flag < '0' || flag > '9'))
    ;
  if (flag == '-')
    tmp = 0;
  else
    tmp = flag - '0';
  while (c = fgetc(stdin), '0' <= c && c <= '9') tmp = tmp * 10 + c - '0';
  return flag == '-' ? -tmp : tmp;
}
int R, C, N, vis[400023], done[400023], ansR[400023], ansC[400023];
int s[400023], d1[400023], d2[400023];
vector<vector<int> > cycles_1, cycles_2;
int lex_smallest_head(string s) {
  int n = s.size(), i = 0, j = 1, k = 0;
  s += s;
  while (j < n && k < n) {
    if (s[i + k] == s[j + k])
      k++;
    else {
      if (s[i + k] < s[j + k])
        j += k + 1;
      else
        i += k + 1;
      k = 0;
    }
    if (i == j) ++j;
  }
  return i;
}
inline int encode(char c, int x) {
  if (c == 'L') return x;
  if (c == 'T') return x + R;
  if (c == 'R') return x + N;
  if (c == 'B') return x + N + R;
  assert(0);
  return -1;
}
inline pair<char, int> decode(int x) {
  if (x < R) return pair<char, int>('L', x);
  if (x < N) return pair<char, int>('T', x - R);
  if (x < N + R) return pair<char, int>('R', x - N);
  if (x < N + N) return pair<char, int>('B', x - N - R);
  assert(0);
  return pair<char, int>('_', -1);
}
inline int opposite(int x) {
  if (x < N) return x + N;
  return x - N;
}
inline string getProfile(const vector<int> &cycle) {
  string res(cycle.size(), '\0');
  int size = cycle.size();
  for (int i = (0); i < (size); ++i) res[i] = decode(cycle[i]).first;
  return res;
}
inline int getType(const vector<int> &cycle) {
  if (cycle.size() != 8) return 0;
  string s = getProfile(cycle);
  if (s == "LTBLRBTR") return 1;
  if (s == "LBTLRTBR") return 2;
  return 0;
}
void DFS(int x, int *next, vector<int> &to) {
  if (vis[x]) return;
  vis[x] = true;
  to.push_back(x);
  DFS(next[x], next, to);
  DFS(opposite(x), next, to);
}
void shift(vector<int> &s, int shift) {
  vector<int> tmp(s);
  int size = s.size();
  for (int i = (0); i < (size); ++i) s[i] = tmp[(i + shift) % size];
}
bool match(int *next) {
  vector<vector<int> > S, T;
  for (int i = 0, size = cycles_2.size(); i < size; ++i) {
    vector<int> &c = cycles_2[i];
    string tmp = getProfile(c);
    shift(c, lex_smallest_head(tmp));
    S.push_back(c);
  }
  memcpy(vis, done, sizeof(vis));
  for (int i = (0); i < (N); ++i)
    if (!vis[i]) {
      vector<int> c;
      DFS(i, next, c);
      string tmp = getProfile(c);
      shift(c, lex_smallest_head(tmp));
      T.push_back(c);
    }
  int n = S.size();
  if (n != (int)T.size()) return false;
  if (n == 0) return true;
  int m = S[0].size();
  for (int i = (0); i < (n); ++i)
    if (m != (int)T[i].size()) return false;
  sort(S.begin(), S.end());
  sort(T.begin(), T.end());
  for (int i = (0); i < (n); ++i)
    for (int j = (0); j < (m); ++j) {
      int s = S[i][j], t = T[i][j];
      pair<char, int> ss(decode(s)), tt(decode(t));
      if (ss.first != tt.first) return false;
      if (ss.first == 'L' || ss.first == 'R')
        ansR[tt.second] = ss.second;
      else
        ansC[tt.second] = ss.second;
    }
  return true;
}
int main() {
  memset(vis, 0, sizeof(vis));
  memset(done, 0, sizeof(done));
  scanf("%d %d\n", &R, &C);
  N = R + C;
  for (int i = (0); i < (N); ++i) {
    char c1, c2;
    int x1, x2, p1, p2;
    scanf("%c %c %d %d\n", &c1, &c2, &x1, &x2);
    p1 = encode(c1, --x1);
    p2 = encode(c2, --x2);
    s[p1] = p2;
    s[p2] = p1;
  }
  for (int i = (0); i < (N); ++i)
    if (!vis[i]) {
      vector<int> cycle;
      DFS(i, s, cycle);
      if (getType(cycle))
        cycles_1.push_back(cycle);
      else
        cycles_2.push_back(cycle);
    }
  int cnt = 0;
  for (int size = cycles_1.size(), i = 0; i < size; ++i) {
    const vector<int> &cycle = cycles_1[i];
    int type = getType(cycle), a, b, c, d;
    if (type == 1) {
      ansR[i] = a = decode(cycle[0]).second;
      ansR[R - 1 - i] = b = decode(cycle[3]).second;
      ansC[i] = c = decode(cycle[1]).second;
      ansC[C - 1 - i] = d = decode(cycle[6]).second;
    } else {
      ansR[i] = a = decode(cycle[3]).second;
      ansR[R - 1 - i] = b = decode(cycle[0]).second;
      ansC[i] = c = decode(cycle[2]).second;
      ansC[C - 1 - i] = d = decode(cycle[5]).second;
    }
    done[encode('L', i)] = done[encode('L', R - 1 - i)] = 1;
    done[encode('R', i)] = done[encode('R', R - 1 - i)] = 1;
    done[encode('T', i)] = done[encode('T', C - 1 - i)] = 1;
    done[encode('B', i)] = done[encode('B', C - 1 - i)] = 1;
  }
  vector<int> o(N + N, 0);
  cnt = 0;
  for (int i = (R - 1); i >= (0); --i)
    if (!done[i]) o[cnt++] = i;
  for (int i = (0); i < (C); ++i)
    if (!done[i + R]) o[cnt++] = i + R;
  for (int i = (0); i < (R); ++i)
    if (!done[i + N]) o[cnt++] = i + N;
  for (int i = (C - 1); i >= (0); --i)
    if (!done[i + N + R]) o[cnt++] = i + N + R;
  for (int i = (0); i < (cnt); ++i) d1[o[i]] = o[cnt - 1 - i];
  cnt = 0;
  for (int i = (0); i < (R); ++i)
    if (!done[i]) o[cnt++] = i;
  for (int i = (0); i < (C); ++i)
    if (!done[i + N + R]) o[cnt++] = i + N + R;
  for (int i = (R - 1); i >= (0); --i)
    if (!done[i + N]) o[cnt++] = i + N;
  for (int i = (C - 1); i >= (0); --i)
    if (!done[i + R]) o[cnt++] = i + R;
  for (int i = (0); i < (cnt); ++i) d2[o[i]] = o[cnt - 1 - i];
  if (match(d1) || match(d2)) {
    for (int i = (0); i < (R); ++i)
      printf("%d%c", ansR[i] + 1, (i == R - 1) ? '\n' : ' ');
    for (int i = (0); i < (C); ++i)
      printf("%d%c", ansC[i] + 1, (i == C - 1) ? '\n' : ' ');
  } else
    puts("No solution");
  return 0;
}
