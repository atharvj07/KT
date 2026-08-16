import java.util.*;
import java.io.*;
public class B1269{
    public static void main(String args[]) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int arr[] = PA(br.readLine().split(" "));
        int n = arr[0] ;
        int m = arr[1];
        int a[] = PA(br.readLine().split(" "));
        Arrays.sort(a);
        int b[] = PA(br.readLine().split(" "));
        Arrays.sort(b);
        int min=Integer.MAX_VALUE;
        for(int i=0;i<n;i++){
           for(int j=0;j<n;j++){
               int x = ((b[j]-a[i])%m+m)%m;
               if(isValid(x,a,b,i,j,m))
                min = Math.min(min,x);
           }
        }
        System.out.println(min);
    }
    
    private static boolean isValid(int x, int[] a, int[] b, int n, int m,int M) {
        for(int i=0;i<a.length;i++){
            int A = (a[(i+n)%a.length] + x)%M;
            int B = (b[(i+m)%a.length])%M;
            if(A!=B)
                return false;
        }
        return true;
    }

    static int PI(String s) {
        return Integer.parseInt(s);
    }
    static int[] PA(String temp[]){
        int arr[] =new int[temp.length];
        for(int i=0;i<arr.length;i++){
            arr[i] = PI(temp[i]);
        }
        return arr;
    }
}
