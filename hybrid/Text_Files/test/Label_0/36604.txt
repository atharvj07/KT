// CODE PRODUCED UNDER ACE PRODUCTIONS 

import java.util.*;
public class Ace
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
       int m,s,i,j,k,d,p=0;
       m=sc.nextInt();
       s=sc.nextInt();
       int[] ar=new int[m];
       int[] br=new int[m];
       k=m*9;
    if(m==1&&s==0) System.out.print("0 0");
       else  if(s>0&&s<=k)
      {
          for(i=0;i<m;i++)
       {
         p=9;
         if(p<s)
         {
              ar[i]=p; br[i]=p;
             s=s-p;
         }
         else if(p>=s)
         {
             ar[i]=s; br[i]=s;
             s=0;
             break;
         }
       }
       
       if(br[m-1]==0)
       {
           for(i=m-1;i>=0;i--)
           {
               if(br[i]!=0)
               {br[m-1]++;
           br[i]--;
               break;
               }
           }
       }
       for(i=m-1;i>=0;i--)
          System.out.print(br[i]); 
       System.out.print(" ");
       for(i=0;i<m;i++)
           System.out.print(+ar[i]);
      }
      else System.out.print("-1 -1");
      
    }  
}