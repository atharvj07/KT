import java.util.*;
import java.io.*;
import java.math.*;
import java.util.regex.Matcher;
//linkedhashmap contains the entry in the same order which we are giving and not in sorted way like in hashmaps
 public class CF {
    FastScanner in;
    PrintWriter out;
    final static int M=1000001;
    public ArrayList<Integer> input(int m){
        ArrayList<Integer> li= new ArrayList<>();
        for(int i=0;i<m;i++)
            li.add(in.nextInt());
        return li;
    }
    class Pair{
        int x;
        int y;
    }
    public class pair<T,V> {
        private T x;
        private V y;

        public void setY(V y) {
            this.y = y;
        }

        public V getY() {
            return y;
        }

        public void setX(T x) {
            this.x = x;
        }

        public T getX() {
            return x;
        }
    }
    Set<Long> primeFactors(long n)
    {
        // Print the number of 2s that divide n
        Set<Long> li=new HashSet<>();

        while (n%2 == 0)
        {
            li.add(2L);
            n = n/2;
        }

        // n must be odd at this point.  So we can skip one element (Note i = i +2)
        for (long i = 3; i <= Math.sqrt(n); i = i+2)
        {
            // While i divides n, print i and divide n
            while (n%i == 0)
            {
                li.add(i);
                n = n/i;
            }
        }

        // This condition is to handle the case whien n is a prime number
        // greater than 2
        if (n > 2)
            li.add(n);
        return li;
    }
    int res[];
    void sieve(){
        res=new int[10000009];

        int p[]=new int[10000009];
        for(int i=2;i<=10000000;i++){
            if(p[i]==0){
                for(int j=i+i;j<=10000000;j+=i){
                    if(p[i]==0){
                        p[j]=i;
                    }
                    res[i]=res[i-1]+i;
                }
            }
            else{
                res[i]=res[i-1]+p[i];
            }
        }
    }
    public static HashSet<String> getAllPermutations(String str) {

        HashSet<String> permutations = new HashSet<String>();

        if(str == null || str.length() == 0) {
            permutations.add("" );
            return permutations;
        }

        char first = str.charAt(0);
        String remainingString = str.substring(1);
        HashSet<String> words = getAllPermutations(remainingString);
        for(String word: words) {
            for(int i = 0; i <= word.length(); i++) {
                String prefix = word.substring(0, i);
                String suffix = word.substring(i);
                permutations.add(prefix + first + suffix);
            }
        }
        return permutations;
    }

//    static class Pair<T> {
//        T a;
//        T b;
//
//        public Pair(T a, T b) {
//            this.a = a;
//            this.b = b;
//        }
//    }

    void solve() {
       int n=in.nextInt();
        int t =in.nextInt();
        int a[]=new int[n];
        for(int i=1;i<n;i++)
            a[i]=in.nextInt();
        int x=1;
        while(x<t){
            x+=a[x];
        }
        if(x==t)
            System.out.println("YES");
        else
            System.out.println("NO");
    }
    static boolean isPali(StringBuilder s){
        for(int i = 0; i < (s.length() >> 1); i++)
            if(s.charAt(i) != s.charAt(s.length() - 1 - i))
                return false;
        return true;
    }
    void run(){
        try {
            in = new FastScanner(new File("B.in"));
            out = new PrintWriter(new File("B.out"));
            solve();
            out.close();
        }
        catch(FileNotFoundException e){
            e.printStackTrace();
        }
    }

    void runIO(){
        in = new FastScanner(System.in);
        out = new PrintWriter(System.out);

        solve();
        out.close();
    }
    class FastScanner{
        BufferedReader br;
        StringTokenizer st;
        public FastScanner(File f){
            try{
                br = new BufferedReader(new FileReader(f));
            }
            catch(FileNotFoundException e){
                e.printStackTrace();
            }
        }
        public FastScanner(InputStream f){
            br = new BufferedReader(new InputStreamReader(f));
        }
        String next(){
            while(st==null || !st.hasMoreTokens()){
                String s = null;
                try{
                    s= br.readLine();
                }
                catch(IOException e){
                    e.printStackTrace();
                }
                if(s==null)
                    return null;
                st = new StringTokenizer(s);
            }
            return st.nextToken();
        }

        boolean hasMoreTokens(){
            while(st==null || !st.hasMoreTokens()){
                String s = null;
                try{
                    s= br.readLine();
                }
                catch(IOException e){
                    e.printStackTrace();
                }
                if(s==null)
                    return false;
                st = new StringTokenizer(s);
            }
            return true;
        }
        int nextInt(){
            return Integer.parseInt(next());
        }
        long nextLong(){
            return Long.parseLong(next());
        }
        double nextDouble(){
            return Double.parseDouble(next());
        }
    }

    public static void main(String[] args) {
        new CF().runIO();
    }
}