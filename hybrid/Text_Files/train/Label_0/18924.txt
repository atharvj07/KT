#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <math.h>
#include <cstring>
#include <time.h>
#include <complex>
#include <algorithm>
#include <queue>
#include <unordered_map>
#include <set>
#include <bitset>

#pragma warning(disable:4996)
#define PII std::pair<long long, long long>
#define PTT std::pair<tree *, tree *>

template<typename T> T min(T x, T y)
{
	return x < y ? x : y;
}
template<typename T> T max(T x, T y)
{
	return x > y ? x : y;
};

const long long INF = 2000000005;// 0000;//autojs.org
const long long mod = 1000000007;// 998244353;//
const long long MAXN = 505;
const long long T = 37;
long long PT[MAXN];

struct TREE {
	int l;
	int r;
	long long h;
	TREE *lson;
	TREE *rson; 
	TREE(int L = 1, int R = MAXN)
	{
		l = L, r = R;
		h = 0;
		lson = rson = NULL;
	}
};
TREE pool[1000000];
int TOP;
long long newtree(int L = 1, int R = MAXN)
{
	pool[TOP] = TREE(L, R);
	return (long long)(pool + TOP++);
}
struct tree {
	int l;
	int r;
	long long h;
	tree *lson;
	tree *rson;
	tree(int L = 1, int R = MAXN)
	{
		l = L, r = R;
		h = 0;
		lson = rson = NULL;
	}

	void pushup()
	{
		int mid = (r + l) / 2;
		h = lson ? lson->h * PT[r - mid] % mod : 0;
		h += rson ? rson->h : 0;
		h %= mod;
	}
	tree *modify(int p, char ch)
	{
		tree *t = (tree *)newtree();
		*t = *this;
		if (t->l == t->r)
		{
			t->h = ch;
			return t;
		}
		int mid = (t->r + t->l) / 2;
		if (p <= mid)
			t->lson = lson ? lson->modify(p, ch) : tree(l, mid).modify(p, ch);
		else
			t->rson = rson ? rson->modify(p, ch) : tree(mid + 1, r).modify(p, ch);
		t->pushup();
		return t;
	}
	char get(int p)
	{
		if (l == r)
			return (char)h;
		int mid = (l + r) / 2;
		if (p <= mid)
			return lson->get(p);
		return rson->get(p);
	}
};
int cmp(tree *T1, tree *T2)
{
	if (!T1 || !T2)
		return T1 ? 1 : (T2 ? -1 : 0);
	if (T1->l == T1->r)
		return T1->h > T2->h ? -1 : T1->h < T2->h;
	if (!T1->lson || !T2->lson || T1->lson->h != T2->lson->h)
		return cmp(T1->lson, T2->lson);
	return cmp(T1->rson, T2->rson);
}
void recycle()
{
	TOP = 0;
}

int N, D;
char a[MAXN], nxt[MAXN];
tree *f[MAXN];

void solve()
{
	scanf("%d %d", &N, &D);
	scanf("%s", a + 1);
	for (int i = 1; i < D; i++)
		nxt['a' + i] = 'a' + i - 1;
	nxt['a'] = nxt['a' + D - 1] = 'a';

	recycle();
	memset(f, 0, sizeof(f));
	tree *t = NULL;

	f[0] = (tree *)newtree();
	f[1] = tree().modify(1, nxt[a[1]]);
	for (int i = 2; i <= N; i++)
	{
		f[i] = f[i - 1]->modify(i, nxt[a[i]]);
		t = f[i - 1]->modify(i - 1, a[i]), t = t->modify(i, f[i - 1]->get(i - 1));
		if (cmp(t, f[i]) == 1)
			f[i] = t;
		t = f[i - 2]->modify(i - 1, nxt[a[i]]), t = t->modify(i, a[i - 1]);
		if (cmp(t, f[i]) == 1)
			f[i] = t;
		if (i == 2) continue;
		t = f[i - 2]->modify(i - 2, a[i]), t = t->modify(i - 1, f[i - 2]->get(i - 2)),
			t = t->modify(i, a[i - 1]);
		if (cmp(t, f[i]) == 1)
			f[i] = t;
	}

	for (int i = 1; i <= N; i++)
		printf("%c", f[N]->get(i));
	printf("\n");
}

int main()
{
	PT[0] = 1;
	for (int i = 1; i < MAXN; i++)
		PT[i] = PT[i - 1] * T % mod;

	int t;
	scanf("%d", &t);
	while (t--)
		solve();

	return 0;
}