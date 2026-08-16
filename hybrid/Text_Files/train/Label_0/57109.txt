import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for(int i = 0; i < n; i++){
            a[i] = sc.nextInt();
        }
        boolean plus = true;
        int ans = 1;
        int prev = 0;
        boolean isFirst = true, isSecond = false, isZero = false;
        for(int i = 0; i < n; i++){
            if(isFirst){
                isFirst = false;
                isSecond = true;
            }else if(isSecond || isZero){
                isSecond = false;
                if(a[i-1] == a[i]){
                    isZero = true;
                }else{
                    isZero = false;
                    plus = a[i-1] < a[i] ? true : false;
                }
            }else if(plus && prev > a[i]){
                ans++;
                isSecond = true;
            }else if(!plus && prev < a[i]){
                ans++;
                isSecond = true;
            }
            prev = a[i];
        }
        System.out.println(ans);
    }
}
