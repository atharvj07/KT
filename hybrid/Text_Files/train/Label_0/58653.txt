import java.util.Scanner;
public class TwoRegular{
    public static  void main(String args[]){
        int t;
        Scanner sc = new Scanner(System.in);
        t = sc.nextInt();
        for(int i = 0;i < t;i++){
            int m,n;
            n = sc.nextInt();
            m = sc.nextInt();
            if(n >= 3 && m >= 3 && n % m == 0){
                System.out.println("YES");
            }else{
                System.out.println("NO");
            }
        }
    }
}