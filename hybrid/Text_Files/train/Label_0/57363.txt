import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        while(true)
        {
            String str = sc.next();
            if(str.equals("-"))
                break;
            int n = sc.nextInt();
            for(int i = 0 ; i < n ; i++)
            {
                int h = sc.nextInt();
                String a = str.substring(0,h);
                String b = str.substring(h);
                str = b + a;
            }
            System.out.println(str);
        }
    }
}
