import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        //値の取得
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        long T = sc.nextLong();
        long[] t = new long[N];
        for (int i = 0; i < N; ++i){
            t[i] = sc.nextLong();
        }
        
        long X = 0; //総和
        
        for (int i = 0; i < N-1; ++i){
            X += Math.min(T,t[i+1]-t[i]);   //t[i+1]-t[i]：次の人が来るまでの時間
        }
        
        X += T; //最後にTを加える
        
        System.out.println(X);
        
    }
}
