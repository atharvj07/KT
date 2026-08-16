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
    int gcd(int a, int b){
        if(a % b == 0)return b;
        return gcd(b, a % b);
    }
    final int mod = (int)(1e9) + 7;
    final int max = 100010;
    long fac[] = new long[max], ifac[] = new long[max];
    long rpe(long a, long b){
        long ans = 1;
        while(b != 0){
            if(b % 2 != 0)ans = ans * a % mod;
            a = a * a % mod; b >>= 1;
        }return ans;
    }
    long f(int x){
        long v = 0;
        for(int i = 0; 2 * i <= x; i++){
            long a = fac[x - i] * ifac[i] % mod * ifac[x - 2 * i] % mod;
            v = (v + a) % mod;
        }return v;
    }
    void solve(){
        fac[0] = ifac[0] = 1;
        for(int i = 1; i < max; i++){
            fac[i] = fac[i - 1] * i % mod;
            ifac[i] = rpe(fac[i], mod - 2);
        }
        char ch[] = in.next().trim().toCharArray();
        long ans = 1;
        int l = ch.length;
        int cu = 0, cn = 0;
        for(int i = 0; i < l; i++){
            if(ch[i] == 'w' || ch[i] == 'm'){
                ans = 0; continue;
            }
            if(ch[i] != 'u' && cu != 0){
                ans = ans * f(cu) % mod;
                cu = 0;
            }
            if(ch[i] != 'n' && cn != 0){
                ans = ans * f(cn) % mod;
                cn = 0;
            }
            if(ch[i] == 'n'){
                cn++;
            }
            if(ch[i] == 'u'){
                cu++;
            }
        }
       if(cu != 0){
            ans = ans * f(cu) % mod;
            cu = 0;
        }
        if(cn != 0){
            ans = ans * f(cn) % mod;
            cn = 0;
        }
        out.print(ans);
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
        