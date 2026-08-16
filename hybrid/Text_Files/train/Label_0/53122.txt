import java.util.Scanner;
public class diagonalWalking {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int q = sc.nextInt();
        long coords[][] = new long[q][2];
        long steps[] = new long[q];
        for (int i = 0; i < q; i++)
        {
            coords[i][0]=Math.abs(sc.nextLong());
            coords[i][1]=Math.abs(sc.nextLong());
            steps[i]=sc.nextLong();
        }
        for(int i = 0; i < q; i++)
        {
            long min=Math.min(coords[i][0],coords[i][1]);
            long max=Math.max(coords[i][0],coords[i][1]);
            if(steps[i]<max)
                System.out.println("-1");
            else
            {
                if((coords[i][0]+coords[i][1])%2==0)
                {
                    if((steps[i]-max)%2==0)
                        System.out.println(steps[i]);
                    else
                        System.out.println(steps[i]-2);
                }
                else
                    System.out.println(steps[i]-1);
            }
        }
    }
}
