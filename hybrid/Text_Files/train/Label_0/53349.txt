

import java.awt.Point;
import java.io.*;
import java.math.BigInteger;
import java.util.*;

import static java.lang.Math.*;

public class C implements Runnable{
    
    final boolean ONLINE_JUDGE = System.getProperty("ONLINE_JUDGE") != null;
    
    BufferedReader in;
    PrintWriter out;
    StringTokenizer tok = new StringTokenizer("");
    
    void init() throws FileNotFoundException{
        if (ONLINE_JUDGE){
            in = new BufferedReader(new InputStreamReader(System.in));
            out = new PrintWriter(System.out);
        }else{
            in = new BufferedReader(new FileReader("input.txt"));
            out = new PrintWriter("output.txt");
        }
    }
    
    String readString() throws IOException{
        while(!tok.hasMoreTokens()){
            try{
                tok = new StringTokenizer(in.readLine());
            }catch (Exception e){
                return null;
            }
        }
        return tok.nextToken();
    }
    
    int readInt() throws IOException{
        return Integer.parseInt(readString());
    }
    
    long readLong() throws IOException{
        return Long.parseLong(readString());
    }
    
    double readDouble() throws IOException{
        return Double.parseDouble(readString());
    }
    
    public static void main(String[] args){
        new Thread(null, new C(), "", 256 * (1L << 20)).start();
    }
    
    long timeBegin, timeEnd;

    void time(){
        timeEnd = System.currentTimeMillis();
        System.err.println("Time = " + (timeEnd - timeBegin));
    }
    
    long memoryTotal, memoryFree;
    

    void memory(){
        memoryFree = Runtime.getRuntime().freeMemory();
        System.err.println("Memory = " + ((memoryTotal - memoryFree) >> 10) + " KB");
    }
    
    void debug(Object... objects){
        if (DEBUG){
            for (Object o: objects){
                System.err.println(o.toString());
            }
        }
    }
    
    public void run(){
        try{
            timeBegin = System.currentTimeMillis();
            memoryTotal = Runtime.getRuntime().freeMemory();
            init();
            solve();
            out.close();
            time();
            memory();
        }catch (Exception e){
            e.printStackTrace(System.err);
            System.exit(-1);
        }
    }
    
    boolean DEBUG = false;
    
    void solve() throws IOException{
        int n = readInt();
        int m = readInt();
        
        int[][] a = new int[n][m];
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                a[i][j] = readInt();
            }
        }
        
        int[][] sumI = new int[n][m];
        for (int i = 0; i < n; i++){
            sumI[i][0] = a[i][0];
            for (int j = 1; j < m; j++){
                sumI[i][j] = sumI[i][j-1] + a[i][j]; 
            }
        }
        
        int[][] sumJ = new int[n][m];
        for (int j = 0; j < m; j++){
            sumJ[0][j] = a[0][j];
            for (int i = 1; i < n; i++){
                sumJ[i][j] = sumJ[i-1][j] + a[i][j]; 
            }
        }
        
        int lim = max(n, m) / 2 + 1;
        int[][][] sum = new int[n][m][3];
        
        int max = Integer.MIN_VALUE;
        
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                sum[i][j][0] = sum[i][j][1] = Integer.MIN_VALUE;
                
                if (i < n - 2 && j < m - 2){
                    int up = sumI[i][j+2];
                    if (j > 0) up -= sumI[i][j-1];
                    
                    int right = sumJ[i+1][j+2];
                    right -= sumJ[i][j+2];
                    
                    int down = sumI[i+2][j+2];
                    if (j > 0) down -= sumI[i+2][j-1];
                    
                    sum[i][j][0] = up + right + down;
                }
                
                if (i < n - 4 && j < m - 4){
                    int up = sumI[i][j+4];
                    if (j > 0) up -= sumI[i][j-1];
                    
                    int right = sumJ[i+3][j+4];
                    right -= sumJ[i][j+4];
                    
                    int down = sumI[i+4][j+4];
                    if (j > 0) down -= sumI[i+4][j-1];
                    
                    int left = sumJ[i+3][j];
                    left -= sumJ[i+2][j];
                    
                    int up2 = sumI[i+2][j+2];
                    if (j > 0) up2 -= sumI[i+2][j-1];
                    
                    sum[i][j][1] = up + right + down + left + up2;
                }
                
                max = max(max, max(sum[i][j][0], sum[i][j][1]));
            }
        }
        
        for (int k = 2; k < lim; k++){
            for (int i = 0; i < n; i++){
                for (int j = 0; j < m; j++){
                    sum[i][j][2] = Integer.MIN_VALUE;
                    
                    int d = 2 * (k + 1);
                    if (i < n - d && j < m - d){
                        int up = sumI[i][j+d];
                        if (j > 0) up -= sumI[i][j-1];
                        
                        int right = sumJ[i+d-1][j+d];
                        right -= sumJ[i][j+d];
                        
                        int down = sumI[i+d][j+d];
                        if (j > 0) down -= sumI[i+d][j-1];
                        
                        int left = sumJ[i+d-1][j];
                        left -= sumJ[i+2][j];
                        
                        int up2 = sumI[i+2][j+1];
                        if (j > 0) up2 -= sumI[i+2][j-1];
                        
                        sum[i][j][2] = sum[i+2][j+2][0] + up + right + down + left + up2;
                    }
                    
                    max = max(max, sum[i][j][2]);
                    
                    sum[i][j][0] = sum[i][j][1];
                    sum[i][j][1] = sum[i][j][2];
                }
            }
        }
        
        out.print(max);
    }
}

