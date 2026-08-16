import java.io.IOException;
import java.io.InputStream;
import java.util.*;

public class Main {
    static Basic basic = new Basic();
    static FastScanner sc = new FastScanner();
    public static void main(String[] args) {
        long n = sc.nextLong();
        long k = sc.nextLong();
        basic.COMinit();
        long MAX = Math.min(n,k);
        long ans = (1+n*(n-1))%MOD;
        for (int i=2;i<=MAX;i++){
            ans=(ans+basic.COM((int)n,i)*basic.HCOM(((int)n-i),i)%MOD)%MOD;
        }
        System.out.println(ans);
    }

    public static long MOD  = 1000000007;
    public static int tenE9 = 1000000000;
    public static class FastScanner {
        private final InputStream in = System.in;
        private final byte[] buffer = new byte[1024];
        private int ptr = 0;
        private int buflen = 0;
        private boolean hasNextByte() {
            if (ptr < buflen) {
                return true;
            }else{
                ptr = 0;
                try {
                    buflen = in.read(buffer);
                } catch (IOException e) {
                    e.printStackTrace();
                }
                if (buflen <= 0) {
                    return false;
                }
            }
            return true;
        }
        private int readByte() { if (hasNextByte()) return buffer[ptr++]; else return -1;}
        private static boolean isPrintableChar(int c) { return 33 <= c && c <= 126;}
        public boolean hasNext() { while(hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++; return hasNextByte();}
        public String next() {
            if (!hasNext()) throw new NoSuchElementException();
            StringBuilder sb = new StringBuilder();
            int b = readByte();
            while(isPrintableChar(b)) {
                sb.appendCodePoint(b);
                b = readByte();
            }
            return sb.toString();
        }
        public long nextLong() {
            if (!hasNext()) throw new NoSuchElementException();
            long n = 0;
            boolean minus = false;
            int b = readByte();
            if (b == '-') {
                minus = true;
                b = readByte();
            }
            if (b < '0' || '9' < b) {
                throw new NumberFormatException();
            }
            while(true){
                if ('0' <= b && b <= '9') {
                    n *= 10;
                    n += b - '0';
                }else if(b == -1 || !isPrintableChar(b)){
                    return minus ? -n : n;
                }else{
                    throw new NumberFormatException();
                }
                b = readByte();
            }
        }
        public int nextInt() {
            long nl = nextLong();
            if (nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE) throw new NumberFormatException();
            return (int) nl;
        }
        public double nextDouble() { return Double.parseDouble(next());}
    }
    public static class Basic {
        //math
        private final int MAX = 510000;
        private final int MOD = 1000000007;
        private final long[] fac = new long[MAX];
        private final long[] finv = new long[MAX];
        private final long[] inv = new long[MAX];
        public long factorial(long num) {
            if (num < 2) return 1;
            else return num * factorial(num - 1);
        }
        public int arraySum(int[] array) {
            int ans = 0;
            for (int value : array) ans += value;
            return ans;
        }
        public double log(double base, double antilogarithm) {
            return Math.log(antilogarithm) / Math.log(base);
        }
        public long gcd(long x, long y) {
            if (y == 0) return x;
            else return gcd(y, x % y);
        }
        public long lcm(long x, long y) {
            return x / gcd(x, y) * y;
        }
        public HashMap<Long, Long> factorization(long num) {
            HashMap<Long, Long> hash = new HashMap<>();
            long n = num;
            long count = 2;
            while (n > 1) {
                while (n % count == 0) {
                    n /= count;
                    if (hash.containsKey(count)) hash.put(count, hash.get(count) + 1);
                    else hash.put(count, 1L);
                }
                count++;
            }
            return hash;
        }
        public int sum(int[] num) {
            int ans = 0;
            for (int i = 0; i < num.length; i++) {
                ans += num[i];
            }
            return ans;
        }
        public int[] reduce(int small, int big) {
            int ins = 2;
            while (ins <= small) {
                if (small % ins == 0 && big % ins == 0) {
                    small /= ins;
                    big /= ins;
                    ins = 2;
                } else {
                    ins++;
                }
            }
            return new int[]{small, big};
        }
        public int reduceCount(int small, int big) {
            int ins = 2;
            int ans = 0;
            while (ins <= small) {
                if (small % ins == 0 && big % ins == 0) {
                    small /= ins;
                    big /= ins;
                    ins = 2;
                    ans++;
                } else {
                    ins++;
                }
            }
            return ans;
        }
        public int binarySearch(int[] array, int target) {
            int pos = -1;
            int left = 0;
            int right = array.length - 1;
            int middle;
            while (pos == -1 && left <= right) {
                middle = (left + right) / 2;
                if (array[middle] == target) pos = middle;
                else if (array[middle] > target) right = middle - 1;
                else left = middle + 1;
            }
            return pos;
        }
        public long modPow(long a, long n, long mod) {
            long res = 1;
            while (n > 0) {
                if ((n & 1) != 0) res = res * a % mod;
                a = a * a % mod;
                n >>= 1;
            }
            return res;
        }
        public long modinv(long a, long mod) {
            return modPow(a, mod - 2, mod);
        }
        public void COMinit() {
            fac[0] = 1;
            fac[1] = 1;
            finv[0] = 1;
            finv[1] = 1;
            inv[1] = 1;
            for (int i = 2; i < MAX; i++) {
                fac[i] = fac[i - 1] * i % MOD;
                inv[i] = MOD - inv[MOD % i] * (MOD / i) % MOD;
                finv[i] = finv[i - 1] * inv[i] % MOD;
            }
        }
        public long COM(int n, int k) {
            if (n < k) return 0;
            if (n < 0 || k < 0) return 0;
            return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD;
        }
        public long PER(int n, int k){
            return fac[n]*finv[n-k]%MOD;
        }
        public long HCOM(int n, int k) {
            return COM(n + k - 1, k);
        }

        //array
        public int[] remove(int[] ar, int pos) {
            int[] ret = new int[ar.length - 1];
            for (int i = 0; i < pos; i++) ret[i] = ar[i];
            for (int i = pos + 1; i < ar.length; i++) ret[i - 1] = ar[i];
            return ret;
        }
        public int[] nextArray(int size,int cons){
            int[] ret = new int[size];
            for (int i=0;i<size;i++)ret[i]=sc.nextInt()+cons;
            return  ret;
        }
        public int[] reverse(int[] ar){
            int[] ret = new int[ar.length];
            for (int i=0;i<ar.length;i++){
                ret[i]=ar[ar.length-1-i];
            }
            return ret;
        }
        //graph
        public void warshall_floyd(int[][] d) {
            int n = d.length;
            for (int k = 0; k < n; k++)
                for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) d[i][j] = Math.min(d[i][j], d[i][k] + d[k][j]);
        }//隣接行列が引数。辺が無い場合、INFを入力。
        public int[] bellman_ford(int[][] d, int size, int start){
            int e = d.length;
            int[] ans = new int[size];
            Arrays.fill(ans,Integer.MAX_VALUE);
            ans[start]=0;
            for (int i=0;i<size;i++){
                for (int[] a : d) {
                    if (ans[a[1]] > ans[a[0]] + a[2]) {
                        ans[a[1]] = ans[a[0]] + a[2];
                        if (i == size - 1) {
                            System.out.println("negative loop");
                            break;
                        }
                    }
                }
            }
            return ans;
        }//辺を配列の要素として管理。

    }
    public static class Queue<T>{
        private final int max = 1000000;
        private final T[] queue = (T[]) new Object[max];
        private int tail = 0; private int head = 0;
        public void init(){this.head = 0; tail = 0;}
        public boolean isEmpty(){return (head==tail);}
        public boolean isFull(){return (head == (tail+1)%max);}
        public void enqueue(T v){
            if (isFull()){
                System.out.println("error: queue is full.");
                return;
            }
            queue[tail++] = v;
            if (tail == max) tail = 0;
        }
        public T dequeue(){
            if (isEmpty()){
                System.out.println("error: queue is empty");
                return null;
            }
            T res = queue[head];
            ++head;
            if (head == max) head = 0;
            return res;
        }
    }
    public static class Stack<T>{
        private final int max = 100000;
        private final T[] stack =(T[]) new Object[max];
        private int top = 0;
        public boolean isEmpty(){return (top==0);}
        public boolean isFull(){return (top==max);}
        public void init(){top=0;}
        public void push(T v){
            if (isFull()){
                System.out.println("error: stack is full.");
                return;
            }
            stack[top++] = v;
        }
        public T pop(){
            if (isEmpty()){
                System.out.println("error: stack is empty");
                return null;
            }
            return stack[--top];
        }
    }
    public static class Pair<K,V>{
        private K A;
        private V B;
        Pair(K a,V b){
            A=a;
            B=b;
        }
        public void changeA(K a){A=a;}
        public void changeB(V b){B=b;}
        public void changeAB(K a,V b){A=a;B=b;}
        public static Comparator numberSortWithA = new Comparator() {
            @Override
            public int compare(Object o1, Object o2) {
                Pair p = (Pair)o1;
                Pair q = (Pair)o2;
                if ((int)p.A<(int)q.A)return -1;
                else if ((int)p.A==(int)q.A){
                    if ((int)p.B<(int)q.B)return -1;
                    else if ((int)p.B==(int)q.B)return 0;
                    else return 1;
                }
                else return 1;
            }
        };
        public static Comparator numberSortWithB = new Comparator() {
            @Override
            public int compare(Object o1, Object o2) {
                Pair p = (Pair)o1;
                Pair q = (Pair)o2;
                if ((int)p.B<(int)q.B)return -1;
                else if ((int)p.B==(int)q.B){
                    if ((int)p.A<(int)q.A)return -1;
                    else if ((int)p.A==(int)q.A)return 0;
                    else return 1;
                }
                else return 1;
            }
        };
    }
    public static class Graph{
        private final HashMap<Integer,HashSet<Integer>> graph = new HashMap<>();
        private final int Size;
        private int[] Depth;
        Graph(int size){
            for (int i=0;i<size;i++)graph.put(i,new HashSet<>());
            Size = size;
        }

        public void addEdge(int node1,int node2){
            if (graph.containsKey(node1)&&graph.containsKey(node2)){
                graph.get(node1).add(node2);
                graph.get(node2).add(node1);
            }
        }
        public void addDirectEdge(int from,int to){
            if (graph.containsKey(from)&&graph.containsKey(to)){
                graph.get(from).add(to);
            }
        }
        public int[] Depth(int root){
            Queue<Integer> q = new Queue<>();
            q.enqueue(root);
            boolean[] seen = new boolean[Size];
            Arrays.fill(seen, false);
            seen[root]=true;
            int[] depth = new int[Size];
            depth[root]=0;
            while (!q.isEmpty()){
                int v = q.dequeue();
                for (int u : graph.get(v)){
                    if (!seen[u]){
                        seen[u]=true;
                        q.enqueue(u);
                        depth[u]=depth[v]+1;
                    }
                }
            }
            Depth = depth.clone();
            return depth;
        }
    }
    public static class WeightedGraph{
        private final HashMap<Integer,HashMap<Integer,Integer>> graph = new HashMap<>();
        private final int Size;
        WeightedGraph(int size){
            for (int i=0;i<size;i++)graph.put(i,new HashMap<>());
            Size = size;
        }

        public void addEdge(int node1,int node2,int weight){
            if (graph.containsKey(node1)&&graph.containsKey(node2)){
                graph.get(node1).put(node2,weight);
                graph.get(node2).put(node1,weight);
            }
        }
        public void addDirectEdge(int from,int to,int weight){
            if (graph.containsKey(from)&&graph.containsKey(to)){
                graph.get(from).put(to,weight);
            }
        }
        public int[] dijkstra(int root){
            Comparator<int[]> c = new Comparator<int[]>() {
                @Override
                public int compare(int[] o1, int[] o2) {
                    return Integer.compare(o1[1], o2[1]);
                }
            };
            PriorityQueue<int[]> q = new PriorityQueue<>(c);
            q.add(new int[]{root,0});
            int[] ret = new int[Size];
            Arrays.fill(ret,Integer.MAX_VALUE);
            ret[root]=0;
            while (!q.isEmpty()){
                int[] v = q.poll();
                if (v[1]<=ret[v[0]]){
                    HashMap<Integer,Integer> h = graph.get(v[0]);
                    for (int u : h.keySet()){
                        if (ret[u]>v[1]+h.get(u)){
                            ret[u]=v[1]+h.get(u);
                            q.add(new int[]{u,ret[u]});
                        }
                    }
                }
            }
            return ret;
        }

    }
    public static class UnionFindTree{
        int[] parent;
        int[] rank;
        int[] Size;
        int Number;
        public UnionFindTree(int size){
            this.parent = new int[size];
            this.rank = new int[size];
            this.Size = new int[size];
            makeSet();
        }
        public void makeSet(){
            for (int i=0;i<Size.length;i++){
                parent[i]=i;
                rank[i]=0;
                Size[i]=1;
            }
            Number= Size.length;
        }
        public void unite(int x, int y){
            int xRoot = find(x);
            int yRoot = find(y);
            if (rank[xRoot]>rank[yRoot]){
                parent[yRoot] = xRoot;
                Size[xRoot]+=Size[yRoot];
                Number--;
            }else if (rank[xRoot]<rank[yRoot]){
                parent[xRoot] = yRoot;
                Size[yRoot]+=Size[xRoot];
                Number--;
            }else if (xRoot!=yRoot){
                parent[yRoot] = xRoot;
                rank[xRoot]++;
                Size[xRoot]+=Size[yRoot];
                Number--;
            }
        }
        public int find(int i){
            if (i!= parent[i]){
                parent[i]=find(parent[i]);
            }
            return parent[i];
        }
        public boolean same(int x, int y){
            return find(x) == find(y);
        }
        public int getSize(int i){return Size[find(i)];}
        boolean isConnected(){
            return Number<2;
        }
    }
    public static class BitSearch<T>{
        T[] Array;
        int Width;
        int Length;
        BitSearch(T[] t, int width){
            Array = t;
            Width = width;
            Length = Array.length;
        }
        void start(){
            long max = (long)Math.pow(Width,Length);
            for (long i=0;i<max;i++){
                StringBuilder s = new StringBuilder(Long.toString(i, Width));
                while (s.length()<Length) s.insert(0, "0");
                run(s);
            }
        }
        void run(StringBuilder s){

        }
    }

}
