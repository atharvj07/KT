import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.NoSuchElementException;
import java.util.Objects;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Random;
import java.util.Scanner;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.function.BiFunction;

public class Main{
	static Scanner scn = new Scanner(System.in);
	static FastScanner sc = new FastScanner();
	static Mathplus mp = new Mathplus();
	static PrintWriter ot = new PrintWriter(System.out);
	static Random rand = new Random();
	static int mod = 1000000007;
	static long inf = (long)1e17;
	public static void main(String[] args) {
		
		int N = sc.nextInt();
		int T = sc.nextInt();
		int[] d = new int[N];
		for(int i=0;i<N;i++) {
			d[i] = sc.nextInt();
		}
		Arrays.sort(d);
		long ans = 1;
		for(int i=0;i<N;i++) {
			ans *= i-mp.isBigger(d,d[i]-T-1)+1;
			ans %= mod;
		}
		System.out.println(ans);
	}
	
}



class SizeComparator implements Comparator<Edge>{
	int[] size;
	SizeComparator(int[] s) {
		size = s;
	}

	public int compare(Edge o1, Edge o2) {
		return size[o1.to]-size[o2.to];

	}

}

class ConvexHullTrick {
	long[] A, B;
	int len;

	public ConvexHullTrick(int n) {
		A = new long[n];
		B = new long[n];
	}

	private boolean check(long a, long b) {
		return (B[len - 2] - B[len - 1]) * (a - A[len - 1]) >= (B[len - 1] - b) * (A[len - 1] - A[len - 2]);
	}

	public void add(long a, long b) {
		while (len >= 2 && check(a, b)) {
			len--;
		}
		A[len] = a;
		B[len] = b;
		len++;
	}

	public long query(long x) {
		int l = -1, r = len - 1;
		while (r - l > 1) {
			int mid = (r + l) / 2;
			if (get(mid,x)>=get(mid+1,x)) {
				l = mid;
			} else {
				r = mid;
			}
		}
		return get(r,x);
	}

	private long get(int k, long x) {
		return A[k] * x + B[k];
	}
}

class Range{
	int l;
	int r;
	int length;
	Range(int L,int R){
		l = L;
		r = R;
		length = R-L+1;
	}

	boolean isIn(int x) {
		return (l<=x&&x<=r);

	}
}
class LeftComparator implements Comparator<Range>{
	public int compare(Range P, Range Q) {
		return P.l-Q.l;
	}
}
class RightComparator implements Comparator<Range>{
	public int compare(Range P, Range Q) {
		return P.r-Q.r;
	}
}
class LengthComparator implements Comparator<Range>{
	public int compare(Range P, Range Q) {
		return P.length-Q.length;
	}
}
class SegmentTree<T,E>{
	int N;
	BiFunction<T,T,T> f;
	BiFunction<T,E,T> g;
	T d1;
	ArrayList<T> dat;
	SegmentTree(BiFunction<T,T,T> F,BiFunction<T,E,T> G,T D1,T[] v){
		int n = v.length;
		f = F;
		g = G;
		d1 = D1;
		init(n);
		build(v);
	}


	void init(int n) {
		N = 1;
		while(N<n)N*=2;
		dat = new ArrayList<T>();
	}

	void build(T[] v) {
		for(int i=0;i<2*N;i++) {
			dat.add(d1);
		}
		for(int i=0;i<v.length;i++) {
			dat.set(N+i-1,v[i]);
		}
		for(int i=N-2;i>=0;i--) {
			dat.set(i,f.apply(dat.get(i*2+1),dat.get(i*2+2)));
		}
	}

	void update(int k,E a) {
		k += N-1;
		dat.set(k,g.apply(dat.get(k),a));
		while(k>0){
			k = (k-1)/2;
			dat.set(k,f.apply(dat.get(k*2+1),dat.get(k*2+2)));
		}
	}

	T query(int a,int b, int k, int l ,int r) {
		if(r<=a||b<=l) return d1;
		if(a<=l&&r<=b) return dat.get(k);
		T vl = query(a,b,k*2+1,l,(l+r)/2);
		T vr = query(a,b,k*2+2,(l+r)/2,r);
		return f.apply(vl, vr);
	}
	T query(int a,int b){
		return query(a,b,0,0,N);
	}

}

class LazySegmentTree<T,E> extends SegmentTree<T,E>{
	BiFunction<E,E,E> h;
	BiFunction<E,Integer,E> p = (E a,Integer b) ->{return a;};
	E d0;
	ArrayList<E> laz;
	LazySegmentTree(BiFunction<T,T,T> F,BiFunction<T,E,T> G,BiFunction<E,E,E> H,T D1,E D0,T[] v){
		super(F,G,D1,v);
		int n = v.length;
		h = H;
		d0 = D0;
		Init(n);
	}
	void build() {

	}
	void Init(int n){
		laz = new ArrayList<E>();
		for(int i=0;i<2*N;i++) {
			laz.add(d0);
		}
	}

	void eval(int len,int k) {
		if(laz.get(k).equals(d0)) return;
		if(k*2+1<N*2-1) {
			laz.set(k*2+1,h.apply(laz.get(k*2+1),laz.get(k)));
			laz.set(k*2+2,h.apply(laz.get(k*2+2),laz.get(k)));
		}
		dat.set(k,g.apply(dat.get(k), p.apply(laz.get(k), len)));
		laz.set(k,d0);
	}

	T update(int a,int b,E x,int k,int l,int r) {
		eval(r-l,k);
		if(r<=a||b<=l) {
			return dat.get(k);
		}
		if(a<=l&&r<=b) {
			laz.set(k,h.apply(laz.get(k),x));
			return g.apply(dat.get(k),p.apply(laz.get(k),r-l));
		}
		T vl = update(a,b,x,k*2+1,l,(l+r)/2);
		T vr = update(a,b,x,k*2+2,(l+r)/2,r);
		dat.set(k,f.apply(vl,vr));
		return dat.get(k);

	}

	T update(int a,int b,E x) {
		return update(a,b,x,0,0,N);
	}

	T query(int a,int b,int k,int l,int r) {
		eval(r-l,k);
		if(r<=a||b<=l) return d1;
		if(a<=l&&r<=b) return dat.get(k);

		T vl = query(a,b,k*2+1,l,(l+r)/2);
		T vr = query(a,b,k*2+2,(l+r)/2,r);
		return f.apply(vl, vr);
	}

	T query(int a,int b){
		return query(a,b,0,0,N);
	}

}
class AddSumLazySegmentTree {
	int N;
	long[] dat;
	long[] laz;
	AddSumLazySegmentTree(long[] v){
		init(v.length);

		for(int i=0;i<v.length;i++) {
			dat[N+i-1]=v[i];
		}
		for(int i=N-2;i>=0;i--) {
			dat[i]=dat[i*2+1]+dat[i*2+2];
		}
	}

	void init(int n) {
		N = 1;
		while(N<n)N*=2;
		dat = new long[2*N];
		laz = new long[2*N];
	}


	void eval(int len,int k) {
		if(laz[k]==0) return;
		if(k*2+1<N*2-1) {
			laz[k*2+1] += laz[k];
			laz[k*2+2] += laz[k];
		}
		dat[k] += laz[k] * len;
		laz[k] = 0;
	}

	long update(int a,int b,long x,int k,int l,int r) {
		eval(r-l,k);
		if(r<=a||b<=l) {
			return dat[k];
		}
		if(a<=l&&r<=b) {
			laz[k] += x;
			return dat[k]+laz[k]*(r-l);
		}
		long vl = update(a,b,x,k*2+1,l,(l+r)/2);
		long vr = update(a,b,x,k*2+2,(l+r)/2,r);
		return dat[k] = vl+vr;


	}

	long update(int a,int b,long x) {
		return update(a,b,x,0,0,N);
	}

	long query(int a,int b,int k,int l,int r) {
		eval(r-l,k);
		if(r<=a||b<=l) return 0;
		if(a<=l&&r<=b) return dat[k];

		long vl = query(a,b,k*2+1,l,(l+r)/2);
		long vr = query(a,b,k*2+2,(l+r)/2,r);
		return vl+vr;
	}

	long query(int a,int b){
		return query(a,b,0,0,N);
	}

}

class BinaryIndexedTree{
	int[] val;
	BinaryIndexedTree(int N){
		val = new int[N+1];
	}
	long sum(int i) {
		if(i==0)return 0;
		long s = 0;
		while(i>0) {
			s += val[i];
			i -= i & (-i);
		}
		return s;
	}
	void add(int x,int i) {
		if(i==0)return;
		while(i<val.length){
			val[i] += x;
			i += i & (-i);
		}
	}
}

class UnionFindTree {
	int[] root;
	int[] rank;
	int[] size;
	UnionFindTree(int N){
		root = new int[N];
		rank = new int[N];
		size = new int[N];
		for(int i=0;i<N;i++){
			root[i] = i;
			size[i] = 1;
		}
	}

	public int find(int x){
		if(root[x]==x){
			return x;
		}else{
			return find(root[x]);
		}
	}

	public void unite(int x,int y){
		x = find(x);
		y = find(y);
		if(x==y){
			return;
		}else{
			if(rank[x]<rank[y]){
				root[x] = y;
				size[y] += size[x];
			}else{
				root[y] = x;
				size[x] += size[y];
				if(rank[x]==rank[y]){
					rank[x]++;
				}
			}
		}
	}

	public boolean same(int x,int y){
		return find(x)==find(y);
	}

}

class ParticalEternalLastingUnionFindTree extends UnionFindTree{
	int[] time;
	int now;
	ParticalEternalLastingUnionFindTree(int N){
		super(N);
		time = new int[N];
		for(int i=0;i<N;i++) {
			time[i] = 1000000007;
		}
	}

	public int find(int t,int i) {
		if(time[i]>t) {
			return i;
		}else {
			return find(t,root[i]);
		}
	}

	public void unite(int x,int y,int t) {
		now = t;
		x = find(t,x);
		y = find(t,y);
		if(x==y)return;
		if(rank[x]<rank[y]){
			root[x] = y;
			size[y] += size[x];
			time[x] = t;
		}else{
			root[y] = x;
			size[x] += size[y];
			if(rank[x]==rank[y]){
				rank[x]++;
			}
			time[y] = t;
		}
	}

	public int sametime(int x,int y) {
		if(find(now,x)!=find(now,y)) return -1;
		int ok = now;
		int ng = 0;
		while(ok-ng>1) {
			int mid = (ok+ng)/2;
			if(find(mid,x)==find(mid,y)) {
				ok = mid;
			}else {
				ng = mid;
			}
		}
		return ok;
	}


}
class Graph {
	ArrayList<Edge>[] list;
	int size;
	TreeSet<LinkEdge> Edges = new TreeSet<LinkEdge>(new LinkEdgeComparator());

	@SuppressWarnings("unchecked")
	Graph(int N){
		size = N;
		list = new ArrayList[N];
		for(int i=0;i<N;i++){
			list[i] = new ArrayList<Edge>();
		}
	}

	void addEdge(int a,int b){
		list[a].add(new Edge(b,1));
	}

	void addWeightedEdge(int a,int b,long c){
		list[a].add(new Edge(b,c));
	}

	void addEgdes(int[] a,int[] b){

		for(int i=0;i<a.length;i++){
			list[a[i]].add(new Edge(b[i],1));
		}
	}

	void addWeighterEdges(int[] a ,int[] b ,int[] c){
		for(int i=0;i<a.length;i++){
			list[a[i]].add(new Edge(b[i],c[i]));
		}
	}

	long[] bfs(int s){
		long[] L = new long[size];
		for(int i=0;i<size;i++){
			L[i] = -1;
		}
		L[s] = 0;
		ArrayDeque<Integer> Q = new ArrayDeque<Integer>();
		Q.add(s);

		while(!Q.isEmpty()){
			int v = Q.poll();
			for(Edge e:list[v]){
				int w = e.to;
				long c = e.cost;
				if(L[w]==-1){
					L[w] = L[v] + c;
					Q.add(w);
				}
			}
		}
		return L;
	}
	long[] bfs2(int[] d,int s){
		long[] L = new long[size];
		for(int i=0;i<size;i++){
			L[i] = -1;
		}
		int p = 0;
		L[s] = 0;
		d[s] = p;
		p++;
		ArrayDeque<Integer> Q = new ArrayDeque<Integer>();
		Q.add(s);

		while(!Q.isEmpty()){
			int v = Q.poll();
			for(Edge e:list[v]){
				int w = e.to;
				long c = e.cost;
				if(L[w]==-1){
					d[w] = p;
					p++;
					L[w] = L[v] + c;
					Q.add(w);
				}
			}
		}
		return L;
	}

	int[] isTwoColor(){
		int[] L = new int[size];
		for(int i=0;i<size;i++){
			L[i] = -1;
		}
		L[0] = 0;
		ArrayDeque<Integer> Q = new ArrayDeque<Integer>();
		Q.add(0);

		while(!Q.isEmpty()){
			int v = Q.poll();
			for(Edge e:list[v]){
				int w = e.to;
				if(L[w]==-1){
					L[w] = 1-L[v];
					Q.add(w);
				}else{
					if(L[v]+L[w]!=1){
						L[0] = -2;
					}
				}
			}
		}
		return L;
	}

	long[] dijkstra(int s){
		long[] L = new long[size];
		for(int i=0;i<size;i++){
			L[i] = -1;
		}
		int[] v = new int[size];
		L[s] = 0;
		PriorityQueue<Pair> Q = new PriorityQueue<Pair>(new SampleComparator());
		Q.add(new Pair(0,s));

		while(!Q.isEmpty()){

			Pair C = Q.poll();
			if(v[(int)C.b]==0){
				L[(int)C.b] = C.a;
				v[(int) C.b] = 1;
				for(Edge D:list[(int) C.b])Q.add(new Pair(L[(int)C.b]+D.cost,D.to));	
			}
		}
		return L;
	}

	ArrayList<Graph> makeapart(){
		ArrayList<Graph> ans = new ArrayList<Graph>();
		boolean[] b = new boolean[size];
		int[] num = new int[size];
		for(int i=0;i<size;i++){
			if(b[i])continue;
			int sz = 0;
			ArrayList<Integer> l = new ArrayList<Integer>();
			ArrayDeque<Integer> Q = new ArrayDeque<Integer>();
			Q.add(i);
			b[i] = true;
			while(!Q.isEmpty()){
				int v = Q.poll();
				num[v] = sz;
				sz++;
				l.add(v);
				for(Edge e:list[v]){
					if(!b[e.to]){
						Q.add(e.to);
						b[e.to] = true;
					}
				}
			}
			Graph H = new Graph(sz);
			for(int e:l){
				for(Edge E:list[e]){
					H.addWeightedEdge(num[e],num[E.to],E.cost);
				}
			}
			ans.add(H);

		}
		return ans;
	}

	long[] bellmanFord(int s) {
		long inf = 1000000000;
		inf *= inf;
		long[] d = new long[size];
		boolean[] n = new boolean[size];
		d[s] = 0;
		for(int i=1;i<size;i++){
			d[i] = inf;
			d[i] *= d[i];
		}
		for(int i=0;i<size-1;i++){
			for(int j=0;j<size;j++){
				for(Edge E:list[j]){
					if(d[j]!=inf&&d[E.to]>d[j]+E.cost){
						d[E.to]=d[j]+E.cost;
					}
				}
			}
		}
		for(int i=0;i<size;i++){
			for(int j=0;j<size;j++){
				for(Edge e:list[j]){
					if(d[j]==inf) continue;
					if(d[e.to]>d[j]+e.cost) {
						d[e.to]=d[j]+e.cost;
						n[e.to] = true;
					}
					if(n[j])n[e.to] = true;
				}
			}
		}
		for(int i=0;i<size;i++) {
			if(n[i])d[i] = inf;
		}
		return d;
	}
	long[] maxtra(int s,long l){
		long[] L = new long[size];
		for(int i=0;i<size;i++){
			L[i] = -1;
		}
		int[] v = new int[size];
		L[s] = -1;

		PriorityQueue<Pair> Q = new PriorityQueue<Pair>(new SampleComparator());
		Q.add(new Pair(l,s));

		while(!Q.isEmpty()){

			Pair C = Q.poll();
			if(v[(int)C.b]==0){
				L[(int)C.b] = C.a;
				v[(int) C.b] = 1;
				for(Edge D:list[(int) C.b])Q.add(new Pair(Math.max(L[(int)C.b],D.cost),D.to));
			}
		}

		return L;
	}
	long Kruskal(){
		long r = 0;
		for(int i=0;i<size;i++) {
			for(Edge e:list[i]) {
				Edges.add(new LinkEdge(e.cost,i,e.to));
			}
		}
		UnionFindTree UF = new UnionFindTree(size);
		for(LinkEdge e:Edges){
			if(e.a>=0&&e.b>=0) {
				if(!UF.same(e.a,e.b)){
					r += e.L;
					UF.unite(e.a,e.b);
				}
			}
		}
		return r;
	}

	ArrayList<Integer> Kahntsort(){

		ArrayList<Integer> ans = new ArrayList<Integer>();
		PriorityQueue<Integer> q = new PriorityQueue<Integer>();
		int[] in = new int[size];
		for(int i=0;i<size;i++) {
			for(Edge e:list[i])in[e.to]++;
		}
		for(int i=0;i<size;i++) {
			if(in[i]==0)q.add(i);
		}
		while(!q.isEmpty()) {
			int v = q.poll();
			ans.add(v);
			for(Edge e:list[v]) {
				in[e.to]--;
				if(in[e.to]==0)q.add(e.to);
			}
		}
		for(int i=0;i<size;i++) {
			if(in[i]>0)return new ArrayList<Integer>();
		}
		return ans;
	}

	RootedTree dfsTree(int i) {
		int[] u = new int[size];
		RootedTree r = new RootedTree(size);
		dfsTree(i,u,r);
		return r;

	}

	private void dfsTree(int i, int[] u, RootedTree r) {
		u[i] = 1;
		for(Edge e:list[i]) {
			if(u[e.to]==0) {
				r.list[i].add(e);
				u[e.to] = 1;
				dfsTree(e.to,u,r);
			}
		}

	}
}


class Tree extends Graph{

	public Tree(int N) {
		super(N);
	}

	long[] tyokkei(){
		long[] a = bfs(0);

		System.out.println();
		int md = -1;
		long m = 0;
		for(int i=0;i<size;i++){
			if(m<a[i]){
				m = a[i];
				md = i;
			}
		}

		long[] b = bfs(md);
		int md2 = -1;
		long m2 = 0;
		for(int i=0;i<size;i++){
			if(m2<b[i]){
				m2 = b[i];
				md2 = i;
			}
		}
		long[] r = {m2,md,md2};
		return r;
	}

}

class RootedTree extends Graph{
	RootedTree(int N){
		super(N);
	}
}
class LinkEdge{
	long L;
	int a ;
	int b;
	LinkEdge(long l,int A,int B){
		L = l;
		a = A;
		b = B;
	}
	public boolean equals(Object o){
		LinkEdge O = (LinkEdge) o;
		return O.a==this.a&&O.b==this.b&&O.L==this.L;
	}

	public int hashCode(){
		return Objects.hash(L,a,b);
	}
}

class Edge{
	int to;
	long cost;

	Edge(int a,long b){
		to = a;
		cost = b;
	}
}
class LinkEdgeComparator implements Comparator<LinkEdge>{
	public int compare(LinkEdge P, LinkEdge Q) {
		long t = P.L-Q.L;
		if(t==0){
			if(P.a>Q.a){
				return 1;
			}else{
				return P.b>Q.b?1:-1;
				
			}
		}
		return t>=0?1:-1;
	}
}

class Triplet{
	long a;
	long b;
	long c;
	Triplet(long p,long q,long r){
		a = p;
		b = q;
		c = r;
	}
	public boolean equals(Object o){
		Triplet O = (Triplet) o;
		return O.a==this.a&&O.b==this.b&&O.c==this.c?true:false;
			
	}

	public int hashCode(){
		return Objects.hash(a,b,c);
	}
}

class TripletComparator implements Comparator<Triplet>{
	public int compare(Triplet P, Triplet Q) {
		long t = P.a-Q.a;
		if(t==0){
			long tt = P.b-Q.b;
			if(tt==0) {
				if(P.c>Q.c) {
					return 1;
				}else if(P.c<Q.c){
					return -1;
				}else {
					return 0;
				}
			}
			return tt>0?1:-1;
		}
		return t>=0?1:-1;
	}
}
class Pair{
	long a;
	long b;

	Pair(long p,long q){
		this.a = p;
		this.b = q;
	}

	public boolean equals(Object o){
		Pair O = (Pair) o;
		return O.a==this.a&&O.b==this.b;
	}

	public int hashCode(){
		return Objects.hash(a,b);
	}
}

class SampleComparator implements Comparator<Pair>{
	public int compare(Pair P, Pair Q) {
		long t = P.a-Q.a;
		if(t==0){
			return P.b>Q.b?1:-1;

		}
		return t>=0?1:-1;
	}
}


class LongIntPair{
	long a;
	int b;

	LongIntPair(long p,int q){
		this.a = p;
		this.b = q;
	}

	public boolean equals(Object o){
		Pair O = (Pair) o;
		return O.a==this.a&&O.b==this.b;

	}

	public int hashCode(){
		return Objects.hash(a,b);
	}
}

class LongIntSampleComparator implements Comparator<LongIntPair>{
	public int compare(LongIntPair P, LongIntPair Q) {
		long t = P.a-Q.a;
		if(t==0){
			if(P.b>Q.b){
				return 1;
			}else{
				return -1;
			}
		}
		return t>=0?1:-1;
	}
}


class IntIntPair{
	int a;
	int b;

	IntIntPair(int p,int q){
		this.a = p;
		this.b = q;
	}

	public boolean equals(Object o){
		Pair O = (Pair) o;
		return O.a==this.a&&O.b==this.b;
			
	}

	public int hashCode(){
		return Objects.hash(a,b);
	}
}

class IntIntSampleComparator implements Comparator<IntIntPair>{
	public int compare(IntIntPair P, IntIntPair Q) {
		int t = P.a-Q.a;
		if(t==0){
			return P.b-Q.b;
		}
		return t;
	}
}


class FastScanner {
    private final java.io.InputStream in = System.in;
    private final byte[] b = new byte[1024];
    private int p = 0;
    private int bl = 0;
    private boolean hNB() {
        if (p<bl) {
            return true;
        }else{
            p = 0;
            try {
                bl = in.read(b);
            } catch (IOException e) {
                e.printStackTrace();
            }
            if (bl<=0) {
                return false;
            }
        }
        return true;
    }
    private int rB() { if (hNB()) return b[p++]; else return -1;}
    private static boolean iPC(int c) { return 33 <= c && c <= 126;}
    private void sU() { while(hNB() && !iPC(b[p])) p++;}
    public boolean hN() { sU(); return hNB();}
    public String next() {
        if (!hN()) throw new NoSuchElementException();
        StringBuilder sb = new StringBuilder();
        int b = rB();
        while(iPC(b)) {
            sb.appendCodePoint(b);
            b = rB();
        }
        return sb.toString();
    }
    public long nextLong() {
        if (!hN()) throw new NoSuchElementException();
        long n = 0;
        boolean m = false;
        int b = rB();
        if (b=='-') {
            m=true;
            b=rB();
        }
        if (b<'0'||'9'<b) {
            throw new NumberFormatException();
        }
        while(true){
            if ('0'<=b&&b<='9') {
                n *= 10;
                n += b - '0';
            }else if(b == -1||!iPC(b)){
                return (m?-n:n);
            }else{
                throw new NumberFormatException();
            }
            b = rB();
        }
    }
    public int nextInt() {
        if (!hN()) throw new NoSuchElementException();
        long n = 0;
        boolean m = false;
        int b = rB();
        if (b == '-') {
            m = true;
            b = rB();
        }
        if (b<'0'||'9'<b) {
            throw new NumberFormatException();
        }
        while(true){
            if ('0'<=b&&b<='9') {
                n *= 10;
                n += b-'0';
            }else if(b==-1||!iPC(b)){
                return (int) (m?-n:n);
            }else{
                throw new NumberFormatException();
            }
            b = rB();
        }
    }
}


class Mathplus{
	int mod = 1000000007;
	long[] fac;
	long[][] comb;
	long[] pow;
	long[] revpow;
	boolean isBuild = false;
	boolean isBuildc = false;
	boolean isBuildp = false;
	int mindex = -1;
	int maxdex = -1;

	void buildFac(){
		fac = new long[3000003];
		fac[0] = 1;
		for(int i=1;i<=3000002;i++){
			fac[i] = (fac[i-1] * i)%mod;
		}
		isBuild = true;
	}
	long divroundup(long n,long d) {
		if(n==0)return 0;
		return (n-1)/d+1;
	}
	public long sigma(long i) {
		return i*(i+1)/2;
	}
	public int digit(long i) {
		int ans = 1;
		while(i>=10) {
			i /= 10;
			ans++;
		}
		return ans;

	}
	public int popcount(int i) {
		int ans = 0;
		while(i>0) {
			ans += i%2;
			i /= 2;
		}
		return ans;
	}
	public boolean contains(int S,int i) {return (S>>i&1)==1;}
	public int bitremove(int S,int i) {return S-(1<<i);}
	public int bitadd(int S,int i) {return S+(1<<i);}
	public boolean isSubSet(int S,int T) {return (S-T)==(S^T);}
	public boolean isDisjoint(int S,int T) {return (S+T)==(S^T);}
	public int isBigger(int[] d, int i) {
		int ok = d.length;
		int ng = -1;
		while(Math.abs(ok-ng)>1) {
			int mid = (ok+ng)/2;
			if(d[mid]>i) {
				ok = mid;
			}else {
				ng = mid;
			}
		}
		return ok;
	}
	public int isSmaller(int[] d, int i) {
		int ok = -1;
		int ng = d.length;
		while(Math.abs(ok-ng)>1) {
			int mid = (ok+ng)/2;
			if(d[mid]<i) {
				ok = mid;
			}else {
				ng = mid;
			}
		}
		return ok;
	}
	public int isBigger(long[] d, long i) {
		int ok = d.length;
		int ng = -1;
		while(Math.abs(ok-ng)>1) {
			int mid = (ok+ng)/2;
			if(d[mid]>i) {
				ok = mid;
			}else {
				ng = mid;
			}
		}
		return ok;
	}
	public int isSmaller(long[] d, long i) {
		int ok = -1;
		int ng = d.length;
		while(Math.abs(ok-ng)>1) {
			int mid = (ok+ng)/2;
			if(d[mid]<i) {
				ok = mid;
			}else {
				ng = mid;
			}
		}
		return ok;
	}
	public int isBigger(ArrayList<Long> d, long i) {
		int ok = d.size();
		int ng = -1;
		while(Math.abs(ok-ng)>1) {
			int mid = (ok+ng)/2;
			if(d.get(mid)>i) {
				ok = mid;
			}else {
				ng = mid;
			}
		}
		return ok;
	}
	public int isSmaller(ArrayList<Long> d, long i) {
		int ok = -1;
		int ng = d.size();
		while(Math.abs(ok-ng)>1) {
			int mid = (ok+ng)/2;
			if(d.get(mid)<i) {
				ok = mid;
			}else {
				ng = mid;
			}
		}
		return ok;
	}
	public HashSet<Integer> primetable(int m) {
		HashSet<Integer> pt = new HashSet<Integer>();
		for(int i=2;i<=m;i++) {
			boolean b = true;
			for(int d:pt) {
				if(i%d==0) {
					b = false;
					break;
				}
			}
			if(b) {
				pt.add(i);
			}
		}
		return pt;
	}
	public ArrayList<Integer> primetablearray(int m) {
		ArrayList<Integer> al = new ArrayList<Integer>();
		Queue<Integer> q = new ArrayDeque<Integer>();
		for(int i=2;i<=m;i++) {
			q.add(i);
			
		}
		boolean[] b = new boolean[m+1];
		while(!q.isEmpty()) {
			int e = q.poll();
			if(!b[e]) {
				al.add(e);
				for(int j=1;e*j<=1000000;j++) {
					b[e*j] = true;
				}
			}
		}
		return al;
	}
	public HashMap<Integer,Integer> hipPush(ArrayList<Integer> l){
		HashMap<Integer,Integer> r = new HashMap<Integer,Integer>();
		TreeSet<Integer> s = new TreeSet<Integer>();
		for(int e:l)s.add(e);
		int p = 0;
		for(int e:s) {
			r.put(e,p);
			p++;
		}
		return r;
	}
	public TreeMap<Integer,Integer> thipPush(ArrayList<Integer> l){
		TreeMap<Integer,Integer> r = new TreeMap<Integer,Integer>();
		Collections.sort(l);
		int b = -(mod+9393);
		int p = 0;
		for(int e:l) {
			if(b!=e) {
				r.put(e,p);
				p++;
			}
			b=e;
		}
		return r;
	}

	
}

