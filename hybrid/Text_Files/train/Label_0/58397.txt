
import java.io.*;
import java.util.*;
public class x
{
    public static void main(String args[])throws IOException
    {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String z[]=br.readLine().split(" ");
        int n=Integer.parseInt(z[0]);
        int m=Integer.parseInt(z[1]);
        String s1=br.readLine();
        String s2=br.readLine();
        int i;
        int diff=0;
        char[] ch=new char[n];
        for(i=0;i<n;i++)
        {
            ch[i]='A';
            if(s1.charAt(i)!=s2.charAt(i))
            {
                diff++;
            }
        }
        if(m<diff/2||m>n)
        {
            System.out.println(-1);
        }
        else if(m==diff/2&&diff%2!=0)
        {
            System.out.println(-1);
        }
        else
        {
            int simi=n-m;
            int count=0;
            for(i=0;i<n;i++)
            {
                if(count<simi&&s1.charAt(i)==s2.charAt(i))
                {
                    ch[i]=s1.charAt(i);
                    count++;
                }
            }
            int count1=0;
            int count2=0;
            for(i=0;i<n;i++)
            {
                if(s1.charAt(i)!=s2.charAt(i))
                {
                    if(count+count1<simi&&count1<=count2)
                    {
                        ch[i]=s1.charAt(i);
                        count1++;
                    }
                    else if(count+count2<simi&&count1>count2)
                    {
                        //System.out.println("yy "+s2.charAt(i));
                        ch[i]=s2.charAt(i);
                        count2++;
                    }
                }
            }
            for(i=0;i<n;i++)
            {
                if(ch[i]=='A')
                {
                    int x=97;
                    while(x==s1.charAt(i)||x==s2.charAt(i))
                    {
                        x++;
                    }
                    ch[i]=(char)(x);
                }
            }
            //System.out.println(Arrays.toString(ch));
            for(i=0;i<n;i++)
            {
                System.out.print(ch[i]);
            }
        }
    }
}