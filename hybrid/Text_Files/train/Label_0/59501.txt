import java.io.*;
import java.util.ArrayList;


public class Main
{
   
    public static void main (String[] args) throws IOException
    {
        BufferedReader in =new BufferedReader (new InputStreamReader(System.in));
        
        String A1[]=in.readLine().split(" ");
        
        ArrayList A=new ArrayList();
        
        int counter = 0 ;
        
        int n=Integer.parseInt(A1[0]),m=Integer.parseInt(A1[1]);
        
        boolean vis[]=new boolean [n+1];
        
        
          for (int i=0;i<=n;i++)
           vis[i]=true;
       
       vis[0]=vis[1]=false;
      
       for (int i=2;i<=n;i++)
       {
           
           if (vis[i])
           {
     for (int j=i*i ; j <=n; j+=i)
         vis[j]=false;
     A.add(i);
           
           }
       }
      
       
 
       for (int i=0;i<A.size();i++)
       {
           for (int j=0;j<A.size()-1;j++)
               if ((int)A.get(i)==((int)A.get(j)+(int)A.get(j+1))+1)
               counter++;
           
       }
        if (counter >= m)System.out.println("YES");
        else
            System.out.println("NO");
        
     
    }



}