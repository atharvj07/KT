#include <bits/stdc++.h>
using namespace std;

#define rep(i,x,y) for(int i=(x);i<(y);++i)
#define debug(x) #x << "=" << (x)

#ifdef DEBUG
#define _GLIBCXX_DEBUG
#define dump(x) std::cerr << debug(x) << " (L:" << __LINE__ << ")" << std::endl
#else
#define dump(x)
#endif

typedef long long int ll;
typedef pair<int,int> pii;
//template<typename T> using vec=std::vector<T>;

const int inf=1<<30;
const long long int infll=1LL<<58;
const double eps=1e-9;
const int dx[]={1,0,-1,0},dy[]={0,1,0,-1};

template <typename T> ostream &operator<<(ostream &os, const vector<T> &vec){
	os << "[";
	for (const auto &v : vec) {
		os << v << ",";
	}
	os << "]";
	return os;
}

string split(const string &str, const string &delim){
    string res;
    size_t current = 0, found, delimlen = delim.size();
    while((found = str.find(delim, current)) != string::npos){
        res+=string(str, current, found - current) + " " + delim + " ";
        current = found + delimlen;
    }
    res+=string(str, current, str.size() - current);
    return res;
}

int n,c;
typedef tuple<int,int,int> edge;
vector<edge> es;
vector<int> dist;

void bellmanford(){
    fill_n(dist.begin(),n,inf);
    dist[0]=0;

    for(int i=0; i<n; ++i){
        for(edge& e:es){
            int a=get<0>(e),b=get<1>(e),w=get<2>(e);
            if(dist[a]+w<dist[b]) dist[b]=dist[a]+w;
        }
    }
}

void add_edge(string& constraint){
    constraint=split(constraint,">=");
    constraint=split(constraint,"<=");
    constraint=split(constraint,"+");
    constraint=split(constraint,"-");

    int a,b,d;
    string tmp1,tmp2;
    stringstream ss(constraint);
    ss >> a >> tmp1 >> b >> tmp2 >> d;
    --a; --b;

    if(tmp1=="<=") es.push_back(make_tuple(b,a,0));
    else if(tmp1==">=") es.push_back(make_tuple(a,b,0));

    int w=-d;
    if(tmp2=="-"){
        w*=-1;
        swap(a,b);
    }
    if(tmp1=="<=") es.push_back(make_tuple(b,a,w));
    else if(tmp1==">=") es.push_back(make_tuple(a,b,w));
}

void solve(){
    cin >> n >> c;

    dist.resize(n);
    vector<string> unfixed;

    rep(i,0,c){
        string constraint;
        cin >> constraint;
        if(constraint.find("*")==string::npos) add_edge(constraint);
        else unfixed.push_back(constraint);
    }
    rep(v,1,n) es.push_back(make_tuple(v,0,0));

    vector<edge> es_=es;
    int ans=-1;
    rep(b,0,1<<unfixed.size()){
        es=es_;
        rep(i,0,unfixed.size()){
            string constraint=unfixed[i];
            if(1&(b>>i)) constraint.replace(constraint.find("*"),1,"<=");
            else constraint.replace(constraint.find("*"),1,">=");
            add_edge(constraint);
        }

        bellmanford();
        if(dist[0]<0) continue;
        rep(i,0,n) ans=max(ans,dist[i]);
    }
    if(ans==inf) cout << "inf" << endl;
    else cout << ans << endl;
}

int main(){
	std::ios::sync_with_stdio(false);
	std::cin.tie(0);
	solve();
	return 0;
}