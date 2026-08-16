import java.io.*;
import java.util.*;
import java.util.Arrays.*;
public class PrimeSquare
{
    public static void main(String[] args) throws IOException
    {
        Scanner in=new Scanner(System.in);
        PrintWriter out=new PrintWriter(System.out);
        int t=in.nextInt();
        while(t-->0)
        {
            int te=0;
            int n=in.nextInt();
            int arr[][]=new int [n][n];
         if(n%2==0)
        {
            for(int i=0;i<n;i++)
            {
                for(int j=0;j<n;j++)
                {
                    if(i==j || j==n-i-1)
                    arr[i][j]=1;
                    else
                    arr[i][j]=0;
                }
            }
        }
       else 
        {
            for(int i=0;i<n;i++)
            {
                //if(i==((n+1)/2)-1)
                
                //arr[i][0]=1;
                
                for(int j=0;j<n;j++)
                {
                    
                    if(i==j || j==n-i-1)
                    arr[i][j]=1;
                    else
                    arr[i][j]=0;
                }
            }
             te=((n+1)/2)-1;
            arr[n-1][te]=1;
            arr[te][0]=1;
        }
            for(int i=0;i<n;i++)
            {
                for(int j=0;j<n;j++)
                {
                    out.print(arr[i][j]+" ");
                }
                out.println();
            }
        }

        out.close();
    }
    
}
