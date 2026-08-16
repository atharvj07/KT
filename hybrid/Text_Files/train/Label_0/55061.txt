import java.util.*;
public final class Main{ 
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); 
        int n = sc.nextInt();
        long s=0;
        for(int i = 0; i <= n; i++){
            if(i%3!=0 && i%5!=0)
                s+=i;
        }
        System.out.print(s);
    }
}

