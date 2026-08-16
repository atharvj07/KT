#include <bits/stdc++.h>
using namespace std;

int p1,p2,a[300005],b[300005];
set<pair<int,int> > st;
vector<int> v1,v2;

int main()
{
	int h,w,m;
	cin>>h>>w>>m;
	
	while(m--)
	{
		int x,y;
		cin>>x>>y;
		st.insert(make_pair(x,y));
		a[x]++;
		b[y]++;
		
		if(a[x]>p1) v1.clear(),p1=a[x];
		if(a[x]==p1) v1.push_back(x);
		
		if(b[y]>p2) v2.clear(),p2=b[y];
		if(b[y]==p2) v2.push_back(y);
	}
	
	for(int i=0;i<v1.size();i++)
	 for(int j=0;j<v2.size();j++)
	  if(st.find(make_pair(v1[i],v2[j]))==st.end())
	  {
	  	cout<<p1+p2<<endl;
	  	return 0;
	  }
	
	cout<<p1+p2-1<<endl;
	return 0;
}