#include<bits/stdc++.h>
using namespace std;

const int N = 2500;
int tr[N][26], leaf[N];
int trid = 0;

void add(string s) {
    int cur = 0;
    for (char c: s) {
        int ch = c-'a';
        if (tr[cur][ch] == 0) {
            tr[cur][ch] = ++trid;
        }
        cur = tr[cur][ch];
    }
    leaf[cur]++;
}

vector<int> to[N];
int nid[N][N];

void go(int a, int b);
void addtr(int a, int b, int na, int nb, int ch) {
//    cout<<a<<","<<b<<" -- "<<char('a' + ch)<<" -- "<<na<<" "<<nb<<endl;
    go(na, nb);
    to[nid[a][b]].push_back(nid[na][nb]);
}

int iid = 0;
void go(int a, int b) {
    if (nid[a][b] != -1)  return;
    nid[a][b] = iid++;
    for (int i=0; i<26; i++) {
        if (!tr[a][i] || !tr[b][i])     continue;
        int na = tr[a][i], nb = tr[b][i];
        addtr(a, b, na, nb, i);
        if (leaf[na])       addtr(a, b, 0, nb, i);
        if (leaf[nb])       addtr(a, b, na, 0, i);
        if (leaf[na] && leaf[nb])       addtr(a, b, 0, 0, i);
    }

}

const int M = 998244353;

typedef vector<long long> row;
typedef vector<row> matrix;

matrix operator*(const matrix&a, const matrix &b) {
    int n = a.size();
    int p = b.size();
    int m = b[0].size();

    matrix ans(n, row(m));
    for (int i=0; i<n; i++)
        for (int j=0; j<m; j++)
            for (int k=0; k<p; k++) {
                ans[i][j] = (ans[i][j] + 1LL*a[i][k]*b[k][j]);
                if (ans[i][j] > 7e18 || k == p-1)   ans[i][j] %= M;
            }
    return ans;
}

matrix unit(int n) {
    matrix ans(n, row(n));
    for (int i=0; i<n; i++)
        ans[i][i] = 1;
    return ans;
}

matrix power(const matrix &a, long long p) {
    if (p == 1)     return a;
    matrix ans = power(a, p/2);
    ans = ans * ans;
    if (p%2)        ans = ans*a;
    return ans;
}

int uid[N];
bool vis[N];

void dfs(int u) {
    if (vis[u]) return;
    vis[u] = 1;
    for (int v: to[u])  dfs(v);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin>>n>>m;

    for (int i=0; i<n; i++) {
        string s;
        cin>>s;
        add(s);
    }

    memset(nid, -1, sizeof nid);
    int k = trid+1;

    go(0, 0);

    int uiid = 0;
    for (int i=0; i<iid; i++) {
        memset(vis, 0, sizeof vis);
        dfs(i);
        if (vis[0])     uid[i] = uiid++;
        else            uid[i] = -1;
    }

    int N = uiid;
    matrix tr(N, row(N));
    for (int i=0; i<iid; i++)
        for (int x: to[i])
            if (uid[i] != -1 && uid[x] != -1)
                tr[uid[i]][uid[x]]++;

    matrix ans = power(tr, m);
    cout<<ans[0][0]<<endl;
}
