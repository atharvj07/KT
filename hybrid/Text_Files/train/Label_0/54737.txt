import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args){
        Scanner ir=new Scanner(System.in);
        for(;;){
            int n=ir.nextInt();
            int l=ir.nextInt();
            int r=ir.nextInt();
            if(n==0){
                return;
            }
            int[] a=new int[n];
            for(int i=0;i<n;i++){
                a[i]=ir.nextInt();
            }
            int ct=0;
            outer:
            for(int i=l;i<=r;i++){
                for(int j=0;j<n;j++){
                    if(i%a[j]==0){
                        if(j%2==0){
                            ct++;
                        }
                        continue outer;
                    }
                }
                if(n%2==0){
                    ct++;
                }
            }
            System.out.println(ct);
        }
    }
}
