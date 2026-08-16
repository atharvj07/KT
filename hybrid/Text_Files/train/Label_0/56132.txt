import java.io.*;
import java.util.*;
import static java.util.Collections.*;
import static java.lang.Math.*;
import java.util.stream.*;
import static java.util.Arrays.*;

@SuppressWarnings("unchecked")
public class B_Dima_and_a_Bad_XOR {
    public static PrintWriter out;
    public static InputReader in;
    public static long MOD = (long)1e9+7;

    public static void main(String[] args)throws IOException {
        in = new InputReader(System.in);
        out = new PrintWriter(System.out);
        
        int cases = 1;
        
        for(int t = 0; t < cases; t++){
            int n = in.nextInt();
            int m = in.nextInt();
            int[][] arr = new int[n][m];
            for(int i=0;i<n;i++){
                for(int j=0;j<m;j++){
                    arr[i][j] = in.nextInt();
                }
            }
            boolean don = false;
            for(int bit = 0; bit<=11;bit++){
                int pres0[] = new int[n];
                int pres1[] = new int[n];
                Arrays.fill(pres0,-1); fill(pres1,-1);
                int v = 1<<bit;
                for(int r=0;r<n;r++){
                    for(int c=0;c<m;c++){
                        if((arr[r][c]&v)!=0) pres1[r]=c;
                        else pres0[r]=c;
                    }
                }
                // out.println("ye:"+pres0[1]+" "+pres1[1]);
                int ct = 0;
                for(int r=0;r<n;r++)
                    if(pres1[r]!=-1) ct++;
                if(ct==0) continue;
                if(ct%2==0) ct--;
                // out.println("bit:"+bit);
                // out.println("ct:"+ct);

                int ans[] = new int[n];
                for(int r=0;r<n;r++){
                    if(pres0[r]!=-1 && pres1[r]!=-1) continue;
                    // out.println("lulr="+r);
                    if(pres1[r]!=-1) ct--;
                    ans[r]=0;
                }
                if(ct<0) {continue;}
                don = true;
                // out.println(ct);
                for(int r=0;r<n;r++){
                    if(pres0[r]!=-1 && pres1[r]!=-1){
                        // out.println("yahar="+r);
                        if(ct>0){
                            ans[r] = pres1[r];
                            ct--;
                        }
                        else{
                            ans[r] = pres0[r];
                            // out.println("r"+r+" "+pres0[r]);
                        }

                    }
                }
                out.println("TAK");
                for(int i=0;i<ans.length;i++){
                    out.print((ans[i]+1)+" ");
                }
                out.println();
                break;
            }
            if(!don) out.println("NIE");
        }

        out.close();
    }
    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

        public int[] nextArrI(int n) {
            int[] a=new int[n];
            for(int i=0; i<n; i++) a[i]=nextInt();
            return a;
        }
        
        public long[] nextArrL(int n) {
            long[] a=new long[n];
            for (int i=0; i<n; i++) a[i]=nextLong();
            return a;
        }
    }

}