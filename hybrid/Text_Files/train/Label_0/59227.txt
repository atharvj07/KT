import java.util.*;
import java.math.*;
import java.io.*;

public class Main
{
    static int point[]=new int[1010];
    static int n;
    static boolean  judge(double x){
    int flag=0;
    int po=-1;
    for(int i=2;i<=n;i++){
        //斜率公式：（y2-y1）=k*(x2-x1)
        if(point[i]-point[1]==x*(i-1)) continue;
        flag=1;
        if(po<0) po=i;
        else if(point[i]-point[po]!=x*(i-po)){
            flag=0;
            break;
        }
    }
    if(flag!=0) return true;
    else return false;
}

    public static void main(String[] args) throws IOException
    {
        StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
      // Scanner sc= new Scanner(System.in);
        FastScanner sc=new FastScanner();
        n=sc.nextInt();
        for(int i=1;i<=n;i++) point[i]=sc.nextInt();
        if(judge((point[2]-point[1])*1.0)||judge((point[3]-point[1])*0.5)||judge(point[3]-point[2]*1.0)){
            out.print("Yes");
        }
        else   out.print("No");
        out.flush();
    }
    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        public FastScanner() {
            try	{
                br = new BufferedReader(new InputStreamReader(System.in));
                st = new StringTokenizer(br.readLine());
            } catch (Exception e){e.printStackTrace();}
        }

        public String next() {
            if (st.hasMoreTokens())	return st.nextToken();
            try {st = new StringTokenizer(br.readLine());}
            catch (Exception e) {e.printStackTrace();}
            return st.nextToken();
        }

        public int nextInt() {return Integer.parseInt(next());}

        public long nextLong() {return Long.parseLong(next());}

        public double nextDouble() {return Double.parseDouble(next());}

        public String nextLine() {
            String line = "";
            if(st.hasMoreTokens()) line = st.nextToken();
            else try {return br.readLine();}catch(IOException e){e.printStackTrace();}
            while(st.hasMoreTokens()) line += " "+st.nextToken();
            return line;
        }

        public int[] nextIntArray(int n) {
            int[] a = new int[n];
            for(int i = 0; i < n; i++) a[i] = nextInt();
            return a;
        }

        public long[] nextLongArray(int n){
            long[] a = new long[n];
            for(int i = 0; i < n; i++) a[i] = nextLong();
            return a;
        }

        public double[] nextDoubleArray(int n){
            double[] a = new double[n];
            for(int i = 0; i < n; i++) a[i] = nextDouble();
            return a;
        }

        public char[][] nextGrid(int n, int m){
            char[][] grid = new char[n][m];
            for(int i = 0; i < n; i++) grid[i] = next().toCharArray();
            return grid;
        }
    }



}