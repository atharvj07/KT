import java.util.*;

public class Main{
    Scanner in = new Scanner(System.in);

    void solve(){
        int a[] = new int[3];
        for(int i = 0; i < 3; i++){
            a[i] = in.nextInt();
        }

        while(a[0] + a[1] + a[2] > 0){
            int n = in.nextInt();
            int[] r = new int[n];
            for(int i = 0; i < n; i++){
                r[i] = in.nextInt();
            }
            Arrays.sort(a);
            for(int i : r){
                if(Math.sqrt(a[0] * a[0] + a[1] * a[1]) < i * 2){
                    System.out.println("OK");
                }else{
                    System.out.println("NA");
                }
            }
            for(int i = 0; i < 3; i++){
                a[i] = in.nextInt();
            }
        }
    }
    
    public static void main(String[] args){
        new Main().solve();    
    }
}