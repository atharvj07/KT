import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;


public class Main {
    static int i, j, k, n, m, t, y, x, sum;
    static long mod = 1000000007;
    static FastScanner fs = new FastScanner();
    static PrintWriter out = new PrintWriter(System.out);
    static String str;
    static int[] arr = new int[10];

    static long ans=0;

    public static void main(String[] args) {

        int n = fs.nextInt();
        k = fs.nextInt();

        combi(0);

        long m1 = ans;
        long m2 = 1;

        long temp = n-k;

        for(i=0;i<n-k;i++){
            m2*=temp;

            m2%=mod;
        }

        ans = (m1*m2)%mod;

        out.println(ans);


        out.close();
    }

    private static void combi(int a){

        if(a==k){
            if(isValid()) {
                ans++;
                ans%=mod;
            }

        }

        else{
            for(int i=0;i<k;i++){
                arr[a]=i;
                combi(a+1);
            }
        }
    }

    private static boolean isValid(){
        long[] vis = new long[k];

        initialize(vis, -1);

        vis[0]=1;

        int f =0;
        for(int i=1;i<k;i++){
            if(checkIndex(vis,i)!=1){
                f=1;
                break;
            }
        }

        return f==0;

    }

    private static int checkIndex(long[] vis,int i){
        if(vis[i]==-1){
            vis[i]=0;
            vis[i] = checkIndex(vis,arr[i]);
        }

        return (int)vis[i];
    }

    private static void initialize(long[] arr, long val){

        int n = arr.length;

        for(int i = 0;i<n;i++){
            arr[i]=val;
        }
    }



    static class FastScanner {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer("");

        String next() {
            while (!st.hasMoreTokens())
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }
    }

    static class Pair implements Comparable<Pair> {
        int first, second;

        public Pair(int first, int second) {
            this.first = first;
            this.second = second;
        }

        public int compareTo(Pair o) {
            return Long.compare(first, o.first);
        }

    }

    static void ruffleSort(int[] a) {
        //ruffle
        int n=a.length;
        Random r=new Random();
        for (int i=0; i<a.length; i++) {
            int oi=r.nextInt(n), temp=a[i];
            a[i]=a[oi];
            a[oi]=temp;
        }

        //then sort
        Arrays.sort(a);
    }


}