import java.util.Scanner;

/**
 * Created by zephyr on 5/30/14.
 */
public class GIft {
    public static void main(String args[]){
        System.out.println(gift());
    }

    public static String gift(){
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        int x100 = 0;
        int x200 = 0;
        while(number-- > 0){
        if (scanner.nextInt() == 100){
            x100 ++;
        }else{
            x200 ++;
        }
        }
        if (x100 % 2 != 0){
            return "NO";
        }else if(x200 % 2 == 0){
            return "YES";
        }else{
            if (x100 < 2){
                return "NO";
            }else{
                return "YES";
            }
        }
    }
}
