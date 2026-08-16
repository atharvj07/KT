#include<bits/stdc++.h>
using namespace std;
int n,a,d,t[1000003],maxa=-1;
int gcd(int x,int y)
{
    if(!y)
		return x;
    return gcd(y,x%y);
}
void fj(int x)
{
    for(int i=2;i*i<=x;)
	{
        if(!(x%i))
		{
            ++t[i];
            while(!(x%i))
				x/=i;
        }
        else
			++i;
    }
    if(x>1)
		++t[x];
}
int main()
{
    cin>>n>>a;
    d=a;
    for(int i=2;i<=n;i++)
	{
        cin>>a;
        if(maxa<a)
			maxa=a;
        d=gcd(d,a);
        fj(a);
    }
    if(d==1)
	{
        for(int i=2;i<=maxa;i++)
            if(t[i]>1)
			{
				cout<<"setwise coprime"<<endl;
				return 0;	
			}
        cout<<"pairwise coprime"<<endl;
    }
    else
		cout<<"not coprime"<<endl;
    return 0;
}