#include<bits/stdc++.h>
#define ull unsigned long long int
#define ll long long
#define vi vector<int>
#define vll vector<ll>
#define pb push_back

using namespace std;

ll arr[100009];
void fun()
{
	ll n; cin>>n;
	arr[0]=INT_MAX;
	arr[n+1]=INT_MAX;
	
	ll low=1;
	ll high=n;
	
	while (low<high)
	{
		
		ll mid=(low+high)/2;
		cout<<"? "<<mid<<endl;
		cout.flush();
		ll tt;
		cin>>tt;
		
		cout<<"? "<<mid+1<<endl;
		cout.flush();
		ll tt1;
		cin>>tt1;
		
		if (tt1>tt)
		{
			high=mid;
			continue;
		}
		else
		{
			low=mid+1;
		}
	}
	
	cout<<"! "<<low<<endl;
}

int main()
{
	int t=1;
//	cin>>t;
	while (t--)
	{
	 fun();
	}
 return 0;
}

