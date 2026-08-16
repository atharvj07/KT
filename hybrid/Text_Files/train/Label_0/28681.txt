#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,k;
        long long a[110];
        long long int sum=0,s[110]={0};
        cin>>n>>k;
        for(int i=1;i<=n;i++)
        {
            scanf("%lld",&a[i]);
            s[i]=a[i]+s[i-1];
        }
        for(int i=2;i<=n;i++)
        {
            if(a[i]*100>s[i-1]*k)
            {
                long long int ans=a[i]*100/k;
                if(a[i]*100%k!=0)
                    ans++;
                sum=max(sum,ans-s[i-1]);
            }
        }
        cout<<sum<<endl;
    }
}

 	     			 				    	  	  			 		