import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int ans=0;

        int a=sc.nextInt();
        int b=sc.nextInt();
        int N=sc.nextInt();
        for (int i=0;i<N;++i)
        {
            int s=sc.nextInt();
            int f=sc.nextInt();

            if (s<=a && a<f) {ans=1; break;}
            if (s<b && b<=f) {ans=1; break;}
            if (a<=s && f<=b) {ans=1; break;}
        }

        System.out.println(ans);
    }
}

