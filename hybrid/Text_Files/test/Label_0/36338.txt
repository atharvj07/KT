
import java.util.*;
import java.io.*;

public class Codeforces {
    
    InputStream is;
    PrintWriter out;
    String INPUT = "";

//----------------------------------------------------------------------------------------------------//
    int a,b,c;
    /*int INF=(int)1e9;
    boolean check1(int x,int shop){
        long s1=a*x;
        long s2=((x+b-1)/x)*c;
        if(shop==1)return s1<s2;
        return s2<s1;
    }
    int binsearch(int shop){
        int l=0;
        int r=INF;
        while(l<r){
            int m=l+(r-l)>>1;
            if(check1(m,shop))return m;
            
        }
    }*/
    class Pair implements Comparator<Pair>,Comparable<Pair>{
        int val,idx;
        Pair(int x,int y){
            val=x;
            idx=y;
        } 

        @Override
        public int compare(Pair o1, Pair o2) {
            return o1.val-o2.val;
        }

        @Override
        public int compareTo(Pair o) {
             return this.val-o.val;
        }
    }
    void solve() {
        int t = 1;
        t=ni();
        while (t-- > 0) {
           char s[]=ns().toCharArray();
            Set<Integer> set = new HashSet<>();
            List<Pair> al = new ArrayList<>();
            

            int x=0;
            int n=s.length;
            for (int i = 0; i <n; i++) {
                if(s[i]=='+')x++;
                else x--;
                if(x<0){
                    if(!set.contains(x)){
                        set.add(x);
                        al.add(new Pair(-x,i+1));
                    }
                }
            }
            if(set.isEmpty()){
                out.println(n);
                continue;
            }
            Collections.sort(al);
            int max=al.get(al.size()-1).val;
            long ans=n;
            int j=0;
            for (int i = 0; i < max; i++) {
                if(i>=al.get(j).val)j++;
                j=Math.min(j,al.size()-1);
                ans+=al.get(j).idx;
            }
            out.println(ans);
        }
    }

//----------------------------------------------------------------------------------------------------//
    int upperBound(List<Integer> v, int x) { //C++:IDX in sorted V strictly greater than x [0....v.size()]
        int n = v.size();
        int l = 0;
        int r = n - 1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (v.get(m) > x) {
                if (l == r) {
                    return r;
                }
                r = m;
            } else {
                l = m + 1;
            }
        }
        return l;
    }

    boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i <= (int) Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
    
    Vector<Integer> sieveOfEratosthenes(int n) {
        boolean[] prime = new boolean[n + 1];
        for (int i = 0; i < n; i++) {
            prime[i] = true;
        }
        for (int p = 2; p * p <= n; p++) {
            if (prime[p] == true) {
                for (int j = p * p; j <= n; j += p) {
                    prime[j] = false;
                }
            }
        }
        Vector<Integer> v = new Vector<>();
        for (int i = 2; i <= n; i++) {
            if (prime[i]) {
                v.add(i);
            }
        }
        return v;
    }
    
    void swap(int a[], int l, int r) {
        int temp = a[l];
        a[l] = a[r];
        a[r] = temp;
    }
    
    long nCr(int n, int k) {
        long C[] = new long[k + 1];
        // nC0 is 1 
        C[0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = Math.min(i, k); j > 0; j--) {
                C[j] = C[j] + C[j - 1];
            }
        }
        return C[k];
    }
    
    int gcd(int s, int l) {
        if (s == 0) {
            return l;
        }
        
        return gcd(l % s, s);
    }
    
    int power(long x, long y, int m) { //log(y)
        if (y == 0) {
            return 1;
        }
        long p = power(x, y / 2, m) % m;
        p = (p * p) % m;
        return (int) ((y % 2 == 0) ? p : (x * p) % m);
    }
    
    int modInverse(int a, int m) // O(Log m) whem m is prime (fermat's little theorem)
    {        
        if (gcd(a, m) != 1) {
            return -1;
        } else {            
            return power(a, m - 2, m);            
        }        
    }    
    
    /*public HashMap<Integer, Integer> sortByValue(HashMap<Integer, Integer> hm) {
        // Create a list from elements of HashMap 
        List<Map.Entry<Integer, Integer>> list
                = new LinkedList<>(hm.entrySet());

        //->change o1,o2 for reverseorder
        Collections.sort(list, (Map.Entry<Integer, Integer> o1, Map.Entry<Integer, Integer> o2) -> (o1.getValue()).compareTo(o2.getValue()));

        // put data from sorted list to hashmap  
        HashMap<Integer, Integer> temp = new LinkedHashMap<>();
        list.forEach((aa) -> {
            temp.put(aa.getKey(), aa.getValue());
        });
        return temp;
    }*/
    
    void run() throws Exception {
        is = System.in;//oj ? System.in : new ByteArrayInputStream(INPUT.getBytes());
        out = new PrintWriter(System.out);
        
        long s = System.currentTimeMillis();
        solve();
        out.flush();
        //tr(System.currentTimeMillis() - s + "ms");
    }
    
    public static void main(String[] args) throws Exception {
        new Codeforces().run();
    }
    
    private byte[] inbuf = new byte[1024];
    public int lenbuf = 0, ptrbuf = 0;
    
    private int readByte() {
        if (lenbuf == -1) {
            throw new InputMismatchException();
        }
        if (ptrbuf >= lenbuf) {
            ptrbuf = 0;
            try {
                lenbuf = is.read(inbuf);
            } catch (IOException e) {
                throw new InputMismatchException();
            }
            if (lenbuf <= 0) {
                return -1;
            }
        }
        return inbuf[ptrbuf++];
    }
    
    private boolean isSpaceChar(int c) {
        return !(c >= 33 && c <= 126);
    }
    
    private int skip() {
        int b;
        while ((b = readByte()) != -1 && isSpaceChar(b));
        return b;
    }
    
    private double nd() {
        return Double.parseDouble(ns());
    }
    
    private char nc() {
        return (char) skip();
    }
    
    private String ns() {
        int b = skip();
        StringBuilder sb = new StringBuilder();
        while (!(isSpaceChar(b))) {  // when nextLine(take whole line as input wid space), (!isSpaceChar(b) || b == ' ') 
            //if(b!=' ') to remove spaces in Str when taking spaces in Str
            sb.appendCodePoint(b);
            b = readByte();
        }
        return sb.toString();
    }
    
    private char[] ns(int n) {
        char[] buf = new char[n];
        int b = skip(), p = 0;
        while (p < n && !(isSpaceChar(b))) {
            buf[p++] = (char) b;
            b = readByte();
        }
        return n == p ? buf : Arrays.copyOf(buf, p);
    }
    
    private char[][] nm(int n, int m) {
        char[][] map = new char[n][];
        for (int i = 0; i < n; i++) {
            map[i] = ns(m);
        }
        return map;
    }
    
    private int[] na(int n) {
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = ni();
        }
        return a;
    }
    
    private int ni() {
        int num = 0, b;
        boolean minus = false;
        while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-'));
        if (b == '-') {
            minus = true;
            b = readByte();
        }
        
        while (true) {
            if (b >= '0' && b <= '9') {
                num = num * 10 + (b - '0');
            } else {
                return minus ? -num : num;
            }
            b = readByte();
        }
    }
    
    private long nl() {
        long num = 0;
        int b;
        boolean minus = false;
        while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-'));
        if (b == '-') {
            minus = true;
            b = readByte();
        }
        
        while (true) {
            if (b >= '0' && b <= '9') {
                num = num * 10 + (b - '0');
            } else {
                return minus ? -num : num;
            }
            b = readByte();
        }
    }
    
    private boolean oj = System.getProperty("ONLINE_JUDGE") != null;
    
    private void tr(Object... o) {
        if (!oj) {
            System.out.println(Arrays.deepToString(o));
            
        }
    }
    
    class Dsu {
        
        int par[];
        int size[];
        int cnt;
        Set<Integer> roots = new HashSet<>();
        //boolean belongs[];
        
        Dsu(int n) {
            cnt = n;//cnt=0;
            par = new int[n];
            size = new int[n];
            //belongs=new boolean[n];
            for (int i = 0; i < n; i++) {
                par[i] = i;
                size[i] = 1;
                roots.add(i);
                //belongs[i]=false;
            }
        }
        
        int root(int i) {
            if (i == par[i]) {
                return i;
            }
            return par[i] = root(par[i]);
        }
        
        boolean find(int p, int q) {
            return root(p) == root(q);
        }
        
        void union(int p, int q) {
            int a = root(p);
            int b = root(q);
            if (a != b) {
                cnt--;
            }
            /*if(!belongs[p]&&!belongs[q])cnt++;
            else if(belongs[p]&&belongs[q]){
                if(a!=b)cnt--;
            }
            belongs[p]=belongs[q]=true;*/
            if (a == b) {
                return;
            }
            if (size[a] < size[b]) {
                int temp = a;
                a = b;
                b = temp;
            }
            par[b] = a;
            size[a] += size[b];
            roots.add(a);
            if (roots.contains(b)) {
                roots.remove(b);
            }
        }
        
        Set<Integer> getRoots() {
            return roots;
        }
        
        int count() {            
            return cnt;
        }
        
    }
}
//upperBound(List<Integer> v,int x) C++;
//isPrime(int)
//Vector<Integer> sieveOfEratosthenes(int n){PRIME NO <=n}
//swap(arr,i,j)
//HashMap sortByValue(map);
//long comb=nCr(5,2);
//int gcd(s,l);
//Pair p=new Pair(x,y);
// Dsu dsu=new Dsu(n);
