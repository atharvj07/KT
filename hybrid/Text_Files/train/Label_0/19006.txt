#include <bits/stdc++.h>

using namespace std;

#define REP(i,n) for(ll (i) = (0);(i) < (n);++i)
#define REV(i,n) for(ll (i) = (n) - 1;(i) >= 0;--i)
#define PB push_back
#define EB emplace_back
#define MP make_pair
#define FI first
#define SE second
#define SHOW1d(v,n) {REP(WW,n)cerr << v[WW] << ' ';cerr << endl << endl;}
#define SHOW2d(v,WW,HH) {REP(W_,WW){REP(H_,HH)cerr << v[W_][H_] << ' ';cerr << endl;}cerr << endl;}
#define ALL(v) v.begin(),v.end()
#define Decimal fixed<<setprecision(20)
#define INF 1000000000
#define LLINF 1000000000000000000LL
#define MOD 1000000007

#define BIT_N 2002
typedef long long ll;
typedef pair<ll,ll> P;
typedef bitset<BIT_N> Bit;
vector<int> baseNum;

char ans[1001][1001];
ll n,m,ran;

void Gaussian_elimination(vector<Bit> &v){
	int v_size = v.size();
    REP(i, m) {
        int pla = -1;
        for(int j = ran;j < v_size;j++){
            if(v[j][i] == 1){
                pla = j;
                break;
            }
        }

        if(pla != -1){
            swap(v[ran], v[pla]);
            for(int j = 0;j < v_size;j++){
				if(j == ran)continue;
                if(v[j][i] == 1)v[j] ^= v[ran];
            }
            ran++;
        }
    }
}

void makeBaseNum(vector<Bit> v) {
    REP(i,n){
        REP(j,BIT_N){
            if(v[i][j] == 1){
                baseNum.EB(j);
                break;
            }
        }
    }
}

void check(int c, vector<Bit> v){

    vector<int> num = baseNum;
    bool ism = false;
    REP(i,n){
        if(v[i][c] == 1){
            v[i][m] = 1;
            if(num[i] == c){
                do{
                    num[i]++;
                }while(v[i][num[i]] != 1);
            }
        }
        if(num[i] == m)ism = true;
        v[i][c] = 0;
    }

    REP(i,n-1){
        if(num[i] > num[i+1]){
            swap(num[i], num[i+1]);
            swap(v[i], v[i+1]);
        }
    }

    REP(i,n){
        bool pla = false;
        bool mai = false;
        REP(j,n){
            auto tmp = v[j][m] ^ v[j][m + 1 + i];
            if(j >= ran && tmp){
                pla = true;
            }
            if(j == ran - 1 && num[ran - 1] == m && !tmp)mai = true;
        }
        if(ism && !pla && mai){
            ans[i][c] = '-';
        }
        else if(!ism && pla){
            ans[i][c] = '+';
        }
        else {
            ans[i][c] = '0';
        }
    }

}

int main(){
	cin.tie(0);cout.tie(0);ios::sync_with_stdio(false);

    vector<Bit> v;
    cin >> n >> m;
    REP(i,n){
        Bit tmp;
        REP(j,m){
            char c;cin >> c;
            if(c == '1')tmp[j] = 1;
        }
        v.EB(tmp);
    }

    REP(i,n){
        v[i][m + 1 + i] = 1;
    }

    Gaussian_elimination(v);
    makeBaseNum(v);

    REP(i,m){
        check(i, v);
    }

    REP(i,n){
        REP(j,m){
            cout << ans[i][j];
        }
        cout << "\n";
    }

    return 0;
}

