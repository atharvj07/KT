import java.util.*;
import java.io.*;

public class _110 {
    public static void main(String[] args) {
        MyScanner sc = new MyScanner();
        PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
        int t = 1;
        while (t-- > 0) {
            int k = sc.nextInt();
            String s = sc.next();
            int n = (1 << k) + (1 << k) - 1;
            int [] a = new int[n + 1];
            Arrays.fill(a, -1);
            int len = s.length();
            int ptr = 1;
            for (int i = len - 1; i >= 0; i--) {
                int put;
                if (s.charAt(i) == '?') put = -1;
                else put = s.charAt(i) - '0';
                a[ptr] = put;
                ptr++;
            }
            int [] b = new int[n + 1];
            for (int i = n; i >= 1; i--) {
                int left = 2 * i + 1;
                int right = 2 * i;
                if (left > n || right > n) {
                    b[i] = 1;
                } else {
                    if (a[i] == -1) b[i] = b[left] + b[right];
                    else if (a[i] == 0) {
                        b[i] = b[left];
                    } else {
                        b[i] = b[right];
                    }
                }
            }
            int q = sc.nextInt();
            for (int i = 0; i < q; i++) {
                int change = len + 1 - sc.nextInt();
                String c = sc.next();
                int to;
                if (c.charAt(0) == '?') to = -1;
                else to = c.charAt(0) - '0';
                int left = b[2 * change + 1];
                int right = b[2 * change];
                if (to == -1) b[change] = left + right;
                else if (to == 0) b[change] = left;
                else b[change] = right;
                a[change] = to;
                change /= 2;
                while (change > 0) {
                    int l = 2 * change + 1;
                    int r = 2 * change;
                    if (a[change] == -1) b[change] = b[l] + b[r];
                    else if (a[change] == 0) {
                        b[change] = b[l];
                    } else {
                        b[change] = b[r];
                    }
                    change /= 2;
                }
                out.println(b[1]);
            }
        }
        out.close();
    }




    static void sort(int[] a) {
        ArrayList<Integer> q = new ArrayList<>();
        for (int i : a) q.add(i);
        Collections.sort(q);
        for (int i = 0; i < a.length; i++) a[i] = q.get(i);
    }

    static void sort(long[] a) {
        ArrayList<Long> q = new ArrayList<>();
        for (long i : a) q.add(i);
        Collections.sort(q);
        for (int i = 0; i < a.length; i++) a[i] = q.get(i);
    }


    //-----------MyScanner class for faster input----------
    public static class MyScanner {
        BufferedReader br;
        StringTokenizer st;

        public MyScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
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