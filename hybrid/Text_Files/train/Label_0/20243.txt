#include <bits/stdc++.h>
using namespace std;
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return 1; } return 0; }
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return 1; } return 0; }

#define COUT(x) cout << #x << " = " << (x) << " (L" << __LINE__ << ")" << endl
template<class T1, class T2> ostream& operator << (ostream &s, pair<T1,T2> P)
{ return s << '<' << P.first << ", " << P.second << '>'; }
template<class T> ostream& operator << (ostream &s, vector<T> P)
{ for (int i = 0; i < P.size(); ++i) { if (i > 0) { s << " "; } s << P[i]; } return s; }
template<class T> ostream& operator << (ostream &s, vector<vector<T> > P)
{ for (int i = 0; i < P.size(); ++i) { s << endl << P[i]; } return s << endl; }
template<class T> ostream& operator << (ostream &s, set<T> P)
{ for(auto it : P) { s << "<" << it << "> "; } return s << endl; }
template<class T1, class T2> ostream& operator << (ostream &s, map<T1,T2> P)
{ for(auto it : P) { s << "<" << it.first << "->" << it.second << "> "; } return s << endl; }


using Graph = vector<vector<int>>;
int N;
Graph G;

vector<vector<long long>> dp;
long long rec(int v, int p = -1) {
    int s = G[v].size();
    long long res = 0;
    dp[v].assign(s, -1);
    for (int i = 0; i < s; ++i) {
        int to = G[v][i];
        if (to == p) continue;
        dp[v][i] = rec(to, v);
        chmax(res, dp[v][i] + 1);
    }
    return res;
}

void rerec(int v, long long pval = 0, int p = -1) {
    int s = G[v].size();
    for (int i = 0; i < s; ++i) {
        int to = G[v][i];
        if (to == p) {
            dp[v][i] = pval;
            continue;
        }
    }
    vector<long long> left(s+1, -1), right(s+1, -1);
    for (int i = 0; i < s; ++i) {
        left[i+1] = max(left[i], dp[v][i]);
        right[i+1] = max(right[i], dp[v][s-i-1]);
    }
    for (int i = 0; i < s; ++i) {
        int to = G[v][i];
        if (to == p) continue;
        rerec(to, max(left[i], right[s-i-1]) + 1, v);
    }
}

void solve() {
    bool ispath = true;
    for (int v = 0; v < N; ++v) {
        if (G[v].size() > 2) ispath = false;
    }
    if (ispath) {
        for (int i = 0; i < N; ++i) cout << 1;
        cout << endl;
        return;
    }

    dp.assign(N, vector<long long>());
    rec(0);
    rerec(0);
    long long res = 2;
    for (int v = 0; v < N; ++v) {
        if (G[v].size() <= 2) continue;
        vector<long long> a;
        for (int i = 0; i < G[v].size(); ++i) a.push_back(dp[v][i]+1);
        sort(a.begin(), a.end(), greater<long long>());
        long long tmp = a[0] + a[2] - (a[0] == a[2]);
        chmax(res, tmp);

        /*
        COUT(v+1);
        COUT(dp[v]);
        COUT(ma);
        COUT(mi);
        */
    }
    //COUT(res);

    if (res == 2) {
        for (int k = 1; k <= N; ++k) cout << "1";
        cout << endl;
    }
    else {
        cout << "11";
        for (int k = 3; k <= res; ++k) cout << "0";
        for (int k = res+1; k <= N; ++k) cout << "1";
        cout << endl;
    }
}

int main() {
    while (cin >> N) {
        G.assign(N, vector<int>());
        for (int i = 0; i < N-1; ++i) {
            int a, b; cin >> a >> b; --a, --b;
            G[a].push_back(b);
            G[b].push_back(a);
        }
        solve();
    }
}
        

