import java.io.*;
import java.util.*;

public class A1{
    
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int arr[] = new int[n];
        int a[] = new int[n];
        int ans=0;
        for(int i=0;i<n;i++){
            arr[i] = in.nextInt();
            ans+=arr[i]/10;
            if(arr[i]!=100){
                a[i] = (arr[i]/10 +1)*10 - arr[i];
            } 
            else{
                a[i]=11;
            }
        }
        Arrays.sort(a);
        for(int i=0;i<n;i++){
            if(a[i]!=11){
                if(k<a[i])
                    break;
                k-=a[i];
                arr[i]+=a[i];
                a[i]=10;
                ans++;
            }
        }
        if(k>0){
            ans+=k/10;
        }
        System.out.println(Math.min(n*10,ans));
    }
}