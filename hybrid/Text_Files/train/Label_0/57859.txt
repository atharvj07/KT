import java.util.*;
public class Solution
{
    public static void main(String args[])
    {
        Scanner s= new Scanner(System.in);
        int t=s.nextInt();
        while(t>0)
        {
            int a=s.nextInt();
            int b=s.nextInt();
            int c=s.nextInt();
            int flag=0;
            if(a+b+1<c)
                flag=1;
            else if(b+c+1<a)
                flag=1;
            else if(a+c+1<b)
                flag=1;
            t--;
            if(flag==1)
                System.out.println("NO");
            else
                System.out.println("YES");
        }
    }
}