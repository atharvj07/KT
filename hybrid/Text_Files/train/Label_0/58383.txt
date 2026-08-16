import java.io.*;
import java.util.*;

public class Main {
    public static final long mod = (long)1e9+7;
    public static final long INF = Long.MAX_VALUE/2;
    public static final int inf = Integer.MAX_VALUE/2;

    static void solve(InputReader in, PrintWriter out){
        int n = in.ni();
        int sqrt = (int)Math.round(Math.sqrt(1+8*n));
        if(sqrt*sqrt==(1+8*n)&&(1+sqrt)%2==0){
            out.println("Yes");
            int k = (1+sqrt)/2;
            out.println(k);
            ArrayList<Integer>[] ans = new ArrayList[k];
            for (int i = 0; i < k; i++) {
                ans[i] = new ArrayList<>();
            }
            int a = 1;
            for (int i = 1; i < k; i++) {
                for (int j = 0; j < i; j++) {
                    ans[i].add(a);
                    ans[j].add(a);
                    a++;
                }
            }
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < k; i++) {
                sb.append(ans[i].size()+" ");
                for(Integer j: ans[i]) sb.append(j+" ");
                sb.append("\n");
            }
            out.println(sb);
        }else{
            out.println("No");
        }
    }

    public static void main(String[] args){
        InputReader in = new InputReader(System.in);
        PrintWriter out = new PrintWriter(System.out);
        solve(in, out);
        out.close();
    }
    public static class InputReader{
        private BufferedReader br;
        private StringTokenizer st;
        public InputReader(InputStream is){
            br = new BufferedReader(new InputStreamReader(is));
            st = null;
        }
        public String ns(){
            if(st == null || !st.hasMoreTokens()){
                try{
                    st = new StringTokenizer(br.readLine());
                }catch (Exception e){
                    throw new RuntimeException(e);
                }
            }
            return st.nextToken();
        }
        public int ni(){
            return Integer.parseInt(ns());
        }
        public long nl(){
            return Long.parseLong(ns());
        }
        public double nd(){
            return Double.parseDouble(ns());
        }
        public char nc(){
            return ns().toCharArray()[0];
        }
        public int[] ni(int n){
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = ni();
            }
            return a;
        }
        public long[] nl(int n){
            long[] a = new long[n];
            for (int i = 0; i < n; i++) {
                a[i] = nl();
            }
            return a;
        }
        public double[] nd(int n){
            double[] a = new double[n];
            for (int i = 0; i < n; i++) {
                a[i] = nd();
            }
            return a;
        }
    }
}