import java.util.*;
import java.io.*;
public class MagicBox {
    
    
    
    /************************ SOLUTION STARTS HERE ************************/
    
    static final double EPS = 1e-8;
    
    static int compare(double a , double b) {
        if(a <= b - EPS)
            return -1;
        else if(a >= b + EPS)
            return 1;
        else
            return 0;
    }
    
    static class Plane {
        double pt[];
        int fixed;  // This coordinate is constant for this particular plane
        double boundry[];
        Plane(double p[] , double b[] , int f) {
            pt = p;
            boundry = b;
            fixed = f;
        }
        boolean parallel(double line[][]) {
            return line[0][fixed] == 0;
        }
        boolean intersect(double line[][]) {   // line[0] = direction vector   line[1] = point in line
            double lambda = (double)(boundry[fixed] - line[1][fixed]) / line[0][fixed];   
            double intersect[] = new double[3];
            for(int i = 0; i < 3; i++)
                intersect[i] = lambda * line[0][i] + line[1][i];
            
            boolean flag = true;
            // System.out.println("intersection " + Arrays.toString(intersect));
            
            for(int i = 0; i < 3; i++) {
                if(i == fixed)
                    flag &= compare(intersect[i] , boundry[fixed]) == 0;
                else
                    flag &= compare(intersect[i] , 0.0) >= 0 && compare(intersect[i] , boundry[i]) <= 0;
            }
            
            return flag;
        }
        
        double distSq(double line[][]) {
            double lambda = (double)(boundry[fixed] - line[1][fixed]) / line[0][fixed];   
            double intersect[] = new double[3];
            double dSq = 0;
            for(int i = 0; i < 3; i++) {
                intersect[i] = lambda * line[0][i] + line[1][i];
                dSq += Math.pow(intersect[i] - line[1][i], 2);
            }
            
            return dSq;
        }
         
    }
    
    private static void solve() {
        
        double curr[] = new double[3];
        for(int i = 0; i < 3; i++) curr[i] = nextDouble();
        
        double box[] = new double[3];
        for(int i = 0; i < 3; i++) box[i] = nextDouble();
        
        int A[] = nextIntArray(6);
        int perm[] = {1 ,2 ,0};
        int score = 0;
        
        Plane planes[] = new Plane[6];
        for(int i = 0; i < 6; i++) {
            double pt[] = new double[3];
            double b[] = new double[3];
            for(int j = 0; j < 3; j++) {
                if(j != perm[i / 2]) {
                    pt[j] = box[j] / 2.0;
                    b[j] = box[j];
                }
                else if(i % 2 == 1)
                    pt[j] = b[j] = box[j];
            }
            planes[i] = new Plane(pt, b, perm[i / 2]);
        }
        
        double payload[][] = new double[2][];
        
        for(int i = 0; i < 6; i++) {
            boolean flag = true;
            double dir[] = new double[3];
            for(int j = 0; j < 3; j++)
                dir[j] = curr[j] - planes[i].pt[j];
            
            payload[0] = dir;
            payload[1] = curr;
            if(!planes[i].parallel(payload)) {
                double thresh = planes[i].distSq(payload);
                for(int j = 0; j < 6; j++)
                    if(i != j && !planes[j].parallel(payload) && planes[j].intersect(payload)) 
                        flag &= compare(planes[j].distSq(payload), thresh) >= 0;
                        
                score += flag ? A[i] : 0;
            }
        }
        
        println(score);
    }
    
    
    
    /************************ SOLUTION ENDS HERE ************************/
    
    
    
    
    
    /************************ TEMPLATE STARTS HERE **********************/
    
    public static void main(String[] args) throws IOException {
        reader = new BufferedReader(new InputStreamReader(System.in));
        writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)), false);
        st     = null;
        solve();
        reader.close();
        writer.close();
    }
    
    static BufferedReader reader;
    static PrintWriter    writer;
    static StringTokenizer st;
    
    static String next()
    {while(st == null || !st.hasMoreTokens()){try{String line = reader.readLine();if(line == null){return null;}            
    st = new StringTokenizer(line);}catch (Exception e){throw new RuntimeException();}}return st.nextToken();}
    static String nextLine()  {String s=null;try{s=reader.readLine();}catch(IOException e){e.printStackTrace();}return s;}             
    static int    nextInt()   {return Integer.parseInt(next());}
    static long   nextLong()  {return Long.parseLong(next());}     
    static double nextDouble(){return Double.parseDouble(next());}
    static char   nextChar()  {return next().charAt(0);}
    static int[]  nextIntArray(int n)         {int[] a= new int[n];   int i=0;while(i<n){a[i++]=nextInt();}  return a;}
    static long[] nextLongArray(int n)        {long[]a= new long[n];  int i=0;while(i<n){a[i++]=nextLong();} return a;}    
    static int[]  nextIntArrayOneBased(int n) {int[] a= new int[n+1]; int i=1;while(i<=n){a[i++]=nextInt();} return a;}            
    static long[] nextLongArrayOneBased(int n){long[]a= new long[n+1];int i=1;while(i<=n){a[i++]=nextLong();}return a;}            
    static void   print(Object o)  { writer.print(o);  }
    static void   println(Object o){ writer.println(o);}
    
    /************************ TEMPLATE ENDS HERE ************************/
    
}