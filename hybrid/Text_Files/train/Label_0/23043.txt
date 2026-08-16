#include<iostream>
#include<string>
#include<queue>
#include<functional>
#include<utility>
#include<climits>
using namespace std;

#define LMAX LLONG_MAX

int n, p1, p2, m, x[1000], y[1000];
string a[1000];
int num[600], d[600], s[600];

bool no = false;
int sNum, divMax, r[600], dif[600], dev;
queue<int> leaf[600];

int sNum2, exist[301];
pair<int, int> press[64];

long long dp[65][301], pow2[64], perm;
bool isLMAX = false, divineSet[64];

priority_queue<int, vector<int>, greater<int> > divine;

int t = 0;

void init(int N){
	for (int i = 0; i < N; i++) {
		num[i] = 1;
		d[i] = -1;
		s[i] = i;
		sNum = 0;
		divMax = 0;
		for (int i = 0; i < N; i++){
			while (!leaf[i].empty()){
				leaf[i].pop();
			}
		}
		sNum2 = 0;
		for (int i = 0; i < 301; i++)
			exist[i] = -1;
	}
}
void dpInit(int M, int N){
	for (int i = 0; i <= M; i++){
		for (int j = 0; j <= N; j++){
			dp[i][j] = -1;
		}
	}
	dp[0][0] = 0;
}
int root(int p){
	if (s[p] == p) return p;
	return (s[p] = root(s[p]));
}
void unit(int p, int q){
	s[root(q)] = root(p);
}
long long Power(int A){
	if (pow2[A] > 0)return pow2[A];
	else{
		return(pow2[A] = (Power(A / 2) * Power(A - A / 2)));
	}
}

int main(){
	pow2[0] = 1;
	pow2[1] = 2;
	while (true)
	{
		t++;
		cin >> n >> p1 >> p2;
		if (n + p1 + p2 == 0) break;
		for (int i = 0; i < n; i++){
			cin >> x[i] >> y[i] >> a[i];
			x[i]--;
			y[i]--;
		}
		if (p1 == p2){
			cout << "no" << endl;
		}
		else{
			m = p1 + p2;
			init(m);
			for (int i = 0; i < n; i++){
				if (a[i] == "yes"){
					if (root(x[i]) != root(y[i])){
						num[root(x[i])] += num[root(y[i])];
						if (d[root(x[i])] >= 0 && d[root(y[i])] >= 0){
							num[d[root(x[i])]] += num[d[root(y[i])]];
							unit(d[root(x[i])], d[root(y[i])]);
						}
						if (d[root(x[i])] < 0 && d[root(y[i])] >= 0){
							d[root(x[i])] = d[root(y[i])];
							d[d[root(y[i])]] = root(x[i]);
						}
						unit(x[i], y[i]);
					}
				}
				else {
					if (d[root(x[i])] != root(y[i])){//if (d[root(x[i]) != root(y[i])])
						if (d[root(x[i])] >= 0){
							num[root(y[i])] += num[d[root(x[i])]];
							s[d[root(x[i])]] = root(y[i]);
						}
						if (d[root(y[i])] >= 0){
							num[root(x[i])] += num[d[root(y[i])]];
							s[d[root(y[i])]] = root(x[i]);
						}
						d[root(x[i])] = root(y[i]);
						d[root(y[i])] = root(x[i]);
					}
				}
			}
			for (int i = 0; i < m; i++){
				leaf[root(i)].push(i);
				if (root(i) == i){
					if (d[i] >= 0){
						if (num[i] == num[d[i]]){
							no = true;
							break;
						}
						else if (num[i] > num[d[i]]){
							r[sNum] = i;
							dif[sNum] = num[i] - num[d[i]];
							divMax += num[i];
							sNum++;
						}
					}
					else {
						r[sNum] = i;
						dif[sNum] = num[i] - 0;
						divMax += num[i];
						sNum++;
					}
				}
			}
			dev = divMax - p1;
			if (no){
				cout << "no" << endl;
				no = false;
				continue;
			}
			else if (dev < 0){
				cout << "noooooo!" << endl;
				continue;
			}
			else if (dev == 0){
				for (int i = 0; i < sNum; i++){
					while (!leaf[r[i]].empty()){
						divine.push(leaf[r[i]].front());
						leaf[r[i]].pop();
					}
				}
				while (!divine.empty()){
					cout << (divine.top() + 1) << endl;
					divine.pop();
				}
				cout << "end" << endl;
				continue;
			}
			else if (divMax == p2){
				for (int i = 0; i < sNum; i++){
					if (d[r[i]] >= 0){
						while (!leaf[d[r[i]]].empty()){
							divine.push(leaf[d[r[i]]].front());
							leaf[d[r[i]]].pop();
						}
					}
				}
				while (!divine.empty()){
					cout << (divine.top() + 1) << endl;
					divine.pop();
				}
				cout << "end" << endl;
				continue;
			}
			for (int i = 0; i < sNum;i++){
				if (exist[dif[i]] < 0){
					press[sNum2].first = dif[i];
					press[sNum2].second = 1;
					exist[dif[i]] = sNum2;
					sNum2++;
				}
				else{
					press[exist[dif[i]]].second++;
				}
			}
			dpInit(sNum2, dev);
			for (int i = 1; i <= sNum2;i++){
				for (int j = 0; j <= dev;j++){
					dp[i][j] = dp[i - 1][j];
					if (dp[i][j] == LMAX) continue;
					for (int k = 1; k < press[i - 1].second;k++){
						if (j - press[i - 1].first * k < 0) break;
						if (dp[i - 1][j - press[i - 1].first * k] >= 0){
							dp[i][j] = LMAX;
							isLMAX = true;
							break;
						}
					}
					if (isLMAX){
						isLMAX = false;
						continue;
					}
					if (j - press[i - 1].first * press[i - 1].second >= 0){
						if (dp[i][j] >= 0 && dp[i - 1][j - press[i - 1].first * press[i - 1].second] >= 0) dp[i][j] = LMAX;
						else if (dp[i][j] < 0 && dp[i - 1][j - press[i - 1].first * press[i - 1].second] >= 0){
							if (dp[i - 1][j - press[i - 1].first * press[i - 1].second] != LMAX) dp[i][j] = dp[i - 1][j - press[i - 1].first * press[i - 1].second] + Power(i - 1);
							else dp[i][j] = LMAX;
						}
					}
				}
			}
			if (dp[sNum2][dev] < 0){
				cout << "noooooo!" << endl;
			}
			else if (dp[sNum2][dev] == LMAX){
				cout << "no" << endl;
			}
			else{
				perm = dp[sNum2][dev];
				for (int i = 0; i < sNum2; i++){
					divineSet[i] = (perm % 2 == 0);
					perm /= 2;
				}
				for (int i = 0; i < sNum; i++){
					if (divineSet[exist[dif[i]]]){
						while (!leaf[r[i]].empty()){
							divine.push(leaf[r[i]].front());
							leaf[r[i]].pop();
						}
					}
					else{
						if (d[r[i]] >= 0){
							while (!leaf[d[r[i]]].empty()){
								divine.push(leaf[d[r[i]]].front());
								leaf[d[r[i]]].pop();
							}
						}
					}
				}
				while (!divine.empty()){
					cout << (divine.top() + 1) << endl;
					divine.pop();
				}
				cout << "end" << endl;
			}
		}
	}
	return 0;
}