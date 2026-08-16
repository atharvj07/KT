#define _USE_MATH_DEFINES
#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<utility>
#include<algorithm>
#include<climits>
#include<set>
#include<map>
#include<cmath>
#include<iomanip>
#include<iterator>
#include<queue>
#include<stack>
#include<cctype>
#include<deque>
#include<time.h>
#include<bitset>
#include<random>
#include <functional>
#include<unordered_set>
#include<unordered_map>
#include<random>
#include<numeric>
#include <chrono>
#include<sstream>
#include <valarray> 
#include<list>
#include<complex>
#include<cassert>

//by Skeef79

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

#pragma warning(disable : 4996)
#pragma comment(linker, "/STACK:16777216")
#define pb push_back
#define en '\n'
#define forn(i,n) for(int i = 0;i<n;i++)
#define for0(i,n) for(int i = 0;i<n;i++)
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define vec vector
#define pii pair<int,int>
#define pll pair<ll,ll>
#define szof(x) int(x.size())
#define vi vector<int>
#define vll vector<ll>
#define vvi vector<vector<int>>
#define vvll vector<vector<ll>>

using namespace std;

const int INF = 1000000000 + 1e8;
const ll LINF = 2000000000000000000;

template<typename T> void print(vector<T>& a)
{
	for (int i = 0; i < a.size(); i++)
		cout << a[i] << ' ';
	cout << en;
}

template<typename T> void print(vector<vector<T>>& a)
{
	for (int i = 0; i < a.size(); i++)
	{
		for (int j = 0; j < a[i].size(); j++)
			cout << a[i][j] << ' ';
		cout << en;
	}
}

template <typename T> void input(vector<T>& a)
{
	for (int i = 0; i < a.size(); i++)
		cin >> a[i];
}

template<typename T> void input(vector<vector<T>>& a)
{
	for (int i = 0; i < a.size(); i++)
		for (int j = 0; j < a[i].size(); j++)
			cin >> a[i][j];
}

ll gcd(ll a, ll b, ll &x, ll &y)
{
	if (b == 0)
	{
		x = 1;
		y = 0;
		return a;
	}
	ll x1, y1;
	ll g = gcd(b, a%b, x1, y1);
	x = y1;
	y = x1 - (a / b) * y1;
	return g;
}

ll crt(ll a1, ll a2, ll n1, ll n2)
{
	ll x1, y1;
	ll d = gcd(n1, n2, x1, y1);
	if ((a1 - a2) % d != 0)
		return -1;

	ll k1 = (a2 - a1) / d * x1;
	ll t = a1 + n1 * (k1%n2);

	while (t < 0)
		t += n1 * n2 / d;

	if (t > (n1*n2) / d)
		t %= (n1*n2) / d;

	return t;
}

ll lccm;
vector<ll>pos1, pos2;
ll N = 0, n, m, k;

vector<ll>crts;

ll get(ll cnt)
{
	ll ans = cnt;
	for (int i = 0; i < N; i++)
	{
		if (pos1[i] == -1 || pos2[i] == -1)
			continue;
		else
		{
			ll fst = crts[i];
			if (fst != -1)
			{
				if (cnt - fst > 0)
				{
					ll t = cnt - fst;
					ans -= (t + lccm - 1) / lccm;
				}
			}
		}
	}
	return ans;
}

void solve()
{
	cin >> n >> m >> k;
	vector<ll>a(n), b(m);
	input(a);
	input(b);

	N = *max_element(all(a));
	N = max(N, *max_element(all(b)));
	N++;

	input(a);
	input(b);
	pos1.resize(N);
	pos2.resize(N);
	fill(all(pos1), -1);
	fill(all(pos2), -1);

	crts.resize(N);

	ll x, y;
	lccm = n * m / gcd(n, m, x, y);

	for (int i = 0; i < n; i++)
		pos1[a[i]] = i;
	for (int i = 0; i < m; i++)
		pos2[b[i]] = i;

	for (int i = 0; i < N; i++)
	{
		if (pos1[i] == -1 || pos2[i] == -1)
			continue;
		else
			crts[i] = crt(pos1[i], pos2[i], n, m);
	}
	
	ll l = 0, r = 1e18;
	while (r - l > 1)
	{
		ll m = (l + r) / 2;
		if (get(m) >= k)
			r = m;
		else
			l = m;
	}
	cout << l + 1;
}

int main()
{
	srand(time(0));
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

#ifdef _DEBUG	
	freopen("input.txt", "r", stdin);
#endif
	//freopen("out.txt", "w", stdout);

	//freopen("igoreha.in", "r", stdin);
	//freopen("igoreha.out", "w", stdout);

	int tst = 1;
	//cin >> tst;

	while (tst--)
		solve();
}