import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        double a=sc.nextInt();
        double b=sc.nextInt();
        double p=sc.nextInt();
        double q=sc.nextInt();
        double r=sc.nextInt();
        if(a>b){
            System.out.println((b*p+q*(a-b))/(q+r)+b);
        }else{
            System.out.println((b*p-q*(b-a))/(q+r)+b);
        }
    }
    
}
