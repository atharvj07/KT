#include <iostream>
#include <cstring>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;

struct pt {
   int c, x, y;
};

int c[4][4][4], N;
bool s[100];

int check(int card, int x, int y) {
	int i;

   for (i=0; i<N; i++) if (s[c[card][x][i]] == false) break;
	if (i == N) return x;

   for (i=0; i<N; i++) if (s[c[card][i][y]] == false) break;
	if (i == N) return N + y;

	if (x == y) {
	   for (i=0; i<N; i++) if (s[c[card][i][i]] == false) break;
		if (i == N) return 2*N;
	}

	if (N-1-x == y) {
		for (i=0; i<N; i++) if (s[c[card][N-1-i][i]] == false) break;
		if (i == N) return 2*N+1;
	}
	return -1;
}

int main() {

int C, i, j, k, S, tmp, cur, BESTS, D, tmpi, d[4];
bool num[100], flag;
vector<int> v;
vector<pt> pos[100];
pt tmppt;

srand(time(0));

cin >> C;
cin >> N;

do {

for (i=0; i<100; i++) pos[i].clear();
memset(num, false, sizeof(num)); v.clear();
for (k=0; k<C; k++) {
   for (i=0; i<N; i++) {
		for (j=0; j<N; j++) {
			cin >> c[k][i][j];
			tmppt.c = k; tmppt.x = i; tmppt.y = j;
			pos[c[k][i][j]].push_back(tmppt);
			if (num[c[k][i][j]] == false) {
				num[c[k][i][j]] = true;
				v.push_back(c[k][i][j]);
			}
		}
	}
}

BESTS = 101;
for (j=0; j<10000; j++) {

	S = D = 0; flag = true;
	memset(s, false, sizeof(s));
	memset(d, -1, sizeof(d));

	while (1) {
   	tmp = rand()%(v.size()-S);
	   cur = v[tmp]; s[cur] = true;
   	tmpi = v[v.size()-S-1];
		v[v.size()-S-1] = v[tmp];
		v[tmp] = tmpi;
		S++;

//		cout << "salio el " << cur; for (i=0; i<C; i++) cout << ' ' << d[i]; cout << endl;

		for (i=0; i<pos[cur].size(); i++) {
			if (d[pos[cur][i].c] == -1) {
				d[pos[cur][i].c] = check(pos[cur][i].c, pos[cur][i].x, pos[cur][i].y);
				if (d[pos[cur][i].c] != -1) {
					D++;
					if (D == 4) break;
					else if (pos[cur][i].c > 0 && d[pos[cur][i].c-1] == -1) {flag = false; break;}
				}
			}
		}
		if (i<pos[cur].size()) {
			if (flag == true) {
				memset(s, false, sizeof(s)); S = 0;
//				cout << "SALIERON ";
//				for (i=0; i<C; i++) cout << d[i] << ' ';
//				cout << " CON LOS NUMEROS ";
				for (i=0; i<C; i++) {
					for (k=0; k<N; k++) {
						if (d[i] < N) tmp = c[i][d[i]][k];
						else if (d[i] < 2*N) tmp = c[i][k][d[i]-N];
						else if (d[i] == 2*N) tmp = c[i][k][k];
						else tmp = c[i][N-1-k][k];
						if (s[tmp] == false) {
//							cout << tmp << ' ';
							s[tmp] = true;
							S++;
						}
					}
				}
//				cout << endl;
				if (BESTS > S) BESTS = S;
			}
			break;
		}
	}
//	cout << "sacamos " << S << " numeros y el resultado fue " << flag << endl << endl;

}
if (BESTS < 101) cout << BESTS << endl;
else cout << 0 << endl;

cin >> C;
cin >> N;

} while (N!=0 || C!=0);

return 0;
}