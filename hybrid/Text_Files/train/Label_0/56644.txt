import java.util.*;
import java.io.*;
public class Main{
    static PrintWriter out;
    static InputReader in;
    public static void main(String args[]){
        out = new PrintWriter(System.out);
        in = new InputReader();
        new Main();
        out.flush(); out.close();
    }   
    Main(){
        solve();
    }
    class pair{
        long F, S;
        pair(long a, long b){
            F = a; S = b;
        }
    }
    final int max = 1000100;
    final long maxv = (long)2e18;
    int n; long c;
    long h[];
    pair seg[] = new pair[4 * max];
    // TreeSet<pair> ts = new TreeSet<>((A, B) -> A.F == B.F ? Long.compare(B.S, A.S) : Long.compare(B.F, A.F));
    long find(pair p, long x){
        return p.F * x + p.S;
    }
    void upd(int n, int s, int e, pair u){
        if(seg[n] == null || s == e){
            seg[n] = u;
            return;
        }
        int mid = (s + e) >> 1;
        boolean lowL = find(seg[n], s) > find(u, s);
        boolean lowM = find(seg[n], mid) > find(u, mid);
        if(lowL && lowM){
            pair f = seg[n];
            seg[n] = u;
            upd(2 * n + 2, mid + 1, e, f);
        }else if(!lowL && !lowM){
            upd(2 * n + 2, mid + 1, e, u);
        }else if(lowL && !lowM){
            upd(2 * n + 1, s, mid, u);
        }else{
            pair f = seg[n];
            seg[n] = u;
            upd(2 * n + 1, s, mid, f);
        }
    }
    long query(int n, int s, int e, long x){
        if(seg[n] == null)return maxv;
        if(s == e)return find(seg[n], x);
        int mid = (s + e) >> 1;
        if(x <= mid)return Math.min(find(seg[n], x), query(2 * n + 1, s, mid, x));
        else return Math.min(find(seg[n], x), query(2 * n + 2, mid + 1, e, x));
    }
    void solve(){
        n = in.nextInt(); c = in.nextLong();
        h = new long[n];
        for(int i = 0; i < n; i++)h[i] = in.nextLong();
        upd(0, 0, max - 1, new pair(-2 * h[0], h[0] * h[0]));
        for(int i = 1; i < n; i++){
            long val = query(0, 0, max - 1, h[i]) + h[i] * h[i] + c;
            if(i == n - 1){
                out.println(val);
                return;
            }
            upd(0, 0, max - 1, new pair(-2 * h[i], val + h[i] * h[i]));
        }
    }
    public static class InputReader{
        BufferedReader br;
        StringTokenizer st;
        InputReader(){
            br = new BufferedReader(new InputStreamReader(System.in));
        }
        public int nextInt(){
            return Integer.parseInt(next());
        }
        public long nextLong(){
            return Long.parseLong(next());
        }
        public double nextDouble(){
            return Double.parseDouble(next());
        }
        public String next(){
            while(st == null || !st.hasMoreTokens()){
                try{
                    st = new StringTokenizer(br.readLine());
                }catch(IOException e){}
            }
            return st.nextToken();
        }
    }
}
        