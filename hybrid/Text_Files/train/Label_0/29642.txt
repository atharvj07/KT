#include <bits/stdc++.h>

using namespace std;

#define REP(i, a, b) for (int i = (a), i##_end_ = (b); i < i##_end_; ++i)
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define SZ(x) (int((x).size()))
#define ALL(x) (x).begin(), (x).end()
#define EXIT(...) printf(__VA_ARGS__), exit(0)

template<typename T> inline bool chkmin(T &a, const T &b) { return b < a ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }

typedef long long LL;

const int oo = 0x3f3f3f3f;

const int maxn = 280000;

int n, L;
int a[maxn + 5];

int ans[maxn + 5];

int pos[maxn + 5];
bool vis[maxn + 5];

int bitrev[maxn + 5];

int pre[maxn + 5];

int get_pre(int x) { return pre[x] == x ? x : pre[x] = get_pre(pre[x]); }

void dfs(int x)
{
	if (vis[x]) return;
	vis[x] = 1;
	int tmp = n - 1;
	REP(i, 0, L) if (!(x >> i & 1))
	{
		dfs(x | (1 << i));
		chkmin(tmp, a[x | (1 << i)]);
	}
	if (!~a[x]) 
	{
		tmp = get_pre(tmp);
		if (tmp == n) EXIT("NO\n");
		a[x] = tmp;
		if (!tmp) pre[tmp] = n;
		else pre[tmp] = get_pre(tmp - 1);
	}
	else if (tmp < a[x]) EXIT("NO\n");
}

int main()
{
#ifdef matthew99
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	scanf("%d", &L), n = 1 << L;
	REP(i, 0, n) scanf("%d", a + i), --a[i], pos[i] = i;
	sort(pos, pos + n, [&](int x, int y) { return a[x] > a[y]; });
	REP(i, 0, n + 1) pre[i] = i;
	REP(i, 0, n) if (~a[i])
	{
		if (!a[i]) pre[a[i]] = n;
		else pre[a[i]] = get_pre(a[i] - 1);
	}
	memset(vis, 0, sizeof vis);
	REP(i, 0, n) if (!vis[pos[i]])
	{
		dfs(pos[i]);
	}
	REP(i, 0, n) bitrev[i] = bitrev[i >> 1] >> 1 | ((i & 1) << (L - 1));
	REP(i, 0, n) 
	{
		ans[bitrev[i]] = a[i];
	}
	REP(i, 0, n) debug("%d ", a[i]);
	debug("\n");
	puts("YES");
	REP(i, 0, n) printf("%d ", ans[i] + 1);
	printf("\n");
	return 0;
}
