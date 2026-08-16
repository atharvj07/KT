#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<list>
#include<string>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<cmath>
using namespace std;

const int MAX = 500001;
const int NIL = -1;
struct Node {
	int key, priority;
	Node* parent, * left, * right;
};
struct Node T[MAX];
Node* head = NULL;
Node* _deleteNode(Node* t, int key);

Node* rightRotate(Node* t)
{
	Node* s = t->left;
	t->left = s->right;
	s->right = t;
	return s;
}

Node* leftRotate(Node* t)
{
	Node* s = t->right;
	t->right = s->left;
	s->left = t;
	return s;
}

Node* getMinimun(Node* x)
{
	while (x->left != NULL)
		x = x->left;
	return x;
}

Node* Find(Node* x, int k)
{
	while (x != NULL && k != x->key) {
		if (k < x->key)
			x = x->left;
		else
			x = x->right;
	}
	return x;
}

Node* getSuccessor(Node* x)
{
	if (x->right != NULL)
		return getMinimun(x->right);
	Node* y = x->parent;
	while (y != NULL && x == y->right) {
		x = y;
		y = y->parent;
	}
	return y;
}

void preParse(Node* u)
{
	if (u == NULL)
		return;
	cout << " " << u->key;
	preParse(u->left);
	preParse(u->right);
}

void inParse(Node* u)
{
	if (u == NULL)
		return;
	inParse(u->left);
	cout << " " << u->key;
	inParse(u->right);
}

Node* insert(Node* t, int key, int priority)
{
	Node* z = new(Node);
	z->key = key;
	z->priority = priority;
	z->left = z->parent = z->right = NULL;
	if (t == NULL) {
		return z;
	}
	if (key == t->key)
		return t;
	else if (key < t->key) {
		t->left = insert(t->left, key, priority);
		if (t->priority < t->left->priority)
			t = rightRotate(t);
	}
	else {
		t->right = insert(t->right, key, priority);
		if (t->priority < t->right->priority)
			t = leftRotate(t);
	}
	return t;
}

Node* deleteNode(Node* t, int key)
{
	if (t == NULL)
		return NULL;
	if (key < t->key)
		t->left = deleteNode(t->left, key);
	else if (key > t->key)
		t->right = deleteNode(t->right, key);
	else
		return _deleteNode(t, key);
	return t;
}

int main(void)
{
	int n, key, priority;
	char ss[10];
	cin >> n;
	memset(ss, 0, sizeof(ss));
	for (int i = 0; i < n; i++) {
		scanf("%s", ss);
		if (ss[0] == 'i') {
			cin >> key >> priority;
			head = insert(head, key, priority);
		}
		else if (ss[0] == 'f') {
			cin >> key;
			if (Find(head, key))
				cout << "yes" << endl;
			else
				cout << "no" << endl;
		}
		else if (ss[0] == 'd') {
			cin >> key;
			head = deleteNode(head, key);
		}
		else {
			inParse(head);
			cout << endl;
			preParse(head);
			cout << endl;
		}
	}
	return 0;
}

Node* _deleteNode(Node* t, int key)
{
	if (t->left == NULL && t->right == NULL)
		return NULL;
	else if (t->left == NULL)
		t = leftRotate(t);
	else if (t->right == NULL)
		t = rightRotate(t);
	else {
		if (t->left->priority > t->right->priority)
			t = rightRotate(t);
		else
			t = leftRotate(t);
		return deleteNode(t, key);
	}
	return deleteNode(t, key);
}


