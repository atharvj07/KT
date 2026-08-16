#include <iostream>
#include <string>
using namespace std;

#define STRMAXT 1000000
#define STRMAXP 10000

void KMP(const string T, const string P){
	int tcur = 0;
	int pcur = 2;
	int tablecur = 0;
	int plen = P.length();
	int tlen = T.length();
	int* Table = new int[plen + 1];
	Table[0] = -1;
	if (plen >= 2){
		Table[1] = 0;
		while (pcur <= plen){
			if (P[pcur - 1] == P[tablecur]){
				Table[pcur] = tablecur + 1;
				pcur = pcur + 1;
				tablecur = tablecur + 1;
			}
			else if (tablecur > 0){
				tablecur = Table[tablecur];
			}
			else{
				Table[pcur] = 0;
				pcur = pcur + 1;
			}
		}
	}
	pcur = 0;
	while (tcur + pcur < tlen){
		if (P[pcur] == T[tcur + pcur]){
			pcur++;
			if (pcur == plen){
				cout << tcur << endl;
				tcur = tcur + pcur - Table[pcur];
				if (pcur > 0){
					pcur = Table[pcur];
				}
			}
		}
		else{
			tcur = tcur + pcur - Table[pcur];
			if (pcur > 0){
				pcur = Table[pcur];
			}
		}
	}
	delete[] Table;
}

int main(){
	string T;
	string P;
	std::cin >> T >> P;
	KMP(T, P);

	return 0;
}
