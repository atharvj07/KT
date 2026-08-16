#include <iostream>
#include <cstdio>
#include <cassert>
#include <cstring>
#include <vector>
#include <valarray>
#include <array>
#include <queue>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <complex>
#include <random>
#include <bitset>

using namespace std;
using ll = long long;
using ull = unsigned long long;
using P = pair<int, int>;

using B = ull;
bool getb(B b, int x, int y, int z) {
//    assert(0 <= x && x < 4);
//    assert(0 <= y && y < 4);
//    assert(0 <= z && z < 4);
    ull mp = (1ULL << (z*16+y*4+x));
    return (b & mp) != 0;
}

B setb(B b, int x, int y, int z, bool d) {
//    assert(0 <= x && x < 4);
//    assert(0 <= y && y < 4);
//    assert(0 <= z && z < 4);
    ull mp = (1ULL << (z*16+y*4+x));
    if (d) b |= mp;
    else b &= ~mp;
    return b;
}

void prib(B b) {
    for (int z = 0; z < 3; z++) {
        for (int y = 0; y < 3; y++) {
            for (int x = 0; x < 3; x++) {
                if (getb(b, x, y, z)) {
                    printf("*");
                } else {
                    printf(".");
                }
            }
            printf("\n");
        }
        printf("\n");
    }
}
using BS = array<B, 24>;
int W, D, H;
vector<BS> Piese;
int Pisz[30];
int PS;

using Z = pair<B, int>;
set<Z> s[30];
bool dfs(B b, int ump) {
//    prib(b);
    if (ump == (1<<PS) - 1) return true;
    int bc = __builtin_popcount(ump);
    if (4 <= bc) {
        if (s[bc].count(Z(b, ump))) return false;
        s[bc].insert(Z(b, ump));
    }
    int nx, ny, nz;
    for (int z = H-1; z >= 0; z--) {
        for (int y = D-1; y >= 0; y--) {
            for (int x = W-1; x >= 0; x--) {
                if (!getb(b, x, y, z)) {
                    nx = x; ny = y; nz = z;
                }
            }
        }
    }
//    if (nx == -1) return true;
    for (int i = PS-1; i >= 0; i--) {
        if (ump & (1<<i)) continue;
        for (int j = Pisz[i]-1; j >= 0; j--) {
            B now = Piese[i][j];
            int fx = -1, fy;
            {
                bool f = false;
                for (int y = 0; y < 3; y++) {
                    for (int x = 0; x < 3; x++) {
                        if (getb(now, x, y, 0)) {
                            fx = x; fy = y;
                            f = true;
                            break;
                        }
                    }
                    if (f) break;
                }
            }
            B nb = b;
            bool f = true;
            int offx = nx - fx, offy = ny - fy;
            for (int z = 0; z < 3; z++) {
                for (int y = 0; y < 3; y++) {
                    for (int x = 0; x < 3; x++) {
                        if (!getb(now, x, y, z)) continue;
                        int sx = offx + x;
                        int sy = offy + y;
                        int sz = nz + z;
                        if (sx < 0 or W <= sx) f = false;
                        else if (sy < 0 or D <= sy) f = false;
                        else if (sz < 0 or H <= sz) f = false;
                        else if (getb(b, sx, sy, sz)) f = false;
                        else nb = setb(nb, sx, sy, sz, true);
                        if (!f) goto end_loop;
                    }
                }
            }
            end_loop:
            if (!f) continue;
            if (dfs(nb, ump | (1<<i))) return true;
        }
    }
    return false;
}

bool calc() {
//    s.clear();
    for (int i = 0; i < 30; i++) {
        s[i].clear();
    }
    return dfs(0, 0);
}


B shrink(B b) {
    B nb;
    while (true) {
        bool f = true;
        for (int z = 0; z < 3; z++) {
            for (int y = 0; y < 3; y++) {
                if (getb(b, 0, y, z)) {
                    f = false;
                    break;
                }
            }
        }
        if (!f) break;
        nb = 0;
        for (int z = 0; z < 3; z++) {
            for (int y = 0; y < 3; y++) {
                for (int x = 0; x < 2; x++) {
                    nb = setb(nb, x, y, z, getb(b, x+1, y, z));
                }
            }
        }
        b = nb;
    }
    while (true) {
        bool f = true;
        for (int x = 0; x < 3; x++) {
            for (int z = 0; z < 3; z++) {
                if (getb(b, x, 0, z)) {
                    f = false;
                    break;
                }
            }
        }
        if (!f) break;
        nb = 0;
        for (int z = 0; z < 3; z++) {
            for (int y = 0; y < 2; y++) {
                for (int x = 0; x < 3; x++) {
                    nb = setb(nb, x, y, z, getb(b, x, y+1, z));
                }
            }
        }
        b = nb;
    }
    while (true) {
        bool f = true;
        for (int y = 0; y < 3; y++) {
            for (int x = 0; x < 3; x++) {
                if (getb(b, x, y, 0)) {
                    f = false;
                    break;
                }
            }
        }
        if (!f) break;
        nb = 0;
        for (int z = 0; z < 2; z++) {
            for (int y = 0; y < 3; y++) {
                for (int x = 0; x < 3; x++) {
                    nb = setb(nb, x, y, z, getb(b, x, y, z+1));
                }
            }
        }
        b = nb;
    }
    return b;
}


bool solve() {
    int N;
    cin >> W >> D >> H >> N;
    if (!W) return false;
    vector<B> v;
    for (int i = 0; i < N; i++) {
        B b = 0;
        int w, d, h;
        cin >> w >> d >> h;
        for (int z = 0; z < h; z++) {
            for (int y = 0; y < d; y++) {
                for (int x = 0; x < w; x++) {
                    char c;
                    cin >> c;
                    bool f = c == '*';
                    b = setb(b, x, y, z, f);
                }
            }
        }
        v.push_back(b);
    }
    vector<BS> nv;
    for (B b: v) {
//        printf("ro b %016llx\n", b);
        BS nb = {};
        for (int z = 0; z < 3; z++) {
            for (int y = 0; y < 3; y++) {
                for (int x = 0; x < 3; x++) {
                    nb[ 0] = setb(nb[ 0], x, y, z, getb(b,   x,   y,   z));
                    nb[ 1] = setb(nb[ 1], x, y, z, getb(b, 2-x, 2-y,   z));
                    nb[ 2] = setb(nb[ 2], x, y, z, getb(b, 2-x,   y, 2-z));
                    nb[ 3] = setb(nb[ 3], x, y, z, getb(b,   x, 2-y, 2-z));

                    nb[ 4] = setb(nb[ 4], x, y, z, getb(b, 2-x,   z,   y));
                    nb[ 5] = setb(nb[ 5], x, y, z, getb(b,   x, 2-z,   y));
                    nb[ 6] = setb(nb[ 6], x, y, z, getb(b,   x,   z, 2-y));
                    nb[ 7] = setb(nb[ 7], x, y, z, getb(b, 2-x, 2-z, 2-y));

                    nb[ 8] = setb(nb[ 8], x, y, z, getb(b, 2-y,   x,   z));
                    nb[ 9] = setb(nb[ 9], x, y, z, getb(b,   y, 2-x,   z));
                    nb[10] = setb(nb[10], x, y, z, getb(b,   y,   x, 2-z));
                    nb[11] = setb(nb[11], x, y, z, getb(b, 2-y, 2-x, 2-z));

                    nb[12] = setb(nb[12], x, y, z, getb(b,   y,   z,   x));
                    nb[13] = setb(nb[13], x, y, z, getb(b, 2-y, 2-z,   x));
                    nb[14] = setb(nb[14], x, y, z, getb(b, 2-y,   z, 2-x));
                    nb[15] = setb(nb[15], x, y, z, getb(b,   y, 2-z, 2-x));

                    nb[16] = setb(nb[16], x, y, z, getb(b,   z,   x,   y));
                    nb[17] = setb(nb[17], x, y, z, getb(b, 2-z, 2-x,   y));
                    nb[18] = setb(nb[18], x, y, z, getb(b, 2-z,   x, 2-y));
                    nb[19] = setb(nb[19], x, y, z, getb(b,   z, 2-x, 2-y));

                    nb[20] = setb(nb[20], x, y, z, getb(b, 2-z,   y,   x));
                    nb[21] = setb(nb[21], x, y, z, getb(b,   z, 2-y,   x));
                    nb[22] = setb(nb[22], x, y, z, getb(b,   z,   y, 2-x));
                    nb[23] = setb(nb[23], x, y, z, getb(b, 2-z, 2-y, 2-x));
                }
            }
        }
        for (int i = 0; i < 24; i++) {
            nb[i] = shrink(nb[i]);
        }
        sort(nb.begin(), nb.end());
        Pisz[nv.size()] = unique(nb.begin(), nb.end()) - nb.begin();
        nv.push_back(nb);
    }
    Piese = nv;
    PS = (int)nv.size();
    if (calc()) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return true;
}

int main() {
    while (solve()) {}
    return 0;
}