import java.util.Scanner;

public class BuyingTorches
{
    static Scanner sc = new Scanner (System.in);
    public static void main(String[] args)
    {
        int t = sc.nextInt();
        while(t-->0)
        {
            solve();
        }
    }
    protected  static void solve()
    {
        long x,y,k;
        x = sc.nextLong();
        y = sc.nextLong();
        k = sc.nextLong();
        long totalStick = x  + (k * (y+1)) - 3;

//        this will count no of trade to get the desired total stick
        long noOfTrade = (long)(totalStick/(x-1));

        long totalNoofTrade = noOfTrade + k;
        System.out.println(totalNoofTrade);


    }
}
