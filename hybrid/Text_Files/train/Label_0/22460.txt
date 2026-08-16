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
#include <stack>

using namespace std;
using ll = long long;
using ull = unsigned long long;

using P = array<int, 2>;
using Q = array<P, 3>;
using D = array<int, 64>;
D resD;
bool dfs(vector<Q> node, D data) {
    int m = (int)node.size();
    if (!m) {
        resD = data;
        return true;
    }
    int now = -1;
    D d = D();
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < 3; j++) {
            for (int k = 0; k < 2; k++) {
                if (!data[node[i][j][k]]) {
                    d[node[i][j][k] & ~(32)]++;
                }
            }
        }
    }
    int ma = -1;
    for (int i = 0; i < 32; i++) {
        if (ma <= d[i]) {
            ma = d[i];
            now = i;
        }
    }
    // for (int i = 0; i < m; i++) {
    //     for (int j = 0; j < 3; j++) {
    //         for (int k = 0; k < 2; k++) {
    //             if (!data[node[i][j][k]]) {
    //                 now = node[i][j][k];
    //             }
    //         }
    //     }
    // }
    assert(now != -1);
    {
        //now = true
        data[now] = 1;
        data[now ^ 32] = -1;
        vector<Q> n_node;
        bool err = false;
        for (int i = 0; i < m; i++) {
            bool ok = false;
            int ec = 0;
            for (int j = 0; j < 3; j++) {
                if (data[node[i][j][0]] == 1 and data[node[i][j][1]] == 1) {
                    ok = true;
                    break;
                }
                if (data[node[i][j][0]] == -1 or data[node[i][j][1]] == -1) {
                    ec++;
                }
            }
            if (ok) continue;
            if (ec == 3) {
                err = true;
                break;
            }
            n_node.push_back(node[i]);
        }
        if (!err and dfs(n_node, data)) return true;
    }
    {
        //now = false
        data[now] = -1;
        data[now ^ 32] = 1;
        vector<Q> n_node;
        bool err = false;
        for (int i = 0; i < m; i++) {
            bool ok = false;
            int ec = 0;
            for (int j = 0; j < 3; j++) {
                if (data[node[i][j][0]] == 1 and data[node[i][j][1]] == 1) {
                    ok = true;
                    break;
                }
                if (data[node[i][j][0]] == -1 or data[node[i][j][1]] == -1) {
                    ec++;
                }
            }
            if (ok) continue;
            if (ec == 3) {
                err = true;
                break;
            }
            n_node.push_back(node[i]);
        }
        if (!err and dfs(n_node, data)) return true;
    }
    return false;
}

bool solve() {
    int m;
    cin >> m;
    if (!m) return false;
    vector<Q> v(m);
    for (int i = 0; i < 3; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < m; j++) {
            for (int k = 0; k < 2; k++) {
                if ('A' <= s[3*j+1+k] && s[3*j+1+k] <= 'Z') {
                    v[j][i][k] = s[3*j+1+k] - 'A';
                }
                if ('a' <= s[3*j+1+k] && s[3*j+1+k] <= 'z') {
                    v[j][i][k] = s[3*j+1+k] - 'a' + 32;
                }
            }
        }
    }
    auto u = dfs(v, D());
    if (!u) {
        cout << "-1" << endl;
        return true;
    }
    vector<char> result;
    for (int i = 0; i < 32; i++) {
        if (resD[i+32] == 1) {
            result.push_back(i + 'A');
        }
    }
    cout << result.size() << " ";
    for (char c: result) {
        cout << c << " ";
    }
    cout << endl;
    return true;
}


int main() {
    ios::sync_with_stdio(false);
    while (solve()) {}
    return 0;
}