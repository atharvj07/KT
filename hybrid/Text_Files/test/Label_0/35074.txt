import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int K = scan.nextInt();
        long[] w = new long[N];
        long[] d = new long[N];
        for(int i=0;i<N;++i){
            w[i] = scan.nextLong();
            d[i] = scan.nextLong();
        }
        
        long left =0;
        long right = 2000000000000000000L;
        while(true){
            long X = (left+right)/2;
            long k = 0;
            for(int i=0;i<N;++i){
                if(X>=w[i])k += (X-w[i])/d[i] +1;
            }
            if(k >=K)right = X;
            else left = X;
            if(right-left == 1)break;
        }
        System.out.println(right);
    }
}