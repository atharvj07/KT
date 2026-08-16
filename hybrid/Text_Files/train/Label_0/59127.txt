import java.lang.*;
import java.util.*;
import java.io.*;

public class Main {
    void solve() {
        int t=ni();
        g=new ArrayList[10];
        for(int i=0;i<10;i++) g[i]=new ArrayList<>();
        out:while(t-->0){
            int n=ni();
            char s[]=ns().toCharArray();
            for(int i=0;i<10;i++) g[i].clear();
            for(int i=0;i<n;i++) g[s[i]-'0'].add(i);
            int ans[]=new int[n];
            int mx,mn;
           out2: for(int i=0;i<10;i++){
                if(check(0,i-1) && check(i+1,9)){
                    mx=-1; mn=n+1;
                    for(int j=0;j<n;j++){
                        if(s[j]-'0'<i){
                            mx=j;
                            ans[j]=1;
                        }else if(s[j]-'0'>i){
                            mn=Math.min(mn,j);
                            ans[j]=2;
                        }
                    }
                    for(int j=0;j<n;j++){
                        if(s[j]-'0'==i){
                            if(j>mx){
                                ans[j]=1;
                            }else if(j<mn)ans[j]=2;
                            else {
                                continue out2;
                            }
                        }
                    }
                    for(int j=0;j<n;j++) pw.print(ans[j]);
                    pw.println("");
                    continue out;

                }
            }
            pw.println("-");

        }
    }
    ArrayList<Integer> g[];
    boolean check(int x,int y){
        if(x>y) return true;
        int r=-1;
        for(int i=x;i<=y;i++){
            if(g[i].size()==0) continue;
            if(g[i].get(0)<=r) return false;
            r=g[i].get(g[i].size()-1);
        }

        return true;
    }

    long M = (long)1e9+7;
    // END
    PrintWriter pw;
    StringTokenizer st;
    BufferedReader br;

    void run() throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));
        pw = new PrintWriter(System.out);
        long s = System.currentTimeMillis();
        solve();
        pw.flush();
    }
    public static void main(String[] args) throws Exception {
        new Main().run();
    }

    String ns() {
        while (st == null || !st.hasMoreElements()) {

            try {
                st = new StringTokenizer(br.readLine());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return st.nextToken();
    }

    String nextLine() throws Exception {
        String str = "";
        try {
            str = br.readLine();
        } catch (IOException e) {
            throw new Exception(e.toString());
        }
        return str;
    }

    int ni() {
        return Integer.parseInt(ns());
    }

    long nl() {
        return Long.parseLong(ns());
    }

    double nd() {
        return Double.parseDouble(ns());
    }
}