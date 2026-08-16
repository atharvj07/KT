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

using namespace std;
using ll = long long;
using ull = unsigned long long;
constexpr int TEN(int n) {return (n==0)?1:10*TEN(n-1);}

using R = long double;
const R EPS = 1e-9;
const int MS = 30030;
using P = array<ll, 2>;

namespace StopWatch {
    clock_t st;
    bool f = false;
    void start() {
        f = true;
        st = clock();
    }
    int msecs() {
        assert(f);
        return (clock()-st)*1000 / CLOCKS_PER_SEC;
    }
}


vector<P> solve(int N, vector<ll> s) {
    int M = (int)s.size();
    vector<P> rng(M);
    fill_n(rng.begin(), M, P{0, N});
    ll ssm = 0;
    for (int i = 0; i < M; i++) {
        ssm += s[i];
    }
    int deg[MS];
    fill_n(deg, MS, 0);
    for (int i = 0; i < M; i++) {
        deg[s[i]]++;
    }
    map<int, ll> mp;
    StopWatch::start();
    for (int i = 0; i < M; i++) {
        if (s[i] == 0) continue;
        if (mp.count(s[i])) {
            rng[i][0] = mp[s[i]];
            continue;
        }
        if (i % 1000 == 0) {
//            printf("end %d %d\n", i, StopWatch::msecs());
        }
        ll l = (N*s[i]-1) / (ssm+M-1);

        while (l < N) {
            l++;
            ll sm = (ssm-s[i]+M-1)*l-(M-1)*(s[i]-1) - s[i]*(N-l);
/*            for (int j = 0; j < M; j++) {
                if (i == j) continue;
                sm += s[i]-1-(s[j]+1)*l%s[i];
                if (0 <= sm) {
                    break;
                }
            }*/
            sm -= s[i]-1-(s[i]+1)*l%s[i];
            int l2 = l%s[i];
            int now = 0;
            for (int j = 0; j < MS; j++) {
                now += l2; if (now >= s[i]) now -= s[i];
                sm += (s[i]-1-now)*deg[j];
                if (0 <= sm) break;
            }
            if (0 <= sm) break;
        }
        mp[s[i]] = rng[i][0] = l;
    }
    mp.clear();
    StopWatch::start();
    for (int i = 0; i < M; i++) {
        if (mp.count(s[i])) {
            rng[i][1] = mp[s[i]];
            continue;
        }
        if (i % 1000 == 0) {
//            printf("end %d %d\n", i, StopWatch::msecs());
        }
        ll l = (N*(s[i]+1)-(M-1)*s[i]) / (ssm+1);
        while (l <= N) {
            l++;
            ll sm = (ssm-s[i])*l - (s[i]+1)*(N-l);
            sm -= s[i] - (s[i]*l+s[i])%(s[i]+1);
            int l2 = l%(s[i]+1);
            int now = s[i];
/*            for (int j = 0; j < M; j++) {
                if (i == j) continue;
                sm += s[i] - (s[j]*l+s[i])%(s[i]+1);
                if (0 < sm) {
                    break;
                }
            }*/
            for (int j = 0; j < MS; j++) {
                sm += (s[i]-now)*deg[j];
                now += l2; if (now >= s[i]+1) now -= s[i]+1;
                if (0 < sm) break;
            }
            if (0 < sm) break;
        }
        mp[s[i]] = rng[i][1] = l-1;
    }
    return rng;
}


int main2() {
    int N, M;
    cin >> N >> M;
    assert(M <= 30000);
    vector<ll> s;
    for (int i = 0; i < M; i++) {
        int x;
        cin >> x;
        s.push_back(x);
    }
    int idx[M], ridx[M];
    iota(idx, idx+M, 0);
    sort(idx, idx+M, [&](const int &l, const int &r){
        return s[l] < s[r];
    });
    for (int i = 0; i < M; i++) {
        ridx[idx[i]] = i;
    }
    vector<ll> s2(M);
    for (int i = 0; i < M; i++) {
        s2[i] = s[idx[i]];
    }
    auto rng = solve(N, s2);
    for (int i = 0; i < M; i++) {
        if (rng[i][0] > rng[i][1]) {
            printf("impossible\n");
            return 0;
        }
    }
    for (int i = 0; i < M; i++) {
        printf("%lld %lld\n", rng[ridx[i]][0], rng[ridx[i]][1]);
    }
    return 0;
}

/*stack size???????????????*/
int main() {
    static ll eord, enew;
    const int sz = 32*1024*1024;
    static unsigned char *p = (unsigned char*)malloc(sz);
    enew = ((ll)(p+sz-1) & ~0xff);
    __asm__ volatile("mov %%rsp, %0" : "=r"(eord));
    __asm__ volatile("mov %0, %%rsp" : : "r"(enew));
    main2();
    __asm__ volatile("mov %0, %%rsp" : : "r"(eord));
    return 0;
}