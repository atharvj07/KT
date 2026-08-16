import java.io.*;
import java.util.*;

public class TaskE {
    static FastIO io = new FastIO("in.txt");
    static int N;
    static int[][] P;
    static BIT cnt0, cnt1, sum;
    static HashMap<Integer, Integer> idxs = new HashMap<>();
    static TreeSet<Integer> idxsList = new TreeSet<>();

    static long query(int n){
        int l = 1, r = N;
        while(l <= r) {
            int m = l + (r - l) / 2;
            long cnt = cnt0.query(m, N) + cnt1.query(m, N);
            if (cnt > n) {
                l = m + 1;
            } else if (cnt < n) {
                r = m - 1;
            } else {
                return sum.query(m, N);
            }
        }
        return 0;
    }

    public static void main(String[] args) throws Exception {
        N = io.nextInt();
        P = new int[N][2];
        for(int i=0; i<N; i++){
            P[i][0] = io.nextInt();
            P[i][1] = io.nextInt();

            int k = Math.abs(P[i][1]);
            idxsList.add(k);
        }

        for(int k : idxsList){
            if(idxs.containsKey(k)) continue;
            idxs.put(k, idxs.size() + 1);
        }

        cnt0 = new BIT(N);
        cnt1 = new BIT(N);
        sum = new BIT(N);


        for(int i=0; i<N; i++){
            int t = P[i][0], d = P[i][1];
            int idx = idxs.get(Math.abs(d));
            if(d > 0){
                if(t == 0) {
                    cnt0.add(idx, 1);
                    sum.add(idx, d);
                }else{
                    cnt1.add(idx, 1);
                    sum.add(idx, d);
                }
            }else{
                if(t == 0){
                    cnt0.add(idx, -1);
                    sum.add(idx, d);
                }else{
                    cnt1.add(idx, -1);
                    sum.add(idx, d);
                }
            }

            long n1 = cnt1.sum(N);
            int tidx = 0;
            int l = 1, r = N;
            while(l <= r){
                int m = l + (r-l)/2;
                long cnt = cnt0.query(m, N) + cnt1.query(m, N);
                if(cnt > n1){
                    l = m + 1;
                }else if(cnt < n1){
                    r = m - 1;
                }else{
                    tidx = m;
                    break;
                }
            }

            long ans = 0;

            long c0 = cnt0.query(tidx, N), c1 = cnt1.query(tidx, N);
            long c = c0 + c1;
            long ct = cnt0.sum(N) + cnt1.sum(N);

            if(cnt1.sum(N) == 0){
                ans = sum.sum(N);
                io.println(ans);
                continue;
            }


            if(c1 == c){
                long sumAll = sum.sum(N);
                long sumDouble = query((int)c1 - 1);
                if(c1 < ct){
                    sumDouble += query((int)c1+1) - query((int)c1);
                }
                ans = sumDouble*2 + sumAll - sumDouble;

            }else{
                c1 = cnt1.sum(N);
                long sumAll = sum.sum(N);
                long sumDouble = query((int)c1);

                ans = sumDouble*2 + sumAll - sumDouble;
            }


            io.println(ans);
        }

        io.close();
    }

    static class BIT {
        long[] C;
        int N;
        public BIT(int n){
            C = new long[n + 1];
            N = n;
        }

        int lowbit(int a){
            return ((a ^ (a - 1)) + 1) >> 1;
        }

        void add(int idx, int a){
            while(idx <= N){
                C[idx] += a;
                idx += lowbit(idx);
            }
        }

        long sum(int idx){
            long ans = 0;
            while(idx > 0){
                ans += C[idx];
                idx -= lowbit(idx);
            }
            return ans;
        }

        long query(int l, int r){
            long ans = sum(r);
            if(l > 1){
                ans -= sum(l - 1);
            }
            return ans;
        }
    }

    static class FastIO {
        static BufferedReader br;
        static StringTokenizer st;
        static PrintStream ps = new PrintStream(System.out);

        public FastIO(String fname) {
            try {
                File input = new File(fname);
                if (input.exists()) {
                    System.setIn(new FileInputStream(fname));
                }
            }catch (Exception e){
                e.printStackTrace();
            }

            br = new BufferedReader(new
                    InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        void flush(){
            ps.flush();
        }

        void close(){
            ps.close();
        }

        void print(Object o){
            ps.print(o);
        }

        void println(Object o){
            ps.println(o);
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
