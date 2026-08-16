#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	cin.tie(0);
	ios::sync_with_stdio(false);

	int h,w;

	cin >> h >> w;

	map <int,int> s;
	multiset <int> vals;

	for(int i=0;i<w;i++)
	{
		s[i] = i;
	}
	for(int i=0;i<w;i++)
	{
		vals.insert(0);
	}

	for(int i=0;i<h;i++)
	{
		int l,r;
		cin >> l >> r;
		l-=1;
		auto it = s.lower_bound(l);
		int mr = -1;
		while(it!=s.end() && it->first <= r)
		{
			mr = max(mr,it->second);
			int x = it->first - it->second;
			vals.erase(vals.find(x));
			s.erase(it++);
		}
		if(mr!=-1 && r < w)
		{
			vals.insert(r-mr);
			s[r] = mr;
		}
		int ans = -1;
		if(vals.size() > 0)
		{
			ans = *vals.begin() + i + 1;
		}
		cout << ans << '\n';
	}
	return 0;	
}
