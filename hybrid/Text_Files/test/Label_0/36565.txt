import java.util.*;
import java.io.*;

public class Solve{
    public static void main(String[] args) throws Exception{
        Scanner sc=new Scanner(new InputStreamReader(System.in));;
        PrintWriter out=new PrintWriter(System.out);
        int n=sc.nextInt();
        int m=sc.nextInt();
        int[][] ar=new int[n][m];
        int ans=100000000;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
            ar[i][j]=sc.nextInt();
            }
        }
        int a=sc.nextInt()-1;
        int b=sc.nextInt()-1;
         for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
              if(i+a<n && j+b<m) { int cnt=0;
               for(int as=i;as<=i+a;as++){
                   for(int bs=j;bs<=b+j;bs++){
                       if(ar[as][bs]==1)cnt++;
                   }
               }
               ans=Math.min(ans,cnt);
            }
            }
        }
        int te=a;
        a=b;
        b=te;
          for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
              if(i+a<n && j+b<m) { int cnt=0;
               for(int as=i;as<=i+a;as++){
                   for(int bs=j;bs<=b+j;bs++){
                       if(ar[as][bs]==1)cnt++;
                   }
               }
               ans=Math.min(ans,cnt);
            }
            }
        }
        out.println(ans);
        
        out.close();
    }
}