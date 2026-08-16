import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);

        int t = in.nextInt();
        for(int i = 0; i < t; i++)
        {

        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();
        int r = in.nextInt();

        int u1 = 0, u2 = 0;
        if(a<b)
        {
            if(c>=a && c<=b)
            {
                if(c-r > a) u1 = c-r-a; 
                if(c+r < b) u2 = b-c-r;
            }
            else if(c<a)
            {
                if(c+r>=a && c+r<b) u2 = b-c-r;
                else if(c+r <= a) u1 = b-a;
            }
            else if(c>b)
            {
                if(c-r<=b && c-r>a) u1 = c-r-a;
                else if(c-r >= b) u1 = b-a;
            }
            else u1 = b-a;
        }
        else if(a>b)
        {
            if(c>=b && c<=a)
            {
                if(c-r > b) u1 = c-r-b; 
                if(c+r < a) u2 = a-c-r;
            }
            else if(c<b)
            {
                if(c+r>=b && c+r<a) u2 = a-c-r;  
                else if(c+r <= b) u1 = a-b;
            }
            else if(c>a)
            {
                if(c-r<=a && c-r>b) u1 = c-r-b;
                else if(c-r >= a) u1 = a-b;
            }
            else u1 = a-b;
        }

        System.out.println(u1+u2);

        }
    }
}