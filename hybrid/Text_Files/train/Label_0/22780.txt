
#include<bits/stdc++.h>
using namespace std;
using ll=long long;
#define                           pb                          push_back
#define                           fr(i,l,r)                   for(ll i=l;i<=r;i++)
#define                           rf(i,r,l)                   for(ll i=r;i>=l;i--)
#define                           done(i)                     cout<<"done = "<<i<<endl;
#define                           show(x,y)                   cout<<x<<" : ";for(auto z:y)cout<<z<<" ";cout<<endl;
#define                           fast                        ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define 						  all(x) 					  x.begin(),x.end()
#define 						  yes 	    				  cout<<"YES"<<endl
#define 						  no 	       				  cout<<"NO"<<endl
ll dp[5005][5005];
ll inf= 1e18;

void Test()
{

	int n;
	cin>>n;
	vector<ll>X,Y;
	X.pb(0);
	Y.pb(0);


	for(int i=1; i<=n; i++)
	{
		int x;
		cin>>x;
		if(x) X.pb(i);
		else Y.pb(i);
	}




	fr(i,1,n)
	fr(j,1,n)
	{
		dp[i][j]=inf;
		dp[i][0]=inf;

	}
	
	dp[0][0]=0;



	for(int i=1; i<X.size(); i++)
	{

		for(int j=1; j<Y.size(); j++)
		{

			ll cost= abs(X[i]-Y[j]) ;
			dp[i][j]= min(dp[i][j-1],dp[i-1][j-1]+ cost);    ;
		}
	}

	cout<<dp[X.size() - 1 ][Y.size() - 1]<<endl;









}


int main()
{

	int t=1;
	//cin>>t;

	while(t--)
		Test();

}


