/**
 * BaZ :D
 */
import java.lang.reflect.Array;
import java.util.*;
import java.io.*;
import static java.lang.Math.*;

public class Main
{
    static MyScanner scan;
    static PrintWriter pw;
    static long MOD = 1_000_000_007;
    static long INF = 1_000_000_000_000_000_000L;
    static long inf = 2_000_000_000;
    public static void main(String[] args) {
        new Thread(null, null, "BaZ", 1 << 27) {
            public void run() {
                try {
                    solve();
                } catch (Exception e) {
                    e.printStackTrace();
                    System.exit(1);
                }
            }
        }.start();
    }

    static void solve() throws IOException
    {
        //initIo(true);
        initIo(false);
        StringBuilder sb = new StringBuilder();
        int t = ni();
        while(t-->0) {
            int n = ni();
            String a = ne(), b = ne();
            int freq_a[] = new int[26];
            int freq_b[] = new int[26];
            for(int i=0;i<n;++i) {
                ++freq_a[a.charAt(i) - 'a'];
                ++freq_b[b.charAt(i) - 'a'];
            }
            boolean can = true;
            int cnt_g_1 = 0;
            for(int i=0;i<26;++i) {
                if(freq_a[i] != freq_b[i]) {
                    can = false;
                    break;
                }
                if(freq_a[i] > 1) {
                    cnt_g_1++;
                }
            }
            if(can) {
                StringBuilder first = new StringBuilder();
                StringBuilder second = new StringBuilder();
                for(int i=0;i<n;++i) {
                    if(freq_a[a.charAt(i) - 'a'] == 1) {
                        first.append(a.charAt(i));
                    }
                    if(freq_b[b.charAt(i) - 'a'] == 1) {
                        second.append(b.charAt(i));
                    }
                }
                if(cnt_g_1>0) {
                    pl("YES");
                }
                else {
                    int swaps = calc(first.toString(), second.toString());
                    if(swaps%2==0) {
                        pl("YES");
                    }
                    else {
                        pl("NO");
                    }
                }
            }
            else {
                pl("NO");
            }
        }
        pw.flush();
        pw.close();
    }
    static int calc(String a, String b) {
        if(a.length() == 0) {
            return 0;
        }
        char c = b.charAt(0);
        int cnt = 0;
        int i;
        for(i=0;i<a.length();++i) {
            if(a.charAt(i) == c) {
                break;
            }
            ++cnt;
        }
        String now = "";
        for(int j=0;j<a.length();++j) {
            if(j==i) {
                continue;
            }
            now+=a.charAt(j);
        }
        return cnt + calc(now , b.substring(1));
    }
    static void initIo(boolean isFileIO) throws IOException {
        scan = new MyScanner(isFileIO);
        if(isFileIO) {
            pw = new PrintWriter("/Users/amandeep/Desktop/output.txt");
        }
        else {
            pw = new PrintWriter(System.out, true);
        }
    }
    static int ni() throws IOException
    {
        return scan.nextInt();
    }
    static long nl() throws IOException
    {
        return scan.nextLong();
    }
    static double nd() throws IOException
    {
        return scan.nextDouble();
    }
    static String ne() throws IOException
    {
        return scan.next();
    }
    static String nel() throws IOException
    {
        return scan.nextLine();
    }
    static void pl()
    {
        pw.println();
    }
    static void p(Object o)
    {
        pw.print(o+" ");
    }
    static void pl(Object o)
    {
        pw.println(o);
    }
    static void psb(StringBuilder sb)
    {
        pw.print(sb);
    }
    static void pa(String arrayName, Object arr[])
    {
        pl(arrayName+" : ");
        for(Object o : arr)
            p(o);
        pl();
    }
    static void pa(String arrayName, int arr[])
    {
        pl(arrayName+" : ");
        for(int o : arr)
            p(o);
        pl();
    }
    static void pa(String arrayName, long arr[])
    {
        pl(arrayName+" : ");
        for(long o : arr)
            p(o);
        pl();
    }
    static void pa(String arrayName, double arr[])
    {
        pl(arrayName+" : ");
        for(double o : arr)
            p(o);
        pl();
    }
    static void pa(String arrayName, char arr[])
    {
        pl(arrayName+" : ");
        for(char o : arr)
            p(o);
        pl();
    }
    static void pa(String listName, List list)
    {
        pl(listName+" : ");
        for(Object o : list)
            p(o);
        pl();
    }
    static void pa(String arrayName, Object[][] arr) {
        pl(arrayName+" : ");
        for(int i=0;i<arr.length;++i) {
            for(Object o : arr[i])
                p(o);
            pl();
        }
    }
    static void pa(String arrayName, int[][] arr) {
        pl(arrayName+" : ");
        for(int i=0;i<arr.length;++i) {
            for(int o : arr[i])
                p(o);
            pl();
        }
    }
    static void pa(String arrayName, long[][] arr) {
        pl(arrayName+" : ");
        for(int i=0;i<arr.length;++i) {
            for(long o : arr[i])
                p(o);
            pl();
        }
    }
    static void pa(String arrayName, char[][] arr) {
        pl(arrayName+" : ");
        for(int i=0;i<arr.length;++i) {
            for(char o : arr[i])
                p(o);
            pl();
        }
    }
    static void pa(String arrayName, double[][] arr) {
        pl(arrayName+" : ");
        for(int i=0;i<arr.length;++i) {
            for(double o : arr[i])
                p(o);
            pl();
        }
    }
    static class MyScanner
    {
        BufferedReader br;
        StringTokenizer st;
        MyScanner(boolean readingFromFile) throws IOException
        {
            if(readingFromFile) {
                br = new BufferedReader(new FileReader("/Users/amandeep/Desktop/input.txt"));
            }
            else {
                br = new BufferedReader(new InputStreamReader(System.in));
            }
        }
        String nextLine()throws IOException
        {
            return br.readLine();
        }
        String next() throws IOException
        {
            if(st==null || !st.hasMoreTokens())
                st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }
        int nextInt() throws IOException
        {
            return Integer.parseInt(next());
        }
        long nextLong() throws IOException
        {
            return Long.parseLong(next());
        }
        double nextDouble() throws IOException
        {
            return Double.parseDouble(next());
        }
    }
}