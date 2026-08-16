import java.util.*;
class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        long X = sc.nextLong();
        HashMap<Integer, Long> map = new HashMap<Integer, Long>();
        long Nlen = 5;
        map.put(1, Nlen);
        for(int i = 2; i <= N; i++) {
            Nlen = Nlen*2 + 3;
            map.put(i, Nlen);
        }

        long tabeta = havePatty(N,X,map);
        System.out.println(tabeta);
    }

    public static long havePatty(int N, long X, HashMap<Integer, Long> map) {
        if(X <= 1) return 0;
        if(N == 1) {
            if(X == 1) return 0;
            else if(X == 2) return 1;
            else if(X == 3) return 2;
            else if(X == 4 || X == 5) return 3;
        }
        //n>1
        long Nlen = map.get(N);
        long l = map.get(N-1);
        if(X == Nlen) {
            return 1 + 2 * havePatty(N-1, l, map);
	} else if(X >= Nlen/2+1){
            return 1 + havePatty(N-1, l, map) + havePatty(N-1, X-l-2, map);
        } else {
            return havePatty(N-1, X-1, map);
        }
    }
}