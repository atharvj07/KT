import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) {
        MyScanner sc = new MyScanner();
        out = new PrintWriter(new BufferedOutputStream(System.out));
        int m=sc.nextInt();
        int[]x=new int[m],y=new int[m];
        for(int i=0;i<m;++i){
            x[i]=sc.nextInt();
            y[i]=sc.nextInt();
        }
        int[]e=new int[1<<m];
        for(int i=0;i<1<<m;++i){
            if(Integer.bitCount(i)<4)continue;
            int max=0;
            for(int j=0;j<m;++j){
                if((i&1<<j)==0)continue;
                for(int k=0;k<m;++k){
                    if(j==k||(i&1<<k)==0)continue;
                    Map<Integer,Integer>hm=new HashMap<Integer,Integer>();
                    for(int l=0;l<m;++l){
                        if((i&1<<l)==0)continue;
                        int cl=x[l]*(y[k]-y[j])-y[l]*(x[k]-x[j]);
                        hm.put(cl,hm.getOrDefault(cl,0)+1);
                    }
                    int c=0;
                    for(Integer el:hm.values()){
                        if(el>=3)System.err.println("err hm="+hm);
                        if(el>=2)
                            c++;
                    }
                    max=Math.max(max,c);
                }
            }
            e[i]=max*(max-1)/2;
        }
        //System.err.println(Arrays.toString(e));
        int[]dp=new int[1<<m];
        for(int i=1;i<1<<m;++i){
            int b=i;
            int max=e[i];
            while(b>0){
                max=Math.max(max,dp[b]+e[b^i]);
                b=(b-1)&i;
            }
            dp[i]=max;
        }
        out.println(dp[(1<<m)-1]);
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