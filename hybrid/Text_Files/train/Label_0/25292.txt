#include<iostream>
using namespace std;
int a[100000];
int n, t;
int main()
{
	cin >> n >> t;
	for(int i = 0; i < n; i++)
		cin >> a[i];
	int minn = 2000000000;
	int maxn = 0;
	int cnt = 0;
	for(int i = 0; i < n; i++)
	{
		if(minn > a[i]) minn = a[i];
		else if(a[i] - minn > maxn) maxn = a[i] - minn, cnt = 1;
		else if(a[i] - minn == maxn) cnt++;
	}
	cout << cnt << endl;
	return 0;
}