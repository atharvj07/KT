import java.util.*;
public class Solution
{
    public static void main(String args[])
    {
        Scanner s= new Scanner(System.in);
        int t=s.nextInt();
        int q=1;
        while(q<=t)
        {
            int n=s.nextInt();
            int[] a=new int[n];
            int[] b=new int[n];
            int prev=-1;
            int sorted=1;
            for(int i=0;i<n;i++)
            {
                a[i]=s.nextInt();
                if(a[i]<prev)
                    sorted=0;
                prev=a[i];
            }
            prev=s.nextInt();
            b[0]=prev;
            int flag=1;
            for(int i=1;i<n;i++)
            {
                b[i]=s.nextInt();
                if(b[i]!=prev)
                    flag=0;
            }

            if(sorted==1)
                System.out.println("Yes");
            else if(flag==0)
                System.out.println("Yes");
            else
                System.out.println("No");

            q++;
        }
    }
 } 