#include <bits/stdc++.h>
using namespace std;
inline int readChar();
template <class T = int>
inline T readInt();
template <class T = int>
inline void writeInt(T first, char end = 0);
inline void writeChar(int first);
inline void writeWord(const char *s);
static const int buf_size = 4096;
inline int getChar() {
  static char buf[buf_size];
  static int len = 0, pos = 0;
  if (pos == len) pos = 0, len = fread(buf, 1, buf_size, stdin);
  if (pos == len) return -1;
  return buf[pos++];
}
inline int readChar() {
  int c = getChar();
  while (c <= 32) c = getChar();
  return c;
}
template <class T>
inline T readInt() {
  int s = 1, c = readChar();
  T first = 0;
  if (c == '-') s = -1, c = getChar();
  while ('0' <= c && c <= '9') first = first * 10 + c - '0', c = getChar();
  return s == 1 ? first : -first;
}
static int write_pos = 0;
static char write_buf[buf_size];
inline void writeChar(int first) {
  if (write_pos == buf_size)
    fwrite(write_buf, 1, buf_size, stdout), write_pos = 0;
  write_buf[write_pos++] = first;
}
template <class T>
inline void writeInt(T first, char end) {
  if (first < 0) writeChar('-'), first = -first;
  char s[24];
  int n = 0;
  while (first || !n) s[n++] = '0' + first % 10, first /= 10;
  while (n--) writeChar(s[n]);
  if (end) writeChar(end);
}
inline void writeWord(const char *s) {
  while (*s) writeChar(*s++);
}
struct Flusher {
  ~Flusher() {
    if (write_pos) fwrite(write_buf, 1, write_pos, stdout), write_pos = 0;
  }
} flusher;
const int sizeOf = 2e5 + 10;
int n, k;
bool univ[sizeOf];
vector<int> edge[sizeOf];
int cnt[sizeOf];
long long sum_cut = 0;
void dfs(int i, int p = 0) {
  for (int j : edge[i]) {
    if (j == p) continue;
    dfs(j, i);
    sum_cut += min(cnt[j], k - cnt[j]);
    cnt[i] += cnt[j];
  }
  cnt[i] += univ[i];
}
const string FileName = "input";
int main(int argc, char const *argv[]) {
  ios::sync_with_stdio(false);
  n = readInt();
  k = readInt();
  k <<= 1;
  for (int i = 0; i < k; ++i) {
    univ[readInt()] = true;
  }
  for (int i = 0; i < n - 1; ++i) {
    int L = readInt(), R = readInt();
    edge[L].push_back(R);
    edge[R].push_back(L);
  }
  dfs(1);
  cout << sum_cut << endl;
}
