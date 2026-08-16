import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Inc_and_Cpy {
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (Exception e) {

                    e.printStackTrace();
                }

            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (Exception e) {
                e.printStackTrace();
            }
            return str;
        }

        long nextLong() {
            return Long.parseLong(next());
        }
    }
    public static void main(String[] args) {
        FastReader in = new FastReader();
        int t = in.nextInt();
        while(t-- > 0){
            long a = in.nextLong();
            System.out.println(Solve(a));
        }
    }
    static long Solve (long n){
        long l = 0;
        long r = n;
        long ans = 0;

        while(l <= r){
            long mid = (l + r)/2;
            if(good(mid,n)){
                r = mid - 1;
                ans = mid;
            }else{
                l = mid + 1;
            }
        }
        return ans;
    }

        private static boolean good(long mid, long n) {
              long val = mid/2 + 1;
              long free = mid - mid/2 + 1;
              return val * free >= n;
        }
        }


