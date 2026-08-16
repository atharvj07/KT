import java.io.*;
import java.util.*;


class Main {
    static int n;
    static int[]p;
    static int a;
    static List<Integer>o;
    static void rot(int v){
        while(a!=v){
            o.add(1);
            a=(a+1)%n;
        }
    }
    static void sw(int v){
        rot(v+1);
        o.add(n-1);
    }
    public static void main(String[] args) {
        MyScanner sc = new MyScanner();
        out = new PrintWriter(new BufferedOutputStream(System.out));
        n=sc.nextInt();
        p=new int[n];
        for(int i=0;i<n;++i)p[i]=sc.nextInt();
        o=new ArrayList<Integer>();
        for(int i=0;i<n;++i)
            for(int j=0;j<n-i-1;++j)
                if(p[j]>p[j+1]){
                    sw(j);
                    int t=p[j];
                    p[j]=p[j+1];
                    p[j+1]=t;
                }
        rot(0);
        out.println(o.size());
        for(int oo:o)out.println(oo);
        out.close();
    }
    // http://codeforces.com/blog/entry/7018
    //-----------PrintWriter for faster output---------------------------------
    public static PrintWriter out;
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
        String nextLine(){
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
