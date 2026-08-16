import java.io.*;
import java.util.*;
 
public class Solution {
    
    static BufferedReader in;
    static StringTokenizer st;
 
    public static void test_cases() throws IOException{ 
        int n = readInt(), k = readInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i] = readInt();
        }
        Integer count[] = new Integer[k];
        int one = 0;
        for(int i=0;i<k;i++){
            count[i] = readInt()-1;
            if(count[i]==0){
                one++;
            }
        }
        if(n==k){
            long ans = 0;
            for(int i=0;i<n;i++)
            {
                ans+=(long)(arr[i]*2);
            }
            System.out.println(ans);
            return;
        }
        Arrays.sort(arr);
        Arrays.sort(count, Collections.reverseOrder());
        long ans = 0;
        for(int i=n-k;i<n;i++){
            ans+=(long)arr[i];
        }
        for(int i=n-one;i<n;i++){
            ans+=(long)arr[i];
        }
        int ind = 0;
        for(int i=0;i<k;i++){
            if(count[i]>0){
                ans+=(long)arr[ind];
                ind+=count[i];
            }
        }
        System.out.println(ans);
    }
 
    public static void main(String[] args) throws IOException {
        in = new BufferedReader(new InputStreamReader(System.in));
        //int  t = 1;
        int t = readInt();
        while(t-->0){
            test_cases();
        }
    }
 
    public static String next() throws IOException {
        while (st == null || !st.hasMoreTokens())
        st = new StringTokenizer(in.readLine().trim());
        return st.nextToken();
    }
 
    public static long readLong() throws IOException {
        return Long.parseLong(next());
    }
 
    public static int readInt() throws IOException {
        return Integer.parseInt(next());
    }
 
    public static double readDouble() throws IOException {
        return Double.parseDouble(next());
    }
    
    public static char readCharacter() throws IOException {
        return next().charAt(0);
    }
    
    public static String readLine() throws IOException {
        return in.readLine().trim();
    }
    
    public static String[] readLineArray() throws IOException{
        return readLine().split(" ");
    }
}