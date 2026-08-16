/**
 * Created by ckboss on 15-4-2.
 */

import java.util.*;
import java.math.*;

public class CF509D {

    int n,m;
    long[][] w;
    long[] a,b;

    long gcd(long a,long b){
        if(b==0) return a;
        return gcd(b,a%b);
    }

    CF509D(){
        Scanner in = new Scanner(System.in);
        n=in.nextInt(); m=in.nextInt();
        w=new long[n][m];
        a=new long[n];
        b=new long[m];
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++) {
                w[i][j] = in.nextLong();
            }
        for(int i=0;i<m;i++) b[i]=w[0][i];
        for(int i=1;i<n;i++) a[i]=w[i][0]-b[0];

        long g=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                long c = Math.abs(a[i]+b[j]-w[i][j]);
                g=gcd(g,c);
            }
        }

        if(g==0) g=10000000007L;
        boolean flag=true;
        for(int i=0;i<n&&flag;i++) {
            for(int j=0;j<m;j++){
                if(w[i][j]>=g){
                    flag=false; break;
                }
            }
        }
        if(flag==false){
            System.out.println("NO");
        }
        else{
            System.out.println("YES");
            System.out.println(g);
            for(int i=0;i<n;i++)
                System.out.printf("%d%c",(a[i]+g)%g,(i==n-1)?'\n':' ');
            for(int i=0;i<m;i++)
                System.out.printf("%d%c",(b[i]+g)%g,(i==m-1)?'\n':' ');
        }
    }

    public static void main(String[] args){
        new CF509D();
    }
}
