#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long ll;
ll mod = 1000000007;
ll get(ll lx, ll ly, ll ux, ll uy, ll a, ll b)
{
	vector<ll>x, y;
	x.push_back(lx), x.push_back(ux + 1), x.push_back(0), x.push_back(a);
	y.push_back(ly), y.push_back(uy + 1), y.push_back(0), y.push_back(b);
	sort(x.begin(), x.end());
	sort(y.begin(), y.end());
	ll r = 0;
	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < 3; j++)
		{
			if (0 <= x[i] && x[i] < a && 0 <= y[j] && y[j] < b)continue;
			if (lx <= x[i] && x[i] <= ux&&ly <= y[j] && y[j] <= uy)r += (x[i + 1] - x[i])*(y[j + 1] - y[j]);
		}
	}
	//printf("%lld %lld %lld %lld   %lld %lld   %lld\n", lx, ly, ux, uy, a, b, r);
	return r % mod;
}
ll calc(ll a, ll b, ll c, ll d)
{
	if (c == 1)return 0LL;
	//printf("-----%lld %lld %lld %lld\n", a, b, c, d);
	vector<ll>v;
	for (ll i = 0; i <= d + 1; i++)for (int j = -1; j <= 2;j++)v.push_back(c*i / a + j + d);
	for (ll i = 0; i <= d + 1; i++)for (int j = -1; j <= 2;j++)v.push_back(c*i / b + j + d);
	for (ll i = 0; i <= d + 1; i++)for (int j = -1; j <= 2;j++)v.push_back(c*(a - i) / a + j + d);
	for (ll i = 0; i <= d + 1; i++)for (int j = -1; j <= 2;j++)v.push_back(c*(b - i) / b + j + d);
	v.push_back(c);
	v.push_back(c + d);
	for (int i = 0; i < v.size(); i++)v[i] = max(d + 1, min(c + d, v[i]));
	sort(v.begin(), v.end());
	ll r = 0;
	for (int i = 0; i < v.size() - 1; i++)
	{
		ll x = (v[i] - d)*a / c;
		ll y = (v[i] - d)*b / c;
		//printf("%lld %lld %lld\n", v[i], x, y);
		ll t = 0;
		if (0 <= v[i] && v[i] < c)t = get(x - d, y - d, x + d, y + d, a, b) % mod;
		else t = (2 * d + 1)*(2 * d + 1);
		//printf("%lld  %lld %lld\n", v[i], v[i + 1] - v[i], t);
		r += t*(v[i + 1] - v[i]);
		r %= mod;
	}
	return r;
}
int main()
{
	ll a, b, c, d;
	scanf("%lld%lld%lld%lld", &a, &b, &c, &d);
	ll ans = (2 * d + 1)*(2 * d + 1)*(2 * d + 1);
	ans = (ans + (a - 1 + b - 1 + c - 1)*(2 * d + 1) % mod*(2 * d + 1)) % mod;
	//printf("%lld\n", ans);
	ll s = calc(a, b, c, d) + calc(b, c, a, d) + calc(c, a, b, d);
	for (ll i = -d; i <= d; i++)
	{
		if (0 <= i&&i < c)s += get(-d, -d, d, d, a, b);
		else s += (2 * d + 1)*(2 * d + 1);
	}
	s %= mod;
	printf("%lld\n", (ans + mod - s) % mod);
}