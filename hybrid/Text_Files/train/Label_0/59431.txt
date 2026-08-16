
import java.util.Scanner;

public class LuckyString {
    public static void main(String asd[])throws Exception
    {
        Scanner in=new Scanner(System.in);
        int n=in.nextInt();
        char ch[]=new char[n];
            for(int i=0;i<n;i+=4)
                ch[i]='a';
            char c='b';
            int m=n%4-1,k=n/4;
           //System.out.println(m+""+k);
            for(int i=0;i<4*k;i+=4)
            {
                c='b';
                for(int j=1;j<=3;j++)
                {
                    ch[i+j]=c;
                    c++;
                }
            }
           c='b';
           for(int i=1;i<=m;i++)
           {
               ch[4*k+i]=c;
               c++;
           }
           for(int i=0;i<n;i++)
               System.out.print(ch[i]);
        
    }
}
