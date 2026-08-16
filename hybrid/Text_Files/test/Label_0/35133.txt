import java.util.*;
import java.math.*;
import java.io.*;
public class Main {
    public static long time = 0;
    public static void main(String[] args) throws Exception {
        time = System.currentTimeMillis();
        
        IN = System.in;
        OUT = System.out;
        in = new BufferedReader(new InputStreamReader(IN));
        out = new PrintWriter(OUT, FLUSH);
        solveOne();
        out.flush();
    }
    
    public static void solveOne() throws Exception {
        int n = ni();
        int m = ni();
        int k = ni();
        int[] l1 = nil(n);
        
        if (n % 2 == 0){
            pn(0);
            return;
        }
        long singleNeed = m / ((n - 1) / 2 + 1);
        long maxTurn = k;
        maxTurn *= singleNeed;
        
        
        long tempMax = Long.MAX_VALUE;
        for (int i = 0 ; i < l1.length; i+= 2){
            tempMax = Math.min(tempMax, l1[i]);
        }
        
        
        
        
        int ans = Integer.MIN_VALUE;
        ans =(int) Math.min(tempMax, maxTurn);
        pn(ans);
    }
    
    public static void solveTwo() throws Exception {
        
    }
    
    public static void solveThree() throws Exception {
        
    }
    
    public static BufferedReader in;
    public static StringTokenizer st;
    public static InputStream IN;
    public static OutputStream OUT;
    public static String nx() throws Exception {
        for (;st == null || !st.hasMoreTokens();){
            String k1 = in.readLine();
            if (k1 == null) return null;
            st = new StringTokenizer(k1);
        }
        return st.nextToken();
    }
    public static int ni () throws Exception {
        return Integer.parseInt(nx());
    }
    public static long nl() throws Exception{
        return Long.parseLong(nx());
    }
    public static double nd() throws Exception{
        return Double.parseDouble(nx());
    }
    private static int[] nil(int n1) throws Exception {
        int[] l1 = new int[n1];
        for (int i = 0 ;i < n1; i++){
            l1[i] = ni();
        }
        return l1;
    }
    private static long[] nll(int n1) throws Exception {
        long[] l1 = new long[n1];
        for (int i = 0 ;i < n1; i++){
            l1[i] = nl();
        }
        return l1;
    }
    private static int[][] nill(int x, int y) throws Exception {
        int[][] l1 = new int[x][y];
        for (int i =0; i < x; i++){
            for (int j = 0; j < y; j++){
                l1[i][j] = ni();
            }
        }
        return l1;
    }
    public static void px(Object ... l1){
        System.out.println(Arrays.deepToString(l1));
    }
    public static boolean FLUSH = false;
    public static PrintWriter out;
    public static void p(Object ... l1){
        for (int i = 0; i < l1.length; i++){
            if (i != 0) out.print(' ');
            out.print(l1[i].toString());
        }
    }
    public static void pn(Object ... l1){
        for (int i = 0; i < l1.length; i++){
            if (i != 0) out.print(' ');
            out.print(l1[i].toString());
        }
        out.println();
    }
    
    public static void pn(Collection l1){
        boolean first = true;
        for (Object e: l1){
            if (first) first = false;
            else out.print(' ');
            out.print(e.toString());
        }
        out.println();
    }
    
    private static BigInteger bi(long n1){
        return BigInteger.valueOf(n1);
    }
    
    private static double usedTime(){
        return (System.currentTimeMillis()-time)*0.001;
    }
    
    
    
}