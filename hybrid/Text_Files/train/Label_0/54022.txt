import java.util.*;
import java.io.*;
import java.math.*;
public class codeforces
{
    public static void main(String args[])throws IOException
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int a=sc.nextInt();
        int b=sc.nextInt();
        ArrayList<Integer> hs=new ArrayList<Integer>();
        for(int i =1;i<=n;i++)
        hs.add(i);
        int round=0;
        while(true)
        {
            round++;
            ArrayList<Integer> hs1=new ArrayList<Integer>();
            Iterator iterator = hs.iterator(); 
            while (iterator.hasNext())
            {
                int a1=(Integer)iterator.next();
                int b1=(Integer)iterator.next();
                if((a1==a&&b1==b)||(a1==b&&b1==a))
                {
                    if((int)Math.pow(2,round)==n)
                    {
                        System.out.println("Final!");
                    }
                    else
                    System.out.println(round);
                    System.exit(0);
                }
                if(a1==a||a1==b)
                hs1.add(a1);
                else if(b1==a||b1==b)
                hs1.add(b1);
                else
                hs1.add(a1);
            }
            hs=hs1;
        }
    }
}