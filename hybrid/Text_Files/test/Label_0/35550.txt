import java.io.*;
import java.util.*;

public class D {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        PrintWriter pw = new PrintWriter(System.out);
        int n = sc.nextInt();
        int[] arr = new int[n];
        PriorityQueue<Pair> p = new PriorityQueue<>();
        HashMap<Integer,Pair> pp = new HashMap<>();
        for(int i=0;i<n;i++){
            Pair tmp = new Pair(sc.nextInt(),i+1);
            p.add(tmp);
            pp.put(i+1,tmp);
        }
        PriorityQueue<Pair2> queries = new PriorityQueue<>();
        int m = sc.nextInt();
        Pair2[] q = new Pair2[m];
        HashMap<Pair2,Integer> reshash = new HashMap<>();
        for(int i=0;i<m;i++){
            int k = sc.nextInt();
            int pos = sc.nextInt();
            Pair2 tmp = new Pair2(pos,k);
            queries.add(tmp);
            q[i] = tmp;
        }
        FenwickTree ft = new FenwickTree(200002);
        int c = 0;
        while (!queries.isEmpty()){
            Pair2 t = queries.poll();

            while (c<t.y){
                c++;
                Pair tmp = p.poll();
                ft.point_update(tmp.y,1);
            }
            reshash.put(t,pp.get(ft.findKthmin(t.x)).x);
        }
        for(int i=0;i<q.length;i++){
            pw.println(reshash.get(q[i]) + " ");
        }
        pw.println();
        pw.flush();
        pw.close();
    }
    static class FenwickTree { // one-based DS

        int n;
        int[] ft;

        FenwickTree(int size) { n = size; ft = new int[n+1]; }

        int rsq(int b) //O(log n)
        {
            int sum = 0;
            while(b > 0) { sum += ft[b]; b -= b & -b;}		//min?
            return sum;
        }

        int rsq(int a, int b) { return rsq(b) - rsq(a-1); }

        void point_update(int k, int val)	//O(log n), update = increment
        {
            while(k <= n) { ft[k] += val; k += k & -k; }		//min?
        }
        int get(int v){
            int sum =0;
            int id=0;
            for (int i =22;i>=0;i--){
                if (id+(1<<i)>n)
                    continue;
                if (sum+ft[id+(1<<i)]<v){
                    id+=(1<<i);
                    sum+=ft[id];
                }
            }
            return id+1;
        }
        public int findKthmin(int k){
            int a = 1;
            int b = n;
            int mid = 0;
            int res= 1;
            while (a<=b){
                mid = (a+b)/2;
                if(this.rsq(mid)>=k){
                    res =mid;
                    b = mid-1;
                }else{
                    a = mid+1;
                }
            }
            return res;
        }
    }

    static class Pair implements Comparable<Pair>{
        int x;
        int y;
        public Pair(int x,int y){
            this.x= x;
            this.y = y;
        }
        public int compareTo(Pair p){
            if(this.x==p.x)
                return Long.compare(this.y,p.y);
            return -Long.compare(this.x,p.x);
        }
        public String toString(){
            return x+ " " + y;
        }
    }
    static class Pair2 implements Comparable<Pair2>{
        int x;
        int y;
        int index;
        public Pair2(int x,int y){
            this.x= x;
            this.y = y;
            this.index = index;
        }
        public int compareTo(Pair2 p){
            if(this.y==p.y)
                return Long.compare(p.x,this.x);
            return Long.compare(this.y,p.y);
        }

    }
    static class Scanner {
        StringTokenizer st;
        BufferedReader br;

        public Scanner(FileReader r) {
            br = new BufferedReader(r);
        }

        public Scanner(InputStream s) {
            br = new BufferedReader(new InputStreamReader(s));
        }

        public String next() throws IOException {
            while (st == null || !st.hasMoreTokens())
                st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }

        public int nextInt() throws IOException {
            return Integer.parseInt(next());
        }

        public long nextLong() throws IOException {
            return Long.parseLong(next());
        }

        public String nextLine() throws IOException {
            return br.readLine();
        }

        public double nextDouble() throws IOException {
            String x = next();
            StringBuilder sb = new StringBuilder("0");
            double res = 0, f = 1;
            boolean dec = false, neg = false;
            int start = 0;
            if (x.charAt(0) == '-') {
                neg = true;
                start++;
            }
            for (int i = start; i < x.length(); i++)
                if (x.charAt(i) == '.') {
                    res = Long.parseLong(sb.toString());
                    sb = new StringBuilder("0");
                    dec = true;
                } else {
                    sb.append(x.charAt(i));
                    if (dec)
                        f *= 10;
                }
            res += Long.parseLong(sb.toString()) / f;
            return res * (neg ? -1 : 1);
        }

        public boolean ready() throws IOException {
            return br.ready();

        }
    }
}