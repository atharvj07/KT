#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <utility>
#include <functional>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <climits>
#include <cassert>
using namespace std;
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long ll;
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
const double EPS = 1e-7;
const double PI  = acos(-1.0);

const double length=1;
struct swimmer{
	int tempo,cnt,cnt_max;
	int remain;
	bool operator<(const swimmer &other) const{
		return tempo<other.tempo;
	}
};
int main(){
	int n;
	while(cin>>n,n){
		vector<swimmer> left;
		vector<swimmer> right;
		REP(i,n){
			int t,c;
			cin>>t>>c;
			left.push_back(swimmer());
			left[i].tempo=t;
			left[i].cnt_max=c;
			left[i].remain=t;
		}
		sort(ALL(left));

		int turn;
		for(turn=1;;turn++){
			int left_prev_remain=0;
			REP(i,left.size()){
				double new_remain=left[i].remain-1;
				if(new_remain<left_prev_remain){
					left[i].remain=left_prev_remain;
				}else{
					left[i].remain=new_remain;
					left_prev_remain=new_remain;
				}
			}
			int right_prev_remain=0;
			REP(i,right.size()){
				double new_remain=right[i].remain-1;
				if(new_remain<right_prev_remain){
					right[i].remain=right_prev_remain;
				}else{
					right[i].remain=new_remain;
					right_prev_remain=new_remain;
				}
			}

			vector<swimmer> left_done_swimmers;
			REP(i,left.size()){
				if(left[i].remain==0){
					left_done_swimmers.push_back(left[i]);
				}
			}
			left.erase(left.begin(),left.begin()+left_done_swimmers.size());

			vector<swimmer> right_done_swimmers;
			int num_right_done_swimmers=0;
			REP(i,right.size()){
				if(right[i].remain==0){
					num_right_done_swimmers++;
					right[i].cnt++;
					if(right[i].cnt<right[i].cnt_max){
						right_done_swimmers.push_back(right[i]);
					}
				}
			}
			right.erase(right.begin(),right.begin()+num_right_done_swimmers);

			sort(ALL(left_done_swimmers));
			sort(ALL(right_done_swimmers));
			REP(i,left_done_swimmers.size()){
				left_done_swimmers[i].remain=left_done_swimmers[i].tempo;
			}
			REP(i,right_done_swimmers.size()){
				right_done_swimmers[i].remain=right_done_swimmers[i].tempo;
			}
			right.insert(right.end(),ALL(left_done_swimmers));
			left.insert(left.end(),ALL(right_done_swimmers));
			if(left.size()==0&&right.size()==0){
				break;
			}
		}
		cout<<turn<<endl;
	}
}