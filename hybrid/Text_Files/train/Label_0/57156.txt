
import java.util.*;
 
 
public class Main {
    public static void main(String[] args)  {
        Scanner in = new Scanner(System.in) ;
        int t = in.nextInt() ;
        while(t-->0){
                int n=in.nextInt();
                int m=in.nextInt();
                boolean flag=false;
                int[][] a=new int[n][m];
                int[][] b=new int[n][m];
                for(int i=0;i<n;i++){
                    for(int j=0;j<m;j++){
                    a[i][j]=in.nextInt();
                    if(i+1<n){
                        b[i][j]++;
                    }
                    if(i-1>=0){
                        b[i][j]++;
                    }
                     if(j+1<m){
                        b[i][j]++;
                    }
                    if(j-1>=0){
                        b[i][j]++;
                    }
                    if(b[i][j]<a[i][j])flag=true;
                    }
                }
                if(flag){
                   System.out.println("NO"); 
                }else{
                    System.out.println("YES");
                for(int i=0;i<n;i++){
                    for(int j=0;j<m;j++){
                    System.out.print(b[i][j]+" ");
                }
                System.out.println();}
                }
               }
	}
}