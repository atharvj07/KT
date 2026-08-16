import java.util.*;

class Main
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();

        String ans = "No";

        if(A%2 == 1 && B % 2 == 1){
            ans = "Yes";
        }
        System.out.println(ans);
    }
}