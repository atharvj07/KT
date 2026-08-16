#include<iostream>
#include<deque>
using namespace std;
int k,dist[100000];
deque<int> q;
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin>>k;
	for(int i=0;i<k;i++)
	{
		dist[i]=1000000009;
	}
	dist[1]=1;
	q.push_back(1);
	while(q.size())
	{
		int x=q.front();
		q.pop_front();
		if(dist[(10*x)%k]>dist[x])
		{
			dist[(10*x)%k]=dist[x];
			q.push_front((10*x)%k);
		}
		if(dist[(x+1)%k]>dist[x]+1)
		{
			dist[(x+1)%k]=dist[x]+1;
			q.push_back((x+1)%k);
		 } 
	}
	cout<<dist[0];
	return 0;
}