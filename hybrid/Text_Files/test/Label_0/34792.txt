import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Codeforces {


    public  void solve() {
        FastScanner fs = new FastScanner();
        PrintWriter out = new PrintWriter(System.out);
        int n = fs.nextInt(), m = fs.nextInt(), s = fs.nextInt(), d = fs.nextInt();
        int[]ar = new int[n];
        for(int i=0;i<n;i++){
            ar[i] = fs.nextInt();
        }
        Arrays.sort(ar);
        int[]ans = new int[2*n+2];
        String imp = "IMPOSSIBLE";
        if(d == 1 || ar[0]-1 < s){
            out.println(imp);
        }else {
            int ind = 0;
            int jump = 0;
            boolean ok = true;
            ans[ind++] = ar[0] - 1;
            for (int i = 0; i < n - 1; i++) {
                if (ar[i + 1] - ar[i] - 2 >= s) {
                    if (jump + 2 <= d) {
                        ans[ind++] = jump + 2;
                        ans[ind++] = ar[i + 1] - ar[i] - 2;
                        jump = 0;
                    } else {
                        ok = false;
                        break;
                    }
                }else{
                    jump += ar[i+1]-ar[i];
                }
            }
            if(jump + 2 > d ){
                ok = false;
            }
            ans[ind++] = jump + 2;
            if(m - ar[n-1] > 1 )
                ans[ind++] = m - ar[n-1]-1;

            if(!ok)
                out.println(imp);
            else{
                for(int i=0;i<ind;i++){
                    if(i%2 ==0)
                        out.println("RUN "+ans[i]);
                    else out.println("JUMP "+ans[i]);
                }
            }
        }
        out.flush();

    }
    public static void main(String[]args){
        try{
            new Codeforces().solve();
        }catch (Exception e){
            e.printStackTrace();
        }

    }
    class FastScanner {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer("");
        String next() {
            while (!st.hasMoreTokens())
                try {
                    st=new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            return st.nextToken();
        }
        String nextLine()
        {
            String str = "";
            try
            {
                str = br.readLine();
            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
            return str;
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
        long nextLong() {
            return Long.parseLong(next());
        }
    }
    class Commands{
        String s;
        long len;
        Commands(String s,long len){
            this.s = s;
            this.len = len;
        }
    }
}