#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long int64;

const int ALPHABET_SIZE = 26;
const int MAX_Q = int(3e5 + 10);
const int MAX_L = int(1e5 + 10);
const int MAX_P = 10;
const int64 INF = int64(2e18 + 10);

int Q;
int64 A, B;
char S[MAX_P + 1];

struct Node {
	int64 size;
	char isChar;
	Node *alter;
	Node *childs[MAX_P + 1];
	Node():size(-1), isChar(0), alter(0)
	{
		memset(childs, 0, sizeof(childs));
	}
};

Node *nodes[ALPHABET_SIZE + 1];

void init() {
	scanf("%s ", S);
	scanf("%d%lld%lld ", &Q, &A, &B);
	--A;
	for (int i = 0; i <= ALPHABET_SIZE; ++i) {
		nodes[i] = new Node();
	}
	for (int i = 0; S[i]; ++i) {
		nodes[ALPHABET_SIZE]->childs[i] = nodes[int(S[i] - 'a')];
	}
}

inline void normalize(int64 &x) {
	if (x > INF) {
		x = INF;
	}
}

void proc() {
	char ch, pat[MAX_P + 1];
	scanf(" %c %s ", &ch, pat);
	Node *old = nodes[int(ch - 'a')];
	nodes[int(ch - 'a')] = new Node();
	if (pat[0] == '.') {
		old->size = 0;
		old->alter = old;
	}
	else {
		for (int i = 0; pat[i]; ++i) {
			old->childs[i] = nodes[int(pat[i] - 'a')];
		}
	}
}

struct State {
	Node *node;
	int index;
	int64 from, to;

	State(){}
	State(Node *node_, int index_, int64 from_ = -1, int64 to_ = -1):
		node(node_), index(index_), from(from_), to(to_)
	{}
};

void traverse(Node *nd) {
	static State stack[MAX_Q + 10];
	int st = 0;
	stack[st++] = State(nd, 0);
	for (;st>0;) {
		State s = stack[--st];
		nd = s.node;
		int idx = s.index;
		if (idx == 0) {
			nd->size = 0;
			nd->alter = nd;
			if (nd->isChar) {
				nd->size = 1;
				continue;
			}
		}

		for (;nd->childs[idx]; ++idx) {
			if (nd->childs[idx]->size == -1) {
				stack[st++] = State(nd, idx+1);
				stack[st++] = State(nd->childs[idx], 0);
				break;
			}
		}
		if (!nd->childs[idx]) {
			for (int i = 0; nd->childs[i]; ++i) {
				normalize(nd->size += nd->childs[i]->size);
			}
			if (nd->size == 0) {
				continue;
			}
			int p = 0;
			for (int i = 0; nd->childs[i]; ++i) if (nd->childs[i]->size > 0) {
				nd->childs[p] = nd->childs[i]->alter;
				++p;
			}
			nd->childs[p] = 0;
			if (nd->size == nd->childs[0]->size) {
				nd->alter = nd->childs[0];
			}
		}
	}
}

void print(Node *nd, int64 from, int64 to) {
	static State stack[MAX_Q + 10];
	int st = 0;
	stack[st++] = State(nd, 0, from, to);
	for (;st>0;) {
		State s = stack[--st];
		nd = s.node;
		int idx = s.index;
		from = s.from;
		to = s.to;

		const int64 len = to - from;
		if (len <= 0) {
			continue;
		}
		if (nd->isChar) {
			putchar(nd->isChar);
			continue;
		}

		for (; nd->childs[idx] && from < to; ++idx) {
			int64 sz = nd->childs[idx]->size;
			if (sz <= from) {
				from -= sz;
				to -= sz;
			}
			else {
				stack[st++] = State(nd, idx+1, 0, to - sz);
				stack[st++] = State(nd->childs[idx], 0, from, min(sz, to));
				break;
			}
		}
	}
}

void solve() {
	for (int _ = 0; _ < Q; ++_) {
		proc();
	}
	for (int i = 0; i < ALPHABET_SIZE; ++i) {
		nodes[i]->isChar = i + 'a';
	}
	traverse(nodes[ALPHABET_SIZE]);
	if (nodes[ALPHABET_SIZE]->size < B) {
		puts(".");
	}
	else {
		print(nodes[ALPHABET_SIZE], A, B);
		puts("");
	}
}

int main() {
	init();
	solve();
	return 0;
}