#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <assert.h>
#include <vector>
#include <set>
#include <queue>

using namespace std;
typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
static const double EPS = 1e-9;
static const double PI = acos(-1.0);

#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define FOR(i, s, n) for (int i = (s); i < (int)(n); i++)
#define FOREQ(i, s, n) for (int i = (s); i <= (int)(n); i++)
#define FORIT(it, c) for (__typeof((c).begin())it = (c).begin(); it != (c).end(); it++)
#define MEMSET(v, h) memset((v), h, sizeof(v))

const int dx[6] = { 1, -1, 0, 0, 0, 0 };
const int dy[6] = { 0, 0, 1, -1, 0, 0 };
const int dz[6] = { 0, 0, 0, 0, 1, -1 };

typedef int Weight;
struct Edge {
  int src;
  int dest;
  Weight weight;
  Edge(int src, int dest, Weight weight) : src(src), dest(dest), weight(weight) {;}
  bool operator<(const Edge &rhs) const {
    if (weight != rhs.weight) { return weight > rhs.weight; }
    if (src != rhs.src) { return src < rhs.src; }
    return dest < rhs.dest;
  }
};
typedef vector<Edge> Edges;
typedef vector<Edges> Graph;
typedef vector<Weight> Array;
typedef vector<Array> Matrix;

void printMatrix(const Matrix &matrix) {
  for (int y = 0; y < (int)matrix.size(); y++) {
    for (int x = 0; x < (int)matrix[y].size(); x++) {
      printf("%d ", matrix[y][x]);
    }
    puts("");
  }
}

Weight augment(const Graph &g, Matrix &capacity, const vector<int> &level, vector<bool> &finished, int from, int t, Weight cur) {
  if (from == t || cur == 0) { return cur; }
  if (finished[from]) { return 0; }
  for (Edges::const_iterator it = g[from].begin(); it != g[from].end(); it++) {
    int to = it->dest;
    if (level[to] <= level[from]) { continue; }
    Weight f = augment(g, capacity, level, finished, to, t, min(cur, capacity[from][to]));
    if (f > 0) {
      capacity[from][to] -= f;
      capacity[to][from] += f;
      return f;
    }
  }
  finished[from] = true;
  return 0;
}

Weight MaxFlow(const Graph &g, int s, int t) {
  int n = g.size();
  Matrix capacity(n, Array(n));
  for (int from = 0; from < n; from++) {
    for (Edges::const_iterator it = g[from].begin(); it != g[from].end(); it++) {
      int to = it->dest;
      capacity[from][to] += it->weight;
    }
  }
  int ans = 0;
  while (true) {
    vector<int> level(n, -1);
    level[s] = 0;
    queue<int> que;
    que.push(s);
    for (int d = n; !que.empty() && level[que.front()] < d; ) {
      int from = que.front();
      que.pop();
      if (from == t) { d = level[from]; }
      for (Edges::const_iterator it = g[from].begin(); it != g[from].end(); it++) {
        int to = it->dest;
        if (capacity[from][to] > 0 && level[to] == -1) {
          que.push(to);
          level[to] = level[from] + 1;
        }
      }
    }
    vector<bool> finished(n);
    bool end = true;
    while (true) {
      Weight f = augment(g, capacity, level, finished, s, t, 1000000000);
      if (f == 0) { break; }
      ans += f;
      end = false;
    }
    if (end) { break; }
  }
  return ans;
}

void printState(int enc);

struct Block {
  int size;
  bool block[3][3][3];
  Block() : size(0) {
    MEMSET(block, false);
  }
  Block RotateX() {
    Block ret = *this;
    REP(x, 3) {
      ret.block[x][0][0] = block[x][2][0];
      ret.block[x][2][0] = block[x][2][2];
      ret.block[x][2][2] = block[x][0][2];
      ret.block[x][0][2] = block[x][0][0];
      ret.block[x][1][0] = block[x][2][1];
      ret.block[x][2][1] = block[x][1][2];
      ret.block[x][1][2] = block[x][0][1];
      ret.block[x][0][1] = block[x][1][0];
    }
    return ret;
  }
  Block RotateY() {
    Block ret = *this;
    REP(y, 3) {
      ret.block[0][y][0] = block[2][y][0];
      ret.block[2][y][0] = block[2][y][2];
      ret.block[2][y][2] = block[0][y][2];
      ret.block[0][y][2] = block[0][y][0];
      ret.block[1][y][0] = block[2][y][1];
      ret.block[2][y][1] = block[1][y][2];
      ret.block[1][y][2] = block[0][y][1];
      ret.block[0][y][1] = block[1][y][0];
    }
    return ret;
  }
  Block RotateZ() {
    Block ret = *this;
    REP(z, 3) {
      ret.block[0][0][z] = block[2][0][z];
      ret.block[2][0][z] = block[2][2][z];
      ret.block[2][2][z] = block[0][2][z];
      ret.block[0][2][z] = block[0][0][z];
      ret.block[1][0][z] = block[2][1][z];
      ret.block[2][1][z] = block[1][2][z];
      ret.block[1][2][z] = block[0][1][z];
      ret.block[0][1][z] = block[1][0][z];
    }
    return ret;
  }
  int Encode() {
    int ret = 0;
    REP(x, 3) REP(y, 3) REP(z, 3) {
      if (block[x][y][z]) {
        ret |= 1 << (z * 9 + y * 3 + x);
      }
    }
    return ret;
  }
  bool Move(int dir, int dist) {
    Block ret = *this;
    MEMSET(ret.block, 0);
    REP(x, 3) REP(y, 3) REP(z, 3) {
      if (block[x][y][z]) {
        int nx = x + dx[dir] * dist;
        int ny = y + dy[dir] * dist;
        int nz = z + dz[dir] * dist;
        if (nx < 0 || nx >= 3 || ny < 0 || ny >= 3 || nz < 0 || nz >= 3) { return false; }
        ret.block[nx][ny][nz] = true;
      }
    }
    *this = ret;
    return true;
  }
  bool operator<(const Block &rhs) const {
    return size < rhs.size;
  }
};

int StateRotateX(int enc) {
  int ret = enc & ((1 << 12) | (1 << 13) | (1 << 14));
  REP(x, 3) {
    ret |= ((enc >> (9 * 0 + 3 * 2 + x)) & 1) << (9 * 0 + 3 * 0 + x);
    ret |= ((enc >> (9 * 2 + 3 * 2 + x)) & 1) << (9 * 0 + 3 * 2 + x);
    ret |= ((enc >> (9 * 2 + 3 * 0 + x)) & 1) << (9 * 2 + 3 * 2 + x);
    ret |= ((enc >> (9 * 0 + 3 * 0 + x)) & 1) << (9 * 2 + 3 * 0 + x);
    ret |= ((enc >> (9 * 1 + 3 * 2 + x)) & 1) << (9 * 0 + 3 * 1 + x);
    ret |= ((enc >> (9 * 2 + 3 * 1 + x)) & 1) << (9 * 1 + 3 * 2 + x);
    ret |= ((enc >> (9 * 1 + 3 * 0 + x)) & 1) << (9 * 2 + 3 * 1 + x);
    ret |= ((enc >> (9 * 0 + 3 * 1 + x)) & 1) << (9 * 1 + 3 * 0 + x);
  }
  return ret;
}
int StateRotateY(int enc) {
  int ret = enc & ((1 << 10) | (1 << 13) | (1 << 16));
  REP(y, 3) {
    ret |= ((enc >> (9 * 0 + 3 * y + 2)) & 1) << (9 * 0 + 3 * y + 0);
    ret |= ((enc >> (9 * 2 + 3 * y + 2)) & 1) << (9 * 0 + 3 * y + 2);
    ret |= ((enc >> (9 * 2 + 3 * y + 0)) & 1) << (9 * 2 + 3 * y + 2);
    ret |= ((enc >> (9 * 0 + 3 * y + 0)) & 1) << (9 * 2 + 3 * y + 0);
    ret |= ((enc >> (9 * 1 + 3 * y + 2)) & 1) << (9 * 0 + 3 * y + 1);
    ret |= ((enc >> (9 * 2 + 3 * y + 1)) & 1) << (9 * 1 + 3 * y + 2);
    ret |= ((enc >> (9 * 1 + 3 * y + 0)) & 1) << (9 * 2 + 3 * y + 1);
    ret |= ((enc >> (9 * 0 + 3 * y + 1)) & 1) << (9 * 1 + 3 * y + 0);
  }
  return ret;
}
int StateRotateZ(int enc) {
  int ret = enc & ((1 << 4) | (1 << 13) | (1 << 22));
  REP(z, 3) {
    ret |= ((enc >> (9 * z + 3 * 0 + 2)) & 1) << (9 * z + 3 * 0 + 0);
    ret |= ((enc >> (9 * z + 3 * 2 + 2)) & 1) << (9 * z + 3 * 0 + 2);
    ret |= ((enc >> (9 * z + 3 * 2 + 0)) & 1) << (9 * z + 3 * 2 + 2);
    ret |= ((enc >> (9 * z + 3 * 0 + 0)) & 1) << (9 * z + 3 * 2 + 0);
    ret |= ((enc >> (9 * z + 3 * 1 + 2)) & 1) << (9 * z + 3 * 0 + 1);
    ret |= ((enc >> (9 * z + 3 * 2 + 1)) & 1) << (9 * z + 3 * 1 + 2);
    ret |= ((enc >> (9 * z + 3 * 1 + 0)) & 1) << (9 * z + 3 * 2 + 1);
    ret |= ((enc >> (9 * z + 3 * 0 + 1)) & 1) << (9 * z + 3 * 1 + 0);
  }
  return ret;
}

Block Decode(int enc) {
  Block ret;
  REP(z, 3) REP(y, 3) REP(x, 3) {
    if (enc & (1 << (z * 9 + y * 3 + x))) {
      ret.block[x][y][z] = true;
      ret.size++;
    }
  }
  return ret;
}

int Normalize(int enc) {
  int ret = 1 << 30;
  REP(i, 6) {
    if (i & 1) {
      enc = StateRotateX(enc);
    } else {
      enc = StateRotateY(enc);
    }
    REP(z, 4) {
      enc = StateRotateZ(enc);
      if (enc < ret) {
        ret = enc;
      }
    }
  }
  return ret;
}

void printState(int state) {
  REP(z, 3) {
    REP(y, 3) {
      REP(x, 3) {
        if (state & (1 << (9 * z + 3 * y + x))) {
          putchar('*');
        } else {
          putchar('.');
        }
      }
      puts("");
    }
    puts("");
  }
}

int W, D, H, N;
set<int> visit;
set<int> blockState[27];
Block blocks[27];

int restCheck(int state) {
  Graph g(29);
  Block block = Decode(state);
  REP(x, 3) {
    REP(y, 3) {
      REP(z, 3) {
        if (block.block[x][y][z]) { continue; }
        int from = z * 9 + y * 3 + x;
        if (from % 2 == 0) {
          g[27].push_back(Edge(27, from, 1));
        } else {
          g[from].push_back(Edge(from, 28, 1));
          continue;
        }
        REP(dir, 6) {
          int nx = x + dx[dir];
          int ny = y + dy[dir];
          int nz = z + dz[dir];
          if (nx < 0 || nx >= 3 || ny < 0 || ny >= 3 || nz < 0 || nz >= 3) { continue; }
          if (block.block[nx][ny][nz]) { continue; }
          int to = nz * 9 + ny * 3 + nx;
          g[from].push_back(Edge(from, to, 1));
          g[to].push_back(Edge(to, from, 0));
        }
      }
    }
  }
  return MaxFlow(g, 27, 28);
}

bool calc(int depth, int state) {
  if (depth == N) { return true; }
  state = Normalize(state);
  if (visit.count(state)) { return false; }
  visit.insert(state);
  if (blocks[depth].size == 2) {
    return restCheck(state) >= N - depth;
  }
  FORIT(it, blockState[depth]) {
    if (state & *it) { continue; }
    if (calc(depth + 1, state | *it)) { return true; }
  }
  return false;
}

int main() {
  while (scanf("%d %d %d %d", &W, &D, &H, &N), W|D|H|N) {
    visit.clear();
    REP(i, 27) { blockState[i].clear(); }
    int iniState = 0;
    REP(x, 3) REP(y, 3) REP(z, 3) {
      if (x >= W || y >= D || z >= H) {
        iniState |= 1 << (9 * z + 3 * y + x);
      }
    }
    int m = 0;
    REP(i, N) {
      int w, d, h;
      scanf("%d %d %d", &w, &d, &h);
      blocks[m] = Block();
      REP(z, h) {
        REP(y, d) {
          REP(x, w) {
            char c;
            scanf(" %c ", &c);
            if (c == '*') {
              blocks[m].block[x][y][z] = true;
              blocks[m].size++;
            }
          }
        }
      }
      if (blocks[m].size > 1) { m++; }
    }
    N = m;
    sort(blocks, blocks + N);
    reverse(blocks, blocks + N);
    REP(i, N) {
      REP(j, 6) {
        if (j & 1) {
          blocks[i] = blocks[i].RotateX();
        } else {
          blocks[i] = blocks[i].RotateY();
        }
        REP(z, 4) {
          blocks[i] = blocks[i].RotateZ();
          FOREQ(dist1, -2, 2) {
            FOREQ(dist2, -2, 2) {
              FOREQ(dist3, -2, 2) {
                Block b = blocks[i];
                if (b.Move(0, dist1) &&
                    b.Move(2, dist2) &&
                    b.Move(4, dist3)) {
                  int enc = b.Encode();
                  blockState[i].insert(enc);
                }
              }
            }
          }
        }
      }
    }
    if (calc(0, iniState)) {
      puts("Yes");
    } else {
      puts("No");
    }
  }
}