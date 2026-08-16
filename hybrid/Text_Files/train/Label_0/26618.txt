#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <vector>
#include <cstring>
using namespace std;

int N, Q, A[100010], B[100010], C[100010], D[100010], E[100010], x[100010], y[100010], ANS[100010];
vector <int> T[100010], Y[100010];
priority_queue <pair <int, int> > q;

int main () {
	scanf ("%d", &N);
	for (int i = 1; i <= N; i++) scanf ("%d%d", &A[i], &B[i]);
	for (int i = 1; i <= N + 1; i++) scanf ("%d", &C[i]);
	scanf ("%d", &Q);
	for (int i = 1; i <= Q; i++) scanf ("%d%d", &D[i], &E[i]);
	
	sort (C + 1, C + N + 2);
	for (int i = 1; i <= N; i++)
		A[i] = lower_bound (C + 1, C + N + 2, A[i]) - C,
		B[i] = lower_bound (C + 1, C + N + 2, B[i]) - C;
	for (int i = 1; i <= Q; i++)
		D[i] = lower_bound (C + 1, C + N + 2, D[i]) - C,
		E[i] = lower_bound (C + 1, C + N + 2, E[i]) - C;
	
	for (int i = 1; i <= N + 1; i++) x[i] = -1;
	for (int i = 1; i <= N; i++) if (A[i] <= N + 1) x[A[i]]++;
	for (int i = 2; i <= N + 1; i++) x[i] += x[i - 1];
	
	for (int i = 1; i <= N; i++) if (B[i] < A[i]) T[A[i] - 1].push_back (B[i]);
	
	int Ans = N;
	for (int i = N + 1, w = 0; i >= 1; i--) {
		sort (T[i].begin (), T[i].end ());
		for (unsigned int p = 0; p < T[i].size (); p++) q.push (make_pair (-T[i][p], i));
		for (int j = x[i] + w; j < -1; j++) {
			if (q.empty ()) { while (Q--) printf ("-1\n"); return 0; }
			pair <int, int> p = q.top (); q.pop ();
			T[p.second].erase (T[p.second].begin ());
			y[-p.first]++, y[p.second + 1]--, Ans--, w++;
		}
		w -= y[i];
	}
	
	for (int i = 1; i <= N + 1; i++) y[i] += y[i - 1], x[i] += y[i];
	while (!q.empty ()) q.pop ();
	
	for (int i = N + 1; i >= 1; i--)
		for (unsigned int p = 0; p < T[i].size (); p++)
			Y[T[i][p]].push_back (i);
	
	memset (y, 0, sizeof (y));
	memset (ANS, -1, sizeof (ANS));
	for (int i = 1, w = 0; i <= N + 1; i++) {
		ANS[i] = Ans;
		for (unsigned int p = 0; p < Y[i].size (); p++) q.push (make_pair (Y[i][p], i));
		for (int j = x[i] + w; j < 0;j++) {
			if (q.empty ()) goto end;
			pair <int, int> p = q.top (); q.pop ();
			y[p.first]++, Ans--, w++;
		}
		w -= y[i];
	}
	ANS[N + 2] = Ans;
	end:;
	
	for (int i = 1; i <= Q; i++) {
		int p = ANS[D[i]], q = ANS[E[i]];
		if (p != -1) p++;
		printf ("%d\n", max (p, q));
	}
	
	return 0;
}