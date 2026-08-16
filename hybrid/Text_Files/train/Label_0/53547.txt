import java.io.*;
import java.util.*;
public class block
{
    public static void main(String args[])
    {
        Scanner in =new Scanner(System.in);
       // System.out.println("Enter");
        int n=in.nextInt();
        int l=in.nextInt();
        int k[]=new int[n];
        int s[]=new int[n];
        int i,j;
        k[0]=in.nextInt();
        int a=k[0],b,sum=0;
        for(i=1;i<n;i++)
       {
         b=in.nextInt();
         k[i]=b-a;
         a=b;
         sum=sum+k[i];
       }
        k[0]=l-sum;
        s[0]=in.nextInt();
        a=s[0];sum=0;
        for(i=1;i<n;i++)
       {
         b=in.nextInt();
         s[i]=b-a;
         a=b;
         sum=sum+s[i];
       }
        s[0]=l-sum;
        int x=0,g=0;
        for(i=0;i<n;i++)
        {
          for(j=0;j<n;j++)
          {
            if(s[i]==k[j])
            {
                
             a=i;
             b=j;
             l=0;
             while(s[a]==k[b])
             {
              a++;
              b++;
              l++;
              
              if(a==n)
              a=0;
              if(b==n)
              b=0;
              if(l==n)
              break;
             }
             if(l==n)
             {g=1;break;}
            }
          }
          if(g==1)break;
        }
        
        if(g==1)
        System.out.println("YES");
        else
        System.out.println("NO");
    }
}