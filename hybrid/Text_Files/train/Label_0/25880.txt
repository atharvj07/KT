#include<iostream>
#include<string>
#include<vector>
using namespace std;
#define REP(i,b,n) for(int i=b;i<n;i++)
#define rep(i,n)   REP(i,0,n)
#define ALL(C)     (C).begin(),(C).end()
#define pb         push_back
#define mp         make_pair

typedef pair<int,int> pii;

const int N=800;
const int Rs='z'+1;
const int SPACE='A'-1;
bool isequal[N][N];
bool leadSpace[N];
string table[21][N];
bool   isexist[21][N];

void get_input(int n,vector<pii> *rule,int &p){
  rep(i,n){
    string in;
    cin>>in;
    if (in.size()== 2){//SPACE
      leadSpace[in[0]]=true;
      rule[in[0]].pb(mp(SPACE,SPACE));
    }else{
      int me  = in[0];
      REP(j,2,(int)in.size()-1){
	//	cout <<"rule "<< me <<" " << (int)in[j] <<" " <<p << endl;
	rule[me].pb(mp(in[j],p));
	me=p;
	p++;
      }
      //      cout <<"rule "<< me <<" " << (int)in[in.size()-1] << " " << SPACE<<endl;
      rule[me].pb(mp(in[in.size()-1],SPACE));
    }
  }
}

void make_space(int p,vector<pii> *rule){
  rep(k,p){
    rep(i,p){
      rep(j,rule[i].size()){
	if (leadSpace[rule[i][j].first]&&leadSpace[rule[i][j].second]){
	  leadSpace[i]=true;
	}
      }
    }
  }
}

bool vis[N];
void make_equal(int from,int now,vector<pii>*rule){
  if (vis[now])return;
  vis[now]=true;
  if (now != SPACE && !((int)'a'<=now && now <=(int)'z'))isequal[from][now]=true;
  rep(i,rule[now].size()){
    if (leadSpace[rule[now][i].first]){
      make_equal(from,rule[now][i].second,rule);
    }
    if (leadSpace[rule[now][i].second]){
      make_equal(from,rule[now][i].first,rule);
    }
  }
}

string solve(int p,int len,vector<pii> *rule){
  rep(i,p){
    rep(j,21){
      table[j][i]=string(1,(char)'z'+1);
      isexist[j][i]=false;
    }
  }

  rep(i,p){
    if (leadSpace[i]){
      table[0][i]="";
      isexist[0][i]=true;
    }
  }

  REP(k,1,len+1){
    rep(i,p){
      rep(j,rule[i].size()){
	if ('a'<= rule[i][j].first && rule[i][j].first <='z'){
	  if (isexist[k-1][rule[i][j].second]){
	    isexist[k][i]=true;
	    table[k][i]=min(table[k][i],string(1,(char)rule[i][j].first)+table[k-1][rule[i][j].second]);
	  }
	}else {
	  rep(l,k+1){
	    if (isexist[l][rule[i][j].first] &&
		isexist[k-l][rule[i][j].second]){
	      isexist[k][i]=true;
	      table[k][i]=min(table[k][i],
			      table[l][rule[i][j].first]+table[k-l][rule[i][j].second]);
	    }
	  }
	}
      }
    }
    
    
    rep(i,p){
      rep(j,p){
	if (i != j && isequal[i][j]){
	  if (isexist[k][i] && isexist[k][j]){
	    table[k][i]=min(table[k][i],table[k][j]);
	  } else if (isexist[k][j] && !isexist[k][i]){
	    isexist[k][i]=true;
	    table[k][i]=table[k][j];
	  }
	}
      }
    }
  }
   
  if (isexist[len]['S'])return table[len]['S'];
  return "-";
}

int main(){
  int n,l;
  while(cin>>n>>l && n){
    rep(i,N){
      rep(j,N)isequal[i][j]=false;
      isequal[i][i]=true;
    }
    rep(i,N)leadSpace[i]=false;
    leadSpace[SPACE]=true;

    vector<pii> rule[N];
    int p = Rs;
    get_input(n,rule,p);

    make_space(p,rule);

    rep(i,p){
      rep(j,p)vis[j]=false;
      make_equal(i,i,rule);
    }

    cout << solve(p,l,rule) << endl;
  }
  return false;
}