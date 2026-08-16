import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Barcode {
    static class Solver {
        int n, m, x, y;
        int[] arr;
        int[][][] mem;

        public void solve(MyReader in, PrintWriter out) {
            n = in.nextInt();
            m = in.nextInt();
            x = in.nextInt();
            y = in.nextInt();

            arr = new int[m];
            char[][] img = new char[n][m];


            for (int i = 0; i < n; i++) {
                img[i] = in.next().toCharArray();
            }

            for (int i = 0; i < m; i++) {
                int cnt = 0;
                for (int j = 0; j < n; j++) {
                    if (img[j][i] == '#') cnt++;
                }
                arr[i] = cnt;
            }

            mem = new int[1001][1001][2];
            for (var mm : mem)for(var m:mm) Arrays.fill(m, -1);

            int ans = Math.min(helper(0, 0,0), helper(0,0,1));
            out.println(ans);

        }

        int INF = (int) 1e9;

        int helper(int l, int prevLines , int wb){
            if (prevLines+m-l < x) return INF;
            if (l == m )return 0;

//            if (prevLines+n-l < x-1)return INF;

            if (mem[l][prevLines][wb] != -1)return mem[l][prevLines][wb];
            int ans = INF;

            //is white
            if (wb == 0){
                int ca = helper(l+1,prevLines+1,0) + arr[l];
                int cb = helper(l+1,1,1 ) + n - arr[l];
                if (prevLines < x){
                    ans = ca;
                }
                else if(prevLines == y){
                    ans = cb;
                }
                else{
                    ans = Math.min(ca,cb);
                }
            }
            else{
                //is black
                int ca = helper(l+1,prevLines + 1,1) + n - arr[l];
                int cb = helper(l+1,1,0) + arr[l];
                if (prevLines < x){
                    ans = ca;
                }
                else if (prevLines == y){
                    ans = cb;
                }
                else{
                    ans = Math.min(ca,cb);
                }
            }

            mem[l][prevLines][wb] = ans;
            return ans;
        }



    }

    public static void main(String[] args) {
        MyReader mr = new MyReader();
        PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
        new Solver().solve(mr, out);
        out.close();
    }

    //    static int[][] dir = {{0,1}, {1,0},{-1,0}, {0,-1}};
//    static int[][] dir = {{0,1}, {1,0},{-1,0}, {0,-1}, {-1,-1},{-1,1}, {1,1}, {1,-1}};
    static class MyReader {
        BufferedReader br;
        StringTokenizer st;

        MyReader() {
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

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String res = "";
            try {
                res = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }

            return res;
        }

        int[] nextIntArray(int n) {
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = nextInt();
            }

            return arr;
        }

        Integer[] nextIntegerArray(int n) {
            Integer[] arr = new Integer[n];
            for (int i = 0; i < n; i++) {
                arr[i] = nextInt();
            }

            return arr;
        }

        Long[] nextLongArray(int n) {
            Long[] arr = new Long[n];
            for (int i = 0; i < n; i++) {
                arr[i] = nextLong();
            }

            return arr;
        }

        String[] nextStringArray(int n) {
            String[] arr = new String[n];
            for (int i = 0; i < n; i++) {
                arr[i] = next();
            }
            return arr;
        }
    }

    static void swap(int[] arr, int i, int j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

}


