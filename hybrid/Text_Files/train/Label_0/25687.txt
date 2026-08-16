#include <bits/stdc++.h>

using namespace std;

#define reep(i,a,b) for(int i=(a);i<(b);i++)
#define rep(i,n) reep((i),0,(n))


template<class V> class MaxFlow_dinic{
public:
	struct edge{int to,reve;V cap;};
	static const int MV = 10100;
	vector<edge> E[MV];
	int itr[MV],lev[MV];

	void add_edge(int x,int y,V cap,bool undir=false){
		E[x].push_back((edge){y,(int)E[y].size(),cap});
		E[y].push_back((edge){x,(int)E[x].size()-1,undir?cap:0});
	}
	void bfs(int cur){
		memset(lev,0xff,sizeof(lev));
		queue<int> q;
		lev[cur] = 0;
		q.push(cur);
		while(q.size()){
			int v=q.front();
			q.pop();
			for(edge &e:E[v]){
				if(e.cap>0&&lev[e.to]<0){
					lev[e.to]=lev[v]+1,q.push(e.to);
				}
			}
		}
	}	

	V dfs(int from,int to,V cf){
		if(from==to) return cf;
		for(;itr[from]<E[from].size();itr[from]++){
			edge &e = E[from][itr[from]];
			if(e.cap>0&&lev[from]<lev[e.to]){
				V f=dfs(e.to,to,min(cf,e.cap));
				if(f>0){
					e.cap-=f;
					E[e.to][e.reve].cap+=f;
					return f;
				}
			}
		}
		return 0;
	}
	V maxflow(int from,int to){
		V fl = 0,tf;
		while(1){
			bfs(from);
			if(lev[to]<0) return fl;
			memset(itr,0,sizeof(itr));
			while((tf=dfs(from,to,numeric_limits<V>::max()))>0) fl+=tf;
		}
	}
};



int n,m;


int main(){
	while(cin>>n>>m,n||m){
		pair<int,int> ans;
		int l,r;
		l=0,r=m+1;
		vector<int> a(m),b(m);
		rep(i,m) cin>>a[i]>>b[i],a[i]--,b[i]--;
		while(r-l>1){
			int mid = (r+l)/2;
			// cout<<"a "<<mid<<endl;
			MaxFlow_dinic<int> mf;
			int source = n+m;
			int sink = n+m+1;
			rep(i,m){
				// int a,b;
				// cin>>a>>b;
				// a--,b--;
				mf.add_edge(i,m+a[i],1);
				mf.add_edge(i,m+b[i],1);
				mf.add_edge(source,i,1);
			}
			rep(i,n){
				mf.add_edge(m+i,sink,mid);
			}
			int t = mf.maxflow(source,sink);
			// cout<<"t "<<t<<endl;
			if(t==mid*n){
				l=mid;
			}
			else{
				r=mid;
			}
		}
		ans.first = l;
		l=0,r=m+1;
		while(r-l>1){
			int mid = (r+l)/2;
			MaxFlow_dinic<int> mf;
			int source = n+m;
			int sink = n+m+1;
			rep(i,m){
				mf.add_edge(i,m+a[i],1);
				mf.add_edge(i,m+b[i],1);
				mf.add_edge(source,i,1);
			}
			rep(i,n){
				mf.add_edge(m+i,sink,mid);
			}
			int t = mf.maxflow(source,sink);
			if(t==m){
				r=mid;
			}
			else{
				l=mid;
			}
		}
		ans.second = r;
		cout<<ans.first <<" "<< ans.second <<endl;
	}
}