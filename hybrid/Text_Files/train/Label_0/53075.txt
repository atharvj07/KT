import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {
    public static int serch(int[] a,int n){
        int k = 0;
        for(int i=0;i<n;i++){
            if(a[i]>k) return i+1;
            if(a[i]==k) k++;
        }
        return -1;
    }
    public static void main(String[] args) throws IOException {
        
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n+1];
        for(int i=0;i<n;i++) a[i] = sc.nextInt();
        int k  = serch(a,n);
        System.out.println(k);
    }
}










